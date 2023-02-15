import subprocess


p=subprocess.Popen(['python','first.py'],text=True,stdout=subprocess.PIPE,universal_newlines=True)
out,err=p.communicate()
print(out)