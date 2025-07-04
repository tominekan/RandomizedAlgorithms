"""
Graphs
---

This an implementation of an undirected multigraph, I implement the graphs as an adjacency list. 

For implementation purposes, I'm going to use a dictionary to represent each vertex in the adjacency list.
I'll also note any changes in runtime that this might cause. Also will be adding functionality as we go on.

NOTE: A FASTER IMPLEMENTATION CAN BE DONE BY ALSO KEEPING TRACK OF THE BOTH IN AND OUTGOING VERTICES
but I'm still not sure how much more helpful it might be considering space. In addition, I already implemented this
and I kinda don't want to make any changes here.
"""

from linked_list import LinkedList
from typing import Iterable

class Graph:
    def __init__(self, vertices: set = {}, edges: Iterable = []):
        """
        This is an implementation of an undirected multigraph. 

        `vertices` are the initial set of vertices in the graph

        `edges` are the initial set of edges in the graph. Note that if there's an edge 
        between nonexistent vertices this program will throw an exception. 

        Each entry in `edges` must be of the form `(e1, e2)`, implying that `e1 -> e2`. 

        ---
        O(|V| + |E|)
        """
        
        self.adj_list = {}
        self.num_vertices = len(vertices)
        self.num_edges = len(edges)

        for vertex in vertices:
            self.adj_list[vertex] = LinkedList()

        for edge in edges:
            if (edge[0] in self.adj_list) and (edge[1] in self.adj_list):
                self.adj_list[edge[0]].add_head(edge[1])
            else:
                raise Exception(f"{edge} contains a nonexistent vertex")
    
    def add_edge(self, edge):
        """
        Adds a directed `edge` in the form of (u, v) to the graph. 
        If either `u` or `v` don't exist in the graph, an exception is thrown

        ---
        O(1)
        """

        if (edge[0] in self.adj_list) and (edge[1] in self.adj_list):
            self.adj_list[edge[0]].add_head(edge[1])
            self.num_edges += 1
        else:
            raise Exception(f"{edge} contains a nonexistent vertex")
        
    def add_undirected_edge(self, edge):
        """
        Adds an undirected `edge` in the form of (u, v) to the graph. 
        If either `u` or `v` don't exist in the graph, an exception is thrown

        ---
        O(1)
        """

        if (edge[0] in self.adj_list) and (edge[1] in self.adj_list):
            self.adj_list[edge[0]].add_head(edge[1])
            self.adj_list[edge[1]].add_head(edge[1])
            self.num_edges += 2
        else:
            raise Exception(f"{edge} contains a nonexistent vertex")
        
    def remove_edge(self, edge):
        """
        Removes `edge` from the graph. Throws an exception if any of 
        the vertices don't exist in the graph

        ---
        O(deg(v))
        """

        if (edge[0] in self.adj_list) and (edge[1] in self.adj_list):
            num_removed = self.adj_list[edge[0]].remove_all(edge[1])
            self.num_edges -= num_removed
        else:
            raise Exception(f"{edge} contains a nonexistent vertex")
    
    def remove_undirected_edge(self, edge):
        """
        Removes `edge` from the graph. Throws an exception if any of 
        the vertices don't exist in the graph

        ---
        O(deg(v))
        """

        if (edge[0] in self.adj_list) and (edge[1] in self.adj_list):
            forward_edges = self.adj_list[edge[0]].remove_all(edge[1])
            back_edges = self.adj_list[edge[1]].remove_all(edge[0])
            self.num_edges -= forward_edges + back_edges
        else:
            raise Exception(f"{edge} contains a nonexistent vertex")
        
    
    def add_vertex(self, vertex):
        """
        Add `vertex` to the graph, throws an exception if `vertex`
        to add already exists.

        ---
        O(1)
        """

        if (vertex not in self.adj_list):
            self.adj_list[vertex] = LinkedList()
            self.num_vertices += 1
        else:
            raise Exception(f"{vertex} already exists in the graph.")
    

    def remove_vertex(self, vertex):
        """
        Removes `vertex` from the graph and all vertex pointing towards and away from `vertex`.

        ---
        O(|V| + |E|)
        """

        if vertex in self.adj_list:
            # Remove all vertices pointing to `vertex`
            for v in self.adj_list.keys():
                num_vertex = self.adj_list[v].remove_all(vertex)
                self.num_edges -= num_vertex

            self.num_edges -= len(self.adj_list[vertex])
            # Delete entry corresponding to `vertex`
            del self.adj_list[vertex]
            self.num_vertices -=1
        else:
            raise Exception(f"{vertex} does not exist in the graph.")
    
    def get_neighbors(self, vertex):
        """
        Returns a Linked List of all the vertices ajdacent to `vertex`
        
        ---
        O(1)
        """

        if vertex in self.adj_list:
            return self.adj_list[vertex]
        else:
            raise Exception(f"{vertex} does not exist in the graph")
    
    def replace_vertex(self, vertex, new_v):
        """
        Replaces all edges pointing to and from `vertex` with `new_v`.

        NOTE: THIS IS MORE COMPLICATED BECAUSE NOW WE HAVE TO ALSO CONSIDER THAT WE NEED TO DELETE THE KEY
        THE VERTEX REPRESENTS, AND REPLACE IT WITH `new_v`
        ---
        O(|V| + |E|)
        """
    
        if vertex in self.adj_list:
            # Replaces all vertices pointing to `vertex`
            for v in self.adj_list.keys():
                self.adj_list[v].replace_all(vertex, new_v)
            
            # Removes that specific vertex from the list of keys
            outgoing_edges = self.adj_list.pop(vertex, None)
            if (new_v in self.adj_list):
                # if the vertex already exists, we just add on the new outgoing edges
                self.adj_list[new_v].join(outgoing_edges)
                # We are adding the edges of `vertex` to the already existing vertices in `new_v`
                # This means we lose one edge overall
                self.num_vertices -= 1
            else:
                self.adj_list[new_v] = outgoing_edges

        else:
            raise Exception(f"{vertex} does not exist in the graph.")
