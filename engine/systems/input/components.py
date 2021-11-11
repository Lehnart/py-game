from typing import Dict, Callable


class InputComponent:

    def __init__(self, input_dicts: Dict[int, Callable]):
        self.input_dicts = input_dicts
