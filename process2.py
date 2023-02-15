import subprocess


p=subprocess.Popen(['powershell.exe','C:\\Users\\user\\Pictures\\local\\hello.ps1'],stderr=subprocess.PIPE,stdout=subprocess.PIPE,text=True,universal_newlines=True)
out,err=p.communicate()
file=open('hello.txt','a')
file.write(out)
# while True:
#     for i in p.stdout.readlines():
#         print(i)
# while True:
#     try:
#         return_code=p.wait()
#         print(return_code)
#         code=p.returncode
#         if code is not None:
#             for out in p.stdout.readlines():
#                 file=open('hello.txt','a')
#                 file.write(out)
#     except subprocess.TimeoutExpired:
#         print("Process timeout is finish")
#     break
