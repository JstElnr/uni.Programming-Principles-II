import os

path = "D:\.vscode\PythonPP\Py"
print("existence:", os.path.exists(path))
print("readability:", os.access(path, os.R_OK))
print("writability:", os.access(path, os.W_OK))
print("executability:", os.access(path, os.X_OK))