# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 11:44:58 2019

@author: Jialong Jiang
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

mdata = sio.loadmat('fig2_data')
locals().update(mdata)
j_mat = - j_mat
exter_h = - exter_h
cur_j0 = - cur_j0
cur_j1 = - cur_j1
cur_j2 = - cur_j2


figw = 17.8 / 2.54 * 2
figh = 17.8 / 20  / 2.54 * 13 * 2
fig = plt.figure(figsize=[figw, figh])
gs = gridspec.GridSpec(2, 3, width_ratios=[1, 1, 1], height_ratios=[1, 1], 
                       left=0.08, right=0.9, top=0.94, bottom=0.1, 
                       wspace=0.25, hspace=0.25)



ax1 = plt.subplot(gs[0])
ax2 = plt.subplot(gs[1])
ax2pos = ax2.get_position()
# ax3 = plt.subplot(gs[2])
ax4 = plt.subplot(gs[3])
ax4pos = ax4.get_position()
ax5 = plt.subplot(gs[4])
# ax6 = plt.subplot(gs[5])

def process_axis(ax):
    ax.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])
    
leftpos = ax2pos.x1 + 0.07
rightpos = 0.94

gs2 = gridspec.GridSpec(2, 2, left=leftpos, right=rightpos, 
                        top=ax4pos.y1, bottom=ax4pos.y0, 
                        wspace=0.15, hspace=0.05)   
ax61 = plt.subplot(gs2[0]) 
process_axis(ax61)
ax62 = plt.subplot(gs2[1]) 
process_axis(ax62)
ax63 = plt.subplot(gs2[2]) 
process_axis(ax63)
ax64 = plt.subplot(gs2[3]) 
process_axis(ax64)

gs1 = gridspec.GridSpec(2, 2, left=leftpos, right=rightpos, 
                        top=ax2pos.y1, bottom=ax2pos.y0, 
                        wspace=0.23, hspace=0.05)   
ax31 = plt.subplot(gs1[0]) 
process_axis(ax31)
ax32 = plt.subplot(gs1[1]) 
process_axis(ax32)
ax33 = plt.subplot(gs1[2]) 
process_axis(ax33)
ax34 = plt.subplot(gs1[3]) 
process_axis(ax34)

move_axis(ax1, - 0.02, 0.02)

move_axis(ax31, 0, 0.02)
move_axis(ax32, 0, 0.02)
move_axis(ax33, 0, - 0.01)

move_axis(ax63, 0, - 0.03)
move_axis(ax64, 0, - 0.03)

im_ax3 = ax31.imshow(rec_all_corr[:, :, 0], cmap='PiYG_r', clim=[- 1, 1])
ax32.imshow(np.mean(rec_all_corr[:, :, :3], axis=2), cmap='PiYG_r', clim=[- 1, 1])
ax33.imshow(np.mean(rec_all_corr[:, :, :6], axis=2), cmap='PiYG_r', clim=[- 1, 1])
ax34.axis('off')

jlim = 3.3
im_ax6 = ax64.imshow(j_mat, cmap='bwr', clim=[- jlim, jlim])
ax61.imshow(cur_j0, cmap='bwr', clim=[- jlim, jlim])
ax62.imshow(cur_j1, cmap='bwr', clim=[- jlim, jlim])
ax63.imshow(cur_j2, cmap='bwr', clim=[- jlim, jlim])

node_posi = [0, 5, 10, 15]
node_ind = [1, 6, 11, 16]

def add_xtick(ax_list):
    for ax in ax_list:
        ax.set_xticks(node_posi)
        ax.set_xticklabels(node_ind)

def add_ytick(ax_list):
    for ax in ax_list:
        ax.set_yticks(node_posi)
        ax.set_yticklabels(node_ind)

add_xtick([ax33, ax32, ax63, ax64])        
add_ytick([ax31, ax33, ax61, ax63])      

# ax32.set_xlabel('Node index')
ax31.set_ylabel('Node index')
ax61.set_ylabel('Node index')
# ax63.set_xlabel('Node index')

ax31.set_title('No perturbation')
ax32.set_title('2 perturbations')
ax33.set_title('5 perturbations')

ax64.set_title('Ground truth')
ax61.set_title('No perturbation')
ax62.set_title('2 perturbations')
ax63.set_title('5 perturbations')

ax6c = fig.add_axes([0.95, 0.13, 0.01, 0.25])
cbar = fig.colorbar(im_ax6, cax=ax6c, ticks=[- 3, 0, 3])
ax6c.set_ylabel('Interaction strength', position=[0.8, 0.62], labelpad=-4)

ax3c = fig.add_axes([0.95, 0.63, 0.01, 0.25])
cbar = fig.colorbar(im_ax3, cax=ax3c, ticks=[- 1, 0, 1])
ax3c.set_ylabel('Correlation', position=[0.6, 0.5], labelpad=-5)


pos = np.load('pos16.npy', allow_pickle=True).item()
ax1, pos = plot_network(ax1, j_mat, 1, 1.3, pos=pos, labeldist=0.06)
ax1.set_ylim([ - 0.771, 1.09])
ax1.set_aspect('equal')

ax2.semilogy(np.diag(reald) * 6)
ax2.semilogy(rec_reald[:, 1] * 2, '--')
ax2.semilogy(rec_reald[:, 4], '-.')
ax2.set_yticks([1e-10, 1e-5, 1])
ax2.set_ylim([1e-12, 1e3])
ax2.set_xticks([0, 40, 80, 120])
ax2.set_xticklabels([120, 80, 40, 0])
ax2.set_xlabel('Eigenvalue index')
ax2.set_ylabel('Eigenvalues of $\mathcal{I}$')
ax2.yaxis.set_label_coords(- 0.18, 0.52) 


xx_cutoff = 2000
train_list = np.arange(1, num_epoch, rec_gap)
ax4.plot(train_list, datf0[0][0][3], label='No perturbation')
ax4.plot(train_list, datf1[0][0][3], '--', label='2 perturbations')
ax4.plot(train_list, datf2[0][0][3], '-.', label='5 perturbations')
ax4.set_xlim([0, xx_cutoff])
ax4.set_xlabel('Steps')
# ax4.legend(bbox_to_anchor=(1.05, 1.35))
ax4.legend(bbox_to_anchor=(2.26, 1.57))
#ax4.set_ylabel(r'$\ell_2$ error')
ax4.set_ylabel(r'Mean error')



ax5.plot(train_list, datf0[0][0][2][:, 0])
ax5.plot(train_list, datf1[0][0][2][:, 0], '--')
ax5.plot(train_list, datf2[0][0][2][:, 0], '-.')
ax5.set_xlim([0, 2000])
ax5.set_xlabel('Steps')
ax5.set_ylabel('Edge prediction')
ax5.yaxis.set_label_coords(- 0.13, 0.5) 


abcd_size = 18
'''
mk_up = 0.02
mk_down = 1 - mk_up
fig.text(mk_up, mk_up, '+', fontsize=abcd_size)
fig.text(mk_up, mk_down, '+', fontsize=abcd_size)
fig.text(mk_down, mk_down, '+', fontsize=abcd_size)
fig.text(mk_down, mk_up, '+', fontsize=abcd_size)
'''

fxx1 = 0.04
fxx2 = 0.34
fxx3 = 0.63
fyy1 = 0.97
fyy2 = 0.49
fig.text(fxx1, fyy1, '(a)', fontsize=abcd_size)
fig.text(fxx1, fyy2, '(d)', fontsize=abcd_size)
fig.text(fxx2, fyy1, '(b)', fontsize=abcd_size)
fig.text(fxx2, fyy2, '(e)', fontsize=abcd_size)
fig.text(fxx3, fyy1, '(c)', fontsize=abcd_size)
fig.text(fxx3, fyy2, '(f)', fontsize=abcd_size)


plt.savefig('fig2.pdf', bbox='tight')

