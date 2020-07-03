import os, sys
Modules = []
for root, dirs, files in os.walk("./Menus/Tools"):
    for filename in files:
        Modules.append(filename[:-3])
def runModule(ModuleCC):
    ModulePath = "./Menus/Tools/" + ModuleCC + ".py"
    os.system('cls' if os.name=='nt' else 'clear')
    os.system("python3 " + ModulePath)
def MainMenu():
    os.system('cls' if os.name=='nt' else 'clear')
    print("   Welcome to the Tools menu!   ")
    for index, value in enumerate(Modules):
        print(" [" + str(index) + "]" , value.replace("_", " "))
    print(" [" + str(len(Modules)) + "]" , "Go Back To Main Menu ")
    choice = input("  ==> ")
    if int(choice) == int(len(Modules)):
        os.system("python3 Main.py")
    if int(choice) <= len(Modules):
        runModule(Modules[int(choice)])
    else:
        MainMenu()
try:
    MainMenu()
except ValueError:
    os.system("python3 " + sys.argv[0])
except KeyboardInterrupt:
    exit()