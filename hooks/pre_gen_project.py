
replace_text = "{{cookiecutter.ProjectName}}" 

print (replace_text)

search_text = "[[project_working_directory]]"

print (search_text)

with open(r'../../.github/workflows/build.yml', 'r') as file:
    data = file.read()
    data = data.replace(search_text, replace_text)

with open(r'../../.github/workflows/build.yml', 'w') as file:
    file.write(data)

print("Text replaced")