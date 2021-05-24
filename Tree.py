#Import minecrrat API module
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
x, y, z = mc.player.getPos()

mc.setBlocks(x-9,y,z,x-9,y+8,z,17)
mc.setBlocks(x-6,y+1,z+3,x-12,y+2,z-3,18)
mc.setBlocks(x-7,y+3,z+2,x-11,y+4,z-2,18)
mc.setBlocks(x-8,y+5,z+1,x-10,y+7,z-1,18)
mc.setBlocks(x-9,y+8,z+1,x-9,y+8,z-1,18)
mc.setBlocks(x-8,y+8,z,x-10,y+8,z,18)
mc.setBlock(x-9,y+9,z,18)
