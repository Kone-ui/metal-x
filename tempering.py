import math

class TemperingModel:
    def __init__(self, initial_hardness):
        self.initial_hardness = initial_hardness

    def calculate(self, temperature, time):
        if temperature < 100:
            reduction = 0.02
        elif temperature < 200:
            reduction = 0.08
        elif temperature < 300:
            reduction = 0.15
        elif temperature < 400:
            reduction = 0.25
        elif temperature < 500:
            reduction = 0.35
        elif temperature < 600:
            reduction = 0.45
        else:
            reduction = 0.55

        time_factor = 1 - math.exp(-time / 60)
        final = self.initial_hardness * (1 - reduction * time_factor)
        return max(final, 100)
