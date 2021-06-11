import sys
sys.path.append("lib")

import Bas

import random
import pyperclip
import Bubble
import Gress

durtion_sum = 30

background = Bas.new_type("background", {
    "d": "M-1000,-1000V15H15V-1000z",
    "fillColor": "0x2b6f9b",
    "zIndex": 99,
    "scale": 9999
}, "path")

fish = Bas.new_type("fish", {
    "content": "<。)#)))≦ ",
    "anchorX": 1,
    "x": "120%"
})

bg = Bas.create_obj(background, {"alpha": 0.2})
Bas.BasAnimate().animate(obj=bg, duration=durtion_sum).finish()

Bubble.create_many(start_time=0, durtion_sum=durtion_sum, group_count=10)
Gress.create_one(start_time=0)

pyperclip.copy(Bas.read_bas())