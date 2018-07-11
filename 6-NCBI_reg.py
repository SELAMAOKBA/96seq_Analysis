#-------------------------------------------------------------------------------
# Name:        NCBI__Reg
# Purpose: create sequences registration ncbi source_modifiers.tsv file
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


File_N = open("Results/source_modifiers.tsv","a")
file_string_N=str('Sequence_ID'+'\t'+'Organism'+'\t'+'Strain'+'\t'+'Isolation-Source'+'\t'+'Country')+"\n"
File_N.write(file_string_N)
File_N.close()

y=0
while y==0:
    try :
        Isolation_Source= raw_input('Enter an isolation source for your samples ex.soil/water...: ')
        Contry= raw_input('Country for your samples: ')
        if str(Isolation_Source).isalnum() :
            print Isolation_Source, Contry
            y=2


    except:
        print"No isolation source was intered"

##Contry='United_Kingdom'

d={}
try:
    with open("Results/output.txt") as f:
            for line in f:
                if "hit" not in line and line[0] in '1':
                    linn = line.strip().split('\t')

                    key=linn[1]
                    val=linn[9]
                    sourceM=str(Contry)+'_'+str(linn[2])+'\t' +linn[6].split(' ')[0]+'\t'+'UK'+ str(linn[2])+'\t'+Isolation_Source+'\t'+Contry
                    print sourceM
                    File_N = open("Results/source_modifiers.tsv","a")
                    file_string_N=str(sourceM)+"\n"
                    File_N.write(file_string_N)
                    File_N.close()
                    if int(linn[0])==1:
    ##                for year,value in mylist:
                        try:
                            d[val].append(key)
                        except KeyError:
                            d[val] = [key]
    f.close()
    r=d.keys()
    r.sort()

except:
    r=[]