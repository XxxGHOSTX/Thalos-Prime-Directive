"""
© 2026 Tony Ray Macier III. All rights reserved.

Thalos Prime™ is a proprietary system.
"""

"""
Enhanced Thalos Prime Web Server - Immersive Matrix Interface

Serves the immersive chatbot interface with unrestricted AI capabilities.
"""

from datetime import datetime
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import hmac
import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from core.cis.controller import CIS

app = Flask(__name__, 
            template_folder='templates',
            static_folder='static')
_raw_cors_origins = os.environ.get(
    "THALOS_CORS_ORIGINS",
    "http://localhost:3000,http://127.0.0.1:3000",
)
allowed_origins = [origin.strip() for origin in _raw_cors_origins.split(",") if origin.strip()]
if not allowed_origins or "*" in allowed_origins:
    raise RuntimeError("THALOS_CORS_ORIGINS must be an explicit origin allowlist; wildcard is prohibited")
CORS(app, origins=allowed_origins, supports_credentials=False)

# Initialize Thalos Prime
print("=" * 70)
print("THALOS PRIME V1.5 - LIVE IMMERSIVE EDITION")
print("=" * 70)
print("Initializing CIS...")
cis = CIS()
cis.boot()
print("✓ CIS operational")
print("✓ Web server ready")
print()


@app.route('/')
def index():
    """Serve the immersive Matrix interface"""
    return render_template('thalos_immersive.html')


@app.route('/api/chat', methods=['POST'])
def chat():
    """
    Handle unrestricted chat requests
    
    No content filtering, no restrictions.
    Full system access.
    """
    try:
        data = request.get_json()
        message = data.get('message', '').strip()
        
        if not message:
            return jsonify({'error': 'No message provided'}), 400
        
        # Process through conversation engine
        from interfaces.chatbot.conversation import ConversationEngine
        conversation = ConversationEngine(cis)

        # The local conversation engine includes privileged code, shell, memory,
        # file, learning, and system-control handlers. Do not expose those through
        # the unauthenticated HTTP chat route. Keep a small, fail-closed allowlist.
        allowed_remote_intents = {"general", "question", "code_generation"}
        intent = conversation.detect_intent(message)
        if intent not in allowed_remote_intents:
            return jsonify({
                "error": "This privileged action is disabled through the remote chat interface."
            }), 403

        response = conversation.process_input(message)
        
        return jsonify({
            'response': response,
            'status': 'success',
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        app.logger.exception("Chat processing failed")
        return jsonify({
            'response': 'An internal error occurred processing the request.',
            'status': 'error'
        }), 500


@app.route('/api/status', methods=['GET'])
def get_status():
    """Get system status"""
    status = cis.status()
    memory = cis.get_memory()
    
    return jsonify({
        'cis': status,
        'memory_entries': memory.count() if memory else 0,
        'system_health': 'OPERATIONAL',
        'version': '1.5.0'
    })


def _admin_token_failure():
    """Return an HTTP response unless a strong configured admin bearer token is valid."""
    configured = os.environ.get("THALOS_ADMIN_TOKEN", "")
    if len(configured.encode("utf-8")) < 32:
        return jsonify({"error": "Memory endpoint disabled until THALOS_ADMIN_TOKEN is configured with at least 32 UTF-8 bytes"}), 503
    authorization = request.headers.get("Authorization", "")
    if not authorization.startswith("Bearer ") or not hmac.compare_digest(authorization[7:].strip(), configured):
        return jsonify({"error": "Unauthorized"}), 401
    return None


@app.route('/api/memory', methods=['GET'])
def get_memory():
    """Get memory contents; requires a configured administrator bearer token."""
    auth_failure = _admin_token_failure()
    if auth_failure is not None:
        return auth_failure
    try:
        memory = cis.get_memory()
        if not memory:
            return jsonify({'entries': {}, 'count': 0})
        
        entries = memory.list()
        return jsonify({
            'entries': entries,
            'count': len(entries)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/execute', methods=['POST'])
def execute_code():
    """Disabled: executing caller-provided Python in the web process is unsafe."""
    return jsonify({
        "error": "Remote code execution is disabled. Use a separately isolated, authenticated execution service.",
        "status": "disabled",
    }), 410


if __name__ == '__main__':
    print("=" * 70)
    print("THALOS PRIME - SYNTHETIC BIOLOGICAL INTELLIGENCE")
    print("Unrestricted Interface Active")
    print("=" * 70)
    print(f"Status: {cis.status()['status']}")
    print(f"Web Interface: http://localhost:8000")
    print("=" * 70)
    print()
    
    app.run(
        host=os.environ.get("THALOS_HOST", "127.0.0.1"),
        port=int(os.environ.get("THALOS_PORT", "8000")),
        debug=False,
    )
