#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 23:26:22 2018

@author: jialongjiang
"""

import matplotlib.pyplot as plt
from matplotlib import cm
import scipy.io as sio
import numpy as np
import matplotlib as mpb
import matplotlib.gridspec as gridspec
from plot_network import plot_network, move_axis

mpb.rcParams.update({'font.size': 14})
mpb.rcParams.update({'axes.labelsize': 16})
mpb.rcParams.update({'axes.titlesize': 16})
mpb.rcParams.update({'figure.dpi': 300})

mdata = sio.loadmat("three_node_optimal")
locals().update(mdata)

'''
change the index to plot two different networks
'''
# cur_ind = 0
cur_ind = 1

figw = 15.3 / 2.54 * 2
figh = figw * 2.3 / 3
fig = plt.figure(figsize=[figw, figh])
gs = gridspec.GridSpec(3, 5, width_ratios=[1, 0.5, 0.5, 1, 0.8], height_ratios=[1, 1, 1.5],
                       hspace=0.4, wspace=0.5)

ax1 = plt.subplot(gs[0, 0])
#ax2 = plt.subplot(gs[1, 0])
ax3 = plt.subplot(gs[: 2, 1: 4])
ax4 = plt.subplot(gs[2,: 2])
ax5 = plt.subplot(gs[2, 2: 4])
ax6 = plt.subplot(gs[0, 4])
ax7 = plt.subplot(gs[1, 4])

axbait = fig.add_axes([0.2, 0.48, 0.012, 0.01])
axbait.axis('off')


topo_ind = topo_list[0, cur_ind] - 1
j_mat = - rec_net[:, :, topo_ind]

ax1.set_aspect('equal')
ax1 = move_axis(ax1, - 0.01, - 0.1)
plot_network(ax1, j_mat, 2, 2)

# manual arrowhead width and length
hw = 0.15
hl = 0.2
lw = 2 # axis line width
ohg = 0.3 # arrow overhang
ax1.annotate(1, (0.4, 0.6))
ax1.annotate(2, (0, - 1))
ax1.annotate(3, (- 0.4, 0.1))
ax1.set_xlim([- 1, 1.2])
ax1.set_ylim([- 1, 1])
cur_dir = rec_bestdir[cur_ind, :] * 1.3
arr1 = ax1.arrow(1.4, - cur_dir[0] / 2, 0, cur_dir[0], fc='k', ec='k', lw = lw, 
             head_width=hw, head_length=hl, overhang = ohg, 
             length_includes_head= True, clip_on = False) 
#arr1.set_zorder(10)
arr2 = ax1.arrow(- 0.83, 0.87 - cur_dir[1] / 2, 0, cur_dir[1], fc='k', ec='k', lw = lw, 
             head_width=hw, head_length=hl, overhang = ohg, 
             length_includes_head= True, clip_on = False) 

arr3 = ax1.arrow(- 0.83, - 0.87 - cur_dir[2] / 2, 0, cur_dir[2], fc='k', ec='k', lw = lw, 
             head_width=hw, head_length=hl, overhang = ohg, 
             length_includes_head= True, clip_on = False) 

#ax2.set_aspect('equal')
cur_fish = rec_fish[cur_ind, :, :]



ax3p = ax3.get_position()
ax3p.x0 += 0.1
ax3.set_position(ax3p)
ax3.set_aspect('equal')
ax3 = move_axis(ax3, - 0.07, 0)

m1p1 = [-1, -0.5, 0, 0.5, 1]
div100 = [0, 24, 49, 74, 99]

ctrinv = np.reshape(rec_trinv[cur_ind, :], [100, 100], order='F')
ax3im = ax3.imshow(np.log(ctrinv), cmap='YlGnBu_r')
ax3.set_xticks(div100)
ax3.set_yticks(div100)
ax3.set_xticklabels(m1p1)
ax3.set_yticklabels(m1p1)
ax3.set_xlabel(r'$h_2$')
ax3.set_ylabel(r'$h_3$', rotation=0)
ax3.set_aspect('equal')
ax3.spines['right'].set_visible(False)
ax3.spines['top'].set_visible(False)
ax3.spines['bottom'].set_visible(False)
ax3.spines['left'].set_visible(False)

ax3c = fig.add_axes([0.67, 0.54, 0.015, 0.25])
cbar = fig.colorbar(ax3im, cax=ax3c, orientation='vertical',
                    ticks=[4, 6])
ax3c.set_ylabel(r'$\log\mathrm{Tr}\mathcal{I}^{- 1}$')


ax4.semilogy(list_inten.T, rec_land[cur_ind, :])
ax4.set_ylabel(r'$\mathrm{Tr}\mathcal{I}^{- 1}$')
ax4.set_xlabel(r'$|h|$')

ax5 = move_axis(ax5, 0.011, 0)        
eng_list = np.arange(2 ** num_spin)
ax5.scatter(eng_list, ori_energy[cur_ind, :])
ax5.scatter(eng_list, rec_energy[cur_ind, :])
ax5.set_xticks([2, 4, 6])
ax5.set_xlabel('State index')
ax5.set_ylabel('Energy', labelpad=-3)
ax5.set_xticks([1, 3, 5, 7])
ax5.set_xticklabels([2, 4, 6, 8])


def large_axis(ax):
    axp = ax.get_position()
    axp.x1 += 0.01
    axp.y1 += 0.02
    ax.set_position(axp)
    return ax

def plot_eig(ax, eigw, eigv):
    ax = move_axis(ax, 0, - 0.12)
    ax = large_axis(ax)
    ax.set_aspect('equal')
    cax = ax.imshow(eigv, cmap='bwr', vmin=- 1, vmax=1)   
    ax.set_xticks([0, 1, 2])
    ax.set_xticklabels(np.round(eigw, 2))
    ax.set_xticks(np.arange(3) - 0.5, minor=True);
    ax.set_yticks(np.arange(3) - 0.5, minor=True);
    ax.grid(which='minor', color='w', linestyle='-', linewidth=3)
    ax.set_ylabel('Edge index')
    ax.set_yticklabels([1, 1, 2, 3])
    return cax



fisho = ori_fish[cur_ind, :, :]
[eigw, eigv] = np.linalg.eig(fisho)
idx = eigw.argsort()[::-1]  
eigw = eigw[idx]
eigv = eigv[:, idx]
plot_eig(ax6, np.log(eigw), eigv)


fishn = rec_fish[cur_ind, :, :]
[eigw, eigv] = np.linalg.eig(fishn)
idx = eigw.argsort()[::-1]  
eigw = eigw[idx]
if cur_ind == 0:    
    eigv = eigv[:, idx]
else:        
    eigv = np.eye(3)
ax7im = plot_eig(ax7, np.log(eigw), eigv)
ax7.set_xlabel('Log of eigenvalue')

ax7c = fig.add_axes([0.94, 0.48, 0.012, 0.15])
cbar = fig.colorbar(ax7im, cax=ax7c, orientation='vertical',
                    ticks=[- 1, 0, 1])
ax7c.set_xlabel(r'Value')


move_axis(ax1, - 0.04, 0)
move_axis(ax4, - 0.04, 0)
move_axis(ax3, - 0.02, 0)
move_axis(ax5, - 0.02, 0)
move_axis(ax3c, - 0.015, 0)

fxx1 = 0.04
fyy1 = 0.88
fyy2 = 0.39
fxx3 = 0.95

abcd_size = 18
fig.text(fxx1, fyy1, '(a)', fontsize=abcd_size)
fig.text(fxx1, fyy2, '(d)', fontsize=abcd_size)
fig.text(0.75, 0.8, '(c)', fontsize=abcd_size)
fig.text(0.27, fyy1, '(b)', fontsize=abcd_size)
fig.text(0.38, fyy2, '(e)', fontsize=abcd_size)

plt.savefig('SI_three_node1.pdf', bbox='tight')
# plt.savefig('SI_three_node2.pdf', bbox='tight')
plt.show()

