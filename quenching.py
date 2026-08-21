import numpy as np

class QuenchingModel:
    COOLING_MEDIA = {
        "Furnace": {"severity": 0.05, "description": "Very slow cooling"},
        "Air": {"severity": 0.15, "description": "Slow cooling"},
        "Oil": {"severity": 0.35, "description": "Moderate cooling"},
        "Water": {"severity": 0.80, "description": "Rapid cooling"},
        "Brine": {"severity": 1.00, "description": "Very rapid cooling"},
    }

    def __init__(self, initial_temperature=850.0, final_temperature=25.0, medium="Water"):
        if medium not in self.COOLING_MEDIA:
            raise ValueError(f"Unknown cooling medium: {medium}")
        if final_temperature >= initial_temperature:
            raise ValueError("Final temperature must be lower than initial temperature.")
        self.initial_temperature = initial_temperature
        self.final_temperature = final_temperature
        self.medium = medium
        self.severity = self.COOLING_MEDIA[medium]["severity"]

    def cooling_rate_at_temperature(self, temperature):
        delta = temperature - self.final_temperature
        return max(self.severity * 0.08 * delta, 0.05)

    def generate(self, time_step=0.1):
        time_values = [0.0]
        temperature_values = [self.initial_temperature]
        time = 0.0
        temperature = self.initial_temperature

        while temperature > self.final_temperature:
            rate = self.cooling_rate_at_temperature(temperature)
            temperature = max(self.final_temperature, temperature - rate * time_step)
            time += time_step
            time_values.append(time)
            temperature_values.append(temperature)

        return np.array(time_values), np.array(temperature_values)

    def average_cooling_rate(self, start_temperature=800.0, end_temperature=500.0):
        time, temperature = self.generate()
        mask = (temperature <= start_temperature) & (temperature >= end_temperature)
        if mask.sum() < 2:
            return None
        t = time[mask]
        temp = temperature[mask]
        return (temp[0] - temp[-1]) / (t[-1] - t[0])

    def information(self):
        return {
            "medium": self.medium,
            "severity": self.severity,
            "description": self.COOLING_MEDIA[self.medium]["description"],
        }
