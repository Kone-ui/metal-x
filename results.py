class SimulationResult:
    def __init__(self, material, temperature, medium):
        self.material = material
        self.temperature = temperature
        self.medium = medium
        self.phases = {}
        self.hardness = {}
        self.temper_result = {}

    def set_phases(self, phases):
        self.phases = phases

    def set_hardness(self, hardness):
        self.hardness = hardness

    def set_tempering(self, result):
        self.temper_result = result

    def summary(self):
        return {
            "material": self.material.name,
            "carbon": self.material.carbon,
            "austenitizing_temperature": self.temperature,
            "quenching_medium": self.medium,
            "phases": self.phases,
            "hardness": self.hardness,
            "tempering": self.temper_result,
        }
