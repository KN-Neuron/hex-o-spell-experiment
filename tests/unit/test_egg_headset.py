from src.egg_headset import EggHeadset


class TestEggHeadset:
    def test_initialization(self) -> None:
        headset = EggHeadset()
        assert headset is not None
