from src.gui import GUIManager


class TestGUIManager:
    def test_initialization(self) -> None:
        gui = GUIManager()
        assert gui is not None
