import streamlit as st
import matplotlib.pyplot as plt

from database import list_materials, get_material
from phase_diagram import PhaseAnalyzer
from quenching import QuenchingModel
from ttt_model import TTTModel
from phase_fraction import PhaseFractionModel
from hardness_model import HardnessModel
from cct_model import CCTModel
from microstructure import MicrostructureModel
from jomini import JominyModel
from tempering import TemperingModel

st.set_page_config(page_title="METAL-X", page_icon="🔥", layout="wide")

st.title("🔥 METAL-X")
st.caption("Python-Based Heat Treatment & Metallurgical Transformation Simulator")

with st.sidebar:
    st.header("Simulation Inputs")
    material_name = st.selectbox("Steel Grade", list_materials())
    temperature = st.number_input("Austenitizing Temperature (°C)", 700.0, 1200.0, 850.0, 5.0)
    medium = st.selectbox("Quenching Medium", ["Furnace", "Air", "Oil", "Water", "Brine"])
    temper_temperature = st.number_input("Tempering Temperature (°C)", 100.0, 700.0, 450.0, 10.0)
    temper_time = st.number_input("Tempering Time (min)", 1.0, 300.0, 60.0, 5.0)
    run = st.button("RUN SIMULATION", type="primary")

steel = get_material(material_name)

col1, col2, col3 = st.columns(3)
col1.metric("Material", steel.name)
col2.metric("Carbon", f"{steel.carbon:.2f} wt%")
col3.metric("Quenching", medium)

if run:
    quench = QuenchingModel(temperature, 25.0, medium)
    time, temp = quench.generate()
    rate = quench.average_cooling_rate(800, 500) or 0.0

    ttt = TTTModel(steel)
    fractions = PhaseFractionModel(steel, ttt).calculate(temp[-1], rate)
    hardness = HardnessModel(steel).predict(fractions)
    micro = MicrostructureModel().classify(fractions)
    critical = CCTModel(steel).critical_temperatures()

    st.success("Simulation completed.")

    a, b, c, d = st.columns(4)
    a.metric("Hardness", f"{hardness['hardness_hv']:.0f} HV")
    b.metric("Martensite", f"{fractions['martensite']:.1f}%")
    c.metric("Bainite", f"{fractions['bainite']:.1f}%")
    d.metric("Pearlite", f"{fractions['pearlite']:.1f}%")

    st.subheader("Cooling Curve")
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(time, temp)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Temperature (°C)")
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)

    st.subheader("Transformation & Microstructure")
    st.write("**Classification:**", micro["classification"])
    st.write(f"**Estimated Ms:** {critical['Ms']:.1f} °C")
    st.write(f"**Estimated Mf:** {critical['Mf']:.1f} °C")
    st.write(f"**Average cooling rate (800→500°C):** {rate:.2f} °C/s")

    st.dataframe({
        "Phase": ["Martensite", "Bainite", "Pearlite", "Retained Austenite"],
        "Estimated Fraction (%)": [
            fractions["martensite"],
            fractions["bainite"],
            fractions["pearlite"],
            fractions["retained_austenite"],
        ],
    }, hide_index=True)

    st.subheader("Hardness")
    st.write(f"**Estimated hardness:** {hardness['hardness_hv']:.1f} HV")
    if hardness["hardness_hrc"] is not None:
        st.write(f"**Approximate hardness:** {hardness['hardness_hrc']:.1f} HRC")

    tempered = TemperingModel(hardness["hardness_hv"]).calculate(
        temper_temperature, temper_time
    )
    st.write(f"**Estimated hardness after tempering:** {tempered:.1f} HV")

    st.subheader("Jominy Hardenability — Model")
    positions, jhardness = JominyModel(steel).hardness_profile()
    fig2, ax2 = plt.subplots(figsize=(10, 4))
    ax2.plot(positions, jhardness, marker="o")
    ax2.set_xlabel("Distance from quenched end (mm)")
    ax2.set_ylabel("Estimated hardness (HV)")
    ax2.grid(True, alpha=0.3)
    st.pyplot(fig2)

else:
    st.info("Choose the material and heat-treatment conditions, then click RUN SIMULATION.")

st.divider()
st.caption("METAL-X is an educational simulation. Model outputs should be validated against material-specific experimental/literature data before engineering use.")
