import os

GBOLD = '\033[1m'+ '\033[32m'
END = '\033[0m'

def SaveData(lap_data, path):
    save_data = ""
    for lap in range(len(lap_data)):
        save_data = save_data + str(lap_data[lap]) + '\n'
    os.chdir('Data')
    
    path_txt = path + ".txt"
    f = os.open(path_txt, os.O_RDWR|os.O_CREAT)
    os.write(f, save_data.encode())

    print(f"\n{GBOLD}Saved {path} in Data folder.{END}")
    