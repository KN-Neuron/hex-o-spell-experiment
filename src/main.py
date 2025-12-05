import sys

import pygame

from src.data_manager import DataManager
from src.egg_headset import EggHeadset
from src.gui import GUIManager


def main():
    gui = GUIManager()
    headset = EggHeadset()
    data_manager = DataManager()
    
    gui.initialize()
    
    if headset.connect():
        print("Connected to EEG headset")
    else:
        print("Warning: Could not connect to EEG headset")
    
    running = True
    clock = pygame.time.Clock()
    
    try:
        while running:
            running = gui.handle_events()
            
            if headset.connected:
                raw_data = headset.read_data()
                if raw_data:
                    processed_data = headset.process_data(raw_data)
                    data_manager.add_data_point(processed_data)
                    
                    # dodajcie logger
            
            gui.update()
            
            gui.render()
            
            clock.tick(60)
            
    except KeyboardInterrupt:
        print("\nShutting down gracefully...")
        
    finally:
        if headset.connected:
            headset.disconnect()
        
        export_file = data_manager.export_current_session("final_session")
        print(f"Session data exported to: {export_file}")
        
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    main()
