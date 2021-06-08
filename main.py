import bas
import random

background = bas.new_type("background", {
    "d": "M-1000,-1000V15H15V-1000z",
    "fillColor": "0x2b6f9b",
    "zIndex": 99,
    "scale": 9999
}, "path")

fish = bas.new_type("fish", {
    "content": "<。)#)))≦ ",
    "anchorX": 1,
    "x": "120%"
})

bubble = bas.new_type("bub", {
    "content": "●",
    "color": "0x2dfffe",
    "y": "100%",
    "fontSize": "15%",
})

gress = bas.new_type("gress", {
    "content": "|",
    "bold": 0,
    "textShadow": 0,
    "anchorY": 1,
    "anchorX": 0.5,
    "fontSize": "130%",
    "fontFamily": "宋体",
    "color": "0x8FBC8F",
    "y": "100%",
    "x": "30%",
    "rotateZ": -5,
})

bg = bas.create_obj(background, {"alpha": 0.2})
bub1 = bas.create_obj(bubble, {"x": f"{random.randint(30, 85)}%", "alpha": 0.3})
bub2 = bas.create_obj(bubble, {"x": f"{random.randint(30, 85)}%", "alpha": 0.3})
bub3 = bas.create_obj(bubble, {"x": f"{random.randint(30, 85)}%", "alpha": 0.3})
bub4 = bas.create_obj(bubble, {"x": f"{random.randint(30, 85)}%", "alpha": 0.3})

g1z = -3
g2z = 0
g3z = 3
g1 = bas.create_obj(gress, {"rotateZ": -3, "alpha": 1, "x": "80%"})
g2 = bas.create_obj(gress, {"rotateZ": 0, "alpha": 1, "x": "82%"})
g3 = bas.create_obj(gress, {"rotateZ": 3, "alpha": 1, "x": "84%"})

g1a = bas.BasAnimate()
g2a = bas.BasAnimate()
g3a = bas.BasAnimate()

x = 84
while x >= -10:
    x -= 10

    g1a.animate(g1, 0, 1, {"rotateZ": g1z + random.randint(-1, 0) if g1a.count%2 else random.randint(2, 4), "x": f"{x-4}%"})
    g2a.animate(g2, 0, 1, {"rotateZ": g2z + random.randint(-1, 0) if g2a.count%2 else random.randint(g1a.attribute['rotateZ'] + 1, g1a.attribute['rotateZ'] + 2), "x": f"{x-2}%"})
    g3a.animate(g3, 0, 1, {"rotateZ": g3z + random.randint(-1, 0) if g3a.count%2 else random.randint(g2a.attribute['rotateZ'] + 1, g2a.attribute['rotateZ'] + 2), "x": f"{x}%"})
g1a.finish()
g2a.finish()
g3a.finish()

# bas.animate(g1, 0.3, 0.6, {"rotateZ": -1, "x": "76%"})