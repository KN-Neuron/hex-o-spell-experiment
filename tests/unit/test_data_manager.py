"""
Unit tests for the Data Manager module.
"""
import json
import os
from src.data_manager import DataManager


class TestDataManager:
    """Test cases for the DataManager class."""
    
    def test_initialization(self, tmp_path):
        """Test data manager initialization."""
        data_dir = tmp_path / "data"
        dm = DataManager(data_dir=str(data_dir))
        
        assert dm.data_dir == str(data_dir)
        assert dm.session_data == []
        assert os.path.exists(str(data_dir))
        
    def test_save_session_data(self, tmp_path):
        """Test saving session data."""
        data_dir = tmp_path / "data"
        dm = DataManager(data_dir=str(data_dir))
        
        test_data = {"test_key": "test_value"}
        filename = dm.save_session_data(test_data, "test_session")
        
        assert os.path.exists(filename)
        
        # Check that the file contains the expected data
        with open(filename, 'r') as f:
            loaded_data = json.load(f)
        
        assert loaded_data["test_key"] == "test_value"
        assert loaded_data["session_id"] == "test_session"
        assert "timestamp" in loaded_data
        
    def test_load_session_data(self, tmp_path):
        """Test loading session data."""
        data_dir = tmp_path / "data"
        dm = DataManager(data_dir=str(data_dir))
        
        # Save some test data first
        test_data = {"test_key": "test_value"}
        dm.save_session_data(test_data, "test_session")
        
        # Load the data back
        loaded_data = dm.load_session_data("test_session")
        
        assert loaded_data is not None
        assert loaded_data["test_key"] == "test_value"
        assert loaded_data["session_id"] == "test_session"
        assert "timestamp" in loaded_data
        
    def test_load_nonexistent_session(self, tmp_path):
        """Test loading a session that doesn't exist."""
        data_dir = tmp_path / "data"
        dm = DataManager(data_dir=str(data_dir))
        
        result = dm.load_session_data("nonexistent_session")
        
        assert result is None
        
    def test_get_all_sessions(self, tmp_path):
        """Test getting all session IDs."""
        data_dir = tmp_path / "data"
        dm = DataManager(data_dir=str(data_dir))
        
        # Save multiple sessions
        dm.save_session_data({"key1": "val1"}, "session1")
        dm.save_session_data({"key2": "val2"}, "session2")
        
        sessions = dm.get_all_sessions()
        
        assert "session1" in sessions
        assert "session2" in sessions
        
    def test_add_data_point(self, tmp_path):
        """Test adding a data point."""
        data_dir = tmp_path / "data"
        dm = DataManager(data_dir=str(data_dir))
        
        test_data = {"test_key": "test_value"}
        dm.add_data_point(test_data)
        
        assert len(dm.session_data) == 1
        assert dm.session_data[0] == test_data
        
    def test_export_current_session(self, tmp_path):
        """Test exporting current session."""
        data_dir = tmp_path / "data"
        dm = DataManager(data_dir=str(data_dir))
        
        # Add some data points
        dm.add_data_point({"point": 1})
        dm.add_data_point({"point": 2})
        
        filename = dm.export_current_session("export_session")
        
        assert os.path.exists(filename)
        
        # Check that the export contains the session data
        with open(filename, 'r') as f:
            loaded_data = json.load(f)
        
        assert loaded_data["session_id"] == "export_session"
        assert len(loaded_data["data_points"]) == 2
        assert loaded_data["data_points"][0]["point"] == 1
        assert loaded_data["data_points"][1]["point"] == 2