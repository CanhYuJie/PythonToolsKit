#coding=utf-8
#Ubuntu desktop creater
import os,stat
print("please run this script by root user")
appName = input("please input appName:")
appPosition = input("please input where is app luncher:")
appIcon = input("please input where is appIcon:")
dirPos = appName+".desktop"
with open(dirPos,"w+") as f:
    f.writelines('[Desktop Entry]\n')
    f.writelines('Version=1.0\n')
    f.writelines('Name=' + appName+"\n")
    f.writelines('Exec=' + appPosition+'\n')
    f.writelines('Terminal=false')
    f.writelines('Icon=' + appIcon+'\n')
    f.writelines('Type=Application\n')
    f.writelines('Categories=Development')
    f.seek(0)
    data = f.read()
print(data)
#create desktop tool,but it can't run if you are not root user