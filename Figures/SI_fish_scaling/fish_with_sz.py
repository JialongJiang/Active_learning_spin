# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 15:48:48 2019

@author: Jialong Jiang
"""

import matplotlib.pyplot as plt
from matplotlib import cm
import scipy.io as sio
import numpy as np
import matplotlib as mpb
import matplotlib.gridspec as gridspec
from plot_network import move_axis 

mpb.rcParams.update({'figure.dpi': 300})
mpb.rcParams.update({'font.size': 14})
mpb.rcParams.update({'axes.labelsize': 16})
mpb.rcParams.update({'axes.titlesize': 16})


mdata = sio.loadmat('fish_with_sznn')
locals().update(mdata)
rec_ftrinv = rec_ftrinv * np.arange(1, 7)


figw = 17.8 / 2.54 * 2
figh = 17.8 / 2.54 * 13 / 40 * 2
fig = plt.figure(figsize=[figw, figh])
gs = gridspec.GridSpec(1, 3, width_ratios=[1, 1, 1], wspace=0.35, 
                       left=0.08, right=0.94)

ax1 = plt.subplot(gs[0])
ax3 = plt.subplot(gs[1])
ax2 = plt.subplot(gs[2])
ax2 = move_axis(ax2, 0.022, 0)

net_sz = np.array([8, 12, 16])
lin0 = ax1.plot(net_sz, np.log10(rec_ftrinv[:, :, 0]), color='C3', linestyle='none', 
         marker='o', label='No perturbations')
ax1.plot(net_sz, np.mean(np.log10(rec_ftrinv[:, :, 0]), axis=1), color='C3')
lin1 = ax1.plot(net_sz, np.log10(rec_ftrinv[:, :, 2]), color='C4', linestyle='none', 
         marker='X', label='2 perturbations')
ax1.plot(net_sz, np.mean(np.log10(rec_ftrinv[:, :, 2]), axis=1), color='C4')
lin2 = ax1.plot(net_sz, np.log10(rec_ftrinv[:, :, 5]), color='C5', linestyle='none', 
         marker='P', label='5 perturbations')
ax1.plot(net_sz, np.mean(np.log10(rec_ftrinv[:, :, 5]), axis=1), color='C5')
ax1.set_xticks([8, 12, 16])
ax1.set_xlabel('Network size')
ax1.set_yticks([2, 6, 10])
ax1.set_yticklabels(['1e2', '1e6', '1e10'])
ax1.set_ylim([0.7, 14])
handles, labels = ax1.get_legend_handles_labels()
ax1.legend(handles[:: 10], labels[:: 10], loc=[0.01, 0.72])
ax1.set_ylabel(r'$\mathrm{Tr}\mathcal{I}^{- 1}$')

def plot_traj(ax, ind, dat, color, dgap=1, lab=False, st=0, linst='-', errshift=0):
    datm = np.mean(dat, axis=1)
    datsd = np.std(dat, axis=1)
    if lab:
        ax.plot(ind, datm, color, linestyle=linst, linewidth=2, label=lab)
    else:
        ax.plot(ind, datm, color, linestyle=linst, linewidth=2)  
    ax.plot(ind, dat, color, linestyle=linst, alpha = 0.2)
    ax.errorbar(ind[st:: dgap] + errshift, datm[st:: dgap], yerr=datsd[st:: dgap], 
                fmt='none', color=color, capsize=4)
    
ind_round = np.arange(1, 6)
change_ratio0 =  np.log10(rec_ftrinv[0, :, 1:]) - np.expand_dims(
        np.log10(rec_ftrinv[0, :, 0]), axis=1)
plot_traj(ax2, ind_round, change_ratio0.T, 'C0')

change_ratio1 =  np.log10(rec_ftrinv[1, :, 1:]) - np.expand_dims(
        np.log10(rec_ftrinv[1, :, 0]), axis=1)
plot_traj(ax2, ind_round, change_ratio1.T, 'C1', linst='--', errshift=0.1)

change_ratio2 =  np.log10(rec_ftrinv[2, :, 1:]) - np.expand_dims(
        np.log10(rec_ftrinv[2, :, 0]), axis=1)
plot_traj(ax2, ind_round, change_ratio2.T, 'C2', linst='-.', errshift=- 0.1)

ax2.set_yticks([- 2, - 4, - 6, - 8])
ax2.set_yticklabels(['1e-2', '1e-4', '1e-6', '1e-8'])
ax2.set_xticks(ind_round)
ax2.set_xlabel('Number of perturbations')
ax2.set_ylabel(r'Fold change of $\mathrm{Tr}\mathcal{I}^{- 1}$')
ax2.yaxis.set_label_coords(- 0.2, 0.5)

ind_round = np.arange(0, 6)
plot_traj(ax3, ind_round, np.log10(rec_ftrinv[0, :, :]).T, 'C0', lab='8-node')
plot_traj(ax3, ind_round, np.log10(rec_ftrinv[1, :, :]).T,
          'C1', linst='--', errshift=0.1, lab='12-node')
plot_traj(ax3, ind_round, np.log10(rec_ftrinv[2, :, :]).T, 
          'C2', linst='-.', errshift=- 0.1, lab='16-node')

ax3.set_yticks([2, 6, 10])
ax3.set_yticklabels(['1e2', '1e6', '1e10'])
ax3.set_xticks(ind_round)
ax3.set_xlabel('Number of perturbations')
ax3.set_ylabel(r'$\mathrm{Tr}\mathcal{I}^{- 1}$')
ax3.yaxis.set_label_coords(- 0.2, 0.65)
ax3.legend()

fxx1 = 0.04
fyy1 = 0.9
fxx2 = 0.36
fxx3 = 0.68

abcd_size = 18
fig.text(fxx1, fyy1, '(a)', fontsize=abcd_size)
fig.text(fxx2, fyy1, '(b)', fontsize=abcd_size)
fig.text(fxx3, fyy1, '(c)', fontsize=abcd_size)

plt.savefig('SI_fish_sz.pdf')
