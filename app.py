from database import get_material
from phase_diagram import PhaseAnalyzer
from quenching import QuenchingModel
from ttt_model import TTTModel
from phase_fraction import PhaseFractionModel
from hardness_model import HardnessModel
from cct_model import CCTModel
from microstructure import MicrostructureModel

MATERIAL_NAME = "AISI 1045"
AUSTENITIZING_TEMPERATURE = 850.0
QUENCHING_MEDIUM = "Water"

steel = get_material(MATERIAL_NAME)
if steel is None:
    raise ValueError("Material not found.")

steel.display()

analyzer = PhaseAnalyzer()
region = analyzer.analyze(steel.carbon, AUSTENITIZING_TEMPERATURE)

quench = QuenchingModel(
    initial_temperature=AUSTENITIZING_TEMPERATURE,
    final_temperature=25.0,
    medium=QUENCHING_MEDIUM,
)

time, temperature = quench.generate()
rate = quench.average_cooling_rate(800, 500) or 0.0

ttt = TTTModel(steel)
fractions = PhaseFractionModel(steel, ttt).calculate(
    temperature[-1], rate
)

hardness = HardnessModel(steel).predict(fractions)
micro = MicrostructureModel().classify(fractions)
critical = CCTModel(steel).critical_temperatures()

print("\nMETAL-X SIMULATION")
print("=" * 50)
print("Material:", steel.name)
print("Carbon:", steel.carbon, "%")
print("Austenitizing:", AUSTENITIZING_TEMPERATURE, "°C")
print("Quenching medium:", QUENCHING_MEDIUM)
print("Initial phase region:", region)
print("Average cooling rate (800→500°C):", round(rate, 2), "°C/s")
print("Ms:", round(critical["Ms"], 2), "°C")
print("Mf:", round(critical["Mf"], 2), "°C")

print("\nPHASE FRACTIONS")
print("-" * 30)
for key in ["martensite", "bainite", "pearlite", "retained_austenite"]:
    print(f"{key.replace('_', ' ').title():20}: {fractions[key]:.2f}%")

print("\nMICROSTRUCTURE")
print("-" * 30)
print(micro["classification"])

print("\nHARDNESS")
print("-" * 30)
print("Estimated HV:", round(hardness["hardness_hv"], 1))
if hardness["hardness_hrc"] is not None:
    print("Approximate HRC:", round(hardness["hardness_hrc"], 1))

print("\nNOTE: Results are simplified educational estimates, not experimental certification.")
