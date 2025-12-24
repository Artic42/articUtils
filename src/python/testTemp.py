import psutil

temps = psutil.sensors_temperatures()
coretemp = temps["coretemp"]
for element in coretemp:
    print(element)
