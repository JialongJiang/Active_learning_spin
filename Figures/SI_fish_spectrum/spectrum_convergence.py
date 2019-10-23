#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 22:29:04 2019

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

mdata = sio.loadmat("SI_data_spectrum")
locals().update(mdata)


figw = 14.3/ 2.54 * 2
figh = figw * 1.5
fig = plt.figure(figsize=[figw, figh])
gs = gridspec.GridSpec(3, 2, hspace=0.3, wspace=0.25)

ax1 = plt.subplot(gs[0, 0])
ax2 = plt.subplot(gs[1, 0])
ax3 = plt.subplot(gs[2, 0])
ax4 = plt.subplot(gs[0, 1])
ax5 = plt.subplot(gs[1, 1])
ax6 = plt.subplot(gs[2, 1])

ax4im = ax4.imshow(data_meanprob[:, :, 0] + 1e-16, cmap=plt.cm.PuBu, norm=mpb.colors.LogNorm(), 
           vmin=1e-4, vmax = 5e-1)
ax5.imshow(data_meanprob[:, :, 1] + 1e-16, cmap=plt.cm.PuBu, norm=mpb.colors.LogNorm(), 
           vmin=1e-4, vmax = 5e-1)
ax6.imshow(data_meanprob[:, :, 5] + 1e-16, cmap=plt.cm.PuBu, norm=mpb.colors.LogNorm(), 
           vmin=1e-4, vmax = 5e-1)

ax4c = fig.add_axes([0.9, 0.69, 0.013, 0.16])
cbar = fig.colorbar(ax4im, cax=ax4c)
ax4c.set_ylabel(r'Squared inner product')


ax1.loglog(data_realfishd[:, 0, :], data_fishd[:, 0, :], '.')
ax1.set_xlim([1e-8, 1e2])
ax1.set_ylim([1e-20, 1e2])
ax1.plot([1e-8, 1e2], [1e-8, 1e2], '--', color='k', linewidth=2)

ax2.loglog(data_realfishd[:, 1, :], data_fishd[:, 1, :], '.')
ax2.set_xlim([1e-7, 1e3])
ax2.set_ylim([1e-18, 1e3])
ax2.plot([1e-7, 1e3], [1e-7, 1e3], '--', color='k', linewidth=2)

ax3.loglog(data_realfishd[:, 5, :], data_fishd[:, 5, :], '.')
ax3.set_xlim([1e-7, 1e3])
ax3.set_ylim([1e-9, 1e3])
ax3.plot([1e-7, 1e3], [1e-7, 1e3], '--', color='k', linewidth=2)



for ax in [ax1, ax2, ax3]:
    ax.set_xlabel(r'Eigenvalues of $\mathcal{I}$')
    ax.set_ylabel('Estimation of eigenvalues')

for ax in [ax4, ax5, ax6]:
    ax.set_xlabel('Eigenvector index')
    ax.set_ylabel('Estimated eigenvector index')
    
ax1.set_title('No perturbation')
ax4.set_title('No perturbation')
ax2.set_title('1 perturbation')
ax5.set_title('1 perturbation')
ax3.set_title('5 perturbations')
ax6.set_title('5 perturbations')

fxx1 = 0.07
fxx2 = 0.5
fyy1 = 0.89
fyy2 = 0.62
fyy3 = 0.35
abcd_size = 18
fig.text(fxx1, fyy1, '(a)', fontsize=abcd_size)
fig.text(fxx1, fyy2, '(c)', fontsize=abcd_size)
fig.text(fxx2, fyy1, '(b)', fontsize=abcd_size)
fig.text(fxx2, fyy2, '(d)', fontsize=abcd_size)
fig.text(fxx1, fyy3, '(e)', fontsize=abcd_size)
fig.text(fxx2, fyy3, '(f)', fontsize=abcd_size)

plt.savefig('si_spectrum.pdf', bbox_inches='tight')
plt.show()








