class PhaseFractionModel:
    def __init__(self, material, ttt_model):
        self.material = material
        self.ttt_model = ttt_model

    def calculate(self, final_temperature, cooling_rate):
        ms = self.ttt_model.martensite_start_temperature()
        martensite = 0.0 if final_temperature >= ms else (
            1 - __import__("math").exp(-0.011 * (ms - final_temperature))
        )
        martensite = max(0.0, min(1.0, martensite))
        retained = 1 - martensite

        if cooling_rate >= 30:
            transformation = "Predominantly Martensitic"
            bainite = (1 - martensite) * 0.10
            pearlite = 0.0
        elif cooling_rate >= 10:
            transformation = "Bainite + Martensite"
            bainite = (1 - martensite)
            pearlite = 0.0
        elif cooling_rate >= 3:
            transformation = "Pearlite + Bainite"
            bainite = 0.40
            pearlite = 0.60
            martensite = 0.0
            retained = 0.0
        else:
            transformation = "Predominantly Pearlite"
            bainite = 0.0
            pearlite = 1.0
            martensite = 0.0
            retained = 0.0

        total = martensite + bainite + pearlite
        available = 1 - retained
        if total > 0:
            scale = available / total
            martensite *= scale
            bainite *= scale
            pearlite *= scale

        return {
            "martensite": martensite * 100,
            "bainite": bainite * 100,
            "pearlite": pearlite * 100,
            "retained_austenite": retained * 100,
            "transformation": transformation,
        }
