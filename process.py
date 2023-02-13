import subprocess,sys,json
# # p=subprocess.run(["powershell.exe","D:\\process\\hello.ps1"],capture_output=True,text=True) #for singlw
# p=subprocess.Popen(["powershell.exe","D:\\process\\hello.ps1"],stdout=subprocess.PIPE,text=True)
# out,err=p.communicate()
import time
from datetime import datetime
for i in range(10):
    p=subprocess.Popen(["powershell.exe","D:\\process\\hello.ps1"],stdout=subprocess.PIPE,text=True)
    out,err=p.communicate()
    current_datetime=str(datetime.now()).replace(':','')
    file_name=str(current_datetime)[:20]+'.txt'
    file=open(file_name,'w')
    file.write(str(out))
    file.close()
    time.sleep(3)