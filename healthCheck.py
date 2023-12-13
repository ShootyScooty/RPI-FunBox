import subprocess

out = str(subprocess.check_output(['cat botHealth.py | ssh aidan@192.168.1.31 python -']))

print(out)

# mcBot = out.split("\n     ")

# for x in mcBot:
#     print(x)