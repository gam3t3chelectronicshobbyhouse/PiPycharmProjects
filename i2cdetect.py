import os
import subprocess
import time

p = subprocess.Popen(['i2cdetect','-y', '1'], stdout=subprocess.PIPE,)

for i in range(0,9):
	line = str(p.stdout.readline())
	print(line)