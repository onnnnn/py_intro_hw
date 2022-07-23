from mcpi.minecraft import Minecraft
from random import randrange
import time

mc = Minecraft.create()
#注意此處玩家ID要設定為自己的ID
myID = "R_Hsien"        
playerID = mc.getPlayerEntityId(myID) 

global step
global score
step = 1
score = 0

for i in range(15):     #隨機顏色設定遊戲牆
    x,y,z = mc.player.getTilePos()
    x = x+15            #距離拉遠
    y = y+i-4           #遊戲牆位置下降
    z = z-7             #左右置中
    for j in range(15):
        r = randrange(0,16)
        z = z+1
        mc.setBlock(x,y,z,35,r)
        
#給玩家遊戲裝備
mc.executeCommand("clear " +myID)
mc.executeCommand("give " +myID + " minecraft:Bow")
mc.executeCommand("give " +myID + " minecraft:Arrow 64")

def check (blkID,DATA):   #檢查and辨認羊毛顏色
    global color
    
    if blkID == 35:
        if DATA == 0:
            color = "白色羊毛"
        if DATA == 1:
            color = "橙色羊毛"
        if DATA == 2:
            color = "洋紅色羊毛"
        if DATA == 3:
            color = "淺藍色羊毛"
        if DATA == 4:
            color = "黃色羊毛"
        if DATA == 5:
            color = "淺綠色羊毛"
        if DATA == 6:
            color = "粉紅色羊毛"
        if DATA == 7:
            color = "灰色羊毛"
        if DATA == 8:
            color = "淺灰色羊毛"
        if DATA == 9:
            color = "青色羊毛"
        if DATA == 10:
            color = "紫色羊毛"
        if DATA == 11:
            color = "藍色羊毛"
        if DATA == 12:
            color = "棕色羊毛"
        if DATA == 13:
            color = "綠色羊毛"
        if DATA == 14:
            color = "紅色羊毛"
        if DATA == 15:
            color = "黑色羊毛"
    else :
        color = "錯誤選項"
    
    return color

def play (playerID):
    global step
    global score
    Tset = time.time()      #取得該回合開始時間
    r = randrange(1,16)
    Target = check (35,r)
    mc.postToTitle(playerID,"目標:"+ Target)
    step = 1
    
    
    while True:     
        hits = mc.events.pollProjectileHits()   #取得箭矢射中位置
        now = time.time()       #取得目前時間
        TD = int(now-Tset)      #開始時間的時間差
        sec = 20 -TD
        
        if score >= 32:
            step = 4
            return step
        elif sec > 0:
            if len(hits) >0:
                hit = hits[0]
                x ,y ,z = hit.pos.x+1 ,hit.pos.y ,hit.pos.z     #往箭矢落點取牆上方塊
                block = mc.getBlockWithData(x,y,z)
                blkID = mc.getBlock(x,y,z)
                DATA = block.data
                if DATA == r:   #判斷是否擊中目標方塊
                    mc.setBlock(x,y,z,0)    #消滅正確的方塊
                    mc.postToChat("不錯喔，金錠+1")
                    mc.executeCommand("give " +myID + " minecraft:Gold_ingot 1")
                    score += 1
                    step = 2
                    return step
                else:
                    color = check (blkID,DATA)
                    mc.postToChat("這不是"+Target+"，這是"+color+"，你還有"+str(sec)+"秒")
        else:
            mc.postToChat("很遺憾，時間到了")
            step = 3
            return step



mc.postToTitle(playerID,"歡迎來到鷹眼神射")
time.sleep(3)
mc.postToTitle(playerID,"接下來")
time.sleep(3)
mc.postToTitle(playerID,"你要射我指定顏色的羊毛")
time.sleep(3)
mc.postToTitle(playerID,"20秒內沒射到")
time.sleep(3)
mc.postToTitle(playerID,"遊戲就會結束")
time.sleep(3)
mc.postToTitle(playerID,"3")
time.sleep(1)
mc.postToTitle(playerID,"2")
time.sleep(1)
mc.postToTitle(playerID,"1")
time.sleep(1)
mc.postToTitle(playerID,"開始")
time.sleep(1)

while step < 3:
    step = play(playerID)

if step == 3:
    mc.postToTitle(playerID,"Game Over")
    mc.createExplosion(x, y-7, z-7, 25)
elif step == 4:
    mc.postToTitle(playerID,"恭喜過關")
    
    
    
            