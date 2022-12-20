import json

replace_text =""

f = open('../../cookiecutter.json')

data = json.load(f)

replace_text = data["ProjectName"].encode('utf-8')

print (replace_text.decode('utf-8'))

search_text = "${{cookiecutter.ProjectName}}"

print (search_text)

with open(r'../../.github/workflows/build.yml', 'r') as file:

    data = file.read()
    print(data)
    data = data.replace(search_text, replace_text.decode('utf-8'))
    print(data)

with open(r'../../.github/workflows/build.yml', 'w') as file:
    file.write(data)

print("Text replaced")