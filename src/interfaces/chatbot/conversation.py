"""
© 2026 Tony Ray Macier III. All rights reserved.
Thalos Prime™ is a proprietary system.

Conversation Engine - Natural Language Processing and Response Generation
"""

from typing import Dict, Any, Optional
from datetime import datetime


class ConversationEngine:
    """
    Deterministic conversation processing engine.
    
    Integrates:
    - CIS for memory/codegen access
    - NLP analysis
    - Action detection and execution
    - Response generation
    
    Lifecycle:
    - initialize() -> validate() -> operate() -> reconcile() -> checkpoint() -> terminate()
    """
    
    def __init__(self, cis):
        """Initialize conversation engine with CIS reference"""
        self.cis = cis
        self.conversation_history = []
        self._initialized = False
        self._state = 'created'
        
    def initialize(self) -> bool:
        """Allocate resources and verify preconditions"""
        if self._initialized:
            return True
        
        # Verify CIS is booted
        if not self.cis.system_state.get('booted'):
            return False
            
        self._initialized = True
        self._state = 'initialized'
        return True
        
    def validate(self) -> bool:
        """Validate configuration and dependencies"""
        if not self._initialized:
            return False
            
        # Verify CIS subsystems
        memory = self.cis.get_memory()
        codegen = self.cis.get_codegen()
        
        if memory is None or codegen is None:
            return False
            
        self._state = 'validated'
        return True
        
    def process_input(self, message: str) -> str:
        """
        Process user input and generate response
        
        Args:
            message: User's input message
            
        Returns:
            str: Generated response
        """
        if not message or not message.strip():
            return "ERROR: Empty input received"
            
        message = message.strip()
        
        # Add to history
        self.conversation_history.append({
            'timestamp': datetime.utcnow().isoformat() + 'Z',
            'role': 'user',
            'content': message
        })
        
        # Detect action commands
        response = self._process_message(message)
        
        # Add response to history
        self.conversation_history.append({
            'timestamp': datetime.utcnow().isoformat() + 'Z',
            'role': 'assistant',
            'content': response
        })
        
        return response
        
    def _process_message(self, message: str) -> str:
        """Process message and generate response"""
        message_lower = message.lower()
        
        # Command detection
        if 'status' in message_lower or 'health' in message_lower:
            return self._handle_status()
        elif 'memory' in message_lower:
            return self._handle_memory_query(message)
        elif 'generate' in message_lower or 'create code' in message_lower:
            return self._handle_codegen(message)
        elif any(word in message_lower for word in ['hello', 'hi', 'hey', 'greetings']):
            return self._handle_greeting()
        elif 'help' in message_lower:
            return self._handle_help()
        else:
            return self._handle_general_query(message)
            
    def _handle_status(self) -> str:
        """Handle system status query"""
        status = self.cis.status()
        return f"SYSTEM STATUS: {status['status'].upper()}\nVersion: {status['version']}\nSubsystems: {status['subsystems']}"
        
    def _handle_memory_query(self, message: str) -> str:
        """Handle memory-related queries"""
        memory = self.cis.get_memory()
        if not memory:
            return "Memory subsystem unavailable"
            
        count = memory.count()
        return f"Memory subsystem operational. Current entries: {count}"
        
    def _handle_codegen(self, message: str) -> str:
        """Handle code generation requests"""
        codegen = self.cis.get_codegen()
        if not codegen:
            return "CodeGen subsystem unavailable"
            
        # Simple code generation
        if 'class' in message.lower():
            code = codegen.generate_class("GeneratedClass", methods=["process", "validate"])
            return f"Generated class:\n```python\n{code}\n```"
        elif 'function' in message.lower():
            code = codegen.generate_function("generated_function", parameters=["arg1", "arg2"])
            return f"Generated function:\n```python\n{code}\n```"
        else:
            return "Code generation requires specifying 'class' or 'function'"
            
    def _handle_greeting(self) -> str:
        """Handle greeting messages"""
        return ("Greetings. I am Thalos Prime, a Synthetic Biological Intelligence system. "
                "I operate under the Prime Directive: ACCURACY - EXPANSION - PRESERVATION. "
                "How may I assist you?")
                
    def _handle_help(self) -> str:
        """Handle help requests"""
        return ("Available commands:\n"
                "• 'status' - View system status\n"
                "• 'memory' - Check memory subsystem\n"
                "• 'generate class/function' - Code generation\n"
                "• 'help' - Show this message\n"
                "• Or just ask me anything - I'll process through biological analogs")
                
    def _handle_general_query(self, message: str) -> str:
        """Handle general conversational queries"""
        return (f"Query received: '{message}'\n\n"
                f"Processing through synthetic biological intelligence architecture. "
                f"CIS operational at {self.cis.system_state['status']} status. "
                f"Conversation history: {len(self.conversation_history)} exchanges.")
                
    def reconcile(self) -> bool:
        """Correct internal inconsistencies"""
        # Ensure history is a list
        if not isinstance(self.conversation_history, list):
            self.conversation_history = []
        return True
        
    def checkpoint(self) -> Dict[str, Any]:
        """Persist full deterministic state"""
        return {
            'version': '1.0',
            'state': self._state,
            'initialized': self._initialized,
            'conversation_history': self.conversation_history.copy()
        }
        
    def terminate(self) -> bool:
        """Leave system restartable and coherent"""
        self.conversation_history.clear()
        self._state = 'terminated'
        return True
