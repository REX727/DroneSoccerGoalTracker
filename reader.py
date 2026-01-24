import ui as u
import translator as t
from time import sleep
import os

print(f"{u.GBOLD}Available files in Data folder:{u.END}")
file_list = t.ScanFile("DroneSoccerGoalTracker/Data")   
for file in file_list:
    print(f"- {u.BOLD}{file}{u.END}")
path = u.AskPath()

lap_data = t.LoadData(path)

os.system("clear" if os.name == "nt" else "clear")
print(f"\n{u.GBOLD}Loaded {path}.txt with {len(lap_data)} goals.{u.END}\n")
for lap in range(len(lap_data)):
    sleep(lap_data[lap])
    print(f"{u.GBOLD}GOAL {lap+1} completed in {lap_data[lap]} seconds!{u.END}")
