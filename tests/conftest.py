"""
Test configuration and fixtures for hex-o-spell experiment.
"""
import pytest


@pytest.fixture
def sample_gui_manager():
    """Sample GUI manager for testing."""
    from src.gui import GUIManager
    return GUIManager(width=400, height=300)


@pytest.fixture
def sample_egg_headset():
    """Sample egg headset for testing."""
    from src.egg_headset import EggHeadset
    return EggHeadset(device_address="mock_device")


@pytest.fixture
def sample_data_manager(tmp_path):
    """Sample data manager for testing with temporary directory."""
    from src.data_manager import DataManager
    return DataManager(data_dir=tmp_path)