import sys, os


missing_modules = []

with open("requirements.txt", "r") as file:
    lines = [i.strip() for i in file.readlines()]

for line in lines:
    if "==" in line:
        module = line.split("==")[0]
    else:
        module = line

    try:
        __import__(module)


    except ModuleNotFoundError:
        missing_modules.append(module)
    
else:
    if len(missing_modules) != 0:
        print("There is some missing modules that you don't have!")
        print("The following command will be executed for installing those modules: " , "pip install " + "&&".join(missing_modules))
        
        i = input("Do you want to install them? [y,n]")

        if i.lower().strip().startswith("y"):
            os.system("pip install " + "&&".join(missing_modules))

        else:
            print("Goodbye !")

            sys.exit()



    __import__("src.main").start(sys.argv)