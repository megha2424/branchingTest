import json

replace_text =""

f = open('cookiecutter.json')

data = json.load(f)

replace_text=data["ProjectName"].encode('utf-8')

print (replace_text)

search_text = "${{cookiecutter.ProjectName}}"

with open(r'test.yml', 'r') as file:

    data = file.read()
    data = data.replace(search_text, replace_text)

with open(r'test.yml', 'w') as file:
    file.write(data)

print("Text replaced" + replace_text + " _ _ " + search_text)