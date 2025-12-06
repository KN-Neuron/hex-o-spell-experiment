from typing import List, Any
import random


class BaseSampler:
    def get_next_command(
        self, available_commands: List[str], history: List[Any]
    ) -> str:
        raise NotImplementedError


class RandomSampler(BaseSampler):
    def get_next_command(
        self, available_commands: List[str], history: List[Any]
    ) -> str:
        return random.choice(available_commands)


class StratifiedSampler(BaseSampler):
    def get_next_command(
        self, available_commands: List[str], history: List[Any]
    ) -> str:
        return random.choice(available_commands)
