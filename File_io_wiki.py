# -*- coding: utf-8 -*-
"""
Created on Sun May 31 12:15:43 2015

@author: Apt
"""
import csv
import networkx as nx

def find_shortest_path(startNode, endNode):
    '''
    Given a starting node (startNode) and ending node (endNode), the method
    returns a list of nodes which represents the shortest path from the 
    start to the end.
    ex. Return [1, 3, 20] given startNode = 1 and endNode = 20
    
    Iterative vs. recursive
    Lookup depth-first and breadth-first search algorithms.
    How to check each edge?
    '''
    if startNode == endNode:
        return


if __name__ == '__main__':
    
    #titlesFile = 'titles-sorted.txt'
    #linksFile = 'links-simple-sorted.txt'
    titlesFile = 'university_titles.txt'
    linksFile = 'university_links.txt'    
    titles = {}
    links = {}
    
    with open(titlesFile, mode='r') as f:
        i = 0
        for line in f.readlines():
            i += 1       
            print line
            titles[i] = line.strip()
    
    with open(linksFile, mode='r') as f:
        for line in f.readlines():
            (source, targetsAsString) = line.strip().split(':')
            targets = targetsAsString.strip().split(' ')
            links[source] = targets
            
    '''for i in range(len(titles)):
        # If entry begins with a non-English character, remove it from the list.
        entry = titles[i]
        if ord(entry[0]) < 33 or ord(entry[0]) > 126:
            print titles.pop(i)'''
    
    G = nx.DiGraph()
    for source in links.keys():
        targets = links[source]
        for target in targets:
            G.add_edge(source, target)
    
