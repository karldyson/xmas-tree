from tree import RGBXmasTree
import random
import time

tree = RGBXmasTree()

def random_color():
    r = random.random() ** 3
    g = random.random() ** 3
    b = random.random() ** 3
    return (r, g, b)

try:
    while True:
        pixel = random.choice(tree)
        pixel.color = random_color()
        pixel.brightness = random.random() ** 3
        time.sleep(0.10)
except KeyboardInterrupt:
    tree.close()
