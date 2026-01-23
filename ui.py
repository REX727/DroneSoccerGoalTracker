#ui module
import datetime

BOLD = '\033[1m'
END = '\033[0m'
GBOLD = BOLD + '\033[32m'
RBOLD = BOLD + '\033[31m'
Split = "===================================================================================="

lap_data = []

def UserInfo():
    UserName = input(f"Enter the {BOLD}User Name{END}: ").replace(" ", "_")

    ProfileName = input(f"Enter the {BOLD}Profile Name{END}: ").replace(" ", "_")
    Date = datetime.date.today()
    path = UserName + "_" + ProfileName
    return path




def UserPrompt(path):
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
            