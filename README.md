# Miami Groundwater–Canal System Hydrologic Model (MODFLOW-NWT + FloPy)
**A Python-first, reproducible workflow (FloPy + pymake) for re-running and modernizing the original USGS urban groundwater–surface water model for Miami-Dade County, Florida.**  
_Adapted from USGS ScienceBase Release:_ https://www.sciencebase.gov/catalog/item/631405b1d34e36012efa2e68  
---

##  Overview
This repository reconstructs, modernizes, and operationalizes the U.S. Geological Survey (USGS) groundwater–surface water model originally developed to evaluate hydrologic conditions in urban Miami-Dade County from 1996–2010. The published model analyzes canal leakage, groundwater dynamics, and the influence of sea-level rise and groundwater pumpage using MODFLOW-NWT with SWR (Surface Water Routing) and SWI2 (Seawater Intrusion) packages.

# Reproducing the USGS Miami-Dade (UMD) MODFLOW-NWT Groundwater–Surface Water Model

[![Python 3.10](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/Monclau1260/MODFLOW_USGS_Reproduction.svg)](https://github.com/Monclau1260/MODFLOW_USGS_Reproduction/commits/main)
[![OS](https://img.shields.io/badge/OS-Windows%2010%2F11-informational.svg)](#)

This repository provides a structured, reproducible, Python-first workflow for reconstructing and re-running the U.S. Geological Survey (USGS) **Urban Miami-Dade (UMD)** MODFLOW-NWT groundwater–surface water model.

The goal is to enable other users (students, researchers, agencies, and practitioners) to:

- Reproduce the baseline USGS UMD simulation using MODFLOW-NWT.
- Work in a modern Python environment (FloPy, Jupyter).
- Perform post-processing and visualization of groundwater heads, budgets, and related diagnostics.
- Use this baseline as a platform for further scenario analysis and research.

All required **small model input files** (for example, `umd.bas`, `umd.dis`, `umd.ets`, `umd.swr`, etc.) are included in this repository under `model/`.  
Large output files (e.g., `UMD.hds`, `UMD.CBC.bin`, `UMD.zta`) are **not** included and will be generated locally when the model is executed. They are excluded from version control via `.gitignore` to keep the repository lightweight.

---

## 1. Repository Structure

```text
MODFLOW_USGS_Reproduction/
│
├── bin/                      # User-supplied MODFLOW-NWT executable (mfnwt.exe)
├── data/                     # Optional supplemental data (not required for baseline run)
├── model/                    # USGS model input files (small, text-based)
│     ├── umd_fb.nam          # Namefile
│     ├── umd.bas             # BAS package
│     ├── umd.dis             # DIS package
│     ├── umd.lpf             # LPF package
│     ├── umd.ets             # ETS package
│     ├── umd.swr             # SWR package
│     ├── umd.swi             # SWI package
│     ├── umd.hyd             # HYDMOD definitions
│     ├── umd.gfb             # Boundary / GHB-related package
│     ├── umd.nwt             # NWT solver options
│     ├── umd.wel             # WEL package
│     ├── umd_obs.drn         # Drain observations
│     ├── umd_obs.ghb         # GHB observations
│     ├── UMD_f.oc            # Output control
│     └── ...                 # Other small input/backup files
│
├── notebooks/
│     └── 01_reproduce_usgs_baseline.ipynb
│                            # Main Jupyter notebook for baseline reproduction
│
├── scripts/
│     └── run_model.py       # Python driver script to execute MODFLOW-NWT
│
├── logs/                    # Runtime logs (created automatically)
│     ├── mf_nwt_stdout.log
│     └── mf_nwt_stderr.log
│
├── .gitignore               # Excludes large binaries, executables, logs from version control
├── LICENSE                  # MIT License
└── README.md

---
## 1. Repository Structure
```text
MODFLOW_USGS_Reproduction/
│
├── bin/                      # User-supplied MODFLOW-NWT executable (mfnwt.exe)
├── data/                     # Optional supplemental data (not required for baseline run)
├── model/                    # USGS model input files (small, text-based)
│     ├── umd_fb.nam          # Namefile
│     ├── umd.bas             # BAS package
│     ├── umd.dis             # DIS package
│     ├── umd.lpf             # LPF package
│     ├── umd.ets             # ETS package
│     ├── umd.swr             # SWR package
│     ├── umd.swi             # SWI package
│     ├── umd.hyd             # HYDMOD definitions
│     ├── umd.gfb             # Boundary / GHB-related package
│     ├── umd.nwt             # NWT solver options
│     ├── umd.wel             # WEL package
│     ├── umd_obs.drn         # Drain observations
│     ├── umd_obs.ghb         # GHB observations
│     ├── UMD_f.oc            # Output control
│     └── ...                 # Other small input/backup files
│
├── notebooks/
│     └── 01_reproduce_usgs_baseline.ipynb
│                            # Main Jupyter notebook for baseline reproduction
│
├── scripts/
│     └── run_model.py       # Python driver script to execute MODFLOW-NWT
│
├── logs/                    # Runtime logs (created automatically)
│     ├── mf_nwt_stdout.log
│     └── mf_nwt_stderr.log
│
├── .gitignore               # Excludes large binaries, executables, logs from version control
├── LICENSE                  # MIT License
└── README.md
---
##2. Prerequisites
Operating system: Windows 10/11 (tested)
Anaconda or Miniconda (recommended)
Git
MODFLOW-NWT executable (mfnwt.exe), obtained from USGS distribution
Internet connection (only needed to clone the repository)
---
##3. Clone the Repository

From a terminal (Command Prompt, PowerShell, or Anaconda Prompt):
## Source Reference
This work is based on the USGS model and report:
```bash
git clone https://github.com/Monclau1260/MODFLOW_USGS_Reproduction
cd MODFLOW_USGS_Reproduction
---
##4. Create and Activate the Python Environment
Create a dedicated Conda environment:
```bash
conda create -n modflow_usgs python=3.10
conda activate modflow_usgs
---
Install required Python packages:
```bash
pip install flopy numpy pandas matplotlib jupyterlab
Additional packages (optional but useful):
```bash
pip install scipy
---
##5. Add the MODFLOW-NWT Executable
The UMD model is built for MODFLOW-NWT.
Download the appropriate mfnwt.exe from the official USGS distribution and place it into the bin/ directory:
```text
Download the appropriate mfnwt.exe from the official USGS distribution and place it into the bin/ directory:
MODFLOW_USGS_Reproduction/
│
└── bin/
       └── mfnwt.exe
The executable is intentionally excluded from this repository due to size and distribution constraints.
---
##6. Model Input Files
All required small model input files from the USGS UMD calibration are already present in the model/ directory, including:
umd_fb.nam – Namefile
umd.bas – Basic package
umd.dis – Discretization package
umd.lpf – Layer property flow
umd.ets – Evapotranspiration
umd.swr – Surface-Water Routing (SWR1)
umd.swi – Saltwater Interface (SWI) configuration
umd.hyd – HYDMOD configuration
umd.gfb – Boundary conditions (e.g., GHB-related file)
umd.nwt – NWT solver settings
umd.wel – Wells
umd_obs.drn, umd_obs.ghb – Observation files
UMD_f.oc – Output control file
Additional small backup/auxiliary text files
No additional downloads of input files are required for this baseline reproduction.
---
##7. Running the UMD Model
The repository includes a Python script to execute the full baseline simulation:
```text
scripts/run_model.py
From the repository root:
```bash
python scripts/run_model.py
---
This script will:
Resolve the project root directory.
Verify that bin/mfnwt.exe exists.
Verify that model/umd_fb.nam exists.
Execute MODFLOW-NWT in the model/ directory using umd_fb.nam.
Capture standard output and error into:
logs/mf_nwt_stdout.log
logs/mf_nwt_stderr.log
Upon successful completion, the script will return exit code 0. ! rc must be 0!
Due to the size and length of the original USGS simulation (5,479 saved timesteps), the run may require several hours depending on hardware and disk performance.
---
##8. Output Files and Reproducibility
After the model run, the model/ directory will contain large binary output files, including (but not limited to):
UMD.hds – Binary heads
UMD.CBC.bin – Cell-by-cell flow budget
UMD.zta – Zeta surfaces (SWI)
UMD.stg – Stage data
UMD.pqm, UMD.fls, UMD.qaq, etc.
These files are generated locally on the user’s machine; they are not tracked by Git; they are excluded via .gitignore and they Are used by notebooks and analysis scripts for post-processing.
This design keeps the repository small while maintaining full scientific reproducibility.
---
##9. Post-Processing and Visualization
The main notebook for reproducing and inspecting the baseline simulation is:
```text
notebooks/01_reproduce_usgs_baseline.ipynb
```bash
jupyter lab
or
```bash
jupyter notebook
```text
notebooks/01_reproduce_usgs_baseline.ipynb
The notebook demonstrates, for example:
Loading heads:
```python
import flopy
from pathlib import Path
model_dir = Path("model")
hds_path = model_dir / "UMD.hds"
hds = flopy.utils.HeadFile(hds_path)
kstpkper = hds.get_kstpkper()
head_last = hds.get_data(kstpkper=kstpkper[-1])

Inspecting shapes and ranges (e.g., layers, rows, columns).
Loading cell-by-cell budgets:
```python
cbc_path = model_dir / "UMD.CBC.bin"
cbc = flopy.utils.CellBudgetFile(cbc_path)
records = cbc.get_unique_record_names()

Generating maps of groundwater heads (plan views) for selected layers and times.
Creating cross-sections along user-defined rows or columns.
Examining budget components (e.g., leakage, canal exchange, recharge contributions).
Extracting and plotting time series at specific model cells or observation locations.
The notebook serves both as documentation and as a template for further analysis (e.g., linking heads and budgets to surface flooding indicators).
---
##10. .gitignore and Large Files
The .gitignore file is configured to exclude:
Large MODFLOW output binaries (*.hds, *.cbc, *.bin, *.zta, etc.).
MODFLOW-NWT executables (bin/, *.exe, *.dll).
Log files (logs/).
Jupyter checkpoint directories (.ipynb_checkpoints/).
OS-specific temporary files (e.g., Thumbs.db, .DS_Store).
This ensures that large outputs are generated locally and not pushed to GitHub and executables are kept local to each user’s environment.
---
##11. Intended Use and Scope:
Educational use in groundwater hydrology and integrated surface-water/groundwater modeling.
Research replication and exploration of the published USGS UMD model.
A starting point for scenario analysis (e.g., alternative forcing, boundary conditions, or climate/event sequences).
Integration with additional tools (e.g., machine-learning workflows, event-based flood modeling, or coupled surface-water models).
The current focus is on baseline reproduction and post-processing. Extensions and scenario workflows can be added on top of this foundation.
---
##12. Citation
This workflow underlies the USGS model in scientific and technical work, as indicated in the overview and title of this repository. 

> Hughes, J.D., and White, J.T., 2016, Model archive of the simulation of hydrologic conditions and the effects of increased groundwater pumpage and increased sea level on canal leakage in the urbanized area of Miami-Dade County, Florida, 1996–2010: U.S. Geological Survey data release, https://doi.org/10.5066/F79P2ZRH  
> Hughes, J.D., 2014, Hydrologic conditions in urban Miami-Dade County, Florida, and the effect of increased sea level on canal leakage and regional groundwater flow: U.S. Geological Survey Scientific Investigations Report 2014–5162.
> Langevin, C.D., 2014, Documentation for the SWR1 Package—A Surface-Water Routing Process for Modeling Surface-Water and Groundwater Interactions: U.S. Geological Survey Techniques and Methods, book 6, chap. A46.
---
##13. License
The code and configuration files in this repository are released under the MIT License.
See the USGS LICENSE  file for full terms. The MODFLOW-NWT executable (mfnwt.exe) is distributed by USGS under its own terms.
The conceptual and numerical model design is based on USGS work and associated publications and data releases.
Users are responsible for complying with all applicable licenses and citation requirements when using the underlying USGS model and tools.
---
Next phase 
##  Project Objectives (Baseline Scope)
✅ Reuse a validated USGS MODFLOW conceptual and numerical framework as the scientific baseline.  
✅ Automate retrieval of the ScienceBase model release and apply provided geospatial metadata for model output georeferencing.  
✅ Compile the required custom **MODFLOW-NWT executable** (with the GFD boundary package) using `pymake`.  
✅ Execute the original calibration (1997–2004) and verification (2005–2010) simulations.  
✅ Post-process heads, budgets, and canal interactions using **FloPy utilities**.  
✅ Re-host the full model workflow in a structured, Python-first environment.  
✅ Support open science and replication through environment documentation, automation scripts, and GitHub-based sharing.

---

## Future Extensions (Beyond Original Scope or reproduction)
- Implement event-based storm analyses in reproducible Jupyter/FloPy workflows.  
- Assess groundwater table rise and canal leakage behavior during flood events.
- Evaluate the role of subsurface conditions as drivers in urban flood dynamics.
-  Provide a platform for later coupling with coastal surge and surface flooding models.  

---

##  Study Domain (Miami Urban Coastal Region)
- Groundwater: Biscayne Aquifer  
- Canals: Little River, Snapper Creek, S-28/S-29/S-31 flow systems  
- Coastal Boundary: Biscayne Bay + NOAA Virginia Key gauge  
- Hydrologic Unit Codes: **HUC 0309020614 (inland core) + section of 0309020618 (coastal influence)**  
- Planned grid: **5–50 m variable cell DISV** (to reflect canal/well density)

---

## Storm Events & Time Windows
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
