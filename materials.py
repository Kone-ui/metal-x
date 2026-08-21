class Material:
    def __init__(self, name, carbon, manganese=0.0, silicon=0.0,
                 chromium=0.0, nickel=0.0, molybdenum=0.0):
        self.name = name
        self.carbon = carbon
        self.manganese = manganese
        self.silicon = silicon
        self.chromium = chromium
        self.nickel = nickel
        self.molybdenum = molybdenum

    def composition(self):
        return {
            "Carbon": self.carbon,
            "Manganese": self.manganese,
            "Silicon": self.silicon,
            "Chromium": self.chromium,
            "Nickel": self.nickel,
            "Molybdenum": self.molybdenum,
        }

    def display(self):
        print(f"\nMaterial: {self.name}")
        print("-" * 40)
        for element, percentage in self.composition().items():
            print(f"{element:<12}: {percentage:.2f}%")
