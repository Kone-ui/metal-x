import math

class TransformationModel:
    def __init__(self, material, alpha=0.011):
        self.material = material
        self.alpha = alpha

    def martensite_fraction(self, temperature, ms):
        if temperature >= ms:
            return 0.0
        return min(max(1 - math.exp(-self.alpha * (ms - temperature)), 0.0), 1.0)

    def calculate(self, temperature, ms):
        martensite = self.martensite_fraction(temperature, ms)
        return {
            "martensite": martensite * 100,
            "retained_austenite": (1 - martensite) * 100,
        }
