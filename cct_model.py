import numpy as np

class CCTModel:
    def __init__(self, material):
        self.material = material

    def critical_temperatures(self):
        c = self.material.carbon
        ms = 539 - 423 * c
        result = {"A1": 727.0, "A3": None, "Ms": ms, "Mf": ms - 150}
        if c < 0.77:
            result["A3"] = 910 - 203 * np.sqrt(c)
        return result

    def classify_cooling(self, cooling_rate):
        if cooling_rate >= 50:
            return "Martensitic"
        if cooling_rate >= 20:
            return "Bainitic + Martensitic"
        if cooling_rate >= 5:
            return "Pearlitic + Bainitic"
        return "Pearlitic"
