import platform
from datetime import datetime

print("Ola! App Python rodando dentro de um container Docker.")
print(f"Sistema: {platform.system()} {platform.release()}")
print(f"Python: {platform.python_version()}")
print(f"Executado em: {datetime.now():%d/%m/%Y %H:%M:%S}")
