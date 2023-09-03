import os
import time
import shutil
import easygui

global folder_path
folder_path = ""

#TODO add swf
stuff_of_radal = {"jpg": os.path.join(os.getcwd(), "data", "images", "radalsan.jpg"),
                  "png": os.path.join(os.getcwd(), "data", "images", "radalsan.png"),
                  "bmp": os.path.join(os.getcwd(), "data", "images", "radalsan.bmp"),
                  "ico": os.path.join(os.getcwd(), "data", "images", "radalsan.ico"),
                  "swf": os.path.join(os.getcwd(), "data", "images", "radalsan.swf"),
                  "mp3": os.path.join(os.getcwd(), "data", "sounds", "sosig.mp3"),
                  "ogg": os.path.join(os.getcwd(), "data", "sounds", "ur moder.ogg"),
                  "wav": os.path.join(os.getcwd(), "data", "sounds", "good ebening.wav")}

def get_folder_path():
    while True:
        global folder_path
        folder_path = easygui.diropenbox()
        if os.path.isdir(folder_path) and folder_path != os.path.join(os.getcwd(), "data"):
            break
        else:
            os.system("clear" if os.name == "posix" else "cls")
            print("Please select a valid folder")


def drop_the_bomb(src):
    for item in os.listdir(src):
        item_path = os.path.join(src, item)
        if os.path.isdir(item_path):
            drop_the_bomb(item_path)
        elif item_path[-3:] in stuff_of_radal:
            shutil.copy(item_path, os.path.join(src, item+f".backup.{item_path[-3:]}"))
            shutil.copy(stuff_of_radal[item_path[-3:]], item_path)
            

def restore_the_damage(src):
    for item in os.listdir(src):
        item_path = os.path.join(src, item)
        if os.path.isdir(item_path):
            restore_the_damage(item_path)
        elif "backup." in item_path[-10:-3] and item_path[-3:] in stuff_of_radal:
            shutil.copy(item_path, os.path.join(src,
                                                item.replace(f".backup.{item_path[-3:]}", "")))
            os.remove(item_path)


def options():
    while True:
        option = input("====> ")
        if option == "1":
            get_folder_path()
            return False
        elif option == "2":
            if folder_path:
                drop_the_bomb(folder_path)
                print("Done!")
                time.sleep(5)
            else:
                print("Please select a folder first.")
                time.sleep(5)
            return False
        elif option == "3":
            if folder_path:
                restore_the_damage(folder_path)
                print("Done!")
                time.sleep(5)
            else:
                print("Please select a folder first.")
                time.sleep(5)
            return False
        elif option == "4":
            exit()
        else:
            print("Please select a valid option.")
        


logo = """
                                                
                                    ▒▒▒▒▒▒      
                                ▒▒▒▒▒▒▒▒▒▒▒▒    
      ▒▒▒▒▒▒                ▒▒▒▒▒▒▒▒▒▒████▒▒    
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████░░░░██    
    ▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████░░░░░░░░░░██  
    ▒▒▒▒██░░░░██████████████░░░░░░░░░░░░░░░░██  
  ██░░▒▒██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓██  
  ██░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓██    
    ████░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓██      
      ██▓▓▓▓▓▓░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓████        
        ████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████            
            ██████████████████                  

"""

text_options = """
[SELECT]
L[1] Select folder to destroy
L[2] Sosigify
L[3] Unsosigify
L[4] Exit
"""

if __name__ == "__main__":
    while True:
        os.system("clear" if os.name == "posix" else "cls")

        print(logo)
        print(f"Current selected folder: {folder_path}")
        print(text_options)
        options()
