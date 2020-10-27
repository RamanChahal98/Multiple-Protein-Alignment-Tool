# Multiple-Protein-Alignment-Tool

This program provides a Python interface to the UniProt website http://uniprot.org to:

1 . Retrieve a top 5 UniProt search for a protein, displaying the entry name, amino acid length, UniProt accession and gene name.

2 . Retrieve amino acid FASTA sequences for the top 5 results and save them to file: top_5.fasta

3 . Perform ClustalW multiple sequence alignment on the top 5 FASTA sequences, displaying the alignment as a table and as a tree.


Installation

This python script uses BioPython, Bioservices and Clustalw2

To install these packages on Linux:

  >> pip install biopython

  >> pip install bioservices 
 
  >> Clustalw2 can be downloaded here: http://www.clustal.org/clustal2/#Download


Before running the script make sure line 56 has the line clustalw_exe = r"PATH" changed to the path of clustalw2.exe on your computer

Usage 

After first running the script you will be promted:

Type Protein/gene name to search through UniProt, for which you want to align and present
 In Format 'Name+AND+TOXONOMY:Organism'
 e.g. HLA+and+taxonomy:human
Type Here: 

Note that the format for the search is not strict and will allow any search. Type as if this was the search bar for UniProt. The resulting alignment should then be successfully presented. 




