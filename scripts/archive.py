"""Archive the native PyInstaller folder before Actions can lose its permissions."""
import argparse
from pathlib import Path
import shutil

FORMATS = {"linux-x64": "gztar", "macos-arm64": "gztar", "windows-x64": "zip"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("platform", choices=FORMATS)
    args = parser.parse_args()
    root = Path("dist")
    executable = root / "LittleSignals" / ("LittleSignals.exe" if args.platform == "windows-x64" else "LittleSignals")
    if not executable.is_file():
        raise SystemExit(f"Missing packaged executable: {executable}")
    Path("packages").mkdir(exist_ok=True)
    archive = shutil.make_archive(f"packages/little-signals-{args.platform}", FORMATS[args.platform],
                                  root_dir=root, base_dir="LittleSignals")
    print(f"Created {archive}")


if __name__ == "__main__":
    main()
