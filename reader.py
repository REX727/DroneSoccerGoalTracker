import DSGT as t
import os
from time import sleep

file_list = t.ScanFile("DroneSoccerGoalTracker/Data")
t.PrintFileList(file_list)
path = t.AskPath()
lap_data = t.LoadData(path)

os.system("clear" if os.name == "nt" else "clear")
print(f"\n{t.GBOLD}Loaded {path}.txt with {len(lap_data)} goals.{t.END}\n")
for lap in range(len(lap_data)):
    sleep(lap_data[lap])
    print(f"{t.GBOLD}GOAL {lap+1} completed in {lap_data[lap]} seconds!{t.END}")
