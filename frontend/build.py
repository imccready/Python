import os

os.system("rm -f .static/*")
os.chdir("../angular/")
os.system("ng build")
os.chdir("dist/angular/")
os.system("cp *.* ../../../frontend/static/")