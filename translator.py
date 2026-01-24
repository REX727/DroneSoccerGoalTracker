#Translator Mdoule
import os

GBOLD = '\033[1m'+ '\033[32m'
END = '\033[0m'

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