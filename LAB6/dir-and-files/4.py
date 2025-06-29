list = ["apple", "banana", "orange"]
path = "D:\.vscode\PythonPP\Py\ fruits.txt"
with open(path, 'w') as f:
    f.write('\n'.join(list))