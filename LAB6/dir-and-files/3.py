import os

path = "D:\.vscode\PythonPP\Py"
if os.path.exists(path):
    print("Exist")
    print("File:", os.path.basename(path))
else:
    print("Doesn't exist")