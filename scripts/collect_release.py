"""Collect exactly the three platform bundles produced by the matrix."""
from pathlib import Path
import shutil

NAMES = (
    "little-signals-linux-x64.tar.gz",
    "little-signals-windows-x64.zip",
    "little-signals-macos-arm64.tar.gz",
)


def main():
    output = Path("release")
    output.mkdir(exist_ok=True)
    for name in NAMES:
        matches = list(Path("downloaded").glob(f"*/{name}"))
        if len(matches) != 1 or not matches[0].stat().st_size:
            raise SystemExit(f"Expected exactly one nonempty bundle: {name}")
        shutil.copy2(matches[0], output / name)
        print(f"Collected {name}")


if __name__ == "__main__":
    main()
