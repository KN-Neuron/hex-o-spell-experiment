from typing import Any, List


class StorageHandler:
    def __init__(self, subject_id: str, data_dir: str = "data") -> None:
        self.subject_id = subject_id
        self.data_dir = data_dir

    def save_calibration_data(self, eeg_data: Any, labels: List[str]) -> None:
        pass
