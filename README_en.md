
# Econ Policy Toolkit

A production-ready, mission-driven fork and extension tailored for policy economists and data analysts.
This project transforms a statistical core into a policy analysis platform with:
- Advanced econometric helpers (DID, event-study templates)
- Climate & geospatial utilities (GeoPandas + PySAL placeholders)
- Interactive dashboards (Streamlit demo included)
- Multi-language docs/support (English + Urdu)
- Interoperability with R, Stata, and common data sources (World Bank, IMF)

**Status:** Prototype with working demo connectors and examples. Some features (PySAL spatial regressions) require optional dependencies to be installed separately.

## Quickstart (local)
1. Create venv and install (recommended to use conda for GeoPandas):
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
For GeoPandas on many systems, consider using conda:
```bash
conda env create -f environment.yml
conda activate econ-policy
```

2. Run tests:
```bash
pytest -q
```

3. Run demo dashboard:
```bash
streamlit run dashboards/streamlit_app.py
```

## What changed in this build
- World Bank API connector with caching (`econ_policy_toolkit.api.worldbank`).
- Streamlit demo loads real World Bank indicators (cached) and presents simple charts.
- Demo DID notebook uses fetched data to create a toy evaluation and plot results.
- Spatial econometrics example scaffolding (`econ_policy_toolkit.geo.spatial_econ`) with instructions for PySAL.
- Sphinx docs skeleton and Urdu translation PO scaffold in `docs/locale/ur/LC_MESSAGES/messages.po`.

## Notes
- API calls are cached under `data/cache/` to avoid repeated requests during demos.
- Replace placeholders and extend notebooks/case studies to create your portfolio-ready artifacts.
