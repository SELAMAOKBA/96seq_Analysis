#-------------------------------------------------------------------------------
# Name:        Phyl_file
#
# Purpose:  Divide strains and references (converted to fasta type) sequences into folders
#           where each folder's name represent a taxonomic group
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

import os

from Bio import SeqIO
import glob
try:
    os.mkdir("Results/seq_attribute/Taxa_fasta_strians")
    os.mkdir("Results/RefRecordsGBK")
    os.mkdir("Results/RefRecordsGBK")
except:
        pass

file_string = ""
files=glob.glob("Results/RefRecordsGBK/*_0.gbk") # pick first sequences hits of all reference sequences
print files

for fil in files:
    SeqIO.convert(fil, "genbank", fil.split('.')[0]+".fas", "fasta") # convert the chosen sequences to fasta format

try:
    os.mkdir("Results/RefRecordsGBK/Taxa_fasta")
except:
        pass
files=glob.glob("Results/RefRecordsGBK/*_0.fas") # pick first hit sequence (fasta) for each strain
for fii in files:
    try:
        os.rename(fii,'Results/RefRecordsGBK/Taxa_fasta/'+fii.split('Results/RefRecordsGBK\\')[1]) # move ref seq to the right taxonomic group

    except:
        pass

## load taxa from file
d={}
try:
    with open("Results/output.txt") as f:
            for line in f:
                if "hit" not in line:
                    linn = line.strip().split('\t')

                    key=linn[1]
                    val=linn[9]
                    if int(linn[0])==1:
                        try:
                            d[val].append(key)
                        except KeyError:
                            d[val] = [key]
    f.close()
    r=d.keys()
    r.sort()

except:
    r=[]

for fi in r:

    try:
        os.mkdir("Results/seq_attribute/Taxa_fasta_strians/"+fi)
    except:
        pass

# move files (strains) to the right taxonomic groups
for i in r:
    print i
    for m in d[i]:
        print m
        try:
            os.rename('Results/seq_attribute/'+m,'Results/seq_attribute/Taxa_fasta_strians/'+i+'/'+m)

        except:
            pass
i=''
m=''

# move files (reference strains) to taxonomic groups
for fi in r:

    try:
        os.mkdir("Results/RefRecordsGBK/Taxa_fasta/"+fi)
    except:
        pass

for i in r:
    print i
    for m in d[i]:
        print m
        try:
            os.rename('Results/RefRecordsGBK/Taxa_fasta/'+m.split('.')[0]+'_0'+'.fas','Results/RefRecordsGBK/Taxa_fasta/'+i+'/'+m.split('.')[0]+'_0'+'.fas')

        except:
            pass
##

