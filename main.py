import DSGT as t
import os
from time import sleep

UserInput = ""


print(t.Split)

while UserInput.lower() != 'q':
    UserInput = input(f"{t.GBOLD}Write mode{t.END} / {t.GBOLD}Read mode{t.END} / {t.RBOLD}quit{t.END} (w/r/q)? :")
    os.system("clear" if os.name == "nt" else "clear")

    if(UserInput.lower() == 'r'):
        file_list = t.ScanFile("Data")
        t.PrintFileList(file_list)
        path = t.AskPath()
        lap_data = t.LoadData(path)

        os.system("clear" if os.name == "nt" else "clear")
        print(f"\n{t.GBOLD}Loaded {path}.txt with {len(lap_data)} goals.{t.END}\n")
        for lap in range(len(lap_data)):
            sleep(lap_data[lap])
            print(f"{t.GBOLD}GOAL {lap+1} completed in {lap_data[lap]} seconds!{t.END}")
    elif(UserInput.lower() == 'w'):
        lap_data = []

        path = t.UserInfo()
        lap_data = t.UserPrompt()

        t.SaveData(lap_data, path)


        t.ExitProgram(path, lap_data)

    else:
        print(f"{t.RBOLD}INVALID INPUT{t.END}")
        print(t.Split)