import CLI_Style as s
import datetime

print(f"{s.BOLD}Drone Soccer Goal Tracker{s.END} - V1.1.0")

lap_data = []

UserName = input(f"Enter the {s.BOLD}User Name{s.END}: ")
ProfileName = input(f"Enter the {s.BOLD}Profile Name{s.END}: ") 
Date = datetime.date.today()
DateString = Date.strftime("%Y%m%d")
path = DateString + "_" + UserName + "_" + ProfileName

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
    if UserInput.lower() == "exit":
        AvgTimes = round((sum(lap_data))/len(lap_data),2)
        
        print(f"{s.RBOLD}Exiting Program{s.END}")
        print(s.BOLD + "\n====="+path+"=====" + s.END)
        print(f"Profile Name: {s.BOLD}{ProfileName}{s.END}")
        print(f"Total Goals: {s.GBOLD}{len(lap_data)}{s.END}")
        print(f"Average Seconds Per Goal: {s.GBOLD}{AvgTimes}s{s.END}(rounded to 2 decimal places))")
        break