import pyautogui as p
import random
import time

timer = input("how many repeat (enter f if you want to run the code forever): ")
run_time = input("do want the time in minutes(m) or seconds(s) or miliseconds(ms): ")
while True :
    the_time = input(f"how many {run_time} betwen clicks :")
    if the_time.isdigit() :
        the_time = int(the_time)
        break
    else :
        print("please entar a number")

if timer.isdigit :
    timer = int(timer)
    for i in range(timer):
        if run_time == "m":
            the_time = the_time * 60
            p.click()
            time.sleep(the_time)
        elif run_time == "s":
            p.click()
            time.sleep(the_time)
        elif run_time == "ms" :
            the_time = the_time /1000
            p.click()
            time.sleep(the_time)
else :
    while True :
        if run_time == "m":
            the_time = the_time * 60
            p.click()
            time.sleep(the_time)
        elif run_time == "s" :
            p.click()
            time.sleep(the_time)
        elif run_time == "ms" :
            the_time = the_time /1000
            p.click()
            time.sleep(the_time)
