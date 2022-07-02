import time
from mcpi.minecraft import Minecraft

mc = Minecraft.create() # 把python跟minecraft做連結

x, y, z = mc.player.getTilePos() # 得到玩家現在的位子（x, y, z)

def buildpyramid(x, y, z, base=10):
    '''建造金字塔'''

    base = base # 底部要多大？
    height = (base//2) + 1 # 金字塔高度

    for i in range(height):
        time.sleep(3) # 讓程式休息
        x1 = x + i
        y1 = y + i
        z1 = z + i

        x2 = x + base - i
        z2 = z + base - i
        mc.setBlocks(x1, y1, z1, x2, y, z2, 24)

# 建第一次金字塔
buildpyramid(x, y, z)
# 建第二次金字塔
#buildpyramid(x+20, y+20, z+20, 30)
