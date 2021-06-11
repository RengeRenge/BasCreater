import Bas
import random

bubble = Bas.new_type("bub", {
    "content": "●",
    "color": "0x2dfffe",
    "y": "120%",
    "fontSize": "15%",
    "bold": 0,
    "textShadow": 0,
    "alpha": 0.4
})

def create_many(start_time, durtion_sum, group_count):
    durtion = 0
    while durtion < durtion_sum + start_time:
        right = random.randint(0, 1)
        count = group_count
        while count >= 0:
            count -= 1
            animate = Bas.BasAnimate()
            # x = random.randint(20, 85)
            x = random.randint(50, 85) if right else random.randint(10, 45)
            bubble_size = random.randint(6, 9)
            bub = Bas.create_obj(type=bubble,
                                 attribute={"x": f"{x}%", 'fontSize': f'{bubble_size}%'})
            animate.animate(obj=bub,
                            delay=start_time + durtion + random.uniform(0, 3),
                            duration=random.uniform(2, 2.5),
                            attribute={
                                "y": f"{random.uniform(-10, -15)}%",
                                "x": f"{x + random.uniform(-5, 20)}%",
                                "alpha": 0,
                                'fontSize': f'{bubble_size + 5}%'
                            })
            animate.finish()
        durtion += 3
