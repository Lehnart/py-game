from typing import Dict, Callable


class InputComponent:

    def __init__(self, input_dicts: Dict[int, Callable], is_repeat=True):
        self.input_dicts = input_dicts
        self.is_repeat = is_repeat
