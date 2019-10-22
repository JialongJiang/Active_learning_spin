#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 20:12:20 2019

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

mdata = sio.loadmat("three_node_trinv")
locals().update(mdata)


figw = 13.4 / 2.54 * 2
figh = figw / 2
fig = plt.figure(figsize=[figw, figh])
gs = gridspec.GridSpec(3, 4, width_ratios=[1, 1, 1, 3], height_ratios=[1, 1, 1]) #, hspace=0.4, wspace=0.5)
                       
ax2 = plt.subplot(gs[:, 3])      

ax11 = plt.subplot(gs[0, 0])     
ax12 = plt.subplot(gs[0, 1])   
ax13 = plt.subplot(gs[0, 2])   
ax14 = plt.subplot(gs[1, 0])   
ax15 = plt.subplot(gs[1, 1])   
ax16 = plt.subplot(gs[1, 2])   
ax17 = plt.subplot(gs[2, 1])   

ax1_list = [ax11, ax12, ax13, ax14, ax15, ax16, ax17]
for ii, ax in enumerate(ax1_list):
    ax.set_aspect('equal')
    ax = move_axis(ax, - 0.02, 0)
    j_mat = - rec_net[:, :, topo_list[0, ii] - 1]
    plot_network(ax, j_mat, 1.5, 1.5)
    ax.annotate(ii + 1, (- 0.1, - 0.1), fontsize=16)
    ax.set_xlim([- 1, 1.2])
    ax.set_ylim([- 1.1, 1.1])
    
ax2 = move_axis(ax2, 0.05, 0)    
gp0 = np.asarray([0, 4])
gp1 = np.asarray([2, 6])
gp2 = np.asarray([1, 3, 5])
gp_list = [gp0, gp1, gp2]
ax2.semilogy([0, 1], rec_ctrinv[:, gp0], color='C0', linestyle='--', 
             marker='o', markersize=10, markerfacecolor='none')
ax2.semilogy([0, 1], rec_ctrinv[:, gp1], color='C1', linestyle='--', 
             marker='^', markersize=10, markerfacecolor='none')
ax2.semilogy([0, 1], rec_ctrinv[:, gp2], color='C2', linestyle='--', 
             marker='x', markersize=10, markerfacecolor='none')
ax2.set_xticks([0, 1])
# ax2.set_xticklabels(['No perturbation', '1 perturbation'])
ax2.set_xticklabels(['Original', 'Perturbed'])
ax2.set_ylabel(r'$\mathrm{Tr}\mathcal{I}^{- 1}$')
ax2.legend(labels=[gp0 + 1, '_nolegend_', gp1 + 1, '_nolegend_', '_nolegend_', gp2 + 1], 
           loc='lower left')

     
abcd_size = 18
fyy1 = 0.9
fig.text(0.06, fyy1, '(a)', fontsize=abcd_size)
fig.text(0.54, fyy1, '(b)', fontsize=abcd_size)

plt.savefig('SI_all_three_node.pdf', bbox_inches='tight')


