"""
Integration tests for the hex-o-spell experiment.
"""
import os
import tempfile
from src.gui import GUIManager
from src.egg_headset import EggHeadset
from src.data_manager import DataManager


class TestIntegration:
    """Integration tests for the main components."""
    
    def test_full_system_integration(self):
        """Test that all components can work together."""
        # Create temporary directory for data
        with tempfile.TemporaryDirectory() as temp_dir:
            # Initialize all components
            gui = GUIManager(width=400, height=300)
            headset = EggHeadset(device_address="test_device")
            data_manager = DataManager(data_dir=temp_dir)
            
            # Connect the headset
            assert headset.connect() == True
            assert headset.connected == True
            
            # Add some data to the data manager
            data_manager.add_data_point({"timestamp": 1, "value": 10})
            data_manager.add_data_point({"timestamp": 2, "value": 20})
            
            # Export the session
            export_file = data_manager.export_current_session("integration_test")
            
            # Verify the export file was created
            assert os.path.exists(export_file)
            
            # Load the exported session
            loaded_session = data_manager.load_session_data("integration_test")
            
            assert loaded_session is not None
            assert loaded_session["session_id"] == "integration_test"
            assert len(loaded_session["data_points"]) == 2