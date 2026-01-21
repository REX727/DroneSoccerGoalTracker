import CLI_Style as s
import datetime

lap_data = []

def UserInfo():
    UserName = input(f"Enter the {s.BOLD}User Name{s.END}: ").replace(" ", "_")

    ProfileName = input(f"Enter the {s.BOLD}Profile Name{s.END}: ").replace(" ", "_")
    Date = datetime.date.today()
    DateString = Date.strftime("%Y%m%d")
    path = DateString + "_" + UserName + "_" + ProfileName
    return path




def UserPrompt(path):
    UserInput = ""
    print(f"Enter lap time in seconds or type '{s.RBOLD}exit{s.END}' to quit:")

    while UserInput.lower() != "exit":
        UserInput = input(f"{s.GBOLD}GOAL {len(lap_data)+1}{s.END}: ")
        if UserInput.lower() != "exit":
                try:
                    lap_data.append(float(UserInput))
                except:
                    print(f"{s.RBOLD}VALUE ERROR{s.END}")
                    pass
        elif UserInput.lower() == "exit":
            return lap_data

def ExitProgram(path, lap_data):
            AvgTimes = round((sum(lap_data))/len(lap_data),2)
            
            print(f"{s.RBOLD}Exiting Program{s.END}")
            print(s.BOLD + "\n====="+path+"=====" + s.END)
            print(f"Total Goals: {s.GBOLD}{len(lap_data)}{s.END}")
            print(f"Average Seconds Per Goal: {s.GBOLD}{AvgTimes}s{s.END}(rounded to 2 decimal places)")
            