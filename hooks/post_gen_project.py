import subprocess

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL="\x1b[0m"

print(f"{MESSAGE_COLOR}Estamos configurando este pedo...{RESET_ALL}")

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Primero lo primero'])

print(f"{MESSAGE_COLOR}Se jugo y se gano!. Plantilla creada{RESET_ALL}")