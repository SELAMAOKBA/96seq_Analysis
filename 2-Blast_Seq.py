#-------------------------------------------------------------------------------
# Name:        Blast_Seq
#
# Purpose: blast sequences and retrieve the three first hit sequences as gb files in
#           "RefRecordsGBK\data" folder
#
# Author:      SELAMA Okba, Chiara BORSETTO , Hocine HACENE   Wellington MH Elizabeth.
#
# Created:     10/07/2018
# Copyright:   (c)  2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from __future__ import division
def main():
    pass

if __name__ == '__main__':
    main()

import glob
from Bio.Blast import  NCBIWWW
from Bio.Blast import NCBIXML
from Bio import SeqIO
from Bio import Entrez
import os

file_string = ""
files=glob.glob("Results/seq_attribute/*.fas")

# Writes output files
# output.txt

try:
    os.mkdir("Results/RefRecordsGBK")
##    os.mkdir("Results/RefRecordsGBK/data")
##    os.mkdir("Results/RefRecordsGBK/Results")
##    os.mkdir("Results/RefRecordsGBK/Results/data")
except:
        pass

File = open("Results/output.txt","a")
file_string ="hit"+"\t"+"File_Name"+"\t"+"Strain"+"\t"+"Query_Sequence_Length"+"\t"+"Sequence_accession"+"\t"+"Sbjct_Sequence_Length"+"\t"+"Sbjct_Description"+"\t"+"Identity"+"\t"+"Phylum"+"\t"+"Sub_Taxa""\n"
File.write(file_string)
File.close()
# output_no_records_found.txt
File_N = open("Results/output_no_records_found.txt","a")
File_N.close()

# Query NCBI DATABASES

Db_name="rRNA_typestrains/prokaryotic_16S_ribosomal_RNA" # you can use "nr" database
hls=3 # Number of first hits records to be returned

Bst="blastn"
N_threshold_search=100

for ii in files:
    with open(ii, "rU") as handle:
        for record in SeqIO.parse(handle, "fasta"):
            print("processed record: ",record.id, len(record))
            if len(record)<N_threshold_search:
                print "record escaped"
                file_string = ""
                File_N = open("Results/output_no_records_found.txt","a")
                file_string_N=str(ii.split('\\')[1])+"\t"+"RE_:"+str(len(record))+ "\n"
                File_N.write(file_string_N)
                File_N.close()
                file_string = ""
                File.close()

            if len(record)>=N_threshold_search:

                file_string = ""
                File = open("Results/output.txt","a")
                fasta_string = open(ii).read()
                print "file : " , ii
                try :
                    x=0
                    result_handle = NCBIWWW.qblast(Bst,Db_name , fasta_string, hitlist_size=hls)
                    blast_records = NCBIXML.parse(result_handle)
                    E_VALUE_THRESH = 0.001
                    for blast_record in blast_records:
                        for alignment in blast_record.alignments:
                            Entrez.email = "A.N.Other@example.com"  #
                            filename = 'Results/RefRecordsGBK/'+ii.split('\\')[1].split('.')[0]+'_'+str(x)+'.gbk'
                            if not os.path.isfile(filename):
                                # Downloading...
                                net_handle = Entrez.efetch(db="nucleotide", id=alignment.accession, rettype="gb", retmode="text")
                                out_handle = open(filename, "w")
                                out_handle.write(net_handle.read())
                                out_handle.close()
                                net_handle.close()
                                print("Saved")

                            print("Parsing...")
                            record = SeqIO.read(filename, "genbank")
                            print (record.annotations['taxonomy'][1], record.id)

                            idn=format(alignment.hsps[0].identities*100/blast_record.query_length, '.2f')
                            x+=1
                            for hsp in alignment.hsps:
                                if hsp.expect < E_VALUE_THRESH:
                                   file_string += str(x)+"\t"+str(ii.split('\\')[1])+"\t"+str(((ii.split('\\')[1]).split("-")[1]).split(".fas")[0])+"\t"+str(blast_record.query_length)+"\t"+(alignment.accession)+"\t"+str(alignment.length)+"\t"+(alignment.hit_def)+"\t"+str(idn)+"\t"+str(record.annotations['taxonomy'][1])+"\t"+str(record.annotations['taxonomy'][2])+"\n"
                    File.write(file_string)
                    File.close()

                except (Exception):
                    file_string = ""
                    File_N = open("Results/output_no_records_found.txt","a")
                    file_string_N=str(ii.split('\\')[1])+"\n"
                    File_N.write(file_string_N)
                    File_N.close()
                    file_string = ""
                    File.close()
                    pass

##execfile("3-phyl_file.py")





