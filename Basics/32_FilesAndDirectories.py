from pathlib import Path

# Absolute Path - from the root - c:\program files\microsoft or usr/local/bin
# Relative Path

path = Path("emails")
# Make a directory and Remove a directory
try:
    print(path.mkdir())  # Directory gets created in the current path i.e. Basics/emails
except FileExistsError:
    print("Directory already exists")
    print(path.rmdir())
    print("Directory Removed")

path2=Path()
# Search all the .py files in the current directory
for file in path2.glob('*.py'):
    print(file)

