from pathlib import Path

for i in Path("/home/david").iterdir():
    print(i)
