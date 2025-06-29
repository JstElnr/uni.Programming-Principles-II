import re

#1
x = 'ab'
print(re.search('a.*b', x))

#2
x='axxb'
print(re.search(r'a.{1,2}b', x))

#3
x = 'hello_world'
print(re.findall(r'[a-z]+_[a-z]+', x))

#4
x = 'Python'
print(re.findall(r'[A-Z][a-z]+', x))

#5
x = 'aaaaaab'
print(re.search('a.*b$', x))

#6
x = 'Hello, World.'
print(re.sub(r'[ .,]', ':', x))

#7
x = 'hello_world'
print(re.sub(r'_([a-z])', lambda x: x.group(1).upper(), x))

#8
x = 'HelloWorld'
print(re.findall(r'[A-Z][a-z]*', x))

#9

x = "HelloWorld"
print(re.sub(r'(?<!^)([A-Z])', r' \1', x))

#10
x= "HelloWorld"
print(re.sub(r'([A-Z])', r'_\1', x).lower().lstrip('_'))