"""
Unit tests for the GUI module.
"""
import pytest
from src.gui import GUIManager


class TestGUIManager:
    """Test cases for the GUIManager class."""
    
    def test_initialization(self):
        """Test GUI manager initialization."""
        gui = GUIManager(width=800, height=600)
        assert gui.width == 800
        assert gui.height == 600
        assert gui.screen is None
        assert gui.clock is None
        
    def test_initialize_method(self, mocker):
        """Test the initialize method."""
        # Mock pygame functions
        mock_pygame = mocker.patch('src.gui.pygame')
        gui = GUIManager(width=800, height=600)
        
        gui.initialize()
        
        # Check that pygame.init was called
        mock_pygame.init.assert_called_once()
        
        # Check that set_mode was called with the correct dimensions
        mock_pygame.display.set_mode.assert_called_once_with((800, 600))
        
        # Check that the caption was set
        mock_pygame.display.set_caption.assert_called_once_with("Hex-O-Spell Experiment")
        
    def test_render_method(self, mocker):
        """Test the render method."""
        # Mock pygame functions
        mock_screen = mocker.Mock()
        mock_pygame = mocker.patch('src.gui.pygame')
        mock_pygame.display.set_mode.return_value = mock_screen
        
        gui = GUIManager(width=800, height=600)
        gui.initialize()
        
        # Call render
        gui.render()
        
        # Check that screen was filled and display was flipped
        mock_screen.fill.assert_called_once_with((0, 0, 0))
        mock_pygame.display.flip.assert_called_once()