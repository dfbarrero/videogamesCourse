from pathlib import Path

# Create directory structure
project = Path('my_project')
data_dir = project / 'data'
data_dir.mkdir(parents=True, exist_ok=True)

# Create and write file
file_path = data_dir / 'output.txt'
file_path.write_text('Hello from pathlib!\n', encoding='utf-8')

# Check if file exists
if file_path.exists():
    print(f"File created: {file_path}")
    print(f"Size: {file_path.stat().st_size} bytes")
    
# Read file contents
content = file_path.read_text(encoding='utf-8')
print(f"Content: {content}")

