from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()
time.sleep(0)

pos = mc.player.getTilePos()
x, y, z = pos

mc.setBlock(x, y-1, z+1, 100)
mc.setBlock(x+1, y-1, z+1, 100)
mc.setBlock(x+2, y-1, z+1, 100)
mc.setBlock(x, y - 1, z, 100)
mc.setBlock(x+1, y-1, z, 11)
mc.setBlock(x+2, y-1, z, 100)
mc.setBlock(x, y-1, z-1, 100)
mc.setBlock(x+1, y-1, z-1, 100)
mc.setBlock(x+2, y-1, z-1, 100)
