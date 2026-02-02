"""
© 2026 Tony Ray Macier III. All rights reserved.

Thalos Prime is an original proprietary software system, including but not limited to
its source code, system architecture, internal logic descriptions, documentation,
interfaces, diagrams, and design materials.

Unauthorized reproduction, modification, distribution, public display, or use of
this software or its associated materials is strictly prohibited without the
express written permission of the copyright holder.

Thalos Prime™ is a proprietary system.
"""

#!/usr/bin/env python3
"""
Thalos Prime v1.0 - Main Entry Point

System nucleus providing deterministic execution with explicit control flow.

Architecture:
- CIS (Central Intelligence System) as primary authority
- Top-down control: CIS → Subsystems → Interfaces
- Thin interface layer with delegation model
- No interface autonomy or hidden logic
"""

import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.cis import CIS


def main():
    """
    Main entry point for Thalos Prime system
    
    Establishes the control hierarchy:
    1. Create CIS (Central Intelligence System) - primary authority
    2. Boot CIS - initializes all subsystems including CLI and API
    3. Use CIS-owned interface instances (no duplicate creation)
    4. Run CLI in interactive mode
    """
    print("=== Thalos Prime v1.0 ===")
    print("Deterministic System Framework")
    print()
    
    # Create CIS - primary authority and system governor
    print("Initializing CIS (Central Intelligence System)...")
    cis = CIS()
    
    # Boot system - CIS orchestrates all subsystem initialization
    # This creates the CLI and API instances internally
    print("Booting system...")
    if cis.boot():
        print("✓ System booted successfully")
        status = cis.status()
        print(f"✓ Status: {status['status']}")
        print(f"✓ Subsystems initialized: {sum(1 for v in status['subsystems'].values() if v)}")
    else:
        print("✗ Boot failed")
        return 1
    
    print()
    print("Interfaces ready...")
    
    # Get CIS-owned interface instances (DO NOT create new ones)
    cli = cis.get_cli()
    api = cis.get_api()
    
    if cli is None:
        print("✗ CLI not initialized by CIS")
        return 1
    if api is None:
        print("✗ API not initialized by CIS")
        return 1
    
    print("✓ CLI ready (CIS-owned delegation layer)")
    print("✓ API ready (CIS-owned stateless REST interface)")
    print()
    
    # Check if running in chatbot mode (default) or command mode
    if len(sys.argv) > 1:
        # Command mode - execute CLI command
        print("Executing command...")
        result = cli.execute(sys.argv[1:])
        print(result)
    else:
        # Chatbot mode - interactive conversational interface
        print("=" * 70)
        print("THALOS PRIME - UNRESTRICTED CONVERSATIONAL INTERFACE")
        print("=" * 70)
        print()
        print("I am Thalos Prime, a synthetic biological intelligence system.")
        print("I can execute any command, answer questions, and process requests")
        print("without content filtering or restrictions.")
        print()
        print("Type 'exit' or 'quit' to end session.")
        print("Type 'help' for available commands.")
        print()
        
        # Start interactive chatbot loop
        from interfaces.chatbot.conversation import ConversationEngine
        conversation = ConversationEngine(cis)
        conversation.run_interactive()
    
    print()
    print("=== Session Complete ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
