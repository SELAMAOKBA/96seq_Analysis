#-------------------------------------------------------------------------------
# Name:        Attribution
# Purpose:  Attribute strains' code to sequences (need 96 table strains and  96 sequences ),
#           rewrite the fasta files with Country head and strain code, and
#           "file name" as the original "file name-strains code".
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
import glob
import shutil as sh
list_table=[]
plate=[]

try:
    os.mkdir("Results")
except:
    pass


try:
    os.mkdir("Results/seq_attribute")
except:
    pass

root_path = "./raw"
dest_path = "./Results/seq_attribute"

for dirpath, dnames, fnames in os.walk(root_path):
    for f in fnames:
        if f.endswith(".fas"):
            source_file_path =  os.path.join(dirpath, f)
            dest_file_path   =  os.path.join(dest_path, f)
            sh.copyfile(source_file_path, dest_file_path)


with open("table.txt") as cl:
    for line in cl:
        val = line.upper().strip().split('\t')
        list_table.extend(val)
cl.close()


##with open("96plate.txt") as pl:
##    for line in pl:
##        val = line.upper().strip().split('\t')
##        plate.extend(val)
##pl.close()


files=glob.glob("Results/seq_attribute/*.fas")



for lt in xrange(0,len(list_table)) :


    try:
        old_file = files[lt]
        new_file = os.path.join("Results/seq_attribute",str(files[lt].split('\\')[1].split(".fas")[0]+"-"+list_table[lt]+".fas"))
        os.rename(old_file, new_file)
    except:
        pass


files=glob.glob("Results/seq_attribute/*.fas")

y=0
while y==0:
    try :

        isolation_cite= raw_input('Country for your samples: ')
        if len(isolation_cite.replace (" ",""))!=0 :
            print isolation_cite
            y=2


    except:
        print"No isolation source was entered"


for fi in files:
    print fi

    file_source= fi
    newname='>'+isolation_cite+'_'+fi.split('-')[1].split('.')[0]+'\n'
    fasta= open(fi)
    newfasta= open(fi.split('.')[0]+'_N.fas', 'w')
##    newfasta=fasta

    for line in fasta:
        if line.startswith('>'):
    ##        newname= newnames.readline()
            newfasta.write(newname)
        else:
            newfasta.write(line)

    fasta.close()
    ##newname.close()
    newfasta.close()
##

files=glob.glob("Results/seq_attribute/*_N.fas")

for fil in files:

    sh.move(fil, fil.replace('_N',''))

##execfile("2-Blast_Seq.py")


