import sys
import time

a = 2
b = 0.2
c = 0.002

s = "string"
for character in s:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(c)
