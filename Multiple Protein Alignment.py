from bioservices import UniProt
from Bio.Align.Applications import ClustalwCommandline
import subprocess
import sys
import os
from Bio import AlignIO
from Bio import Phylo

# accessing UniProt and retrieving top 5 protein results
print()
u = UniProt()
input1 = input("Type Protein/gene name to search through UniProt, for which you want to align and present\n In Format 'Name+AND+TOXONOMY:Organism'\n e.g. HLA+and+taxonomy:human\nType Here: ")
res = u.search(input1, limit=5, frmt="tab", columns="entry name, length, id, genes")
print()
print("Top 5 proteins from UniProt Search:")
print(res)

# retieve UniProt Accession of top 5 search, to be stored
res_id = u.search(input1, limit=5, frmt="tab", columns="id")
acc_1 = res_id[6:12]
acc_2 = res_id[13:19]
acc_3 = res_id[20:26]
acc_4 = res_id[27:33]
acc_5 = res_id[34:40]

uniprot_accessions = [acc_1, acc_2, acc_3, acc_4, acc_5]

# Retrieve FASTA sequence for top 5 results

acc_1_fasta = u.retrieve(acc_1, "fasta")
acc_2_fasta = u.retrieve(str(acc_2), "fasta")
acc_3_fasta = u.retrieve(acc_3, "fasta")
acc_4_fasta = u.retrieve(acc_4, "fasta")
acc_5_fasta = u.retrieve(acc_5, "fasta")

top_5_fasta = [acc_1_fasta, acc_2_fasta, acc_3_fasta, acc_4_fasta, acc_5_fasta]


# Write FASTA sequences to a file
ofile = open("top_5.fasta", "w")
for i in range(len(top_5_fasta)):
    ofile.write(str(top_5_fasta[i]))
ofile.close()

# View the FASTA
print("Fasta Sequences")
sneak_peak = open("top_5.fasta", "r")
for line in sneak_peak:
    print(line.strip())
sneak_peak.close()
print()

#Aligning top 5 FASTA sequences
# setup clustal
# replace line 56 with the location of clustalw2.exe
clustalw_exe = r"G:\Programming\Clustalw\clustalw2.exe"
try:
    cline = ClustalwCommandline(clustalw_exe, infile="top_5.fasta")
    # Execute clustal
    child = subprocess.call(str(cline), shell=(sys.platform != "win32"))

    # as alignment
    align = AlignIO.read("top_5.aln", "clustal")
    print("Alignment:")
    print(align)

    # as tree
    tree = Phylo.read("top_5.dnd", "newick")
    print("Alignment representation as Tree:")
    Phylo.draw_ascii(tree)
except ValueError:
    print("Need at least 5 sequences for multiple alignment")


