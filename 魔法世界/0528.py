from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

x, y, z = mc.player.getTilePos()

# 直的道路
for i in range(20):
    #mc.setBlock(x, y-1, z+i, 1)
    # print(i)
    break  # 斷開

# 先做樓梯
for i in range(20):  # 20層的樓梯
    # mc.setBlocks(x, y-1+i, z+i, x+2, y-1+i, z+i, 2)  # 每一層有這個長方形
    break

# 做空中平台
#mc.setBlocks(x, y-1, z, x+6, y-1, z+6, 2)
