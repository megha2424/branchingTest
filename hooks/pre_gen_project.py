import json

replace_text =""

f = open('../../cookiecutter.json')

data = json.load(f)

replace_text = data["ProjectName"].encode('utf-8')

print (replace_text)

search_text = "${{cookiecutter.ProjectName}}"

with open(r'../../.github/workflows/build.yml', 'r') as file:

    data = file.read()
    data = data.replace(search_text, replace_text.decode('utf-8'))

with open(r'../../.github/workflows/build.yml', 'w') as file:
    file.write(data)

print("Text replaced")