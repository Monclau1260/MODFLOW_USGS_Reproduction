from pathlib import Path
import subprocess


def main():
    # Project root is one level above this script
    project_root = Path(__file__).resolve().parents[1]

    model_dir = project_root / "model"
    exe = project_root / "bin" / "mfnwt.exe"  # your MF-NWT executable
    namfile = "umd_fb.nam"  # main namefile for the UMD model

    print("Project root :", project_root)
    print("Model folder :", model_dir)
    print("Executable   :", exe)

    # Basic checks
    if not exe.exists():
        raise FileNotFoundError(
            f"MF-NWT executable not found at {exe}.\n"
            "Make sure mfnwt.exe is placed in the bin/ folder."
        )

    nam_path = model_dir / namfile
    if not nam_path.exists():
        raise FileNotFoundError(
            f"Namefile {namfile} not found in {model_dir}.\n"
            "Check that your model input files are in the model/ folder."
        )

    # Create logs folder
    logs_dir = project_root / "logs"
    logs_dir.mkdir(exist_ok=True)

    print("\nRunning MF-NWT...")
    # Run MODFLOW-NWT in the model directory
    res = subprocess.run(
        [str(exe), namfile],
        cwd=str(model_dir),
        capture_output=True,
        text=True,
    )

    print("\nReturn code:", res.returncode)

    # Save stdout / stderr to logs for debugging
    (logs_dir / "mf_nwt_stdout.log").write_text(res.stdout or "", errors="ignore")
    (logs_dir / "mf_nwt_stderr.log").write_text(res.stderr or "", errors="ignore")

    print(f"\nSTDOUT written to: {logs_dir / 'mf_nwt_stdout.log'}")
    print(f"STDERR written to: {logs_dir / 'mf_nwt_stderr.log'}")

    if res.returncode != 0:
        print("\n⚠️ Non-zero return code. Check mf_nwt_stderr.log for details.")
    else:
        print("\n✅ Model run completed successfully.")


if __name__ == "__main__":
    main()

