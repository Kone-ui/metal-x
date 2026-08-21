# METAL-X

Python-based heat-treatment and metallurgical transformation simulator.

## Features
- Steel material database
- Simplified Fe-C phase analysis
- Quenching-media cooling curves
- TTT-inspired transformation model
- CCT cooling classification
- Phase-fraction estimation
- Martensite estimation
- Hardness estimation
- Tempering model
- Jominy hardenability model
- Streamlit web interface

## Run desktop/console version

```bash
pip install -r requirements.txt
python app.py
```

## Run web version

```bash
streamlit run streamlit_app.py
```

## Important scientific limitation

The current models are educational/simplified models. They are not validated experimental data and should not be used as certified engineering predictions. A future research-grade version should use material-specific TTT/CCT/Jominy/hardness datasets and compare predictions against experimental measurements.
