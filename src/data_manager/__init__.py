"""
Data manager module for hex-o-spell experiment.
Handles data storage, retrieval, and processing.
"""
import json
import os
from datetime import datetime
from typing import Dict, Any, Optional, List


class DataManager:
    """Manages data storage and retrieval for the experiment."""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        self.session_data = []
        self.ensure_data_dir()
        
    def ensure_data_dir(self):
        """Ensure the data directory exists."""
        os.makedirs(self.data_dir, exist_ok=True)
        
    def save_session_data(self, data: Dict[str, Any], session_id: Optional[str] = None) -> str:
        """Save session data to a JSON file."""
        if session_id is None:
            session_id = f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            
        filename = os.path.join(self.data_dir, f"{session_id}.json")
        
        # Add timestamp to the data
        data["timestamp"] = datetime.now().isoformat()
        data["session_id"] = session_id
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
            
        return filename
        
    def load_session_data(self, session_id: str) -> Optional[Dict[str, Any]]:
        """Load session data from a JSON file."""
        filename = os.path.join(self.data_dir, f"{session_id}.json")
        
        if not os.path.exists(filename):
            return None
            
        with open(filename, 'r') as f:
            return json.load(f)
            
    def get_all_sessions(self) -> List[str]:
        """Get a list of all session IDs."""
        sessions = []
        for filename in os.listdir(self.data_dir):
            if filename.endswith('.json'):
                sessions.append(filename[:-5])  # Remove '.json' extension
        return sessions
        
    def add_data_point(self, data: Dict[str, Any]):
        """Add a data point to the current session."""
        self.session_data.append(data)
        
    def export_current_session(self, session_id: str) -> str:
        """Export the current session data."""
        session_data = {
            "session_id": session_id,
            "data_points": self.session_data,
            "export_timestamp": datetime.now().isoformat()
        }
        return self.save_session_data(session_data, session_id)