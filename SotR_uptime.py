from matplotlib import rc
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('text', usetex = True)

SotR_recharge = 18.  # SotR recharge time
SotR_duration = 4.5  # SotR buff duration
J_recharge = 6.      # Judgment cooldown/recharge time
Sera_stats = 1007.   # Stat boost from Seraphim
Sera_uptime = 16./45. # relative Seraphim uptime when used on CD
h_conversion = 68.   # rating conversion for haste at 120
c_conversion = 72.   # rating conversion for crit at 120

# make a haste-crit-grid
h = np.arange(0,61,1)
c = np.arange(0,41,1)
hh,cc = np.meshgrid(h,c)
hh_Sera = hh+Sera_stats/h_conversion # increased haste value during Seraphim
cc_Sera = cc+Sera_stats/c_conversion # increased crit value during Seraphim

SotR_recharge_rate      = (1.+(1+cc     /100.)*(1+hh     /100.)/3)*(1+hh     /100.)
SotR_recharge_rate_Sera = (1.+(1+cc_Sera/100.)*(1+hh_Sera/100.)/3)*(1+hh_Sera/100.)
# avg. recharge rate during Sera is slightly higher due to higher stats from Sera
SotR_recharge_mean_Sera = Sera_uptime *SotR_recharge_rate_Sera + (1-Sera_uptime) * SotR_recharge_rate - 36./45.
SotR_uptime      = SotR_duration / SotR_recharge * SotR_recharge_rate
SotR_uptime_Sera = SotR_duration / SotR_recharge * SotR_recharge_mean_Sera
SotR_loss_Sera   = 1. - SotR_uptime_Sera / SotR_uptime

fig,ax = plt.subplots(3,1,figsize=(6,9),sharex = True,sharey = True)
ax[0].contourf(hh,cc,100*SotR_uptime,levels = np.arange(5.,101.,1),cmap = 'RdYlGn')
cs0 = ax[0].contour(hh,cc,100*SotR_uptime,levels = np.arange(5.,101.,5),linewidths=0.5,colors = 'black')
ax[0].clabel(cs0, inline = 1, fontsize = 10, fmt = "%i")
ax[0].yaxis.set_major_formatter(mtick.PercentFormatter())
ax[0].set_ylabel(r"crit") #, size = 20)
ax[0].set_title(r"SotR base uptime in percent as a function of haste and crit without Seraphim")
ax[0].xaxis.set_major_formatter(mtick.PercentFormatter())
ax[1].contourf(hh,cc,100*SotR_uptime_Sera,levels = np.arange(5.,101.,1),cmap = 'RdYlGn')
cs0 = ax[1].contour(hh,cc,100*SotR_uptime_Sera,levels = np.arange(5.,101.,5),linewidths=0.5,colors = 'black')
ax[1].clabel(cs0, inline = 1, fontsize = 10, fmt = "%i")
ax[1].yaxis.set_major_formatter(mtick.PercentFormatter())
ax[1].set_title(r"with Seraphim")
ax[1].yaxis.set_major_formatter(mtick.PercentFormatter())
ax[1].set_ylabel(r"crit") #, size = 20)
ax[2].contourf(hh,cc,100*SotR_loss_Sera,levels = np.arange(20.,61.,1),cmap = 'RdYlGn_r')
cs0 = ax[2].contour(hh,cc,100*SotR_loss_Sera,levels = np.arange(20.,61.,5),linewidths=0.5,colors = 'black')
ax[2].clabel(cs0, inline = 1, fontsize = 10, fmt = "%i")
ax[2].yaxis.set_major_formatter(mtick.PercentFormatter())
ax[2].set_title(r"relative loss due to Seraphim")
plt.xlabel(r"haste") #, size = 20)
plt.ylabel(r"crit") #, size = 20)
plt.savefig("SotR_uptime_all.pdf")
plt.show()
