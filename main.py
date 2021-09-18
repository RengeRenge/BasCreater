import random
import pyperclip
from MyAnimate import *
from lib import Bas

durtion_sum = 4*60 + 34


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
    bubble(duration)


def t16():
    blueFish = Bas.BasType.parseXML('./resource/blue_fish.svg')
    fish_many(blueFish, 0, 120, base_y=40, y_offset_min=-
              5, y_offset_max=10, count=11, duration=8)
    bubble(16)


def t32():
    blueFish = Bas.BasType.parseXML('./resource/blue_fish.svg')
    fish_many(blueFish, 0, 120, base_y=40, y_offset_min=-10,
              y_offset_max=-4, count=9, duration=4, beforeDelay=0.5)
    bubble(10)


def t41():
    orangeFish = Bas.BasType.parseXML('./resource/red_fish_left.svg')
    count = 9
    delay = 0
    beforeDelay = 1
    index = 0
    durtion = 8
    scale = 0.06
    end_x = -20 * scale * 10
    while index < count:
        delay = random.uniform(delay, delay+beforeDelay)
        delay = max(0, delay)
        s = delay

        start_x = 120 + index
        sum_l = start_x - end_x
        v = sum_l/durtion

        d = 8 - s
        l = d * v
        fish_one(orangeFish,
                 start_time=s,
                 start_x=start_x,
                 base_y=60 + random.uniform(-20, 20),
                 y_offset_min=-10,
                 y_offset_max=5,
                 duration=d,
                 scale=scale,
                 end_x=start_x-l
                 )
        index += 1
        print("end_x", start_x-l, "start_x", start_x,
              "start_time", s, "duration", d)
    bubble(9)


def t47_5():
    import Bubble
    import Gress

    fish = Bas.BasType.parseXML(
        './resource/purple_fish_left.svg', offsetX=-350, offsetY=-350)

    delay = 1.5
    bubble_duration = 0.6

    g_delay = bubble_duration + delay

    swim_quick(fish, start_time=6, duration=8, start_x=120,
               base_y=30, sectorColor='0x6A5ACD', sectorBorder=False)
    # fish_many(fish, 4, 120, base_y=10,
    #           count=1, duration=8, beforeDelay=1.5, scale=0.3)

    Gress.create_one(start_time=g_delay + 0.4, start_x=20, end_x=-20,
                     colors=['0x063D53', '0x057ABD'], included_angle=[-5, 3])
    Gress.create_one(start_time=g_delay + 0.6, start_x=45, end_x=-20,
                     colors=['0x006DAF', '0x058AD4', '0x1288A8'], included_angle=[-5, 0, 8])
    Gress.create_one(start_time=g_delay + 0.8, start_x=70, end_x=-20,
                     colors=['0x008ACE', '0x26BAD0'], included_angle=[-2, 5])
    Gress.create_one(start_time=g_delay + 1.0, start_x=95, end_x=-20,
                     colors=['0x018A86', '0x028E83', '0x024E28'], included_angle=[-6, 0, 4])
    Gress.create_one(start_time=g_delay + 1.2, start_x=120, end_x=-20,
                     colors=['0x077B43', '0x39A12F'], included_angle=[-4, 0, 2])

    # 需要提前消失
    Gress.create_one(start_time=g_delay + 1.4, start_x=145, end_x=20,
                     colors=['0x32A03C', '0x3D7233'], included_angle=[-7, 0])
    Gress.create_one(start_time=g_delay + 1.6, start_x=170, end_x=40,
                     colors=['0xF0D719', '0xFEC70B', '0xF8D04B'], included_angle=[-4, 1, 5])
    Gress.create_one(start_time=g_delay + 1.8, start_x=195, end_x=60,
                     colors=['0xED9801', '0xEE8C8F'], included_angle=[0, 6])
    Gress.create_one(start_time=g_delay + 2.0, start_x=220, end_x=80,
                     colors=['0xEE4823', '0xEE4823'], included_angle=[-4, 3])

    Bubble.create_many(
        start_time=0,
        duration_sum=delay,
        group_count=30,
        x_min=-20,
        x_max=90,
        y_end_base=-30,
        group_duration=bubble_duration,
        bubble_duration=bubble_duration,
        size_base=0,
        alpha_base=1,
        end_alpha=0.6
    )

    Bubble.create_many(
        start_time=delay,
        duration_sum=bubble_duration*3,
        group_count=80,
        x_min=-20,
        x_max=90,
        y_end_base=-30,
        group_duration=bubble_duration,
        bubble_duration=bubble_duration,
        size_base=10,
        alpha_base=1,
        end_alpha=0.6
    )
    bubble(10, 6)


def t63():
    import Bubble
    bubble_duration = 0.6

    blueFish = Bas.BasType.parseXML(
        './resource/white_blue_fish.svg', offsetX=-300, offsetY=-550)
    swim_rush(blueFish, start_time=1 + bubble_duration*2.5,
              sectorColor="0x05498F", sectorBorder=False, base_y=80, scale=0.5)

    Bubble.create_many(
        start_time=0,
        duration_sum=1.5,
        group_count=10,
        x_min=-20,
        x_max=90,
        y_end_base=-30,
        group_duration=bubble_duration,
        bubble_duration=bubble_duration,
        size_base=0,
        alpha_base=1,
        end_alpha=0.6
    )

    Bubble.create_many(
        start_time=2,
        duration_sum=bubble_duration*3,
        group_count=80,
        x_min=-20,
        x_max=90,
        y_end_base=-30,
        group_duration=bubble_duration,
        bubble_duration=bubble_duration,
        size_base=10,
        alpha_base=1,
        end_alpha=0.6
    )


def t70():
    orangeFish = Bas.BasType.parseXML(
        './resource/orange_white_fish_left_no_sector.svg', offsetX=-350, offsetY=-300)
    swim_rush(orangeFish, start_time=0,
              sectorColor="0xFF9640", base_y=45)

    orangeFish = Bas.BasType.parseXML(
        './resource/orange_white_fish_left_no_sector_yellow.svg', offsetX=-350, offsetY=-300)
    swim_rush(orangeFish, start_time=2.3,
              sectorColor="0xECB915", base_y=75, scale=0.55)

    fish = Bas.BasType.parseXML(
        './resource/long_fish.svg', offsetX=-135, offsetY=-170)
    swim_quick(fish, 7, 9, 120, 20, '0x734F4D', scale=0.4, sectorScale=0.5,
               sectorBorder=False, sectorRorateX=180, sectorRorateZMin=30, sectorRorateZMax=60)
    swim_quick(fish, 8, 9, 120, 25, '0x734F4D', scale=0.4, sectorScale=0.5,
               sectorBorder=False, sectorRorateX=180, sectorRorateZMin=30, sectorRorateZMax=60)
    swim_quick(fish, 8, 10, 120, 15, '0x734F4D', scale=0.4, sectorScale=0.5,
               sectorBorder=False, sectorRorateX=180, sectorRorateZMin=30, sectorRorateZMax=60)

    # orangeFish = Bas.BasType.parseXML(
    #     './resource/团鱼.svg', offsetX=-150, offsetY=-200)
    # swim_quick(orangeFish, start_time=9, duration=8, start_x=120,
    #           sectorColor="0xFF9640", sectorScale=0.3, sectorBorder=False, base_y=45)

    orangeFish = Bas.BasType.parseXML(
        './resource/团鱼.svg', offsetX=-150, offsetY=-200)
    swim_rush(orangeFish, start_time=8.5,
              sectorColor="0xFF9640", sectorScale=0.6, sectorBorder=False, base_y=70, scale=0.9)
    bubble(9)


def t79():
    fish = Bas.BasType.parseXML(
        './resource/long_fish_purple.svg', offsetX=-135, offsetY=-170)

    count = 12
    while count >= 0:
        swim_quick(fish,
                   start_time=5 + random.uniform(0, 2),
                   duration=8 + random.uniform(0, 2),
                   start_x=120,
                   base_y=25 + random.uniform(-10, 10),
                   sectorColor='0xBD95BC',
                   scale=0.2, sectorScale=0.25, sectorBorder=False, sectorRorateX=180, sectorRorateZMin=30, sectorRorateZMax=60)
        count -= 1

    fish = Bas.BasType.parseXML(
        './resource/带鱼.svg', offsetX=-135, offsetY=-170)
    swim_rush(fish, 4, 90, '0x000000', sectorBorder=False,
              sectorScale=0, scale=1.4)

    bubble(9)


def t88():

    orangeFish = Bas.BasType.parseXML(
        './resource/orange_fish_left.svg', offsetX=-350, offsetY=-300)
    swim_rush(orangeFish, start_time=0.5, sectorBorder=0,
              sectorColor="0xFF8931", base_y=20, offsetY=20)

    blueFish = Bas.BasType.parseXML('./resource/blue_fish.svg')
    fish_many(blueFish, 3, 120, base_y=30, y_offset_min=-
              5, y_offset_max=10, count=11, duration=10)
    bubble(13)


def t101():
    bubble(18)


def t119():
    blueFish = Bas.BasType.parseXML('./resource/blue_fish.svg')
    fish_many(blueFish, 0, 120, base_y=40, y_offset_min=-
              5, y_offset_max=10, count=11, duration=8)
    orangeFish = Bas.BasType.parseXML('./resource/red_fish_left.svg')
    fish_many(orangeFish, 6, 120, base_y=60, y_offset_min=-
              5, y_offset_max=10, count=11, duration=8, scale=0.06)
    bubble(14)

def t133():
    blueFish = Bas.BasType.parseXML('./resource/dark_blue.svg')
    fish_many(blueFish, 0, 120, base_y=40, y_offset_min=-
              5, y_offset_max=10, count=11, duration=8)
    orangeFish = Bas.BasType.parseXML('./resource/dark_blue_white.svg')
    fish_many(orangeFish, 6, 120, base_y=60, y_offset_min=-
              5, y_offset_max=10, count=11, duration=8, scale=0.06)
    bubble(14)


# t0(6)
# t6(10)
# t16()
# t32()
# t41()
# t47_5()
# t63()
# t70()
# t79()
# t88()
# t101()
# t119()
t133()


pyperclip.copy(Bas.read_bas())


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
