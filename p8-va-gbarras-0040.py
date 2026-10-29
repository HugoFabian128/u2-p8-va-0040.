import matplotlib.pyplot as plt
import numpy as np


diasx=["lun","mar","mie","jue","vie"]
califa_va_y=[5,6,3,8,10]

plt.bar(diasx,califa_va_y)
plt.title("califas en VA de Hugo Fabian NC 0040")
plt.xlabel("dias de la semana habil")
plt.ylabel("calificaciones en VA")
plt.grid()
plt.show()