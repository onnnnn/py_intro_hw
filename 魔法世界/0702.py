import random
from time import sleep
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x, y, z = mc.player.getTilePos()

init = 20
while init < 10:
    mc.executeCommand("time add 50")
    sleep(0.05)
    init += 1
    # "control + c" 可以提前退出程式

