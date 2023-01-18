import time 

def timer25():
    #25 minute timer
    t=25*60
    print("Time left to work: ")
    while t:
        mins = t // 60
        secs = t % 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -=1

def s_break():
    #5 minute break
    t=5*60
    print("Break time! Time to enjoy: ")
    while t:
        mins = t // 60
        secs = t % 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -=1

def l_break():
    #10 minute break
    t=10*60
    print("Break time! Time to enjoy: ")
    while t:
        mins = t // 60
        secs = t % 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -=1

def test_timer():
    #5 second timer for testing
    t=5
    print("Break time! Time to enjoy: ")
    while t:
        mins = t // 60
        secs = t % 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -=1