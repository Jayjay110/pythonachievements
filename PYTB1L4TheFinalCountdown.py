import time
countdown = 100
print (countdown)
while 5 > 1:
    countdown -= 1
    time.sleep(1)
    print (countdown)
    if countdown == 0:
        import sys
        sys.exit()
