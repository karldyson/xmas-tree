from tree import RGBXmasTree
from colorzero import Color, Hue

tree = RGBXmasTree()

tree.color = Color('red')

try:
    tree.brightness = 0
except KeyboardInterrupt:
    tree.close()
