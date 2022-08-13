# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 13:23:15 2019

@author: st8g14
"""

import os
import matplotlib.pyplot as plt
import numpy as np

os.environ['PATH'] = os.environ['PATH'] + ':/Library/TeX/texbin'


def figure_3a():
    # loading files
    line_1 = np.loadtxt('3a/3a_1-1.csv',
                        delimiter=',')
    line_2 = np.loadtxt('3a/3a_2-3.csv',
                        delimiter=',')

    # setting up plots
    fig, ax = plt.subplots()
    ax.plot(line_1[:, 0], line_1[:, 1], color='black', marker='^',
            label='$\\mathrm{d}_l=1.1$mm, We=1700, VR=14.1')
    ax.plot(line_2[:, 0], line_2[:, 1], color='black', marker='o',
            label='$\\mathrm{d}_l=2.3$mm, We=2100, VR=13.3')

    # setting axis limits
    ax.set_xlim(0, 35)
    ax.set_ylim(80, 225)
    # labelling axis
    ax.set_xlabel('$\\frac{Z}\\mathrm{d}_l}$')
    ax.set_ylabel('$D_{3,2} (\\mu m)$')
    ax.legend(fontsize=7, frameon=False)
    fig.set_size_inches(2.5, 2.5)
    fig.savefig('hardalupas_figure3a.pgf', bbox_inches='tight')


def figure_3b():
    # loading files
    line_1 = np.loadtxt('3b/3b_1054.csv',
                        delimiter=',')
    line_2 = np.loadtxt('3b/3b_1370.csv',
                        delimiter=',')
    line_3 = np.loadtxt('3b/3b_1815.csv',
                        delimiter=',')

    # setting up plots
    fig, ax = plt.subplots()
    ax.plot(line_1[:, 0], line_1[:, 1], color='black', marker='o',
            label='$\\mathrm{d}_l=2.3$mm, We=1054, VR=23.9')
    ax.plot(line_2[:, 0], line_2[:, 1], color='black', marker='^',
            label='$\\mathrm{d}_l=1.1$mm, We=1370, VR=25.2')
    ax.plot(line_3[:, 0], line_3[:, 1], color='black', marker='s',
            label='$\\mathrm{d}_l=1.1$mm, We=1815, VR=28.8')

    # setting axis limits
    ax.set_xlim(0, 35)
    ax.set_ylim(80, 225)
    # labelling axis
    ax.set_xlabel('$\\frac{Z}{\\mathrm{d}_l}$')
    ax.set_ylabel('$D_{3,2} (\\mu m)$')
    ax.legend(loc='upper center', fontsize=7, frameon=False,
              bbox_to_anchor=(0.5, 1.2))
    fig.set_size_inches(2.5, 2.5)
    fig.savefig('hardalupas_figure3b.pgf', bbox_inches='tight')
