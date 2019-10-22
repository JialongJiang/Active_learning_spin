#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 22:56:52 2019

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

figw = 17.8 / 2.54 * 2
figh = 17.8 / 2.54 * 13 / 40 * 2 * 3.3
fig = plt.figure(figsize=[figw, figh])
gs = gridspec.GridSpec(3, 3, width_ratios=[1, 1, 1], wspace=0.27, hspace=0.3,
                       left=0.12, right=0.96)

def plot_traj(ax, ind, dat, color, dgap=1, lab=False, st=0, linst='-'):
    datm = np.mean(dat, axis=1)
    datsd = np.std(dat, axis=1)
    if lab:
        ax.plot(ind, datm, color, linestyle=linst, linewidth=2, label=lab)
    else:
        ax.plot(ind, datm, color, linestyle=linst, linewidth=2)  
    ax.plot(ind, dat, color, linestyle=linst, alpha = 0.2)
    ax.errorbar(ind[st:: dgap], datm[st:: dgap], yerr=datsd[st:: dgap], 
                fmt='none', color=color, capsize=4)



ax1 = plt.subplot(gs[0, 0])
ax2 = plt.subplot(gs[0, 1])
ax3 = plt.subplot(gs[0, 2])

mdata = sio.loadmat('plot_sz8nn')
locals().update(mdata)

ind_round = np.arange(1, 8)

plot_traj(ax2, ind_round, rec_size_curve[:, :, 0, 4], color='C0')
plot_traj(ax2, ind_round, rec_size_curve[:, :, 2, 4], color='C1', linst='--')
plot_traj(ax2, ind_round, rec_size_curve[:, :, 5, 4], color='C2', linst='-.')

plot_traj(ax3, ind_round, rec_size_curve[:, :, 0, 1], color='C0')
plot_traj(ax3, ind_round, rec_size_curve[:, :, 2, 1], color='C1', linst='--')
plot_traj(ax3, ind_round, rec_size_curve[:, :, 5, 1], color='C2', linst='-.')

eig_ind = np.arange(rec_fish_eigs.shape[2] + 1, 1, - 1)
plot_traj(ax1, eig_ind, np.log10(rec_fish_eigs[:, 0, :].T), color='C0', 
          dgap=6, lab='No perturbation')
plot_traj(ax1, eig_ind, np.log10(rec_fish_eigs[:, 2, :].T), color='C1', 
          dgap=6, linst='--', lab='2 perturbations')
plot_traj(ax1, eig_ind, np.log10(rec_fish_eigs[:, 5, :].T), color='C2', 
          dgap=6, linst='-.', lab='5 perturbations')

ax1.legend()
ax1.set_xlabel('Eigenvalue index')
ax1.set_ylabel('Eigenvalues')
ax1.set_yticks([- 10, - 6, - 2, 2])
ax1.set_yticklabels(['1e-10', '1e-6', '1e-2', '1e2'])
ax1.invert_xaxis()

ax2.set_xlabel('Sample size')
ax2.set_ylabel('Mean error')
ax2.set_xticklabels(['5', '5e1', '5e2', '5e3', '5e4', '5e5', '5e6'])
ax2.set_xticks([1, 2, 3, 4, 5, 6, 7])
ax2.set_yticks([0, 0.5, 1, 1.5])

ax3.set_xlabel('Sample size')
ax3.set_ylabel('Edge prediction')
ax3.set_xticklabels(['5', '5e1', '5e2', '5e3', '5e4', '5e5', '5e6'])
ax3.set_xticks([1, 2, 3, 4, 5, 6, 7])



ax1 = plt.subplot(gs[1, 0])
ax2 = plt.subplot(gs[1, 1])
ax3 = plt.subplot(gs[1, 2])

mdata = sio.loadmat('plot_sz12nn')
locals().update(mdata)

ind_round = np.arange(1, 8)

plot_traj(ax2, ind_round, rec_size_curve[:, :, 0, 4], color='C0')
plot_traj(ax2, ind_round, rec_size_curve[:, :, 2, 4], color='C1', linst='--')
plot_traj(ax2, ind_round, rec_size_curve[:, :, 5, 4], color='C2', linst='-.')

plot_traj(ax3, ind_round, rec_size_curve[:, :, 0, 1], color='C0')
plot_traj(ax3, ind_round, rec_size_curve[:, :, 2, 1], color='C1', linst='--')
plot_traj(ax3, ind_round, rec_size_curve[:, :, 5, 1], color='C2', linst='-.')

eig_ind = np.arange(rec_fish_eigs.shape[2] + 1, 1, - 1)
plot_traj(ax1, eig_ind, np.log10(rec_fish_eigs[:, 0, :].T), color='C0', 
          dgap=15, lab='Without perturb')
plot_traj(ax1, eig_ind, np.log10(rec_fish_eigs[:, 2, :].T), color='C1', 
          dgap=15, linst='--', lab='With 2 perturb')
plot_traj(ax1, eig_ind, np.log10(rec_fish_eigs[:, 5, :].T), color='C2', 
          dgap=15, linst='-.', lab='With 5 perturb')

ax1.set_xlabel('Eigenvalue index')
ax1.set_ylabel('Eigenvalues')
ax1.set_yticks([- 10, - 6, - 2, 2])
ax1.set_yticklabels(['1e-10', '1e-6', '1e-2', '1e2'])
ax1.invert_xaxis()

ax2.set_xlabel('Sample size')
ax2.set_ylabel('Mean error')
ax2.set_xticklabels(['5', '5e1', '5e2', '5e3', '5e4', '5e5', '5e6'])
ax2.set_xticks([1, 2, 3, 4, 5, 6, 7])
ax2.set_yticks([0, 0.5, 1, 1.5])

ax3.set_xlabel('Sample size')
ax3.set_ylabel('Edge prediction')
ax3.set_xticklabels(['5', '5e1', '5e2', '5e3', '5e4', '5e5', '5e6'])
ax3.set_xticks([1, 2, 3, 4, 5, 6, 7])




ax1 = plt.subplot(gs[2, 0])
ax2 = plt.subplot(gs[2, 1])
ax3 = plt.subplot(gs[2, 2])

mdata = sio.loadmat('plot_sz16nn')
locals().update(mdata)

ind_round = np.arange(1, 8)

plot_traj(ax2, ind_round, rec_size_curve[:, :, 0, 4], color='C0')
plot_traj(ax2, ind_round, rec_size_curve[:, :, 2, 4], color='C1', linst='--')
plot_traj(ax2, ind_round, rec_size_curve[:, :, 5, 4], color='C2', linst='-.')

plot_traj(ax3, ind_round, rec_size_curve[:, :, 0, 1], color='C0')
plot_traj(ax3, ind_round, rec_size_curve[:, :, 2, 1], color='C1', linst='--')
plot_traj(ax3, ind_round, rec_size_curve[:, :, 5, 1], color='C2', linst='-.')

eig_ind = np.arange(rec_fish_eigs.shape[2] + 1, 1, - 1)
plot_traj(ax1, eig_ind, np.log10(rec_fish_eigs[:, 0, :].T), color='C0', 
          dgap=25, lab='Without perturb')
plot_traj(ax1, eig_ind, np.log10(rec_fish_eigs[:, 2, :].T), color='C1', 
          dgap=25, linst='--', lab='With 2 perturb')
plot_traj(ax1, eig_ind, np.log10(rec_fish_eigs[:, 5, :].T), color='C2', 
          dgap=25, linst='-.', lab='With 5 perturb')


ax1.set_xlabel('Eigenvalue index')
ax1.set_ylabel('Eigenvalues')
ax1.set_yticks([- 10, - 6, - 2, 2])
ax1.set_yticklabels(['1e-10', '1e-6', '1e-2', '1e2'])
ax1.invert_xaxis()

ax2.set_xlabel('Sample size')
ax2.set_ylabel('Mean error')
ax2.set_xticklabels(['5', '5e1', '5e2', '5e3', '5e4', '5e5', '5e6'])
ax2.set_xticks([1, 2, 3, 4, 5, 6, 7])
ax2.set_yticks([0, 0.5, 1, 1.5])

ax3.set_xlabel('Sample size')
ax3.set_ylabel('Edge prediction')
ax3.set_xticklabels(['5', '5e1', '5e2', '5e3', '5e4', '5e5', '5e6'])
ax3.set_xticks([1, 2, 3, 4, 5, 6, 7])

textgap = 0.27
textxx = 0.02
fig.text(textxx, 0.7 + 0.01, '8-node networks', fontsize=18, rotation='vertical')
fig.text(textxx, 0.7 - textgap, '12-node networks', fontsize=18, rotation='vertical')
fig.text(textxx, 0.7 - textgap * 2, '16-node networks', fontsize=18, rotation='vertical')


fxx1 = 0.06
fxx2 = 0.375
fxx3 = 0.68
fyy1 = 0.89
fyy2 = fyy1 - textgap
fyy3 = fyy2 - textgap - 0.005


abcd_size = 18
fig.text(fxx1, fyy1, '(a)', fontsize=abcd_size)
fig.text(fxx2, fyy1, '(b)', fontsize=abcd_size)
fig.text(fxx3, fyy1, '(c)', fontsize=abcd_size)
fig.text(fxx1, fyy2, '(d)', fontsize=abcd_size)
fig.text(fxx2, fyy2, '(e)', fontsize=abcd_size)
fig.text(fxx3, fyy2, '(f)', fontsize=abcd_size)
fig.text(fxx1, fyy3, '(g)', fontsize=abcd_size)
fig.text(fxx2, fyy3, '(h)', fontsize=abcd_size)
fig.text(fxx3, fyy3, '(i)', fontsize=abcd_size)



plt.savefig('si_net_sz.pdf', bbox='tight')

