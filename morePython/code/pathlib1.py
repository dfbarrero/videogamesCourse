from pathlib import Path

path = Path('data') / "file.txt"
# path is a Path object, not a string!
file = open(str(path))
