import math

class PhaseAnalyzer:
    EUTECTOID_CARBON = 0.77
    EUTECTOID_TEMPERATURE = 727.0

    def calculate_a3(self, carbon):
        if carbon >= self.EUTECTOID_CARBON:
            return None
        return 910 - 203 * math.sqrt(carbon)

    def calculate_acm(self, carbon):
        if carbon <= self.EUTECTOID_CARBON:
            return None
        return 727 + (2.11 - carbon) * ((1147 - 727) / (2.11 - 0.77))

    def analyze(self, carbon, temperature):
        if carbon < 0 or temperature < 0:
            return "Invalid input"

        if abs(carbon - self.EUTECTOID_CARBON) < 0.01:
            return "Austenite" if temperature > 727 else "Pearlite"

        if carbon < self.EUTECTOID_CARBON:
            a3 = self.calculate_a3(carbon)
            if temperature > a3:
                return "Austenite"
            if temperature > 727:
                return "Ferrite + Austenite"
            return "Ferrite + Pearlite"

        acm = self.calculate_acm(carbon)
        if temperature > acm:
            return "Austenite"
        if temperature > 727:
            return "Austenite + Cementite"
        return "Pearlite + Cementite"
