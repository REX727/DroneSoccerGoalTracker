# DroneSoccerGoalTracker Module
import module.style as s
import module.ui as ui 

#Third-Party Modules
import datetime

lap_data = []

path = ui.UserInfo()
lap_data = ui.UserPrompt(path)


ui.ExitProgram(path, lap_data)