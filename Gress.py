from lib import Bas
import random

gress = Bas.BasType({
    "content": "|",
    "bold": 0,
    "textShadow": 0,
    "anchorY": 1,
    "anchorX": 0.5,
    "fontSize": "130%",
    "fontFamily": "宋体",
    "color": "0x8FBC8F",
    "y": "110%",
    "x": "30%",
    "rotateZ": -5,
})


def create_one(start_time, start_x):
    g1z = -3
    g2z = 0
    g3z = 3
    animate_space = 0.2
    duration = 1.5
    g1 = Bas.BasObject(gress, {"rotateZ": -5, "x": f"{start_x}%"})
    g2 = Bas.BasObject(gress, {"rotateZ": 2, "x": f"{start_x + 2}%"})
    g3 = Bas.BasObject(gress, {"rotateZ": 6, "x": f"{start_x + 4}%"})

    g1a = Bas.BasAnimate().animate(g1, duration=start_time).animate(g1, duration=0.1, attribute={"alpha": 1})
    g2a = Bas.BasAnimate().animate(g2, duration=start_time).animate(g2, duration=0.1, attribute={"alpha": 1})
    g3a = Bas.BasAnimate().animate(g3, duration=start_time).animate(g3, duration=0.1, attribute={"alpha": 1})

    offsetX = 10 * animate_space

    x1 = g2.get_float('x') - offsetX
    g2a.animate(g2, duration=animate_space, attribute={"x": f"{x1}%"})

    x1 = g3.get_float('x') - offsetX * 2
    g3a.animate(g3, duration=animate_space * 2, attribute={"x": f"{x1}%"})

    while g3.get_float('x') > -20:
        left = g1a.count % 2

        rorate = (random.uniform(-1, -0.5) if left else random.uniform(5, 6))
        x = g1.get_float('x')
        g1a.animate(g1, duration=duration, attribute={"rotateZ": g1z + rorate, "x": f"{x - 10}%"})

        x = g2.get_float('x')
        rorate = (random.uniform(-1, -0.5) if left else random.uniform(5, 6))
        g2a.animate(g2, duration=duration, attribute={"rotateZ": g2z + rorate, "x": f"{x - 10}%"})

        x = g3.get_float('x')
        rorate = (random.uniform(-1, -0.5) if left else random.uniform(5, 6))
        g3a.animate(g3, duration=duration, attribute={"rotateZ": g3z + rorate, "x": f"{x - 10}%"})

    g1a.finish()
    g2a.finish()
    g3a.finish()
