"""
© 2026 Tony Ray Macier III. All rights reserved.

Thalos Prime™ is a proprietary system.

Chatbot Integration Tests - Test NLP, action handling, and chatbot capabilities
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

import pytest
from core.cis import CIS
from wetware.organoid_core import OrganoidCore
from wetware.mea_interface import MEAInterface
from wetware.life_support import LifeSupport
from ai.neural.bio_neural_network import BioNeuralNetwork
from ai.learning.reinforcement_learner import ReinforcementLearner
from database.connection_manager import DatabaseManager
from interfaces.web.nlp_processor import NLPProcessor
from interfaces.web.action_handler import ActionHandler


class TestNLPProcessor:
    """Test NLP message analysis"""
    
    @pytest.fixture
    def nlp(self):
        """Create NLP processor"""
        return NLPProcessor()
    
    def test_greeting_detection(self, nlp):
        """Test greeting intent detection"""
        messages = ["Hello", "Hi there", "Good morning"]
        
        for msg in messages:
            analysis = nlp.analyze_message(msg)
            assert analysis['intent'] == 'greeting'
            assert 'sentiment' in analysis
    
    def test_question_detection(self, nlp):
        """Test question intent detection"""
        questions = [
            "What is Thalos Prime?",
            "How do you work?",
            "What are organoids?"
        ]
        
        for question in questions:
            analysis = nlp.analyze_message(question)
            assert 'question' in analysis['intent']  # May be 'question', 'question_what', etc.
            assert 'topics' in analysis
    
    def test_response_generation(self, nlp):
        """Test response generation with wetware data"""
        msg = "Hello"
        analysis = nlp.analyze_message(msg)
        
        wetware_data = {
            'lobe_responses': [],
            'life_support': {'viability': 0.95},
            'total_spikes': 150,
            'decoded': {'confidence': 0.85},
            'mea_stats': {'active_channels': 999}
        }
        
        response = nlp.generate_response(msg, analysis, wetware_data)
        assert isinstance(response, str)
        assert len(response) > 0


class TestActionHandler:
    """Test action detection and execution"""
    
    @pytest.fixture
    def system(self):
        """Setup complete system for action testing"""
        cis = CIS()
        cis.boot()
        
        db_manager = DatabaseManager(db_type="memory")
        life_support = LifeSupport()
        life_support.initialize()
        
        mea = MEAInterface(channels=100)
        mea.initialize()
        
        organoids = []
        for i, lobe_type in enumerate(['logic', 'abstract', 'governance']):
            org = OrganoidCore(f"org_{i}", lobe_type)
            org.initialize()
            organoids.append(org)
        
        neural_net = BioNeuralNetwork("test_net")
        input_layer = neural_net.create_layer(10, "input")
        output_layer = neural_net.create_layer(5, "output")
        neural_net.connect_layers(input_layer, output_layer, 0.5)
        
        rl_agent = ReinforcementLearner(state_dim=10, action_dim=5)
        
        action_handler = ActionHandler(
            cis, organoids, mea, life_support, 
            neural_net, rl_agent, db_manager
        )
        
        yield {
            'cis': cis,
            'action_handler': action_handler,
            'db_manager': db_manager
        }
        
        # Cleanup
        db_manager.close()
        cis.shutdown()
    
    def test_memory_create_action(self, system):
        """Test memory creation action"""
        action_type, params = system['action_handler'].detect_action(
            "Store username as Tony"
        )
        assert action_type == "memory_create"
        
        result = system['action_handler'].execute_action(action_type, params)
        assert result['success'] is True
    
    def test_memory_retrieve_action(self, system):
        """Test memory retrieval action"""
        # First create a memory
        system['action_handler'].execute_action(
            "memory_create", 
            {'key': 'username', 'value': 'Tony'}
        )
        
        # Then retrieve it
        action_type, params = system['action_handler'].detect_action(
            "What is username?"
        )
        assert action_type == "memory_retrieve"
        
        result = system['action_handler'].execute_action(action_type, params)
        assert result['success'] is True
    
    def test_calculation_action(self, system):
        """Test calculation action"""
        action_type, params = system['action_handler'].detect_action(
            "Calculate 25 + 17"
        )
        assert action_type == "calculate"
        
        result = system['action_handler'].execute_action(action_type, params)
        assert result['success'] is True
        assert 'result' in result
    
    def test_system_status_action(self, system):
        """Test system status action"""
        action_type, params = system['action_handler'].detect_action(
            "Show system status"
        )
        assert action_type == "system_status"
        
        result = system['action_handler'].execute_action(action_type, params)
        assert result['success'] is True
    
    def test_code_generation_action(self, system):
        """Test code generation action"""
        action_type, params = system['action_handler'].detect_action(
            "Generate a Python function called hello_world"
        )
        assert action_type == "generate_code"
        
        result = system['action_handler'].execute_action(action_type, params)
        assert result['success'] is True
        if 'code' in result:
            assert len(result['code']) > 0


class TestChatbotIntegration:
    """Test complete chatbot integration with all systems"""
    
    @pytest.fixture
    def full_system(self):
        """Setup complete chatbot system"""
        cis = CIS()
        cis.boot()
        
        db_manager = DatabaseManager(db_type="memory")
        life_support = LifeSupport()
        life_support.initialize()
        
        mea = MEAInterface(channels=1000)
        mea.initialize()
        
        organoids = []
        for i, lobe_type in enumerate(['logic', 'abstract', 'governance']):
            org = OrganoidCore(f"org_{i}", lobe_type)
            org.initialize()
            organoids.append(org)
        
        neural_net = BioNeuralNetwork("chatbot_net")
        input_layer = neural_net.create_layer(10, "input")
        hidden_layer = neural_net.create_layer(20, "hidden")
        output_layer = neural_net.create_layer(5, "output")
        neural_net.connect_layers(input_layer, hidden_layer, 0.6)
        neural_net.connect_layers(hidden_layer, output_layer, 0.7)
        
        rl_agent = ReinforcementLearner(state_dim=10, action_dim=5)
        nlp = NLPProcessor()
        action_handler = ActionHandler(
            cis, organoids, mea, life_support,
            neural_net, rl_agent, db_manager
        )
        
        yield {
            'cis': cis,
            'db_manager': db_manager,
            'life_support': life_support,
            'mea': mea,
            'organoids': organoids,
            'neural_net': neural_net,
            'rl_agent': rl_agent,
            'nlp': nlp,
            'action_handler': action_handler
        }
        
        # Cleanup
        db_manager.close()
        cis.shutdown()
    
    def test_complete_conversation_flow(self, full_system):
        """Test complete conversation flow from input to response"""
        message = "Hello, what is Thalos Prime?"
        
        # Analyze message
        analysis = full_system['nlp'].analyze_message(message)
        assert 'intent' in analysis
        assert 'sentiment' in analysis
        
        # Detect action
        action_type, params = full_system['action_handler'].detect_action(message)
        
        # Process through wetware
        digital_signal = {
            'type': 'query',
            'data': {'text': message},
            'intensity': 0.7
        }
        pulse_pattern = full_system['mea'].encode_digital_to_pulse(digital_signal)
        
        # Get organoid responses
        lobe_responses = []
        for org in full_system['organoids']:
            stimulus = {
                'type': 'pattern',
                'intensity': 0.7,
                'data': pulse_pattern
            }
            response = org.process_stimulus(stimulus)
            lobe_responses.append(org.get_status())
        
        # Update life support
        full_system['life_support'].update(dt=1.0)
        
        # Generate response
        wetware_data = {
            'lobe_responses': lobe_responses,
            'life_support': full_system['life_support'].get_status(),
            'total_spikes': 150,
            'decoded': {'confidence': 0.85},
            'mea_stats': {'active_channels': 999}
        }
        wetware_data['life_support']['viability'] = full_system['life_support'].get_viability_score()
        
        response = full_system['nlp'].generate_response(message, analysis, wetware_data)
        assert isinstance(response, str)
        assert len(response) > 0
    
    def test_memory_operations_through_chatbot(self, full_system):
        """Test memory operations through chatbot interface"""
        # Create
        msg1 = "Store my name as Tony"
        action_type, params = full_system['action_handler'].detect_action(msg1)
        result = full_system['action_handler'].execute_action(action_type, params)
        assert result['success'] is True
        
        # Retrieve
        msg2 = "What is my name?"
        action_type, params = full_system['action_handler'].detect_action(msg2)
        result = full_system['action_handler'].execute_action(action_type, params)
        assert result['success'] is True
    
    def test_neural_learning_through_chatbot(self, full_system):
        """Test that neural network learns from interactions"""
        initial_stats = full_system['neural_net'].get_network_stats()
        initial_spikes = initial_stats['total_spikes']
        
        # Simulate multiple interactions
        for i in range(5):
            pattern = [0.5 + (i * 0.1)] * 10
            full_system['neural_net'].stimulate_inputs(pattern)
            
            for _ in range(20):
                full_system['neural_net'].simulate_step()
        
        final_stats = full_system['neural_net'].get_network_stats()
        final_spikes = final_stats['total_spikes']
        
        # Network should have accumulated activity
        assert final_spikes > initial_spikes
