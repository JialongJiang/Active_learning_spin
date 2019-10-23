#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 16:10:17 2019

@author: Jialong Jiang
"""

import matplotlib.pyplot as plt
from matplotlib import cm
import scipy.io as sio
import numpy as np
import matplotlib as mpb
import matplotlib.gridspec as gridspec
from plot_network import plot_network, move_axis


mdata = sio.loadmat('fig3_pert')
locals().update(mdata)
cmdata = sio.loadmat('random_controlnn')
locals().update(cmdata)


mpb.rcParams.update({'font.size': 14})
mpb.rcParams.update({'axes.labelsize': 16})
mpb.rcParams.update({'axes.titlesize': 16})
mpb.rcParams.update({'figure.dpi': 300})

num_spin = np.squeeze(num_spin)
num_j = np.squeeze(num_j)
num_data = np.squeeze(num_data)
num_round = np.squeeze(num_round)


figw = 11.4 / 2.54 * 2
figh = figw
fig = plt.figure(figsize=[figw, figh])
gs = gridspec.GridSpec(2, 2, width_ratios=[1, 1], height_ratios=[1, 1])


ax1 = plt.subplot(gs[0])
ax2 = plt.subplot(gs[1])
ax3 = plt.subplot(gs[2])
ax4 = plt.subplot(gs[3])

ax1 = move_axis(ax1, - 0.02, 0)
ax2 = move_axis(ax2, 0, 0.03)
ax3 = move_axis(ax3, - 0.02, 0)


ax1.set_axis_off()
def put_network(j_mat, pos):
    ax1a = fig.add_axes(pos)
    ax1a = plot_network(ax1a, - j_mat, 0.9, 1.2, spring=True)

net_sz = 0.18
net_sz2 = net_sz * figw / figh
pos_st = 0.07
pos_hi = 0.53
put_network(rec_net[:, :, 0], [pos_st + net_sz, pos_hi + net_sz2 - 0.08, net_sz, net_sz2])
put_network(rec_net[:, :, 2], [pos_st, pos_hi + net_sz2, net_sz, net_sz2])
put_network(rec_net[:, :, 3], [pos_st, pos_hi, net_sz, net_sz2])
# put_network(rec_net[:, :, 4], [pos_st + net_sz, pos_hi, net_sz, net_sz2])

ind_round = np.arange(num_round)

def plot_traj(ax, dat, color, lab=False, st=1, linst='-'):
    datm = np.mean(dat, axis=1)
    datsd = np.std(dat, axis=1)
    if lab:
        ax.plot(ind_round, datm, color, linestyle=linst, linewidth=2, label=lab)
    else:
        ax.plot(ind_round, datm, color, linestyle=linst, linewidth=2)  
    ax.plot(ind_round, dat, color, linestyle=linst, alpha = 0.1)
    ax.errorbar(ind_round[st:: 2], datm[st:: 2], yerr=datsd[st:: 2], 
                fmt='none', color=color, capsize=4)

def find_last(dat):
    xx, yy, zz = dat.shape
    last_arr = np.zeros([yy, zz])
    for ii in range(yy):
        ind = np.max(np.nonzero(dat[:, ii, 0]))
        last_arr[ii, :] = dat[ind, ii, :]
    return last_arr

def average_abs(cur_j, j_mat):
    j_mat = np.expand_dims(j_mat, axis=2)
    pre_abs = np.abs(cur_j - j_mat)
    fin_abs = np.sum(pre_abs, axis=(0, 1)) / 2 / num_j
    return fin_abs

    
all_jmat = rec_net[:, :, np.squeeze(data_id) - 1]    
    
# l2_traj = data_l2[- 1, :, :]
# cl2_traj = find_last(cdata_l2)
l2_traj = average_abs(data_curj, all_jmat)
cl2_traj = average_abs(cdata_curj, all_jmat)
ax2.set_xlabel('Perturbation number')
ax2.set_ylabel(r'Mean error', labelpad=2)

plot_traj(ax2, l2_traj, 'C0')
plot_traj(ax2, cl2_traj, 'C1', st=0, linst='--')

topk_traj = data_topk[- 1, 0, :, :]
ctopk_traj = find_last(cdata_topk[:, 0, :, :])
plot_traj(ax3, topk_traj, 'C0', 'Perturbed')
plot_traj(ax3, ctopk_traj, 'C1', 'Unperturbed', st=0, linst='--')
ax3.set_xlabel('Perturbation number')
ax3.set_ylabel('Edge prediction')

ax3.legend(bbox_to_anchor=(1.14, 1.35))

ax4.loglog(data_realfishd[0, 0, :], l2_traj[- 1, :], 'o', alpha=0.8)
ax4.loglog(data_realfishd[0, 0, :], cl2_traj[- 1, :], 'o', alpha=0.8)
ax4.set_xlabel('Minimal eigenvalue')
ax4.set_ylabel(r'Final mean error', position=[0, 0.6],
               labelpad=- 5)
ax4.yaxis.set_ticks([0.05, 0.2, 0.5])
ax4.yaxis.set_ticklabels(['0.05', '0.2', '0.5'])
# ax4.get_yaxis().set_major_formatter(mpb.ticker.ScalarFormatter())

fxx1 = 0.03
fxx2 = 0.5
fyy1 = 0.89
fyy2 = 0.48
abcd_size = 18
fig.text(fxx1, fyy1, '(a)', fontsize=abcd_size)
fig.text(fxx1, fyy2, '(c)', fontsize=abcd_size)
fig.text(fxx2, fyy1, '(b)', fontsize=abcd_size)
fig.text(fxx2, fyy2, '(d)', fontsize=abcd_size)

plt.savefig('fig3.pdf', bbox_inches='tight')



