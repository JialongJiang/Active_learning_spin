# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 11:17:57 2019

@author: Jialong Jiang
"""

import matplotlib.pyplot as plt
from matplotlib import cm
import scipy.io as sio
import numpy as np
import matplotlib as mpb
import matplotlib.gridspec as gridspec
import sys

sys.path.append('..')
from plot_network import plot_network, move_axis

mpb.rcParams.update({'font.size': 14})
mpb.rcParams.update({'axes.labelsize': 16})
mpb.rcParams.update({'figure.dpi': 300})

figw = 17.8 / 2.54 * 2
figh = 17.8 / 20  / 2.54 * 13 * 2
fig = plt.figure(figsize=[figw, figh])
gs = gridspec.GridSpec(2, 3, width_ratios=[1, 1, 1], height_ratios=[1, 1], 
                       left=0.1, right=0.94, top=0.94, bottom=0.1, 
                       wspace=0.25, hspace=0.25)

ax1 = plt.subplot(gs[0])
ax2 = plt.subplot(gs[1])
ax3 = plt.subplot(gs[2])
# ax4 = plt.subplot(gs[3])
ax5 = plt.subplot(gs[4])
ax6 = plt.subplot(gs[5])

axp = ax2.get_position()
axp.y0 += 0.03
ax2.set_position(axp)
# ax2 = move_axis(ax2, 0,)
ax2.set_aspect('equal')

gs2 = gridspec.GridSpec(2, 2, width_ratios=[1, 1], height_ratios=[1, 1], 
                       left=0.05, right=0.34, top=0.5, bottom=0.08, 
                       wspace=0.15, hspace=0.02)
ax41 = plt.subplot(gs2[0])
ax42 = plt.subplot(gs2[1])
ax43 = plt.subplot(gs2[2])
ax44 = plt.subplot(gs2[3])


ax43p = ax43.get_position()
ax43p.y0 += 0.023
ax43p.y1 -= 0.008
ax43.set_position(ax43p)

ax44p = ax44.get_position()
ax44p.y0 += 0.023
ax44p.y1 -= 0.008
ax44.set_position(ax44p)

ax41.set_aspect('equal')
ax42.set_aspect('equal')
ax43.set_aspect('equal')
ax44.set_aspect('equal')

move_axis(ax44, - 0.035, 0)
move_axis(ax42, - 0.03, 0)


mdata = sio.loadmat("fig1_data_two_spinn")
locals().update(mdata)
xxm = - xxm
yym = - yym
j_mat = - j_mat.astype(np.float32)
h_pert = - h_pert 

ax11 = fig.add_axes([0.15, 0.56, 0.08, 0.2])
# ax11 = fig.add_axes([0.24, 0.77, 0.08, 0.2])
ax11.set_aspect('equal')
ax11, pos = plot_network(ax11, j_mat, 1, 3)
ax11.set_ylim([- 0.6, 0.6])
ax11.set_xlim([- 1.4, 1.4])
cors = np.array(list(pos.values()))
sca = 4
#ax11.quiver(cors[:, 0] - 0.24, cors[:, 1] - h_pert[:, 0] / sca, 
qv11 = ax11.quiver(cors[:, 0], cors[:, 1] - h_pert[:, 0] / sca, 
            0, h_pert[:, 0], scale=sca, color='k', edgecolor='k', 
            width=0.02)
ax11.text(- 0.85, - 0.95, r'$h = h^*$', fontsize=14)
qv11.set_zorder(10)

mdata = sio.loadmat("fig1_data_ising_chainnn")
locals().update(mdata)
inten_list = np.squeeze(inten_list) 
j_mat = - j_mat
h_pert = - h_pert


ax41, pos = plot_network(ax41, j_mat, 1, 1, labeldist=- 0.12)
ax41.set_ylim([- 1.4, 1.4])
ax41.set_xlim([- 1.2, 1.1])
sca = 20
cors = np.array(list(pos.values()))
# ax41.quiver(cors[:, 0] - 0.16, cors[:, 1] - h_pert[:, 0] / sca, 
qv41 = ax41.quiver(cors[:, 0], cors[:, 1] - h_pert[:, 0] / sca, 
            0, h_pert[:, 0], scale=sca, color='k', edgecolor='k', 
            width=0.014)
qv41.set_zorder(10)
ax42, pos = plot_network(ax42, j_mat, 1, 1)
ax42.set_ylim([- 1.4, 1.4])
ax41.set_xlim([- 1.2, 1.1])
cors = np.array(list(pos.values()))
# cplotq = ax42.quiver(cors[:, 0] - 0.16, cors[:, 1] - h_pert[:, 1] / sca, 
cplotq = ax42.quiver(cors[:, 0], cors[:, 1] - h_pert[:, 1] / sca, 
            0, h_pert[:, 1], scale=sca, color='k', edgecolor='k', 
            width=0.014)
cplotq.set_zorder(10)
ax41.text(- 0.4, - 0.1, r'$h = h^{(1)}$', fontsize=14)
ax42.text(- 0.4, - 0.1, r'$h = h^{(2)}$', fontsize=14)
ax42.quiverkey(cplotq, - 0.1, 0.2, 4, label='h = 4', fontproperties={'size': 12}, 
              labelpos='S', angle=90, labelsep=0.2)

ax43.imshow(rec_corrs[:, :, 1], cmap='PiYG_r', clim=[- 1, 1])
# ax44.imshow(np.mean(rec_corrs[:, :, 1:], axis=2), cmap='PiYG_r', clim=[- 1, 1])
imax4 = ax44.imshow(rec_corrs[:, :, 2], cmap='PiYG_r', clim=[- 1, 1])
ax44.set_yticks([])
ax43.set_ylabel('Node index')
ax44.set_xlabel('Node index', position=[- 0.1, 0])
# ax43.yaxis.tick_right()
# ax43.yaxis.set_label_position('right')
ax43.set_xticks(np.arange(8) - 0.5, minor=True);
ax43.set_yticks(np.arange(8) - 0.5, minor=True);
ax43.grid(which='minor', color='w', linestyle='-', linewidth=1)
ax43.set_xticks([1, 3, 5, 7])
ax43.set_xticklabels([2, 4, 6, 8])
ax43.set_yticks([1, 3, 5, 7])
ax43.set_yticklabels([2, 4, 6, 8])
# ax43.minorticks_off()
ax43.tick_params(which='minor', length=0)


ax44.set_xticks(np.arange(8) - 0.5, minor=True);
ax44.set_yticks(np.arange(8) - 0.5, minor=True);
ax44.grid(which='minor', color='w', linestyle='-', linewidth=1)
ax44.set_xticks([1, 3, 5, 7])
ax44.set_xticklabels([2, 4, 6, 8])
# ax43.minorticks_off()
ax44.tick_params(which='minor', length=0)


ax44c = fig.add_axes([0.3, 0.1, 0.01, 0.18])
cbar = fig.colorbar(imax4, cax=ax44c, ticks=[- 1, 0, 1])
ax44c.set_ylabel('Correlation', position=[0.8, 0.48], labelpad=-10)


def plot_wline(xx, yy, wd, color, label):
    for ii in range(xx.size):
        cxx = xx[ii]
        cyy = yy[ii]
        ax1.semilogy([cxx - wd, cxx + wd], [cyy, cyy], color=color, 
                     linewidth=2, label=label)
        

ax1.plot(line_para.T, corr_minus.T)
ax1.plot([0, 1.6], [0, 0], '--', color='k')
ax1.set_ylabel('Correlation')
ax1.yaxis.label.set_color('C0')
ax1.set_xlabel(r'Field strength $h_1 = - h_2$')
sc1 = ax1.scatter(1 + np.log(2)/2, 0, color='k')
sc1.set_zorder(10)
ax1.set_ylim([- 0.6, 1.05])
ax1.set_yticks([- 0.5, 0, 0.5, 1])
#ax1.annotate(r'$\mathcal{I} = 1$', xy=[1 + np.log(2)/2, 0], 
#             xytext=[1.0, - 0.15], fontsize=14)
ax1.tick_params(axis='y', labelcolor='C0')

ax1f = ax1.twinx()
ax1f.plot(line_para.T, fish_minus.T, 'C1')
sc2 = ax1f.scatter(1 + np.log(2)/2, 1, color='k')
sc2.set_zorder(10)
ax1f.plot([1 + np.log(2)/2, 1 + np.log(2)/2], [- 0.2, 1.05], '--', color='k')
ax1f.set_ylabel(r'$\mathcal{I}$', rotation=0, labelpad=-10, fontsize=16)
ax1f.set_ylim([0.2, 1.05])
ax1f.set_yticks([0.5, 1])
move_axis(ax1, - 0.015, 0)
ax1p = ax1.get_position()
ax1p.y0 += 0.03
ax1.set_position(ax1p)
ax1f.tick_params(axis='y', labelcolor='C1')
ax1f.spines['left'].set_color('C0')
ax1f.spines['right'].set_color('C1')
ax1f.yaxis.label.set_color('C1')


cset = ax2.contour(xxm, yym, zz, cmap=cm.coolwarm)
surf = ax2.contourf(xxm, yym, zz, cmap=cm.coolwarm, alpha=0.5)

ax2.set_xlabel(r'$h_1$', position=[0.4, -1], labelpad=- 5)
ax2.set_xticks([- 2, 0, 2])
ax2.set_xlim(- 3, 3)
ax2.set_ylabel(r'$h_2$', rotation=0, labelpad=- 2, position=[0, 0.6])
ax2.set_yticks([- 2, 0, 2])
ax2.set_ylim(- 3, 3)
ax2.xaxis.tick_top()
ax2.xaxis.set_label_position('top')
ax2.scatter(1 + np.log(2)/2, - (1 + np.log(2)/2), color='k')
ax2.text(1.2, - 1, r'$h^*$')
        

axp = ax2.get_position()
gg = 0.15
cax2n = fig.add_axes([(axp.x0 + axp.x1 - gg) / 2, axp.y0 - 0.03, gg, 0.02])
cbarn = fig.colorbar(surf, cax=cax2n, orientation='horizontal',
                    ticks=[0, 0.5, 1])
cax2n.set_xticklabels([0, 0.5, 1])
cax2n.text(- 0.2, 0, r'$\mathcal{I}$', fontsize=18)

# manual arrowhead width and length
hw = 0.4 
hl = 0.4
lw = 2 # axis line width
ohg = 0.3 # arrow overhang
arr1 = ax2.arrow(0, 0, 2, - 2, fc='k', ec='k', lw = lw, 
             head_width=hw, head_length=hl, overhang = ohg, 
             length_includes_head= True, clip_on = False) 
arr1.set_zorder(10)



rec_inten = np.squeeze(rec_inten)
rec_fishinv = np.squeeze(rec_fishinv)
ax3.semilogy(rec_inten, rec_fishinv, label=r'$h = 0$')
ax3.semilogy(rec_inten, np.ones(rec_fishinv.shape), '--', label=r'$h = h^*$')
ax3.legend()
ax3.set_xlabel(r'Interaction strength $J$')
ax3.set_ylabel(r'$\mathcal{I}^{- 1}$', position=[- 0.14, 0.55], labelpad=- 5)
ax3p = ax3.get_position()
ax3p.y0 += 0.03
ax3.set_position(ax3p)
move_axis(ax3, 0.01, 0)



eig_ind = np.arange(8, 0, - 1)
ax5.semilogy(eig_ind, rec_eigs[:, 0], label=r'$h = 0$')
ax5.semilogy(eig_ind, rec_eigs[:, 1], '--', label=r'$h = h^{(1)}$')
ax5.semilogy(eig_ind, rec_eigs[:, 2], '-.', label=r'$\{h^{(1)}, h^{(2)}\}$')
#ax3.plot(eig_ind, np.log10(np.diag(fishdb)), label='Both')
ax5.legend(loc=[0.1, 0.1])
ax5.set_xlabel('Eigenvalue index')
ax5.set_ylabel(r'Eigenvalues of $\mathcal{I}$', position=[- 0.1, 0.5], labelpad=0)
ax5.set_yticks([1e-4, 1e-2, 1])
ax5.invert_xaxis()

ax5p = ax5.get_position()
ax5p.y0 += 0.01
ax5.set_position(ax5p)
move_axis(ax5, 0.007, 0)



ax6.semilogy(inten_list, rec_trinv[0, :].T, label=r'$h = 0$')
ax6.semilogy(inten_list, rec_trinv[1, :].T, '--', label=r'$h = h^{(1)}$')
ax6.semilogy(inten_list, rec_trinv[2, :].T, '-.', label=r'$\{h^{(1)}, h^{(2)}\}$')
ax6.legend()
ax6.set_xlabel(r'Interaction strength $J$')
ax6.set_ylabel(r'$\mathrm{Tr}\mathcal{I}^{- 1}$', position=[- 0.14, 0.55], labelpad=0)

ax6p = ax6.get_position()
ax6p.y0 += 0.01
ax6.set_position(ax6p)
move_axis(ax6, 0.01, 0)


abcd_size = 18

xx0 = 0.05
xx1 = 0.37
xx2 = 0.65
yy1 = 0.5
yy0 = 0.96
fig.text(xx0, yy0, '(a)', fontsize=abcd_size)
fig.text(xx1, yy0, '(b)', fontsize=abcd_size)
fig.text(xx2, yy0, '(c)', fontsize=abcd_size)
fig.text(xx0, yy1, '(d)', fontsize=abcd_size)
fig.text(xx1, yy1, '(e)', fontsize=abcd_size)
fig.text(xx2, yy1, '(f)', fontsize=abcd_size)

plt.savefig('fig1.pdf', bbox='tight')