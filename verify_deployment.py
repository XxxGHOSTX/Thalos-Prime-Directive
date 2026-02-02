#!/usr/bin/env python3
"""
© 2026 Tony Ray Macier III. All rights reserved.
Thalos Prime™ is a proprietary system.

Deployment Verification - Ensure System is Fully Operational
"""

import sys
import os
from pathlib import Path

def verify_critical_files():
    """Verify all critical files exist"""
    print("="*70)
    print("THALOS PRIME DEPLOYMENT VERIFICATION")
    print("="*70)
    print()
    
    critical_files = [
        'boot_thalos.py',
        'src/core/cis/controller.py',
        'src/interfaces/web/immersive_server.py',
        'src/interfaces/chatbot/__init__.py',
        'src/interfaces/chatbot/conversation.py',
        'src/interfaces/web/templates/thalos_immersive.html',
        'requirements.txt'
    ]
    
    print("1. Checking Critical Files...")
    all_exist = True
    for file in critical_files:
        exists = Path(file).exists()
        status = "✓" if exists else "✗"
        print(f"  {status} {file}")
        if not exists:
            all_exist = False
    
    if not all_exist:
        print("\n✗ VERIFICATION FAILED: Missing critical files")
        return False
    
    print("  ✓ All critical files present\n")
    return True

def verify_imports():
    """Verify critical imports work"""
    print("2. Checking Critical Imports...")
    
    # Add src to path
    sys.path.insert(0, str(Path(__file__).parent / "src"))
    
    try:
        from core.cis.controller import CIS
        print("  ✓ CIS import successful")
    except ImportError as e:
        print(f"  ✗ CIS import failed: {e}")
        return False
    
    try:
        from interfaces.chatbot.conversation import ConversationEngine
        print("  ✓ ConversationEngine import successful")
    except ImportError as e:
        print(f"  ✗ ConversationEngine import failed: {e}")
        return False
    
    print("  ✓ All critical imports successful\n")
    return True

def verify_cis_boot():
    """Verify CIS can boot"""
    print("3. Testing CIS Boot Sequence...")
    
    sys.path.insert(0, str(Path(__file__).parent / "src"))
    
    try:
        from core.cis.controller import CIS
        
        cis = CIS()
        print("  ✓ CIS instantiated")
        
        if not cis.initialize():
            print("  ✗ CIS initialization failed")
            return False
        print("  ✓ CIS initialized")
        
        if not cis.validate():
            print("  ✗ CIS validation failed")
            return False
        print("  ✓ CIS validated")
        
        if not cis.boot():
            print("  ✗ CIS boot failed")
            return False
        print("  ✓ CIS booted")
        
        status = cis.status()
        print(f"  ✓ CIS status: {status['status']}")
        
        cis.shutdown()
        print("  ✓ CIS shutdown successful\n")
        return True
        
    except Exception as e:
        print(f"  ✗ CIS boot test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def verify_conversation_engine():
    """Verify ConversationEngine works"""
    print("4. Testing ConversationEngine...")
    
    sys.path.insert(0, str(Path(__file__).parent / "src"))
    
    try:
        from core.cis.controller import CIS
        from interfaces.chatbot.conversation import ConversationEngine
        
        cis = CIS()
        cis.boot()
        
        conversation = ConversationEngine(cis)
        print("  ✓ ConversationEngine instantiated")
        
        if not conversation.initialize():
            print("  ✗ ConversationEngine initialization failed")
            return False
        print("  ✓ ConversationEngine initialized")
        
        if not conversation.validate():
            print("  ✗ ConversationEngine validation failed")
            return False
        print("  ✓ ConversationEngine validated")
        
        response = conversation.process_input("Hello")
        print(f"  ✓ ConversationEngine response: {response[:50]}...")
        
        cis.shutdown()
        print("  ✓ ConversationEngine test successful\n")
        return True
        
    except Exception as e:
        print(f"  ✗ ConversationEngine test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Run all verification tests"""
    results = []
    
    results.append(("Critical Files", verify_critical_files()))
    results.append(("Critical Imports", verify_imports()))
    results.append(("CIS Boot", verify_cis_boot()))
    results.append(("ConversationEngine", verify_conversation_engine()))
    
    print("="*70)
    print("VERIFICATION SUMMARY")
    print("="*70)
    
    for name, passed in results:
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"{name:30s}: {status}")
    
    all_passed = all(result[1] for result in results)
    
    print("="*70)
    if all_passed:
        print("\n🎉 ALL VERIFICATIONS PASSED!")
        print("✓ Thalos Prime is ready for deployment")
        print("✓ Run: python boot_thalos.py")
        return 0
    else:
        print("\n✗ VERIFICATION FAILED")
        print("System is NOT ready for deployment")
        return 1

if __name__ == "__main__":
    sys.exit(main())
