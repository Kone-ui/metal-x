class JominyModel:
    def __init__(self, material):
        self.material = material

    def hardness_profile(self):
        carbon = self.material.carbon
        positions = [0, 5, 10, 15, 20, 25, 30, 40, 50]
        base = 180 + 900 * carbon
        hardness = [max(150, base - position * 3) for position in positions]
        return positions, hardness
