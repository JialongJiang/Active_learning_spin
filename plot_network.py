#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 15:46:47 2019

@author: jiangjl
"""

import networkx as nx
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np


def move_axis(ax, delx, dely):
    axp = ax.get_position()
    axp.x0 += delx
    axp.x1 += delx
    axp.y0 += dely
    axp.y1 += dely
    ax.set_position(axp)
    return ax
    
def plot_network(ax, j_mat, nodesz, linewz, pos=None, labeldist=False, spring=False): 
    ax.set_aspect('equal')
    G = nx.from_numpy_array(j_mat)
        
    eposi= [(u, v) for (u,v,d) in G.edges(data=True) if d['weight'] > 0]
    wposi= np.array([d['weight'] for (u,v,d) in G.edges(data=True) if d['weight'] > 0])
    
    enega = [(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] < 0]
    wnega = np.array([d['weight'] for (u,v,d) in G.edges(data=True) if d['weight'] < 0])
    if not pos:
        if spring:
            pos = nx.spring_layout(G, weight=1) # positions for all nodes
        else:
            pos = nx.circular_layout(G)

    #cmp1 = cm.get_cmap('YlGnBu')
    #col1 = cmp1(0.3)
    col1 = '#f0dab1'
    nx.draw_networkx_nodes(G, pos, ax=ax, node_size=61.8 * nodesz, node_color=col1, edgecolors=None)
    
    if labeldist:
        num_spin = j_mat.shape[0]
        poslab = {}
        labtext = {}
        for ii in range(num_spin):
            # poslab[key] = np.array([item[0] + 0.06, item[1] + 0.06]) 
            poslab[ii] = np.array([pos[ii][0] + labeldist, pos[ii][1] + labeldist]) 
            labtext[ii] = ii + 1
        nx.draw_networkx_labels(G, poslab, labels=labtext, ax=ax, font_size=12)
    # edges
    nx.draw_networkx_edges(G, pos, ax=ax, edgelist=eposi, width=linewz * wposi, edge_color='#ff9999')
    
    nx.draw_networkx_edges(G, pos, ax=ax, edgelist=enega, width=- linewz * wnega, edge_color='#9999ff')
    ax.set_axis_off()
    return ax, pos

if __name__ == '__main__':
    #j_mat = rec_net[:, :, 1]
    fig = plt.figure(figsize=[5, 5])
    ax = plt.axes()
    # ax0, pos = plot_network(ax, j_mat, 1, 1.4)
    #np.save('pos16', pos)