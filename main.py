# DroneSoccerGoalTracker Module
import style as s
import ui as ui 
import translator as t


lap_data = []

path = ui.UserInfo()
lap_data = ui.UserPrompt(path)

t.SaveData(lap_data, path)


ui.ExitProgram(path, lap_data)