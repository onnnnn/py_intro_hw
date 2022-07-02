from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

mc.postToChat('hello_world!')

x, y, z = mc.player.getTilePos()

#mc.setBlock(x, y, z, 200)
#mc.setBlocks(x, y, z, x+3, y+3, z+3, 5)

mc.postToChat('hello')

t = 0
while False:
    x, y, z = mc.player.getTilePos()
    a = mc.getBlock(x, y-1, z+1)
    b = mc.getBlock(x, y-1, z-1)
    c = mc.getBlock(x-1, y-1, z)
    d = mc.getBlock(x+1, y-1, z)

    if a in [8, 9] or b in [8, 9] or c in [8, 9] or d in [8, 9]:
        mc.setBlocks(x+1, y-1, z+1, x-1, y-1, z-1, 103)
        time.sleep(0.01)
        print(t)
        t += 1

# generate flower whenever i go
while False:
    x, y, z = mc.player.getTilePos()
    mc.setBlock(x, y, z, 38)
    time.sleep(0.2)


x, y, z = mc.player.getTilePos()
a = 0
while a < 5:
    mc.setBlocks(x+10, y-30, z, x-10, y+1, z, 19)
    z = z - 5
    a = a + 1
