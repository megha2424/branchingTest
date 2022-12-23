
replace_text = "{{cookiecutter.Namespace}}.{{cookiecutter.ProjectName}}" 

print (replace_text)

working_directory_search_text = "[[project_working_directory]]"

print (working_directory_search_text)

project_full_name_search_text = "[[Namespace]].[[ProjectName]]"

print (project_full_name_search_text)

with open(r'../../.github/workflows/build.yml', 'r') as file:

    data = file.read()
    data = data.replace(working_directory_search_text, replace_text)
    data = data.replace(project_full_name_search_text, replace_text)

with open(r'../../.github/workflows/build.yml', 'w') as file:
    file.write(data)

print("Text replaced")

packageName_searchTest = "[[packageName]]"
packageName_replace_text = "{{cookiecutter.Namespace}}.{{cookiecutter.ProjectName}}PluginBase" 
with open(r'../../.github/workflows/release.yml', 'r') as file:

    data = file.read()
    data = data.replace(packageName_searchTest, packageName_replace_text)

with open(r'../../.github/workflows/release.yml', 'w') as file:
    file.write(data)
    
with open(r'../../.github/workflows/release-preview.yml', 'r') as file:

    data = file.read()
    data = data.replace(packageName_searchTest, packageName_replace_text)

with open(r'../../.github/workflows/release-preview.yml', 'w') as file:
    file.write(data)