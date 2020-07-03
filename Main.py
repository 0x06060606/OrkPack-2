import os, sys
Modules = ["Checkers", "Tools"]
for root, dirs, files in os.walk("./Modules"):
    for filename in files:
        Modules.append(filename[:-3])
def runModule(ModuleCC):
    ModulePath = "./Menus/" + ModuleCC + ".py"
    os.system("python3 " + ModulePath)
def MainMenu():
    os.system('cls' if os.name=='nt' else 'clear')
    print("   Welcome to CheckTheDeck!   ")
    print("  This tool was supplied by @OrkSec ")
    print("  And Revamped by @0x06060606 ")
    print("  What Menu would you like to enter? ")
    for index, value in enumerate(Modules):
        print(" [" + str(index) + "]" , value)
    print(" [" + str(len(Modules)) + "]" , "Exit ")
    choice = input("  ==> ")
    if int(choice) == int(len(Modules)):
        exit()
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