import subprocess,sys,json
# # p=subprocess.run(["powershell.exe","D:\\process\\hello.ps1"],capture_output=True,text=True) #for singlw
# p=subprocess.Popen(["powershell.exe","D:\\process\\hello.ps1"],stdout=subprocess.PIPE,text=True)
# out,err=p.communicate()
# import time
# from datetime import datetime
# p=subprocess.Popen(["C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe","D:\\process\\hello.ps1"],stdout=subprocess.PIPE,text=True)
# out,err=p.communicate()
# current_datetime=str(datetime.now()).replace(':','')
# file_name=str(current_datetime)[:20]+'.txt'
# file=open(file_name,'w')
# file.write(str(out))
# file.close()
# time.sleep(1)
# p=subprocess.Popen(["C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe","D:\\process\\hello.ps1"],stdout=subprocess.PIPE,text=True)
# out,err=p.communicate()
# print(out)
# p=subprocess.Popen(["C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe","D:\\process\\hello.ps1"],stdout=subprocess.PIPE,text=True)
# reTu=p.communicate()
# reco=p.returncode
# if reco=='0':
#     print('Deleted')
# else:
#     print('Error')


###################################Get-Variable###############################################
p=subprocess.Popen(["C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe","D:\\process\\hello.ps1"],stdout=subprocess.PIPE,text=True)
out,err=p.communicate()
print(out)
p.kill()
# file=open("hello.xml",'w')
# file.write(str(out))