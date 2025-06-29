import string

path = "D:\.vscode\PythonPP\Py\EE"
for letter in string.ascii_uppercase:
    with open(f"{path}\\{letter}.txt", 'w') as f:
        f.write(letter)