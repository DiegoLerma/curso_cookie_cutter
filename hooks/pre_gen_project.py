import os
import sys

project_slug = "{{ cookiecutter.project_slug }}"

ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

if project_slug.startswith("x"):
    print(f"{ERROR_COLOR}ERROR: {MESSAGE_COLOR} {project_slug} is not a valid name for this project. Please use a valid name{RESET_ALL}")
    
    sys.exit(1)

print(f"{MESSAGE_COLOR}A buebo! Piensa en cosas chingonas{RESET_ALL}")
print(f"Creando proyecto en{ os.getcwd() }{RESET_ALL}")