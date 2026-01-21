import CLI_Style as s
import ui 
import datetime



lap_data = []


path = ui.UserInfo()
lap_data = ui.UserPrompt(path)

ui.ExitProgram(path, lap_data)