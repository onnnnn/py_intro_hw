from mcpi.minecraft import Minecraft
import random, time
#import time

mc = Minecraft.create()

x, y, z = mc.player.getTilePos()           # 我的位置

# 在一個地方爆炸
time.sleep(3)
#mc.createExplosion(x, y, z)                # 爆炸

# 在一整個範圍內爆炸
pos = mc.player.getTilePos()
for i in range(30):                        # 要爆多少次
    break
    time.sleep(0.5)                        # 暫停多少秒
    x = pos.x + random.uniform(-20, 20)    # 範圍 
    z = pos.z + random.uniform(-20, 20)
    y = pos.y                              # 高度（y不變 -> 原地）
    #mc.createExplosion(x, y, z)
    pass

mc.setBlocks(
    x-1, y+3, z-1, 
    x+1, y+5, z+1, 
    161) # 葉子

mc.setBlocks(
    x, y, z, 
    x, y+4, z, 
    17) # 樹幹

x+=5
y+=5
z+=5

def plant_tree(x, y, z):
    mc.setBlocks(
        x-1, y+3, z-1, 
        x+1, y+5, z+1, 
        161) # 葉子

    mc.setBlocks(
        x, y, z, 
        x, y+4, z, 
        17) # 樹幹



for i in range(10):
    for j in range(5):
        plant_tree(x+i*5, y, z+j)