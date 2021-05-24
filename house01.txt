#Import minecrrat API module
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
x, y, z = mc.player.getPos()
Floor = [x-2, y-1, z-2, x+2, y-1, z+2, 5]
roof = [x-2,y+3,z-2,x+2,y+3,z+2, 17]
def house():
    mc.setBlocks(Floor)
    mc.setBlocks(x-2,y,z-2,x-2,y+2,z+2,5) #wall1
    mc.setBlocks(x-2,y,z-2,x+2,y+2,z-2,5) #wall2
    mc.setBlocks(x+2,y,z-2,x+2,y+2,z+2,5) #wall3
    mc.setBlocks(x-2,y,z+2,x+2,y+2,z+2,5) #wall4
    mc.setBlocks(roof)
    mc.setBlock(x-2,y+1,z,20) #window1
    mc.setBlock(x,y+1,z-2,20) #window2
    mc.setBlock(x+2,y+1,z,20) #window3
    mc.setBlock(x,y+1,z+2, 0) #door1
    mc.setBlock(x,y,z+2, 0) #door2
house()
