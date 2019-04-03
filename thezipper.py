import os
import zipfile
import tarfile
import platform
from time import sleep
def clear():
    if(platform.system() == "Windows"):
        os.system("cls")
    else:
        os.system("clear")
def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))
def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))
clear()
zipmethod = ""
fol = ""
def find_platform():
    if(platform.system() == "Windows"):
        zipmethod = ".zip"
        return zipmethod
    elif(platform.system() == "Mac OS X"):
        zipmethod = input("Which format do you want to use? (type " + '"' +
                          ".zip" + '"' + " for compatibility with OS X and Linux,"
                          + "or " +'"' + ".tar.gz" + '"' + " for compatibility accross"
                          + "all platforms.) # ")
        return zipmethod
    else:
        zipmethod = input("Which format do you want to use? (type " + '"' +
                          ".zip" + '"' + " for compatibility with OS X and Linux,"
                          + "or " +'"' + ".tar.gz" + '"' + " for compatibility accross"
                          + "all platforms.) # ")
        return zipmethod
def update_bar(lastdialogue):
    clear()
    print("theZipper is now zipping files...")
    print("")
    print(lastdialogue)
def zipfol():
    lastdialogue = "0%... [                ] "
    if(zipmethod == ".zip"):
        if(platform.system() == "Windows"):
            os.chdir(fol + "\..")
        else:
            os.chdir(fol + "/..")
        lastdialogue = "25%... [||||            ]"
        update_bar(lastdialogue)
        zipf = zipfile.ZipFile(zipnam + ".zip", 'w', zipfile.ZIP_DEFLATED)
        lastdialogue = "50%... [||||||||        ]"
        update_bar(lastdialogue)
        zipdir(folnam, zipf)
        lastdialogue = "75%... [||||||||||||    ]"
        update_bar(lastdialogue)
        zipf.close()
        lastdialogue = "100%... [||||||||||||||||]"
        update_bar(lastdialogue)
    else:
        if(platform.system() == "Windows"):
            os.chdir(fol + "\..")
        else:
            os.chdir(fol + "/..")
        lastdialogue = "50%... [|||||||||       ]"
        update_bar(lastdialogue)
        make_tarfile(zipnam + ".tar.gz", folnam)
        lastdialogue = "100%... [||||||||||||||||]"
        update_bar(lastdialogue)
print("Welcome to theZipper Zip Wizard!")
print("")
print("")
zipmethod = find_platform()
#print(platform.system())
#print(zipmethod)
clear()
print("theZipper Zip Wizard")
print("")
print("")
print("Create a directory then put all zipped files in there.")
sleep(5)
fol = input("Please copy and paste the full file path here. # ")
folnam = input("The folder name here.                          # ")
clear()
print("theZipper Zip Wizard")
print("")
print("")
zipnam = input("What is the name of your zip. Exclude file ending. # ")
clear()
print("theZipper is now zipping files...")
print("")
print("0%... ")
zipfol()
sleep(3)
print("")
print("")
print("")
print("All Done.")
exit()
