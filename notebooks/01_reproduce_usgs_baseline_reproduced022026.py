#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pathlib import Path

# Calibration folder
cal_dir = Path(r"C:\Users\monic\Desktop\MF\MODFLOW_USGS_Reproduction\model")

# MF-NWT executable (adjust if using md_mfnwt_x64.exe)
exe = Path(r"C:\Users\monic\Desktop\MF\MODFLOW_USGS_Reproduction\bin\mfnwt.exe")

print("Executable exists:", exe.exists(), exe)
print("Calibration dir exists:", cal_dir.exists(), cal_dir)


# In[2]:


lst_files = list(cal_dir.glob("*.lst")) + list(cal_dir.glob("*.LIST")) + list(cal_dir.glob("*.list"))
print("LST files found:", [p.name for p in lst_files])

if lst_files:
    lst = lst_files[0]
    text = lst.read_text(errors="ignore")
    lines = text.splitlines()

    print("\n--- LST Diagnostics (ERROR / STOP / SEVERE) ---\n")
    for ln in lines:
        u = ln.upper()
        if "ERROR" in u or "STOP" in u or "SEVERE" in u:
            print(ln)
else:
    print("⚠️ No LST file found.")


# In[3]:


import subprocess

print("Running:", exe)
print("Working directory:", cal_dir)

res = subprocess.run(
    [str(exe), "umd_fb.nam"], 
    cwd=str(cal_dir),
    capture_output=True,
    text=True
)

print("✔ Model run completed.")
print("Return code:", res.returncode)

if res.stdout:
    print("\nSTDOUT:\n", res.stdout[:5000])
if res.stderr:
    print("\nSTDERR:\n", res.stderr[:5000])


# In[4]:


def human(n):
    for u in ["B","KB","MB","GB","TB"]:
        if n < 1024: 
            return f"{n:.0f} {u}"
        n /= 1024
    return f"{n:.1f} PB"

print("📁 UMD* output files:\n")
for p in sorted(cal_dir.glob("UMD*")):
    print(f"{p.name:22s} {human(p.stat().st_size):>8s}")


# In[9]:


pip install flopy


# In[11]:


from flopy.utils import HeadFile
import numpy as np

hds = cal_dir / "UMD.hds"

print("HDS exists:", hds.exists(), "size:", hds.stat().st_size)

hf = HeadFile(str(hds))
kstpkper = hf.get_kstpkper()

print("Saved timesteps:", len(kstpkper))
print("First 5:", kstpkper[:5])
print("Last 5 :", kstpkper[-5:])

# Final simulated heads
H_last = hf.get_data(kstpkper=kstpkper[-1])
print("Head array shape:", H_last.shape)
print("Mean head (layer 1):", float(np.nanmean(H_last[0])))


# In[12]:


import matplotlib.pyplot as plt

plt.figure(figsize=(7, 6))
plt.imshow(H_last[0], origin="lower")
plt.colorbar(label="Head (m)")
plt.title("Final Simulated Head – Layer 1")
plt.tight_layout()
plt.show()


# In[13]:


from flopy.utils import CellBudgetFile

cbc = cal_dir / "UMD.CBC.bin"
print("CBC exists:", cbc.exists(), "size:", cbc.stat().st_size)

cbf = CellBudgetFile(str(cbc))
labels = sorted({rec.strip() for rec in cbf.get_unique_record_names()})

print("📘 CBC record types (first 20):")
for lab in labels[:20]:
    print(" •", lab)


# In[14]:


hmin = float(np.nanmin(H_last[0]))
hmax = float(np.nanmax(H_last[0]))
hmean = float(np.nanmean(H_last[0]))

print("Layer 1 min:", hmin)
print("Layer 1 max:", hmax)
print("Layer 1 mean:", hmean)


# In[16]:


from pathlib import Path

cal_dir = Path(r"C:\Users\monic\Desktop\MF\MODFLOW_USGS_Reproduction\model")
lst = cal_dir / "UMD_f.lst"

print("LST exists:", lst.exists(), "size (MB):", lst.stat().st_size / (1024**2))

text = lst.read_text(errors="ignore")
up = text.upper()

for key in ["NORMAL TERMINATION", "ABNORMAL TERMINATION", "FAILED"]:
    print(f"\n--- Searching for '{key}' ---")
    if key in up:
        start = up.index(key)
        print(text[max(0, start-200): start+200])
    else:
        print("Not found.")


# In[17]:


from flopy.utils import HeadFile
import numpy as np

hds = cal_dir / "UMD.hds"
hf = HeadFile(str(hds))
kstpkper = hf.get_kstpkper()

print("Number of saved time steps:", len(kstpkper))
print("First 3:", kstpkper[:3])
print("Last 3:", kstpkper[-3:])

H_last = hf.get_data(kstpkper=kstpkper[-1])
print("Head array shape:", H_last.shape)
print("Min / Max / Mean (layer 1):",
      float(np.nanmin(H_last[0])),
      float(np.nanmax(H_last[0])),
      float(np.nanmean(H_last[0])))


# In[18]:


H1 = H_last[0]

# Mask criteria for real heads only
mask = (H1 < 900) & (H1 > -100) & (np.abs(H1) < 1e20)

hmin = float(np.nanmin(H1[mask]))
hmax = float(np.nanmax(H1[mask]))
hmean = float(np.nanmean(H1[mask]))

print("Masked Layer 1 min/max/mean:", hmin, hmax, hmean)



# In[19]:


plt.imshow(np.where(mask, H1, np.nan),
           origin="lower",
           vmin=hmin, vmax=hmax)
plt.colorbar()
plt.title("Final simulated head – Layer 1 (masked)")
plt.show()


# In[ ]:




