import sys
import shutil
from pathlib import Path

def recursive_copy(src: Path, dst: Path):
    try:
        for item in src.iterdir():
            if item.is_dir():

                recursive_copy(item, dst)

            else:

                folder = item.suffix[1:] if item.suffix else "others"
                target_dir = dst / folder
                target_dir.mkdir(parents=True, exist_ok=True)
                shutil.copy(item, target_dir / item.name)
                
    except Exception as e:
        print(f"Error processing {src}: {e}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python task1.py <source_dir> [output_dir]")
        return

    src = Path(sys.argv[1])
    dst = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("dist")

    if not src.exists():
        print("Error: Source directory does not exist.")
        return

    recursive_copy(src, dst)
    print("Files sorted successfully.")

if __name__ == "__main__":
    main()