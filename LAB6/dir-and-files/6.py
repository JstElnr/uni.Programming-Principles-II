source = "D:\.vscode\PythonPP\Py\EE\A.txt"
destiny = "D:\.vscode\PythonPP\Py\QQ\AAA"
with open(source) as s:
    with open(destiny, 'w') as d:
        d.write(s.read())