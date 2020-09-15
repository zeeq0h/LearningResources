import sys
import time
import os
from codecs import decode

os.system('mode con: cols=200 lines=60')

ascii_art = """
$$$$$$$\  $$$$$$$\  $$$$$$\ $$\      $$\ $$$$$$$$\       $$\   $$\ $$\   $$\ $$\      $$\ $$$$$$$\  $$$$$$$$\ $$$$$$$\        $$$$$$$$\  $$$$$$\   $$$$$$\  $$\       
$$  __$$\ $$  __$$\ \_$$  _|$$$\    $$$ |$$  _____|      $$$\  $$ |$$ |  $$ |$$$\    $$$ |$$  __$$\ $$  _____|$$  __$$\       \__$$  __|$$  __$$\ $$  __$$\ $$ |      
$$ |  $$ |$$ |  $$ |  $$ |  $$$$\  $$$$ |$$ |            $$$$\ $$ |$$ |  $$ |$$$$\  $$$$ |$$ |  $$ |$$ |      $$ |  $$ |         $$ |   $$ /  $$ |$$ /  $$ |$$ |      
$$$$$$$  |$$$$$$$  |  $$ |  $$\$$\$$ $$ |$$$$$\          $$ $$\$$ |$$ |  $$ |$$\$$\$$ $$ |$$$$$$$\ |$$$$$\    $$$$$$$  |         $$ |   $$ |  $$ |$$ |  $$ |$$ |      
$$  ____/ $$  __$$<   $$ |  $$ \$$$  $$ |$$  __|         $$ \$$$$ |$$ |  $$ |$$ \$$$  $$ |$$  __$$\ $$  __|   $$  __$$<          $$ |   $$ |  $$ |$$ |  $$ |$$ |      
$$ |      $$ |  $$ |  $$ |  $$ |\$  /$$ |$$ |            $$ |\$$$ |$$ |  $$ |$$ |\$  /$$ |$$ |  $$ |$$ |      $$ |  $$ |         $$ |   $$ |  $$ |$$ |  $$ |$$ |      
$$ |      $$ |  $$ |$$$$$$\ $$ | \_/ $$ |$$$$$$$$\       $$ | \$$ |\$$$$$$  |$$ | \_/ $$ |$$$$$$$  |$$$$$$$$\ $$ |  $$ |         $$ |    $$$$$$  | $$$$$$  |$$$$$$$$\ 
\__|      \__|  \__|\______|\__|     \__|\________|      \__|  \__| \______/ \__|     \__|\_______/ \________|\__|  \__|         \__|    \______/  \______/ \________|
                                                                                                                                                                      
"""           


for char in ascii_art:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.0001)
                                                                                                                                                                      


#the code itself
start = int(input("what number do you want to start detecting prime numbers at: "))
finish = int(input("what number do you want to stop detecting prime numbers at: "))

for n in range(start, finish):
    for x in range (2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x} ")
            break
    else:
        print(f"{n} is a prime number.")
        time.sleep(0.5)


#shutdown timer
print(" ")
print(" ")
when_to_stop = 0
while True:
    uin = 60
    try:
        when_to_stop = abs(int(uin))
    except KeyboardInterrupt:
        break
    except:
        print("Not a number!")
    while when_to_stop > 0:
        m, s = divmod(when_to_stop, 60)
        h, m = divmod(m, 60)
        time_left = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
        print("\r", "program auto closing in: " , end=time_left)
        time.sleep(1)
        when_to_stop -= 1
    time.sleep(1)
    exit()

