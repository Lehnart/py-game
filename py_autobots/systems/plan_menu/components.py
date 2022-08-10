from typing import List


class PlanMenuComponent:

    def __init__(self, plans: List[int]):
        self.plans = plans
        self.selected_index = -1
