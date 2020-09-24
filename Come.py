from playsound import playsound
import sched, time


##s = sched.scheduler(time.time, time.sleep)
##
##
##
##t = time.localtime()
##hour_now = time.strftime("%H", t)
##min_now = time.strftime("%M", t)
##
##def do_something(sc): 
##    #print("Doing stuff...")
##    playsound('Come.mp3')
##    # do your stuff
##    s.enter(10, 1, do_something, (sc,))
##
##
##for x in range(3):
##    t = time.localtime()
##    hour_now = time.strftime("%H", t)
##    min_now = time.strftime("%M", t)
##    if hour_now >= 11 and hour_now <= 13:
##        if min_now 
##    s.enter(10, 1, do_something, (s,))
##    s.run()
##
##

for x in range(10):
    playsound('Come.mp3')
    time.sleep(5)
