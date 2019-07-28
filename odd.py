from datetime import  datetime
import time
import random

odds=[ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
      21,23,25,27,29, 31, 33, 35, 37, 39,
      41,43,45,47,49, 51, 53, 55, 57, 59]
for i in range(5):
    right_this_minute=datetime.today().minute

    if right_this_minute in odds:
        print("This minute sees a little odd")
    else:
        print("Not an odd minute")
    wait_time=random.randint(1,60)
    print(wait_time)
    time.sleep(wait_time)
'''for的三种典型用法：
   1. for i in [1,2,3]:
            print(i)
            1
            2
            3
   2. for ch in "Hi!"
             print(ch)
             H
             i 
             !
   3. for i in range(5)
            print("Hello,World")
            Hello,World
            Hello,World
            Hello,World
            Hello,World
            Hello,World'''

