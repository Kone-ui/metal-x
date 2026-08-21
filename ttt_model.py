import numpy as np

class TTTModel:
    def __init__(self, material):
        self.material = material
        self.carbon = material.carbon

    def pearlite_start_time(self, temperature):
        distance = max(abs(temperature - 550.0), 1.0)
        return 2.0 * np.exp(distance / 80.0)

    def bainite_start_time(self, temperature):
        distance = max(abs(temperature - 400.0), 1.0)
        return 5.0 * np.exp(distance / 100.0)

    def martensite_start_temperature(self):
        return 539 - 423 * self.carbon

    def martensite_finish_temperature(self):
        return self.martensite_start_temperature() - 150

    def transformation_region(self, temperature):
        ms = self.martensite_start_temperature()
        if temperature < ms:
            return "Martensite region"
        if temperature < 550:
            return "Bainite region"
        return "Pearlite region"
