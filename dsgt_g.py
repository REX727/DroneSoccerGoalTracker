import DSGT as t
import os
from time import sleep
import matplotlib.pyplot as plt
import numpy as np

UserInput = ""


file_list = t.ScanFile("Data")
t.PrintFileList(file_list)
path = t.AskPath()
lap_data = t.LoadData(path)

os.system("clear" if os.name == "nt" else "clear")
print(f"\n{t.GBOLD}Loaded {path}.txt with {len(lap_data)} goals.{t.END}\n")


y1 = np.array(lap_data)
print(y1)

file_list = t.ScanFile("Data")
t.PrintFileList(file_list)
path2 = t.AskPath()
lap_data2 = t.LoadData(path2)

y2 = np.array(lap_data2)
print(y2)

plt.figure(figsize=(10, 6))
plt.plot(y1, label=path, marker='o')
plt.plot(y2, label=path2, marker='s', linestyle = 'dashed')
plt.xlabel('Goal Number')
plt.ylabel('Time (seconds)')
plt.legend()
plt.grid(True)
plt.show()