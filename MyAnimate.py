from lib import Bas
import random


def bubble(duration, delay=0):
    import Bubble
    Bubble.create_many(delay, duration, 10)


def fish_many(type: Bas.BasType, start_time, start_x, base_y=40, y_offset_min=-10, y_offset_max=5, count=10, duration=8.0, beforeDelay=1, scale=0.1):
    delay = 0
    while count > 0:
        delay = random.uniform(delay, delay+beforeDelay)
        delay = max(0, delay)
        fish_one(type,
                 start_time=start_time + random.uniform(0, delay),
                 start_x=start_x + count,
                 base_y=base_y + random.uniform(-20, 20),
                 y_offset_min=y_offset_min,
                 y_offset_max=y_offset_max,
                 duration=duration,
                 scale=scale)
        count -= 1


def fish_one(type: Bas.BasType, start_time, start_x, base_y, y_offset_min, y_offset_max, duration, scale=0.1, end_x=-20):
    if base_y is None:
        base_y = random.uniform(10, 90)
    attr = {"x": f"{start_x}%", "y": f"{base_y}%", "alpha": 1, 'scale': scale}
    fish = None
    fish = Bas.BasObject(type, attr)

    animate = Bas.BasAnimate().animate(
        fish, duration=start_time
    )

    y_change_count = random.randint(1, 3)
    x = start_x
    l = start_x - end_x
    loop_count = 6
    offset = 1.0 * l / loop_count

    time = 0
    count = 0
    y_count = 0
    random_y = 0
    while fish.get_float('x') > end_x * scale*10:
        x = fish.get_float('x')
        y = fish.get_float('y')
        d = duration/loop_count

        if count % 2 == 0 and random.randint(1, 2) == 1 and y_count <= y_change_count:
            y_count += 1
            random_y = random.uniform(y_offset_min, y_offset_max)

        animate.animate(
            fish, duration=d, attribute={
                "x": f"{x - offset}%", "y": f"{y + random_y / (loop_count / y_change_count)}%"}
        )
        count += 1
        time += d
    animate.finish()


def swim_rush(type: Bas.BasType, start_time, base_y, sectorColor, sectorBorder=True, sectorScale=1, start_x=120, scale=0.3, offsetY=0):
    if base_y is None:
        base_y = random.uniform(10, 90)
    attr = {"x": f"{start_x}%", "y": f"{base_y}%", "alpha": 0, 'scale': scale}
    fish = None
    fish = Bas.BasObject(type, attr)

    if sectorScale > 0:
        sector = Bas.BasType(attribute={
            "content": "⎖",
            "bold": 1,
            "strokeWidth": 1 if sectorBorder else 0,
            "strokeColor": "0x000001",
            "textShadow": 1 if sectorBorder else 0,
            "anchorY": 0.85,
            "anchorX": 0.17,
            "color": sectorColor,
            "fontSize": f"{90*scale/0.3}",
            "x": f"{start_x}%",
            "y": f"{base_y}%",
            "rotateZ": 110,
            "scale": sectorScale
        })
        sectorObj = Bas.BasObject(sector, attribute={"alpha": 0, "y": f"{base_y}%"})

    animate = Bas.BasAnimate().animate(
        fish, duration=start_time,
    ).animate(
        fish, attribute={"alpha": 1}
    )

    if sectorScale > 0:
        sectorAni = Bas.BasAnimate().animate(
            sectorObj, duration=start_time,
        ).animate(
            sectorObj, attribute={"alpha": 1}
        )

    rush_duration = 0.4
    float_duration = 0.6
    end_x = -20 * scale * 10
    l = start_x

    rush_count = 10
    rush_offset = l * rush_duration / \
        (rush_duration + float_duration) / rush_count

    rush_v = rush_offset / rush_duration
    float_v = rush_v
    # x = start_x
    # l = start_x - -20.0
    # offset = 1.0 * (l - rush_count * rush_offset) / rush_count
    rush_offset_y = offsetY * rush_duration / \
        (rush_duration + float_duration) / rush_count
    rush_v_y = rush_offset_y / rush_duration
    float_v_y = rush_v_y

    while fish.get_float('x') > end_x:
        x = fish.get_float('x')
        att = {
            "x": f"{x - rush_offset}%",
        }
        if offsetY > 0:
            att["y"] = f"{fish.get_float('y') + rush_offset_y}%"

        animate.animate(
            fish,
            duration=rush_duration,
            attribute=att,
            timeFunction=Bas.BasAnimate.easeIn
        )
        if sectorScale > 0:
            att = {
                "x": f"{x - rush_offset}%", "rotateZ": 80
            }
            if offsetY > 0:
                att["y"] = f"{sectorObj.get_float('y') + rush_offset_y}%"

            sectorAni.animate(
                sectorObj,
                duration=rush_duration,
                attribute=att,
                timeFunction=Bas.BasAnimate.easeIn
            )

        x = fish.get_float('x')
        att = {
            "x": f"{x - float_duration * float_v}%",
        }
        if offsetY > 0:
            att["y"] = f"{fish.get_float('y') + float_duration * float_v_y}%"

        animate.animate(
            fish,
            duration=float_duration,
            attribute=att,
            timeFunction=Bas.BasAnimate.easeOut
        )
        if sectorScale > 0:
            att = {
                "x": f"{x - float_duration * float_v}%", "rotateZ": 110
            }
            if offsetY > 0:
                att["y"] = f"{sectorObj.get_float('y') + float_duration * float_v_y}%"

            sectorAni.animate(
                sectorObj,
                duration=float_duration,
                attribute=att,
                timeFunction=Bas.BasAnimate.easeOut
            )
    animate.finish()
    if sectorScale > 0:
        sectorAni.finish()


def swim_quick(type: Bas.BasType, start_time, duration, start_x, base_y, sectorColor, sectorBorder=True, scale=0.3, sectorScale=1, sectorRorateX=0, sectorRorateZMin=80, sectorRorateZMax=110):
    if base_y is None:
        base_y = random.uniform(10, 90)
    attr = {"x": f"{start_x}%", "y": f"{base_y}%", "alpha": 0, 'scale': scale}
    fish = None
    fish = Bas.BasObject(type, attr)

    sector = Bas.BasType(attribute={
        "content": "⎖",
        "bold": 1,
        "strokeWidth": 1 if sectorBorder else 0,
        "strokeColor": "0x000001",
        "textShadow": 1 if sectorBorder else 0,
        "anchorY": 0.85,
        "anchorX": 0.17,
        "color": sectorColor,
        "fontSize": "90",
        "x": f"{start_x}%",
        "y": f"{base_y}%",
        "rotateZ": sectorRorateZMax,
        "rotateX": sectorRorateX,
        "scale": sectorScale
    })
    sectorObj = Bas.BasObject(
        sector, attribute={"alpha": 0, "x": f"{start_x}%"})

    animate = Bas.BasAnimate().animate(
        fish, duration=start_time,
    ).animate(
        fish, attribute={"alpha": 1}
    )

    sectorAni = Bas.BasAnimate().animate(
        sectorObj, duration=start_time,
    ).animate(
        sectorObj, attribute={"alpha": 1}
    )

    rush_duration = 0.2
    end_x = -20 * scale * 10
    l = start_x - end_x

    rush_offset = l * (rush_duration / duration)
    # rush_v = rush_offset / rush_duration

    animate.animate(
        fish,
        duration=duration,
        attribute={
            "x": f"{end_x}%",
        }
    )

    while sectorObj.get_float('x') > end_x:
        x = sectorObj.get_float('x')
        sectorAni.animate(
            sectorObj,
            duration=rush_duration,
            attribute={
                "x": f"{x - rush_offset}%", "rotateZ": sectorRorateZMin
            },
        )

        x = sectorObj.get_float('x')
        sectorAni.animate(
            sectorObj,
            duration=rush_duration,
            attribute={
                "x": f"{x - rush_offset}%", "rotateZ": sectorRorateZMax
            },
        )

    animate.finish()
    sectorAni.finish()
