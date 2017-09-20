'''
 Rosalind utilities

 Copyright (C) 2017 Greenweaves Software Pty Ltd

 This is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 This software is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with GNU Emacs.  If not, see <http://www.gnu.org/licenses/>

 As is the case with point mutations, the most common type of sequencing
 error occurs when a single nucleotide from a read is interpreted incorrectly.

 Given: A collection of up to 1000 reads of equal length (at most 50 bp) in
 FASTA format. Some of these reads were generated with a single-nucleotide error.
 For each read s in the dataset, one of the following applies:
    s was correctly sequenced and appears in the dataset at least twice
	   (possibly as a reverse complement);
    s is incorrect, it appears in the dataset exactly once, and its
	  Hamming distance is 1 with respect to exactly one correct read 
	  in the dataset (or its reverse complement).

 Return: A list of all corrections in the form "[old read]->[new read]". 
 (Each correction must be a single symbol substitution, and you may return the corrections in any order.)
'''

def revc(dna):
    return dna.translate({
            ord('A'): 'T',
            ord('C'): 'G',
            ord('G'):'C', 
            ord('T'): 'A'})[::-1]

def dbru(S,include_revc=True):
    '''DBRU Constructing a De Bruijn Graph'''
    def union(S):                    
        U=set(S)
        for s in S:
            s_revc=revc(s)
            if include_revc and not s_revc in U:
                U.add(s_revc)
        return U
    def nodes(E):
        B=[]
        for (a,b) in E:
            if not a in B:
                B.append(a)
            if not b in B:
                B.append(b)
        return B
    E= [(e[0:-1],e[1:]) for e in union(S)]
    return (nodes(E),E)

def distance(p1,p2):
    return sum([(p1[i]-p2[i])**2 for i in range(len(p1))])
    
def read_strings(file_name):
    '''
    Read a bunch of strings from file, e.g. reads
    '''
    with open(file_name) as f: 
        return [line.strip() for line in f ]

def read_list(file_name):
    '''
    Read a single list of numbers from file
    '''    
    with open(file_name) as f:
        return [int(n) for n in f.read().split()]
        
def write_list(numeric_list,out=None):
    text=' '.join(str(l) for l in numeric_list )
    if out==None:
        print (text)
    else:
        with open(out,'w') as outfile:
            outfile.write(text)
            