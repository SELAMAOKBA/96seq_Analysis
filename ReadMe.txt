96seq_Analysis:

"96seq_Analysisis" is a six separate python scripts that run in chronological order 1-6.
This pipeline is created to help analysis sequences retrieved from 96 plate sequencing. 
Sequencing was performed by GATC Biotech Lighton barcode service, however; it can be adapted to other sequencing providers.
the pipeline needs python 2.7.x and the package Biopython 1.6 to run. The scripts were tested under windows 7 environment, Python 2.7.13 and Biopython 1.69.
the pipeline requires also raw files of sequenceing in "fasta" format. Files should be put in "raw" named folder in the same directory as the scripts. 
in addition,"table.txt", matrix 12*8 (tab: separator) file is used to correct plate well(sequence) with strain code. 
all results are saved in "Results" folder.    

1-attribution:Attribute strain's code to sequences (need table.txt and sequences in "raw" folder ),
#           	rewrite the fasta files with Country and strain code in sequence head.
#           	"file name" is modified as as the original "file name-strains code".

2-Blast_Seq: blast sequences and retrieve the three first hit sequences as gb files in
#           	"RefRecordsGBK\data" folder

3-Phyl_file: Divide strains and references sequences (converted to fasta type) into folders
#           	where each folder's name represents a taxonomic group

4-RefRecordsGBK_id_record: pick up all taxonomic groups and the corresponding accession numbers from references strains 
#		and save them in "RefRecordsGBK_id_record.txt" file

5-genus_VennDIS: script used to retrieve genera for different techniques

6-NCBI_reg:  create sequences registration ncbi source_modifiers.tsv file


licence and citation:

for licence and citation use fellow the publication copyright.




  
