import os
from parser import parse

def inspect_source(path: str):
    dir_list = os.listdir(path)

    print("-------------------")
    print("Start inspecting the source code")
    print(dir_list)

    for content in dir_list:
        current_path = f"{path}/{content}"

        if (os.path.isdir(current_path)) is True:
            print(f"Calling itself again for a folder: {current_path}")
            inspect_source(current_path)
        else:
            print(f"Calling parse for a file: {current_path}")


    

if __name__ == "__main__":

    pwd = os.getcwd()
    inspect_source(f"{pwd}/input")


