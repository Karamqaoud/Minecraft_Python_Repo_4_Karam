from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

blockType = mc.getBlock(x, y, z)
blockType = mc.getBlock(x, y - 1, z)
mc.postToChat(" The player is in a tree: " + str(blockType == 18 or blockType2 == 11))  
