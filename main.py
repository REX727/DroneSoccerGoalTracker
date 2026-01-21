import CLI_Style as s
import ui 
import datetime

print(f"{s.BOLD}Drone Soccer Goal Tracker{s.END} - V1.2.0")

lap_data = []


path = ui.UserInfo()
lap_data = ui.UserPrompt(path)

ui.ExitProgram(path, lap_data)