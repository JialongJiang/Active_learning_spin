# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 18:07:12 2019

@author: Jialong Jiang
"""

import matplotlib.pyplot as plt
from matplotlib import cm
import scipy.io as sio
import numpy as np
import matplotlib as mpb
import matplotlib.gridspec as gridspec
from plot_network import plot_network, move_axis

mdata = sio.loadmat('SI_pertJ')
locals().update(mdata)
j_mat = - j_mat
rec_estij = - rec_estij

mpb.rcParams.update({'font.size': 14})
mpb.rcParams.update({'axes.labelsize': 16})
mpb.rcParams.update({'axes.titlesize': 16})
mpb.rcParams.update({'figure.dpi': 300})


figw = 17.8 / 2.54 * 2
figh = 17.8 / 20  / 2.54 * 11.5
fig = plt.figure(figsize=[figw, figh])
gs = gridspec.GridSpec(1, 4, width_ratios=[0.6, 0.6, 1, 1],
                       left=0.08, right=0.92, top=0.92, bottom=0.15, 
                       wspace=0.3)


ax0 = plt.subplot(gs[0])
ax1 = plt.subplot(gs[1])
ax2 = plt.subplot(gs[2])
ax3 = plt.subplot(gs[3])

move_axis(ax0, 0, - 0.1)
move_axis(ax1, - 0.035, - 0.1)
move_axis(ax2, - 0.015, 0)

ax0.set_aspect('equal')
jlim = np.max(j_mat)
im0 = ax0.imshow(j_mat, cmap='bwr', clim=[- jlim, jlim])

ax1.set_aspect('equal')
im1 = ax1.imshow(np.mean(rec_estij, axis=2), cmap='bwr', clim=[- jlim, jlim])
ax1.set_yticks([])
node_ind = np.array([4, 9, 14])
node_tick = node_ind + 1
ax0.set_xticks(node_ind)
ax0.set_xticklabels(node_tick)
ax1.set_xticks(node_ind)
ax1.set_xticklabels(node_tick)
ax0.set_yticks(node_ind)
ax0.set_yticklabels(node_tick)
ax0.set_ylabel('Node index')
ax0.set_xlabel('Node index', position=[1.05, 0])
ax0.set_title('Truth')
ax1.set_title('Inferred')

ax1c = fig.add_axes([0.14, 0.8, 0.14, 0.04])
cbar = fig.colorbar(im1, cax=ax1c, ticks=[- 1, 0, 1], orientation='horizontal')
ax1c.set_xlabel('Interaction strength')
ax1c.xaxis.tick_top()
ax1c.xaxis.set_label_position('top') 

aux_ind = np.ones(10)
ax2.semilogy(0 * aux_ind, rec_fintrinv[:, 2], 'X', color='C0')
ax2.semilogy(1 * aux_ind, rec_fintrinv[:, 0], 'X', color='C1')
ax2.semilogy(2 * aux_ind, rec_fintrinv[:, 1], 'X', color='C2')
ax2.semilogy([0, 1, 2], ctrinv[0,] * [1, 1, 1], '--', color='k')
ax2.set_xticks([0, 1, 2])
ax2.set_xticklabels(['Random', 'Inferred', 'Truth'])
ax2.set_ylabel(r'$\mathrm{Tr}\mathcal{I}^{- 1}$')
ax2.text(0.2, 6e4, 'original problem', fontsize=14)

rec_perthat = rec_perthat * np.sign(rec_perthat[6, :])[None, :]
rec_pertori = rec_pertori * np.sign(rec_pertori[6, :])[None, :]
node_index = np.arange(1, 17)

ax3.plot(node_index, rec_perthat, alpha=0.5, color='C1', label='Inferred')
ax3.plot(node_index, rec_pertori, '--', alpha=0.5, color='C2', label='Truth')
ax3.set_xticks(node_ind)
ax3.set_xticklabels(node_tick)
ax3.set_xlabel('Node index')
ax3.set_ylabel('Field strength', labelpad=- 2)
ax3.set_ylim([- 10, 10])
handles, labels = ax3.get_legend_handles_labels()
ax3.legend(handles[:: 10], labels[:: 10])

abcd_size = 18
fxx1 = 0.04
fxx2 = 0.35
fxx3 = 0.65
fyy1 = 0.93
fig.text(fxx1, fyy1, '(a)', fontsize=abcd_size)
fig.text(fxx2, fyy1, '(b)', fontsize=abcd_size)
fig.text(fxx3, fyy1, '(c)', fontsize=abcd_size)

plt.savefig('si_pertJ.pdf', bbox='tight')


