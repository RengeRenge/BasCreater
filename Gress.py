from array import array
from lib import Bas
import random

gressl = Bas.BasType({
    "content": "⎝",
    "bold": 0,
    "textShadow": 0,
    "anchorY": 1,
    "anchorX": 1,
    "fontSize": "30%",
    "color": "0x8FBC8F",
    "y": "125%",
    "x": "30%",
    "rotateZ": 0,
})

gressm = Bas.BasType({
    "content": "⎝",
    "bold": 0,
    "textShadow": 0,
    "anchorY": 1,
    "anchorX": 1,
    "fontSize": "30%",
    "color": "0x8FBC8F",
    "y": "125%",
    "x": "30%",
    "rotateZ": 10,
})

gressr = Bas.BasType({
    "content": "⎠",
    "bold": 0,
    "textShadow": 0,
    "anchorY": 1,
    "anchorX": 0,
    "fontSize": "30%",
    "color": "0x8FBC8F",
    "y": "125%",
    "x": "30%",
    "rotateZ": -15,
})

gress_types = [gressl, gressm, gressr]


def create_one(start_time, start_x, end_x, colors: array, included_angle: array):
    animate_space = 0.2
    duration_of_offset = 0.7
    offset_x_of_angle_animate = 6
    obj_group: array[Bas.BasObject] = []
    for i, color in enumerate(colors):
        g = gress_types[i]
        angle = included_angle[i] + g.get_float('rotateZ')
        obj_group.append(
            Bas.BasObject(
                g, {"color": color, "rotateZ": f"{angle}", "x": f"{start_x - i * 2}%"})
        )

    animate_group: array[Bas.BasAnimate] = []
    # dislpay
    for g in obj_group:
        animate = Bas.BasAnimate().animate(
            g,
            duration=start_time
        ).animate(
            g,
            duration=0.1,
            attribute={"alpha": 1}
        )
        animate_group.append(animate)

    offsetX = offset_x_of_angle_animate * animate_space

    for i, obj in enumerate(obj_group):
        if i > 0:
            animate = animate_group[i]

            x1 = obj.get_float('x') - offsetX
            animate.animate(obj, duration=animate_space,
                            attribute={"x": f"{x1}%"})

    while obj_group[-1].get_float('x') > end_x:
        left = animate_group[0].count % 2

        for i, obj in enumerate(obj_group):
            animate = animate_group[i]

            rorate = (random.uniform(-1, -0.5)
                      if left else random.uniform(5, 6))
            x = obj.get_float('x')
            rorate_z = included_angle[i] + gress_types[i].get_float('rotateZ')
            animate.animate(obj, duration=duration_of_offset, attribute={
                "rotateZ": rorate_z + rorate, "x": f"{x - offset_x_of_angle_animate}%"})

    for ani in animate_group:
        ani.finish()


def create_one_to_end(start_time, start_x, colors: array, included_angle: array):
    animate_space = 0.2
    duration_of_offset = 0.7
    offset_of_angle_animate = 5
    obj_group: array[Bas.BasObject] = []
    for i, color in enumerate(colors):
        angle = included_angle[i]
        obj_group.append(
            Bas.BasObject(
                gressl, {"color": color, "rotateZ": f"{angle}", "x": f"{start_x + i * 2}%"})
        )
    # g1 = Bas.BasObject(gress, {"rotateZ": -5, "x": f"{start_x}%"})
    # g2 = Bas.BasObject(gress, {"rotateZ": 2, "x": f"{start_x + 2}%"})
    # g3 = Bas.BasObject(gress, {"rotateZ": 6, "x": f"{start_x + 4}%"})

    animate_group: array[Bas.BasAnimate] = []
    # dislpay
    for g in obj_group:
        animate = Bas.BasAnimate().animate(
            g,
            duration=start_time
        ).animate(
            g,
            duration=0.1,
            attribute={"alpha": 1}
        )
        animate_group.append(animate)

    offsetX = offset_of_angle_animate * animate_space

    for i, obj in enumerate(obj_group):
        if i > 0:
            animate = animate_group[i]

            x1 = obj.get_float('x') - offsetX
            animate.animate(obj, duration=animate_space,
                            attribute={"x": f"{x1}%"})

    while obj_group[-1].get_float('x') > -20:
        left = animate_group[0].count % 2

        for i, obj in enumerate(obj_group):
            animate = animate_group[i]

            rorate = (random.uniform(-1, -0.5)
                      if left else random.uniform(5, 6))
            x = obj.get_float('x')
            rorate_z = included_angle[i]
            animate.animate(obj, duration=duration_of_offset, attribute={
                "rotateZ": rorate_z + rorate, "x": f"{x - offset_of_angle_animate}%"})

    for ani in animate_group:
        ani.finish()
