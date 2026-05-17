import subprocess
import time 

url="https://github.com/Harikaran14"

for i in range(100):
    task=["brave-browser",url]
    process= subprocess.Popen(task)
    time.sleep(2)
    process.terminate()
    time.sleep(1)