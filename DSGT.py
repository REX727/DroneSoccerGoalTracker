import os
import datetime

BOLD = '\033[1m'
END = '\033[0m'
GBOLD = BOLD + '\033[32m'
RBOLD = BOLD + '\033[31m'
Split = "===================================================================================="
welcome_msg = print(f"{BOLD}Drone Soccer Goal Tracker{END}")

def SaveData(lap_data, path):
    save_data = ""
    for lap in range(len(lap_data)):
        save_data = save_data + str(lap_data[lap]) + '\n'
    os.chdir('DroneSoccerGoalTracker/Data')
    
    path_txt = path + ".txt"
    f = os.open(path_txt, os.O_RDWR|os.O_CREAT)
    os.write(f, save_data.encode())

    print(f"\n{GBOLD}Saved {path} in Data folder.{END}")
    
def LoadData(path):
    os.chdir('DroneSoccerGoalTracker/Data')
    lap_data = []

    path_txt = path + ".txt"
    f = open(path_txt, 'rt')
    for line in f:
        lap_data.append(float(line.strip()))
    return lap_data
    f.close()

def ScanFile(path):
    f = os.scandir(path)
    file_list = []
    for file in f:
        file_list.append(file.name)
    return file_list



lap_data = []

def UserInfo():
    UserName = input(f"Enter the {BOLD}User Name{END}: ").replace(" ", "_")

    ProfileName = input(f"Enter the {BOLD}Profile Name{END}: ").replace(" ", "_")
    path = UserName + "_" + ProfileName
    return path




def UserPrompt():
    UserInput = ""
    print(f"Enter lap time in seconds or type '{RBOLD}exit{END}' to quit:")

    while UserInput.lower() != "exit":
        UserInput = input(f"{GBOLD}GOAL {len(lap_data)+1}{END}: ")
        if UserInput.lower() != "exit":
                try:
                    lap_data.append(float(UserInput))
                except:
                    print(f"{RBOLD}VALUE ERROR{END}")
                    pass
        elif UserInput.lower() == "exit":
            return lap_data

def ExitProgram(path, lap_data):
            AvgTimes = round((sum(lap_data))/len(lap_data),2)
            
            print(f"{RBOLD}Exiting Program{END}")
            print(BOLD + "\n===== "+path+".txt =====" + END)
            for lap in range(len(lap_data)):
                  print(f"G{BOLD}{lap+1}{END}: {GBOLD}{lap_data[lap]}s{END}")
            print(Split)
            print(f"Total Goals: {GBOLD}{len(lap_data)}{END}")
            print(f"Average Seconds Per Goal: {GBOLD}{AvgTimes}s{END}(rounded to 2 decimal places)")

def AskPath():
    path = input(f"Enter the {BOLD}file name{END} to load (without .txt): ")
    return path

def PrintFileList(file_list):
    print(f"{GBOLD}Available files in Data folder:{END}") 
    for file in file_list:
        print(f"- {BOLD}{file}{END}")
