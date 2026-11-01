"""
Thalos Prime immersive web interface.

Security posture:
- Binds to loopback only.
- Debug mode is always disabled.
- Chat, memory export, and arbitrary code execution HTTP endpoints are
  intentionally disabled until authentication and execution isolation exist.
"""

from datetime import datetime
import os
import sys

from flask import Flask, jsonify, render_template
from flask_cors import CORS

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from core.cis.controller import CIS

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static",
)

# CORS is a browser-origin control, not authentication. Keep the allowlist
# explicit and reject wildcard configuration.
_default_origins = "http://localhost:3000,http://127.0.0.1:3000"
_raw_origins = os.environ.get("THALOS_CORS_ORIGINS", _default_origins)
_allowed_origins = [origin.strip() for origin in _raw_origins.split(",") if origin.strip()]
if not _allowed_origins or "*" in _allowed_origins:
    raise RuntimeError("THALOS_CORS_ORIGINS must be a non-empty explicit origin allowlist")
CORS(app, resources={r"/*": {"origins": _allowed_origins}})

# Initialize Thalos Prime
print("=" * 70)
print("THALOS PRIME - LOOPBACK-ONLY INTERFACE")
print("=" * 70)
print("Initializing CIS...")
cis = CIS()
cis.boot()
print("CIS initialized")
print("Web server ready")


@app.route("/")
def index():
    """Serve the immersive interface."""
    return render_template("thalos_immersive.html")


@app.route("/api/chat", methods=["POST"])
def chat_disabled():
    """Keep chat offline until authentication and execution isolation exist."""
    return jsonify({
        "error": "Chat API is temporarily disabled",
        "status": "unavailable",
        "reason": "Authentication and execution isolation are not yet implemented",
    }), 503


@app.route("/api/status", methods=["GET"])
def get_status():
    """Return non-sensitive system status."""
    status = cis.status()
    return jsonify({
        "cis": status,
        "system_health": "OPERATIONAL",
        "version": "1.5.0",
    })


if __name__ == "__main__":
    # This interface intentionally cannot bind to a public network address.
    # Deploy behind a separately authenticated reverse proxy only after review.
    print("Thalos Prime interface: http://127.0.0.1:8000")
    app.run(host="127.0.0.1", port=8000, debug=False)
