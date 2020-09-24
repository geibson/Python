import os
import shutil
os.chdir('C:\\') #Make sure you add your source and destination path below

dir_src = ("C:\\Users\\geibsonl\\MyPythonScripts\\")
dir_dst = ("C:\\Users\\geibsonl\\OneDrive - DBserver Assessoria em Sistemas de Informação Ltda\\Python\\MyPythonScripts\\")

for filename in os.listdir(dir_src):
    if filename.endswith('.py') or filename.endswith('.bat'):
        shutil.copy( dir_src + filename, dir_dst)
    print(filename)
