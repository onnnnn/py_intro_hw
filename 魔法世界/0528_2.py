from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x, y, z = mc.player.getTilePos()


# 先做樓梯
for i in range(20):  # 20層的樓梯
    mc.setBlocks(x, y-1+i, z+i, x+2, y-1+i, z+i, 2)  # 每一層有這個長方形

# 做空中平台
mc.setBlocks(x+2, y-1+19, z+19, x+6+2, y-1+19, z+6+19, 2)
