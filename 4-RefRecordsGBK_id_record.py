#-------------------------------------------------------------------------------
# Name:        RefRecordsGBK_id_record
#
# Purpose:  pick up all the accession numbers from refrences strains and save them in "RefRecordsGBK_id_record.txt" file
#
# Author:      SELAMA Okba, Chiara BORSETTO , Hocine HACENE   Wellington MH Elizabeth.
#
# Created:     10/07/2018
# Copyright:   (c)  2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import glob
import os
from Bio import SeqIO

for filename in os.listdir("Results/seq_attribute/Taxa_fasta_strians/"):
    if ".fas" not in filename:
        print  filename
        file_string = ""
        File_N = open("Results/RefRecordsGBK_id_record.txt","a")
        file_string_N=str(filename)+ "\n"
        File_N.write(file_string_N)
        File_N.close()
        files=glob.glob("Results/RefRecordsGBK/Taxa_fasta/"+filename+"/*.fas")
        for fil in files:
            with open(fil, "rU") as handle:
                for record in SeqIO.parse(handle, "fasta"):
                    print("processed record: ",record.id, len(record))
                    file_string = ""
                    File_N = open("Results/RefRecordsGBK_id_record.txt","a")
                    file_string_N=str(record.id)+ "\n"
                    File_N.write(file_string_N)
                    File_N.close()










