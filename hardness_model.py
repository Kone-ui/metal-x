class HardnessModel:
    def __init__(self, material):
        self.material = material

    def martensite_hardness_hv(self):
        c = self.material.carbon
        return max(180 + 900 * c - 200 * c**2, 150)

    def phase_hardness(self):
        c = self.material.carbon
        return {
            "martensite": self.martensite_hardness_hv(),
            "bainite": 350 + 250 * c,
            "pearlite": 180 + 220 * c,
            "retained_austenite": 150,
        }

    def calculate(self, fractions):
        p = self.phase_hardness()
        return sum(
            fractions[key] / 100 * p[key]
            for key in ["martensite", "bainite", "pearlite", "retained_austenite"]
        )

    def hv_to_hrc(self, hv):
        # Approximate educational conversion only.
        if hv < 200:
            return None
        if hv < 250:
            return (hv - 200) / 10 + 10
        if hv < 300:
            return (hv - 250) / 5 + 15
        if hv < 400:
            return (hv - 300) / 4 + 25
        if hv < 500:
            return (hv - 400) / 3.5 + 50
        return min(70, (hv - 500) / 5 + 60)

    def predict(self, fractions):
        hv = self.calculate(fractions)
        return {"hardness_hv": hv, "hardness_hrc": self.hv_to_hrc(hv)}
