from matplotlib import rc
import numpy as np
import matplotlib.pyplot as plt

rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})

block_K=6300. # constant
block_base=np.arange(2000,6001,50)
block_div=np.arange(2000,6001,50)

# make a grid
bb,bd=np.meshgrid(block_base,block_div)
# calculate block reduction for both
DR_base=bb/(bb+block_K)
DR_div=(bb+bd)/(bb+bd+block_K)
# calculate the relative reduction
DR_rel=1-(1-DR_div)/(1-DR_base)

# diags
print bb.shape
print bd.shape
print DR_base.shape
fig,ax=plt.subplots(2,2,sharex=True,sharey=True)
ax[0,0].contourf(bb,bd,100*DR_base,levels=np.arange(20,71,1),cmap='RdYlGn')
cs0=ax[0,0].contour(bb,bd,100*DR_base,levels=np.arange(20,71,5),colors='black')
ax[0,0].clabel(cs0, inline=1, fontsize=10, fmt="%i")
ax[0,1].contourf(bb,bd,100*DR_div,levels=np.arange(20,76,1),cmap='RdYlGn')
cs1=ax[0,1].contour(bb,bd,100*DR_div,levels=np.arange(20,76,5),colors='black')
ax[0,1].clabel(cs1, inline=1, fontsize=10, fmt="%i")
ax[1,0].contourf(bb,bd,100*DR_rel,levels=np.arange(10,46,1),cmap='RdYlGn')
cs2=ax[1,0].contour(bb,bd,100*DR_rel,levels=np.arange(10,46,5),colors='black')
ax[1,0].clabel(cs2, inline=1, fontsize=10, fmt="%i")
ax[1,1]=[]
#plt.grid()
#plt.colorbar()
plt.show()
