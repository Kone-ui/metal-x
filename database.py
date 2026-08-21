from materials import Material

STEEL_DATABASE = {
    "AISI 1040": Material("AISI 1040", 0.40, 0.75, 0.25),
    "AISI 1045": Material("AISI 1045", 0.45, 0.75, 0.25),
    "High Carbon 1.05": Material("High Carbon 1.05", 1.05, 0.40, 0.25),
    "AISI 4140": Material("AISI 4140", 0.40, 0.85, 0.25, 1.00, 0.0, 0.20),
    "AISI 4340": Material("AISI 4340", 0.40, 0.70, 0.25, 0.80, 1.80, 0.25),
    "AISI 52100": Material("AISI 52100", 1.00, 0.35, 0.25, 1.45),
    "AISI 304": Material("AISI 304", 0.08, 2.00, 1.00, 18.00, 8.00),
}

def get_material(name):
    return STEEL_DATABASE.get(name)

def list_materials():
    return list(STEEL_DATABASE.keys())
