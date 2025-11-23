from pathlib import Path
import subprocess

def main():
    # Project root = one level up from this script
    project_root = Path(__file__).resolve().parents[1]

    model_dir = project_root / "model"
    exe       = project_root / "bin" / "mfnwt.exe"  # user must place this

    namfile   = "umd_fb.nam"

    print("Project root:", project_root)
    print("Model dir   :", model_dir)
    print("Executable  :", exe)

    if not exe.exists():
        raise FileNotFoundError(
            f"MF-NWT executable not found at {exe}. "
            "Place your mfnwt.exe in the bin/ folder."
        )

    if not (model_dir / namfile).exists():
        raise FileNotFoundError(
            f"Namefile {namfile} not found in {model_dir}."
        )

    # Run MODFLOW-NWT
    print("\nRunning MF-NWT...")
    res = subprocess.run(
        [str(exe), namfile],
        cwd=model_dir,
        capture_output=True,
        text=True
    )

    print("\nReturn code:", res.returncode)

    # Save logs
    logs_dir = project_root / "logs"
    logs_dir.mkdir(exist_ok=True)

    (logs_dir / "mf_nwt_stdout.log").write_text(res.stdout or "", errors="ignore")
    (logs_dir / "mf_nwt_stderr.log").write_text(res.stderr or "", errors="ignore")

    print("STDOUT and STDERR written to logs/")

    if res.returncode != 0:
        print("\n⚠️ Non-zero return code. Check logs/mf_nwt_stderr.log for details.")
    else:
        print("\n✅ Model run completed successfully.")

if __name__ == "__main__":
    main()
