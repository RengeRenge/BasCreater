import random
import pyperclip
from lib import Bas
from gui import app

durtion_sum = 4*60 + 34


def bubble(duration):
    import Bubble
    Bubble.create_many(0, duration, 10)


def t0(duration):
    # background = Bas.BasType({
    #     "d": "M-1000,-1000V15H15V-1000z",
    #     "fillColor": "0x2b6f9b",
    #     "zIndex": 99,
    #     "scale": 9999
    # }, "path")

    # bg = Bas.BasObject(background, {"alpha": 0.2})
    # Bas.BasAnimate().animate(bg, duration=durtion_sum).finish()

    title = Bas.BasType({
        "color": "0xffffff",
        "fontSize": '20%',
        "alpha": 1,
        "content": " ",
        "y": "60%",
        "anchorY": 1
    })
    Bas.BasAnimate().animate(Bas.BasObject(
        title, {"content": "#", "fontSize": '15%'}), duration=duration).finish()
    Bas.BasAnimate().animate(Bas.BasObject(
        title, {"content": " 1", "y": str(title.get_int("y")+2)+"%"}), duration=duration).finish()
    Bas.BasAnimate().animate(Bas.BasObject(
        title, {"content": "　　 に", "y": str(title.get_int("y")+2)+"%", "fontSize": '8%', "rotateZ": -12}), duration=duration).finish()

    title2 = Bas.BasType({
        "color": "0xffffff",
        "fontSize": '20%',
        "alpha": 1,
        "content": " ",
        "y": "93%",
        "x": "10%",
        "anchorY": 1,
        "anchorX": 0.5
    })
    Bas.BasAnimate().animate(Bas.BasObject(
        title2, {"content": "つ"}), duration=duration).finish()
    Bas.BasAnimate().animate(Bas.BasObject(
        title2, {"content": "    づ", "y": str(title2.get_int("y")+2)+"%"}), duration=duration).finish()
    Bas.BasAnimate().animate(Bas.BasObject(
        title2, {"content": "        く", "y": str(title2.get_int("y")+4)+"%", "rotateZ": -12}), duration=duration).finish()

    orangeWhiteFish = Bas.BasType.parseXML(
        './resource/orange_white_fish_left.svg')
    attr = {"x": f"{85}%", "y": f"{40}%", "scale": 0.4,
            "anchorY": 0.5, "anchorX": 1, "alpha": 1}
    fish = Bas.BasObject(orangeWhiteFish, attr)
    Bas.BasAnimate().animate(
        fish, duration=duration
    ).finish()

    import Bubble
    x = 50
    while x > 0:
        bub = Bas.BasObject(
            Bubble.bubble, {"x": f"{x}%", "y": f"{x*0.8 - 5 + random.randint(-5, 5)}%", 'fontSize': f'{2 + (50 - x) * 0.3}%', "anchorX": 1})
        Bas.BasAnimate().animate(
            bub,
            duration=duration
        ).finish()
        x -= 8


def t6(duration):
    import Bubble
    Bubble.create_many(0, duration, 10)


def t16():
    blueFish = Bas.BasType.parseXML('./resource/blue_fish.svg')
    create_many(blueFish, 0, 120, base_y=40, y_offset_min=-
                5, y_offset_max=10, count=10, duration=8)
    bubble(16)


def t32():
    blueFish = Bas.BasType.parseXML('./resource/blue_fish.svg')
    create_many(blueFish, 0, 120, base_y=40, y_offset_min=-10,
                y_offset_max=-4, count=8, duration=4, beforeDelay=0.5)
    bubble(10)


def t40():
    orangeFish = Bas.BasType.parseXML('./resource/orange_white_fish_left.svg')
    create_many(orangeFish, 0, 120, base_y=60,
                count=8, duration=8, beforeDelay=1.5)
    bubble(9)


def t49():
    import Bubble
    import Gress

    Bubble.create_many(
        start_time=0,
        duration_sum=1,
        group_count=10,
        x_min=-20,
        x_max=70,
        y_end_base=-20,
        group_duration=0.6,
        bubble_duration=0.6,
        size_base=0,
        alpha_base=1,
        end_alpha=0.6
    )

    Bubble.create_many(
        start_time=0.3,
        duration_sum=1,
        group_count=10,
        x_min=-20,
        x_max=90,
        y_end_base=-20,
        group_duration=0.6,
        bubble_duration=0.6,
        size_base=0,
        alpha_base=1,
        end_alpha=0.6
    )
    delay = 1.5
    bubble_duration = 0.6

    g_delay = bubble_duration + delay
    Gress.create_one(start_time=g_delay + 0.4, start_x=20)
    Gress.create_one(start_time=g_delay + 0.6, start_x=40)
    Gress.create_one(start_time=g_delay + 0.8, start_x=60)
    Gress.create_one(start_time=g_delay + 1.0, start_x=80)

    Bubble.create_many(
        start_time=delay,
        duration_sum=2,
        group_count=60,
        x_min=-20,
        x_max=90,
        y_end_base=-20,
        group_duration=bubble_duration,
        bubble_duration=bubble_duration,
        size_base=0,
        alpha_base=1,
        end_alpha=0.6
    )

    Bubble.create_many(
        start_time=delay + 0.3,
        duration_sum=1,
        group_count=60,
        x_min=-20,
        x_max=90,
        y_end_base=-20,
        group_duration=bubble_duration,
        bubble_duration=bubble_duration,
        size_base=10,
        alpha_base=1,
        end_alpha=0.6
    )


def create_many(type: Bas.BasType, start_time, start_x, base_y=40, y_offset_min=-10, y_offset_max=5, count=10, duration=8.0, beforeDelay=1):
    delay = 0
    while count >= 0:
        delay = random.uniform(delay, delay+beforeDelay)
        delay = max(0, delay)
        create_one(type,
                   start_time=start_time + random.uniform(0, delay),
                   start_x=start_x + count,
                   base_y=base_y + random.uniform(-20, 20),
                   y_offset_min=y_offset_min,
                   y_offset_max=y_offset_max,
                   duration=duration)
        count -= 1


def create_one(type: Bas.BasType, start_time, start_x, base_y, y_offset_min, y_offset_max, duration):
    if base_y is None:
        base_y = random.uniform(10, 90)
    attr = {"x": f"{start_x}%", "y": f"{base_y}%", "alpha": 1, 'scale': 0.1}
    fish = None
    fish = Bas.BasObject(type, attr)

    animate = Bas.BasAnimate().animate(
        fish, duration=start_time
    )

    change_count = random.randint(1, 3)
    x = start_x
    l = start_x - -20.0
    offset = 1.0 * l / change_count

    while fish.get_float('x') > -20:
        x = fish.get_float('x')
        y = fish.get_float('y')
        animate.animate(
            fish, duration=duration/change_count, attribute={"x": f"{x - offset}%", "y": f"{y + random.uniform(y_offset_min, y_offset_max)}%"}
        )
    animate.finish()


def demo():

    # import Bubble
    # import Gress
    # import Fish
    # import random

    # Gress.create_one(start_time=0, start_x=100)

    # Fish.create_many(2, random.randint(0, 3), 120, 20)

    # # Fish.create_one(3, random.randint(3, 12), 120)
    # Gress.create_one(start_time=0.4, start_x=120)

    # Fish.create_one(0, random.randint(3, 12), 120)
    # Fish.create_one(1, random.randint(3, 12), 120)

    # # Fish.create_one(4, random.randint(3, 12), 120)
    # # Fish.create_one(5, random.randint(3, 12), 120)
    # Fish.create_one(6, random.randint(3, 12), 120)

    # Fish.create_many(7, random.randint(3, 6), 120, 15)
    # Fish.create_many(8, random.randint(3, 6), 120, 10)

    # Gress.create_one(start_time=0.6, start_x=140)

    # Gress.create_one(start_time=0, start_x=200)
    # Gress.create_one(start_time=0.4, start_x=220)
    # Gress.create_one(start_time=0.6, start_x=240)
    # Fish.create_many(2, random.randint(6, 15), 120, 20)

    # Bubble.create_many(start_time=0, durtion_sum=durtion_sum, group_count=10)

    pyperclip.copy(Bas.read_bas())


# app.run()
# t0(6)
# t6(10)
# t16()
# t32()
# t40()
t49()

pyperclip.copy(Bas.read_bas())
