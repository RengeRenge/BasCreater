import sys
sys.path.append("lib")

import Bas

import random
import pyperclip
import Bubble
import Gress
import Fish

durtion_sum = 30

background = Bas.BasType({
    "d": "M-1000,-1000V15H15V-1000z",
    "fillColor": "0x2b6f9b",
    "zIndex": 99,
    "scale": 9999
}, "path")

bg = Bas.BasObject(background, {"alpha": 0.2})
Bas.BasAnimate().animate(obj=bg, duration=durtion_sum).finish()

Gress.create_one(start_time=0, start_x=100)

Fish.create_many(2, random.randint(0, 3), 120, 20)

Fish.create_one(3, random.randint(3, 12), 120)
Gress.create_one(start_time=0.4, start_x=120)

Fish.create_one(0, random.randint(3, 12), 120)
Fish.create_one(1, random.randint(3, 12), 120)

Fish.create_one(4, random.randint(3, 12), 120)
Fish.create_one(5, random.randint(3, 12), 120)
Fish.create_one(6, random.randint(3, 12), 120)

Fish.create_many(7, random.randint(3, 6), 120, 15)
Fish.create_many(8, random.randint(3, 6), 120, 10)

Gress.create_one(start_time=0.6, start_x=140)

Gress.create_one(start_time=0, start_x=200)
Gress.create_one(start_time=0.4, start_x=220)
Gress.create_one(start_time=0.6, start_x=240)
Fish.create_many(2, random.randint(6, 15), 120, 20)

Bubble.create_many(start_time=0, durtion_sum=durtion_sum, group_count=10)

pyperclip.copy(Bas.read_bas())