import subprocess


# p=subprocess.Popen(['powershell.exe','C:\\Users\\user\\Pictures\\local\\NetRmm\\hello.ps1'],stdout=subprocess.PIPE,universal_newlines=True)
# # out,err=p.communicate()
# # print(p.stdout.readlines())
# for i in p.stdout.readlines():
#     print(i.strip())

import threading  
def print_hello():  
    p=subprocess.Popen(['powershell.exe','C:\\Users\\user\\Pictures\\local\\NetRmm\\hello.ps1'],stdout=subprocess.PIPE,universal_newlines=True)
    for i in p.stdout.readlines():
        print(i.strip())
T1 = threading.Thread( target = print_hello,)  
T1.start()  
T1.join()  