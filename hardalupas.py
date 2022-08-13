# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 13:23:15 2019

@author: st8g14
"""

import os
import matplotlib.pyplot as plt
import csv
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
    ax.set_xlabel('$\\frac{Z}{\mathrm{d}_l}$')
    ax.set_ylabel('$D_{3,2}$')
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
    ax.plot(line_1[:, 0], line_1[:, 1], color='black', marker='^',
            label='$\\mathrm{d}_l=1.1$mm, We=1700, VR=14.1')
    ax.plot(line_2[:, 0], line_2[:, 1], color='black', marker='o',
            label='$\\mathrm{d}_l=2.3$mm, We=2100, VR=13.3')

    # setting axis limits
    ax.set_xlim(0, 35)
    ax.set_ylim(80, 225)
    # labelling axis
    ax.set_xlabel('$\\frac{Z}{\mathrm{d}_l}$')
    ax.set_ylabel('$D_{3,2}$')
    ax.legend(fontsize=7, frameon=False)
    fig.set_size_inches(2.5, 2.5)
    fig.savefig('hardalupas_figure3a.pgf', bbox_inches='tight')


def hopfinger():
    # loading files
    rayleigh = np.loadtxt('hopfinger_rayleigh.csv', delimiter=',')
    nonaxisymmetric = np.loadtxt('hopfinger_nonaxisymmetric_rayleigh.csv',
                                 delimiter=',')
    wave_like = np.loadtxt('hopfinger_wave_like.csv', delimiter=',')
    fiber = np.loadtxt('hopfinger_fiber.csv', delimiter=',')

    # setting up plots
    fig, ax = plt.subplots()

    # plotting regime lines
    ax.plot(rayleigh[:, 0], rayleigh[:, 1], color='black')
    ax.plot(nonaxisymmetric[:, 0], nonaxisymmetric[:, 1], color='black')
    ax.plot(wave_like[:, 0], wave_like[:, 1], color='black')
    ax.plot(fiber[:, 0], fiber[:, 1], color='black')

    # setting log scales
    ax.set_xscale('log')
    ax.set_yscale('log')

    # setting axis limits
    ax.set_xlim(1e-3, 1e5)
    ax.set_ylim(1e1, 1e6)

    # labelling axis
    ax.set_xlabel('$\\mathrm{We}_\\mathrm{g}$')
    ax.set_ylabel('$\\mathrm{Re}_l$')

    # labelling regimes
    ax.text(2e-3, 4e1, 'Rayleigh breakup', )
    ax.text(3.5e-3, 1.5e1, 'Non-axisymmetric Rayleigh breakup', rotation=-35)
    ax.text(1e-1, 5e3, 'wave-like')
    ax.text(1e2, 2e1, 'membrane breakup', rotation=-80)
    ax.text(1e1, 1e5, 'fiber type')

    # plotting case locations
    ax.plot(5.22, 1551, label='Case 1', marker='o', color='black',
            linestyle='none')
    ax.plot(11.6, 1551, label='Case 2', marker='X', color='black',
            linestyle='none')
    ax.plot(22.9, 1551, label='Case 3', marker='^', color='black',
            linestyle='none')
    ax.plot(52.7, 1551, label='Case 4', marker='s', color='black',
            linestyle='none')

    ax.plot(5.22, 2940, label='Case 5', marker='o', color='red',
            linestyle='none')
    ax.plot(11.6, 2940, label='Case 6', marker='X', color='red',
            linestyle='none')
    ax.plot(22.9, 2940, label='Case 7', marker='^', color='red',
            linestyle='none')
    ax.plot(52.7, 2940, label='Case 8', marker='s', color='red',
            linestyle='none')

    ax.plot(5.22, 6444, label='Case 9', marker='o', color='blue',
            linestyle='none')
    ax.plot(11.6, 6444, label='Case 10', marker='X', color='blue',
            linestyle='none')
    ax.plot(22.9, 6444, label='Case 11', marker='^', color='blue',
            linestyle='none')
    ax.plot(52.7, 6444, label='Case 12', marker='s', color='blue',
            linestyle='none')

    # adding legend
    ax.legend()

    # resizing chart
    fig.set_size_inches(6, 4)
    # saving as pgf file
    fig.savefig('hopfinger_cases_regime.pgf', bbox_inches='tight')


def glr_calculator(weber_number, reynolds_number):
    # liquid jet diameter
    d_l = 2e-3
    # gas jet diameter
    d_g = 7e-3
    # viscosity of liquid
    mu_l = 8.9e-4
    # density of liquid
    rho_l = 1000
    # surface tension
    sigma = 0.07
    # gas density
    rho_g = 1.225
    # liquid velocity
    u_l = reynolds_number*mu_l/(rho_l*d_l)
    # gas velocity
    u_g = np.sqrt((weber_number*sigma)/(d_l*rho_g))+u_l
    # liquid area
    A_l = np.pi*d_l**2/4
    A_g = np.pi*d_g**2/4 - A_l
    glr = (rho_g*u_g*A_g)/(rho_l*u_g*A_g)
    ar = A_l/A_g
    return glr, ar


def zhao_glr():
    # loading files
    rayleigh = np.loadtxt('zhao_glr_rayleigh.csv', delimiter=',')
    bag = np.loadtxt('zhao_glr_bag.csv', delimiter=',')
    membrane = np.loadtxt('zhao_glr_membrane.csv', delimiter=',')

    # setting up plots
    fig, ax = plt.subplots()

    # plotting regime lines
    ax.plot(rayleigh[:, 0], rayleigh[:, 1], color='black')
    ax.plot(bag[:, 0], bag[:, 1], color='black')
    ax.plot(membrane[:, 0], membrane[:, 1], color='black')

    # setting log scales
    ax.set_xscale('log')
    ax.set_yscale('log')



    # labelling regimes
    ax.text(1e0, 1e1, 'Rayleigh')
    ax.text(1e0, 2e1, 'Bag breakup')
    ax.text(1e0, 5e1, 'Membrane-fiber regime')
    ax.text(1e0, 5e2, 'Fiber breakup')

    # Plotting case locations
    ax.plot(glr_calculator(5.22, 1551), 5.22, label='Case 1', marker='o',
            color='black', linestyle='none')
    ax.plot(glr_calculator(11.6, 1551), 11.6, label='Case 2', marker='v',
            color='black', linestyle='none')
    ax.plot(glr_calculator(22.9, 1551), 22.9, label='Case 3', marker='^',
            color='black', linestyle='none')
    ax.plot(glr_calculator(52.7, 1551), 52.7, label='Case 4', marker='<',
            color='black', linestyle='none')

    ax.plot(glr_calculator(5.22, 2940), 5.22, label='Case 5', marker='>',
            color='black', linestyle='none')
    ax.plot(glr_calculator(11.6, 2940), 11.6, label='Case 6', marker='1',
            color='black', linestyle='none')
    ax.plot(glr_calculator(22.9, 2940), 22.9, label='Case 7', marker='s',
            color='black', linestyle='none')
    ax.plot(glr_calculator(52.7, 2940), 52.7, label='Case 8', marker='p',
            color='black', linestyle='none')

    ax.plot(glr_calculator(5.22, 6444), 5.22, label='Case 9', marker='P',
            color='black', linestyle='none')
    ax.plot(glr_calculator(11.6, 6444), 11.6, label='Case 10', marker='*',
            color='black', linestyle='none')
    ax.plot(glr_calculator(22.9, 6444), 22.9, label='Case 11', marker='X',
            color='black', linestyle='none')
    ax.plot(glr_calculator(52.7, 6444), 52.7, label='Case 12', marker='D',
            color='black', linestyle='none')

    # resizing figure
    fig.set_size_inches(6, 4)
