try:
    with open("D:\.vscode\PythonPP\Py\ fruits.txt", 'r') as file:
        print("Lines:", len(file.readlines()))
except:
    print("File not found!")