class MicrostructureModel:
    def classify(self, phases):
        m = phases["martensite"]
        b = phases["bainite"]
        p = phases["pearlite"]

        if m > 80:
            classification = "Predominantly Martensitic"
        elif m > 50:
            classification = "Martensite + Bainite"
        elif b > 50:
            classification = "Predominantly Bainitic"
        elif p > 60:
            classification = "Predominantly Pearlitic"
        else:
            classification = "Mixed Microstructure"

        return {
            "classification": classification,
            **phases,
        }
