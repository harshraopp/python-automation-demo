import os
from datetime import datetime
folderpath = "pythontest"
newpath = "pythontest2"
name = str(input("enter your name"))
timenow = datetime.now()
print(f"time is {timenow}")
print("saving to a file name.txt")
with open("name.txt", "a") as file:
    file.write(f" the name is: \n{name} and time is {timenow} ")
if not os.path.exists(folderpath):
    print("creating folder")
    os.mkdir(folderpath)
    if os.path.exists(folderpath):
        os.rename(folderpath, newpath)
    else:
        print("unsuccessfull")
else:
    print("folder exists")


# Major python commands:
# input("enter username")
# date.time.now()
# with open("filename.txt", "r") as file:
#     f.read()
# with open("filename.txt", "w") as file:
#     f.write("lets write something")
# if os.path.exists(pathname)
# os.rename(oldname, newname)
# os.mkdir(newfolder)
#shutil.move(source, destination)
# os.listdir("logs")
# if file.endswith(".txt"):


    