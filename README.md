# Miami Groundwater–Canal System Hydrologic Model (MODFLOW-NWT + FloPy)
**A Python-first, reproducible workflow (FloPy + pymake) for re-running and modernizing the original USGS urban groundwater–surface water model for Miami-Dade County, Florida.**  
_Adapted from USGS ScienceBase Release:_ https://www.sciencebase.gov/catalog/item/631405b1d34e36012efa2e68  
---

## 📍 Overview
This repository reconstructs, modernizes, and operationalizes the U.S. Geological Survey (USGS) groundwater–surface water model originally developed to evaluate hydrologic conditions in urban Miami-Dade County from 1996–2010. The published model analyzes canal leakage, groundwater dynamics, and the influence of sea-level rise and groundwater pumpage using MODFLOW-NWT with SWR (Surface Water Routing) and SWI2 (Seawater Intrusion) packages.

This project provides a fully scripted, Python-based workflow for reproducing the model using modern tools (FloPy + pymake), ensuring transparent execution, georeferenced output analysis, and a structured foundation for future scenario testing.

The main goal of the reproduction will enable evaluation of groundwater response under specific storm conditions (e.g., Hurricanes Matthew 2016, Irma 2017, and Tropical Storm Eta 2020) to investigate groundwater contributions to urban flooding.

---

## 📘 Source Reference
This work is based on the USGS model and report:

> Hughes, J.D., and White, J.T., 2016, Model archive of the simulation of hydrologic conditions and the effects of increased groundwater pumpage and increased sea level on canal leakage in the urbanized area of Miami-Dade County, Florida, 1996–2010: U.S. Geological Survey data release, https://doi.org/10.5066/F79P2ZRH  

> Hughes, J.D., 2014, Hydrologic conditions in urban Miami-Dade County, Florida, and the effect of increased sea level on canal leakage and regional groundwater flow: U.S. Geological Survey Scientific Investigations Report 2014–5162.  

---

## 🎯 Project Objectives (Baseline Scope)
✅ Reuse a validated USGS MODFLOW conceptual and numerical framework as the scientific baseline.  
✅ Automate retrieval of the ScienceBase model release and apply provided geospatial metadata for model output georeferencing.  
✅ Compile the required custom **MODFLOW-NWT executable** (with the GFD boundary package) using `pymake`.  
✅ Execute the original calibration (1997–2004) and verification (2005–2010) simulations.  
✅ Post-process heads, budgets, and canal interactions using **FloPy utilities**.  
✅ Re-host the full model workflow in a structured, Python-first environment.  
✅ Support open science and replication through environment documentation, automation scripts, and GitHub-based sharing.

---

## 📈 Future Extensions (Beyond Original Scope or reproduction)
🚀 Implement event-based storm analyses in reproducible Jupyter/FloPy workflows.  
🚀 Assess groundwater table rise and canal leakage behavior during flood events.  
🚀 Evaluate the role of subsurface conditions as drivers in urban flood dynamics.  
🚀 Provide a platform for later coupling with coastal surge and surface flooding models.  

---

## 🌐 Study Domain (Miami Urban Coastal Region)
- Groundwater: Biscayne Aquifer  
- Canals: Little River, Snapper Creek, S-28/S-29/S-31 flow systems  
- Coastal Boundary: Biscayne Bay + NOAA Virginia Key gauge  
- Hydrologic Unit Codes: **HUC 0309020614 (inland core) + section of 0309020618 (coastal influence)**  
- Planned grid: **5–50 m variable cell DISV** (to reflect canal/well density)

---

## 📦 Storm Events & Time Windows
| Event | Approx Time Window | Data Sources |
|-------|-------------------|--------------|
| Hurricane Matthew (2016) | Sep 30 – Oct 10, 2016 | NOAA rainfall + tide + USGS groundwater |
| Hurricane Irma (2017) | Sep 6 – Sep 20, 2017 | NOAA, USGS, FRIS Canal Ops |
| Tropical Storm Eta (2020) | Nov 3 – Nov 15, 2020 | NOAA, NEXRAD, USGS G-852 & S-28 |

📌 Finalized windows can be modified in `./scripts/event_setup.py`

---

## 🛠️ Model Framework Transition
| Component | Original USGS Model | Current Version | Planned Upgrade |
|-----------|--------------------|----------------|-----------------|
| Engine | MODFLOW (legacy) | MODFLOW 6 (FloPy) | Fully Py-based |
| Grid | Structured | HUC-based DISV | Canal-structured DISV |
| Boundaries | Generalized | Miami CHD/GHB | Coupled Delft3D |
| Input style | Raw files | Python scripts | GUI + web access |
| Calibration | Provided | Revalidated | Auto-cal via PEST |

---

## 📂 Repository Structure (GitHub Layout)
