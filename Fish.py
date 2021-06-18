import Bas
import random

fish = Bas.BasType({
    "content": "<。)#)))≦ ",
    "anchorX": 1,
    "x": "120%"
})

orangeFish = Bas.BasType.parseXML('./resource/orange_fish_left.svg')
orangeWhiteFish = Bas.BasType.parseXML('./resource/orange_white_fish_left.svg')
blueFish = Bas.BasType.parseXML('./resource/blue_fish.svg')
squid = Bas.BasType.parseXML('./resource/squid.svg')
squid_eye = Bas.BasType.parseXML('./resource/squid_eye.svg')
octopus = Bas.BasType.parseXML('./resource/octopus.svg')
red_fish = Bas.BasType.parseXML('./resource/red_fish_left.svg')
long_fish = Bas.BasType.parseXML('./resource/long_fish.svg')
long_fish1 = Bas.BasType.parseXML('./resource/long_fish1.svg')

fishs = [orangeFish, orangeWhiteFish, blueFish, squid,
         squid_eye, octopus, red_fish, long_fish, long_fish1]

fish_path1 = Bas.BasType({
    "d": "M472.2688 808.96c-47.104 0-105.8816-32.9728-147.0464-60.8256-7.168-4.7104-9.8304-13.312-6.9632-21.504 2.8672-7.9872 10.4448-12.9024 19.0464-12.0832 82.1248 8.192 289.9968 15.5648 443.8016-95.0272l7.7824-5.5296 6.144 7.3728c44.8512 53.6576 87.4496 73.3184 115.3024 80.2816 9.216 2.2528 17.6128 3.4816 24.576 3.8912-37.6832-33.792-60.416-83.7632-63.488-140.9024-3.4816-63.8976 17.8176-124.3136 57.9584-166.7072-74.1376 4.5056-133.7344 83.5584-134.3488 84.5824l-6.144 8.3968-8.192-6.3488c-134.5536-102.4-366.7968-94.8224-434.5856-90.112-5.7344 0.4096-10.4448-3.8912-10.8544-9.4208-0.4096-5.7344 3.8912-10.4448 9.4208-10.8544 68.4032-4.7104 299.2128-12.288 440.32 88.2688 20.6848-24.7808 88.4736-96.6656 170.8032-83.5584l22.528 3.6864-17.8176 14.336c-45.8752 37.2736-72.2944 101.1712-68.608 166.5024 3.2768 61.0304 31.3344 112.8448 76.5952 141.9264l19.456 12.4928-22.1184 5.9392c-3.6864 1.024-88.064 22.3232-180.224-82.3296-153.3952 105.472-353.28 101.9904-441.5488 94.208 51.8144 33.9968 97.0752 52.4288 128.4096 52.4288 18.2272 0 30.72-3.6864 35.2256-10.4448 4.096-5.9392 1.2288-13.7216 1.2288-13.9264-2.048-5.3248 0.4096-11.264 5.7344-13.312 5.3248-2.048 11.264 0.4096 13.312 5.7344 2.6624 6.5536 4.9152 20.8896-3.2768 32.9728-9.0112 13.312-26.624 19.8656-52.4288 19.8656z",
}, 'path')

fish_path2 = Bas.BasType({
    "d": "M239.616 716.8c-19.2512 0-105.472-30.5152-154.4192-78.6432-23.9616-23.552-36.2496-48.5376-36.4544-73.728 0-27.648 15.36-57.5488 45.2608-88.6784 26.2144-27.2384 63.6928-55.5008 108.544-81.5104 89.088-51.6096 199.0656-90.3168 287.1296-100.9664 103.8336-12.6976 169.3696 13.5168 184.32 73.9328 1.4336 5.5296-2.048 11.0592-7.3728 12.4928-5.5296 1.4336-11.0592-2.048-12.4928-7.3728-16.384-65.9456-108.544-64.9216-161.9968-58.368-85.4016 10.4448-192.512 48.128-279.3472 98.304-89.9072 52.0192-143.5648 108.9536-143.7696 152.3712 0.2048 19.456 10.4448 39.5264 30.3104 59.1872 41.984 41.3696 114.2784 68.4032 135.5776 72.2944 39.1168-47.9232 52.4288-103.0144 39.7312-163.4304-9.8304-47.104-32.768-80.0768-32.9728-80.2816-3.2768-4.7104-2.048-11.0592 2.4576-14.336 4.7104-3.2768 11.0592-2.048 14.336 2.4576 1.024 1.4336 25.1904 36.2496 36.0448 87.04 10.0352 47.3088 10.0352 118.1696-47.5136 185.7536l-3.072 3.4816H239.616z",
}, 'path')

fish_path3 = Bas.BasType({
    "d": "M185.344 533.2992m-22.9376 0a22.9376 22.9376 0 1 0 45.8752 0 22.9376 22.9376 0 1 0-45.8752 0Z",
}, 'path')


def create_default(start_time, start_x):
    y = random.uniform(10, 90)
    attr = {"x": f"{start_x}%", "y": f"{y}%",
            "fillColor": "0x2b6f9b", "scale": 0.1}
    f1 = Bas.BasObject(fish_path1, attr)
    f2 = Bas.BasObject(fish_path2, attr)
    f3 = Bas.BasObject(fish_path3, attr)
    group = Bas.BasGroup([f1, f2, f3])

    Bas.BasAnimate().animate_g(
        group, duration=start_time
    ).animate_g(
        group, duration=0, attribute={"alpha": 1}
    ).animate_g(
        group, duration=8, attribute={"x": f"-10%"}
    ).finish()


def create_many(type, start_time, start_x, count=10):
    blue_fish_start_time = random.randint(3, 12) + start_time
    y = random.randint(10, 80)
    while count >= 0:
        create_one(type, blue_fish_start_time + random.uniform(0, 2),
                   start_x + count, y + random.uniform(0, 40))
        count -= 1


def create_one(type, start_time, start_x, y=None):
    if y is None:
        y = random.uniform(10, 90)
    attr = {"x": f"{start_x}%", "y": f"{y}%", 'scale': 0.05}
    fish = None
    if type < len(fishs):
        fish = Bas.BasObject(fishs[type], attr)
        Bas.BasAnimate().animate(
            fish, duration=start_time
        ).animate(
            fish, duration=0, attribute={"alpha": 1}
        ).animate(
            fish, duration=8, attribute={"x": f"-10%"}
        ).finish()
    else:
        create_default(start_time, start_x)
