import os

path = "D:\.vscode\PythonPP\Py\QQ\AA"
if os.path.exists(path) and os.path.isfile(path) and os.access(path, os.W_OK):
    os.remove(path)