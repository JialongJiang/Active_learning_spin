#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 16:10:17 2019

@author: jiangjl
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

#fit_xx = np.log(5e6 * data_realfishd[0, 0, :])
#fit_yy = np.log(l2_traj[- 2, :])
#fit_res = np.polyfit(fit_xx, fit_yy, 1)



'''




ax2.plot(ind_round, data_l2[- 1, :, :])


data_errinnop = np.zeros([num_j, num_round, num_data])
for ii in range(num_data):
    for jj in range(num_round):       
        data_errinnop[:, jj, ii] = np.dot(data_realfishv[:, :, jj, ii].T, 
                             (data_veccurj[:, jj, ii] - data_vecjmat[:, ii]))
    
plt.hist2d(np.ravel(np.log(data_realfishd[:, 0, :])), 
           np.ravel(np.log(np.abs(data_errinnop[:, 0, :]))), bins=80)

plt.scatter(np.ravel(np.log(data_realfishd[:, 0, :])), 
           np.ravel(np.log(np.abs(data_errinnop[:, 0, :]))), color='b', alpha=0.02)
plt.scatter(np.ravel(np.log(data_realfishd[:, 4, :])), 
           np.ravel(np.log(np.abs(data_errinnop[:, 4, :]))), color='g', alpha=0.02)
plt.scatter(np.ravel(np.log(data_realfishd[:, 9, :])), 
           np.ravel(np.log(np.abs(data_errinnop[:, 9, :]))), color='r', alpha=0.02)



# num_round = np.squeeze(num_round) 

plt.savefig('1.pdf')

plt.plot(ind_round, data_topk[- 1, 0, :, :])
plt.savefig('2.pdf')


# for it_round in ind_round:
it_round = 0
plt.loglog(data_realfishd[:, it_round, :], data_fishd[:, it_round, :], '.')
plt.savefig('3.pdf')

test = np.abs(data_fishinnop[:, :, it_round, 1])
np.std(test, axis=0)
plt.imshow(test)

plt.semilogx(data_fishd[:, it_round, :], np.std(np.abs(data_fishinnop[:, :, it_round, :]), axis=0), '.')

plt.loglog(data_corrd[:, it_round, :], np.abs(data_pertproj[:, it_round, :]), '.')
plt.xlim([1e-6, 20])


it_round = 5
test = data_fishinnop[:, :, it_round, :] ** 2
#plt.imshow(test)

aux_mat = np.multiply(np.ones([num_j, num_j]), np.arange(num_j)).T
aux_mat2 = aux_mat ** 2
aux_mat = np.expand_dims(aux_mat, axis=2)
aux_mat2 = np.expand_dims(aux_mat2, axis=2)
var = np.sum(np.multiply(test, aux_mat2), axis=0) - np.sum(np.multiply(test, aux_mat), axis=0) ** 2
plt.loglog(data_realfishd[:, it_round, :], var, '.')

data_errproj = zeros([num_j, num_])

for ii in np.arange(num_data):
    plt.imshow(test[:, :, ii])
    
net_id = 1
test1 = data_fish[:, :, it_round, net_id]
test2 = data_realfish[:, :, it_round, net_id]

plt.imshow(test1)
plt.imshow(test2)
plt.imshow(data_fishinnop[:, :, it_round, net_id])
plt.imshow(np.dot(data_fishv[:, :, it_round, net_id].T, data_realfishv[:, :, it_round, net_id]))
plt.imshow(data_realfishv[:, :, it_round, net_id])
plt.semilogy(data_realfishd[:, it_round, net_id])
'''