"""
GUI module for hex-o-spell experiment.
Contains all graphical user interface components.
"""
import pygame


class GUIManager:
    """Manages the GUI components of the application."""
    
    def __init__(self, width: int = 800, height: int = 600):
        self.width = width
        self.height = height
        self.screen = None
        self.clock = None
        
    def initialize(self):
        """Initialize pygame and create the display surface."""
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Hex-O-Spell Experiment")
        self.clock = pygame.time.Clock()
        
    def update(self):
        """Update the GUI state."""
        self.clock.tick(60)  # 60 FPS
        
    def render(self):
        """Render the GUI elements."""
        # Fill screen with a background color
        self.screen.fill((0, 0, 0))  # Black background
        # Add your rendering code here
        pygame.display.flip()
        
    def handle_events(self):
        """Handle pygame events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True