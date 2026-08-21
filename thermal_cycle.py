import numpy as np

class ThermalCycle:
    def __init__(self, initial_temperature=25.0, austenitizing_temperature=850.0,
                 heating_rate=10.0, holding_time=30.0, cooling_rate=20.0):
        if heating_rate <= 0 or cooling_rate <= 0:
            raise ValueError("Heating and cooling rates must be positive.")
        if holding_time < 0:
            raise ValueError("Holding time cannot be negative.")
        if austenitizing_temperature <= initial_temperature:
            raise ValueError("Austenitizing temperature must be higher than initial temperature.")

        self.initial_temperature = initial_temperature
        self.austenitizing_temperature = austenitizing_temperature
        self.heating_rate = heating_rate
        self.holding_time = holding_time
        self.cooling_rate = cooling_rate

    def heating_time(self):
        return (self.austenitizing_temperature - self.initial_temperature) / self.heating_rate

    def cooling_time(self):
        return (self.austenitizing_temperature - self.initial_temperature) / self.cooling_rate

    def generate(self):
        ht = self.heating_time()
        hold = self.holding_time * 60
        ct = self.cooling_time()

        n1 = max(int(ht * 10), 2)
        n2 = max(int(hold * 10), 2)
        n3 = max(int(ct * 10), 2)

        t1 = np.linspace(0, ht, n1)
        y1 = self.initial_temperature + self.heating_rate * t1

        t2 = np.linspace(ht, ht + hold, n2)
        y2 = np.full(n2, self.austenitizing_temperature)

        t3 = np.linspace(ht + hold, ht + hold + ct, n3)
        elapsed = t3 - (ht + hold)
        y3 = self.austenitizing_temperature - self.cooling_rate * elapsed

        return (
            np.concatenate([t1, t2[1:], t3[1:]]),
            np.concatenate([y1, y2[1:], y3[1:]]),
        )
