from .sampling_strategies import RandomSampler, StratifiedSampler, BaseSampler
from .storage_handler import StorageHandler


class SessionManager:
    def __init__(self, subject_id: str, strategy: str = 'random') -> None:
        self.storage = StorageHandler(subject_id)
        self.sampler: BaseSampler

        if strategy == 'random':
            self.sampler = RandomSampler()
        elif strategy == 'stratified':
            self.sampler = StratifiedSampler()
        else:
            # Fallback
            self.sampler = RandomSampler()

    def run_trial(self) -> None:
        pass
