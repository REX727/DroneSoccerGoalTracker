import DSGT as t

lap_data = []

path = t.UserInfo()
lap_data = t.UserPrompt()

t.SaveData(lap_data, path)


t.ExitProgram(path, lap_data)