import shutil

du = shutil.disk_usage('/')

total_gb = du.total / (1024**3)
used_gb = du.used / (1024**3)
free_gb = du.free / (1024**3)

print(f"Общее местечко: {total_gb:.1f} ГБ")
print(f"Использовано: {used_gb:.1f} ГБ")
print(f"Free:         {free_gb:.1f} ГБ")


if free_gb < 5:
    print ("\n ВНИМАНИЕ: Свободного места меньше 5 ГБ! Почистите диск!")
else:
    print("\n Всё в порядке. Достаточно свободного места.")
    