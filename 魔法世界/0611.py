from mcpi.minecraft import Minecraft
import random
import time


mc = Minecraft.create()
x, y, z = mc.player.getTilePos() # 我的位置

while True: # 一直都有達到條件
    #mc.postToChat('hello world')
    hits = mc.events.pollBlockHits() # list 清單/串列
    if len(hits) > 0:
        hit = hits[0]
        x, y, z = hit.pos.x, hit.pos.y, hit.pos.z # 每次點擊的位子
        #block = mc.getBlock(x, y, z) # 拿到是什麼方塊
        #mc.postToChat('恭喜你拿到了' + str(block))
        #mc.setBlock(x, y, z, 41) # 放置方塊
    break # 暫停 退出

mc.setSign(
    x, y, z, # 放的位置
    63, # 告示牌種類
    15, # 面向的角度
    '我愛', # 第一行文字
    'Minecraft', 
    '', 
    '也愛Python'
)

# CHICKEN = Entity(93, "CHICKEN") #雞
# COW = Entity(92, "COW") #牛
for i in range(10):
    #mc.spawnEntity(x, y, z, 92)
    pass # 不知道要做什麼，反正就下一步（跳過）


pos = mc.player.getTilePos()
for i in range(50):
    x = pos.x + random.uniform(-20, 20) # 範圍 
    z = pos.z + random.uniform(-20, 20)
    y = pos.y + 50 # 高度
    mc.spawnEntity(x, y, z, 93)
    time.sleep(0.2)