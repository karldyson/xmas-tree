# README #

This code is designed to work with the xmas tree kit from The Pi Hut.

https://thepihut.com/products/3d-xmas-tree-for-raspberry-pi

I wrote the code on a Pi Zero W, and so have no idea if it will work as expected on other Pi models

xmas-tree is some code I knocked together based on the example that causes the tree to glimmer all over.

There are a number of different options; you can type the one you want at the command line, or, if omitted, the code will pick a new one at random every 60 seconds.

There's no code annotation yet, but you should be able to work out most of it. I'll try to find some time to add annotation, mostly because otherwise I'll have totally forgotten what I did by next Christmas.

## Installation ##

Copy it to somewhere, and run it (duh). I had it in ```/usr/local/bin``` so that it was in the path, and then I added ```/usr/local/bin/xmas-tree &``` to ```/etc/rc.local``` on the pi zero.

## Warranty ##

There is, of course, no warranty with this code. It works for me, and does what I want. It's not my fault if it eats your cat or scares your children.
