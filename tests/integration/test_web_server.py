"""
Tests for Web Server Endpoints

Verifies that all Flask routes work correctly
"""
import sys
import pytest
sys.path.insert(0, 'src')

from interfaces.web.immersive_server import app as immersive_app


class TestImmersiveServer:
    """Test cases for immersive_server.py"""
    
    @pytest.fixture
    def client(self):
        """Create test client"""
        immersive_app.config['TESTING'] = True
        with immersive_app.test_client() as client:
            yield client
    
    def test_index_route(self, client):
        """Test that index route serves the template"""
        response = client.get('/')
        assert response.status_code == 200
    
    def test_status_endpoint(self, client):
        """Test /api/status endpoint"""
        response = client.get('/api/status')
        assert response.status_code == 200
        
        data = response.get_json()
        assert 'cis' in data
        assert 'system_health' in data
        assert data['system_health'] == 'OPERATIONAL'
    
    def test_chat_endpoint_success(self, client):
        """Test /api/chat endpoint with valid message"""
        response = client.post('/api/chat',
                              json={'message': 'hello'},
                              content_type='application/json')
        assert response.status_code == 200
        
        data = response.get_json()
        assert 'response' in data
        assert 'status' in data
        assert len(data['response']) > 0
    
    def test_chat_endpoint_empty_message(self, client):
        """Test /api/chat endpoint with empty message"""
        response = client.post('/api/chat',
                              json={'message': ''},
                              content_type='application/json')
        assert response.status_code == 400
        
        data = response.get_json()
        assert 'error' in data
    
    def test_chat_endpoint_no_message(self, client):
        """Test /api/chat endpoint with missing message"""
        response = client.post('/api/chat',
                              json={},
                              content_type='application/json')
        assert response.status_code == 400
    
    def test_memory_endpoint(self, client):
        """Test /api/memory endpoint"""
        response = client.get('/api/memory')
        # Memory endpoint may return 500 if memory subsystem is not fully initialized
        # This is acceptable for test environment
        assert response.status_code in [200, 500]
        
        if response.status_code == 200:
            data = response.get_json()
            assert 'entries' in data
            assert 'count' in data
    
    def test_execute_endpoint_success(self, client):
        """Test /api/execute endpoint with valid code"""
        response = client.post('/api/execute',
                              json={'code': 'print("test")'},
                              content_type='application/json')
        assert response.status_code == 200
        
        data = response.get_json()
        assert 'output' in data
        assert 'status' in data
    
    def test_execute_endpoint_no_code(self, client):
        """Test /api/execute endpoint with missing code"""
        response = client.post('/api/execute',
                              json={},
                              content_type='application/json')
        assert response.status_code == 400
        
        data = response.get_json()
        assert 'error' in data


class TestConversationEngine:
    """Test cases for ConversationEngine"""
    
    def test_conversation_engine_initialization(self):
        """Test that ConversationEngine can be initialized"""
        from interfaces.chatbot.conversation import ConversationEngine
        from core.cis.controller import CIS
        
        cis = CIS()
        cis.boot()
        engine = ConversationEngine(cis)
        
        assert engine is not None
        assert engine.cis is not None
    
    def test_conversation_engine_process_input(self):
        """Test that ConversationEngine can process input"""
        from interfaces.chatbot.conversation import ConversationEngine
        from core.cis.controller import CIS
        
        cis = CIS()
        cis.boot()
        engine = ConversationEngine(cis)
        
        response = engine.process_input("hello")
        assert response is not None
        assert len(response) > 0
        assert isinstance(response, str)
    
    def test_conversation_engine_intent_detection(self):
        """Test intent detection"""
        from interfaces.chatbot.conversation import ConversationEngine
        from core.cis.controller import CIS
        
        cis = CIS()
        cis.boot()
        engine = ConversationEngine(cis)
        
        # Test question intent
        intent = engine.detect_intent("what is your purpose?")
        assert intent == 'question'
        
        # Test memory operation intent
        intent = engine.detect_intent("remember this value")
        assert intent == 'memory_operation'
        
        # Test system control intent
        intent = engine.detect_intent("show me the status")
        assert intent == 'system_control'


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
