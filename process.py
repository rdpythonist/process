import subprocess,sys,json
# p=subprocess.run(["powershell.exe","D:\\process\\hello.ps1"],capture_output=True,text=True)
p=subprocess.Popen(["powershell.exe","D:\\process\\hello.ps1"],stdout=subprocess.PIPE,text=True)
out,err=p.communicate()
print(json.dumps(out))