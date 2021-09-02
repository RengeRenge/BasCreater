from lib import Bas
import random

bubble = Bas.BasType({
    "content": "●",
    "color": "0x2dfffe",
    "y": "120%",
    "fontSize": "15%",
    "bold": 0,
    "textShadow": 0,
    "alpha": 0.4
})


def create_many(start_time, duration_sum, group_count, x_min=None, x_max=None, y_end_base=-10, group_duration=3, bubble_duration=2, size_base=0, alpha_base=None, end_alpha=0):
    t = 0
    while t < duration_sum:
        right = random.randint(0, 1)
        count = group_count
        while count >= 0:
            count -= 1
            animate = Bas.BasAnimate()
            # x = random.randint(20, 85)
            if x_min != None and x_max != None:
                x = random.randint(x_min, x_max)
            else:
                x = random.randint(50, 85) if right else random.randint(10, 45)
            bubble_size = random.randint(6, 9) + size_base
            atti = {"x": f"{x}%", 'fontSize': f'{bubble_size}%'}
            if alpha_base is not None:
                atti['alpha'] = alpha_base
            bub = Bas.BasObject(bubble, atti)
            animate.animate(obj=bub,
                            delay=start_time + t +
                            random.uniform(0, group_duration),
                            duration=bubble_duration + random.uniform(0, 0.5),
                            attribute={
                                "y": f"{y_end_base + random.uniform(0, -5)}%",
                                "x": f"{x + random.uniform(-5, 20)}%",
                                "alpha": end_alpha,
                                'fontSize': f'{bubble_size + 5}%'
                            })
            animate.finish()
        t += group_duration
