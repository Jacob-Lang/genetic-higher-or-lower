# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 13:33:01 2018

@author: Jacob
"""
import numpy as np
import HOLgame as game
import matplotlib.pyplot as plt
import copy
from random import randint

Npop = 100
methods = []
for i in range(Npop):
    methods.append([np.random.rand()])
    
Nreps = 100

distance = np.zeros((Npop, Nreps))
nguesses = np.zeros((Npop, Nreps))


def method_extend(methods):
    new_methods = [method + [np.random.rand()] for method in methods]
    return new_methods

def method_breed(methods1, methods2):
    new_methods = []
    for i, val in enumerate(methods1):
        len1 = len(methods1[i])
        len2 = len(methods2[i])
        split_position = randint(0, min(len1, len2))
        new_methods.append(methods1[i][0:split_position] + methods2[i][split_position:])
        new_methods.append(methods2[i][0:split_position] + methods1[i][split_position:])
    return new_methods

def method_mutate(methods):
    new_methods = []
    for i, val in enumerate(methods):
        method_mutated = [ri*np.random.normal(1, 0.1) for ri in methods[i]]
        new_methods.append(method_mutated)
    return new_methods


# takes generation (list) of 'methods'.
# determines best methods. 
# creates new generation of methods
def evolve(r, mean_distance):    
    
    order = np.argsort(mean_distance)  
    r_ordered = [r[i] for i in order] # order 'methods' by mean_distance
        
    methods_grown = method_extend(r_ordered)
    
    r_best_dads, r_best_mums = r_ordered[::2], r_ordered[1::2]
    methods_children = method_breed(r_best_mums, r_best_dads)
    
    methods_mutated = method_mutate(r_ordered)
    
    npop = len(r)
    [ngrown, nbred, nmutated] = [int(0.25*npop), int(0.5*npop), int(0.25*npop)]
    nspare = npop - (ngrown + nbred + nmutated)
    
    new_gen_r = methods_grown[0:ngrown] + methods_children[0:nbred] + methods_mutated[0:nmutated] + r_ordered[0:nspare]
    return new_gen_r
    
 
# plot best mean_distance for each generation.

Ngenerations = 20

gen_mean_distance = np.zeros((Ngenerations, Npop))
gen_mean_nguesses = np.zeros((Ngenerations, Npop))

for ngen in range(Ngenerations):

    for i in range(Npop):
        for ii in range(Nreps):
            [distance[i, ii], nguesses[i, ii]] = game.playGame(methods[i], 1, 10 )
    
    mean_distance = np.mean(distance, 1)
    mean_nguesses = np.mean(nguesses, 1)
    
    gen_mean_distance[ngen, :] = mean_distance
    gen_mean_nguesses[ngen, :] = mean_nguesses
    
    order = np.argsort(mean_distance)  
    methods_ordered = [methods[i] for i in order] # order 'methods' by mean_distance
    
    nbullseye = Npop - np.count_nonzero(mean_distance)
    methods_bullseye_lengths= np.array([len(x) for x in methods_ordered[0:nbullseye]])
    
    order_bylength = np.argsort(methods_bullseye_lengths)
    methods_orderedtwice = [methods_ordered[i] for i in order_bylength] + methods_ordered[nbullseye:]
    
    methods = methods_orderedtwice
    
    if ngen < Ngenerations:   # don't evolve in last loop
        methods = evolve(methods_orderedtwice, mean_distance)


for ngen in range(Ngenerations):
    plt.hist(gen_mean_distance[ngen,:], bins = range(50), alpha=0.5, label = str(ngen))
plt.legend()
plt.show()
