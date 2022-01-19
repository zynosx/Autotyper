from random import randint
import random
from pynput.keyboard import Key, Controller
import time
kb = Controller()


def typethetext(inputstring):
    text = inputstring
    text = text.split() 
    for i in text:
        kb.type(i)
        kb.press(Key.space)
        time.sleep(1)
    kb.press(Key.enter)
    time.sleep(randint(1,4))

def randomiser():
    # shuffler_list = ["pls hunt","pls fish","pls dig","pls beg","pls dep max","pls search","pls hl"]
    shuffler_list = ["pls hunt","pls fish","pls dig","pls beg","pls dep max"]
    random.shuffle(shuffler_list)
    # print(shuffler_list)
    for a in shuffler_list:
        typethetext(a)
    


#starting the bot(main func)    
st_time=time.time()
hour = int(input("enter time (in):"))
sec = hour * 60 * 60
cur_time = time.time()
elap_time = cur_time - st_time
count = 0

print(st_time)
print(elap_time)

time.sleep(randint(3,5))
while not elap_time > sec:
    cur_time = time.time()
    elap_time = cur_time - st_time
    time.sleep(1)
    randomiser()
    count+=4
    print("Running -","commands count",count)
    time.sleep(randint(46,49))