import Bas
import random

gress = Bas.new_type("gress", {
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


def create_one(start_time):
    g1z = -3
    g2z = 0
    g3z = 3
    animate_space = 0.3
    g1 = Bas.create_obj(gress, {"rotateZ": -3, "alpha": 1, "x": "80%"})
    g2 = Bas.create_obj(gress, {"rotateZ": 0, "alpha": 1, "x": "82%"})
    g3 = Bas.create_obj(gress, {"rotateZ": 3, "alpha": 1, "x": "84%"})

    g1a = Bas.BasAnimate()
    g2a = Bas.BasAnimate()
    g3a = Bas.BasAnimate()

    x = 84
    while x >= -10:
        x -= 10
        rorate = g1z + random.uniform(-1, 0) if g1a.count % 2 else random.uniform(2, 4)
        g1a.animate(g1, start_time, 1, {"rotateZ": rorate, "x": f"{x-4}%"})
        
        rorate = g2z + random.uniform(-1, 0) if g2a.count % 2 else random.uniform(rorate + 1, rorate + 2)
        g2a.animate(g2, start_time, 1, {"rotateZ": rorate, "x": f"{x-2}%"})

        rorate = g3z + random.uniform(-1, 0) if g3a.count % 2 else random.uniform(rorate + 1, rorate + 2)
        g3a.animate(g3, start_time, 1, {"rotateZ": rorate, "x": f"{x}%"})

    g1a.finish()
    g2a.finish()
    g3a.finish()
