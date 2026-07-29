import sla2
import importlib


for i in range(10):
    importlib.reload(sla2)
    print(f"{i + 1}")