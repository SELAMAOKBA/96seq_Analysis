#-------------------------------------------------------------------------------
# Name:        genera_VennDIS
# Purpose: script used to retrieve genera for different techniques
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

d=()
list_Alginate=[]
list_Agarose=[]
list_Plates=[]
with open("Results/output.txt") as f:
        for line in f:
            m=line.strip().split('\t')
            if m[0] in '1':
                if m[2][0] in '2' :
                    list_Alginate.append((m[6].split(' '))[0])
                if m[2][0] in '3' :
                    list_Agarose.append((m[6].split(' '))[0])
                if m[2][0] not in '2' and m[2][0] not in '3':
##                    print m[2][0], '    ', m[6]
                    list_Plates.append((m[6].split(' '))[0])

f.close()
# techniques list three technique are used
list_Alginate_B=list(set(list_Alginate))
list_Agarose_B=list(set(list_Agarose))
list_Plates_B=list(set(list_Plates))

Technique_list= {"list_Alginate_B":list_Alginate_B, "list_Agarose_B":list_Agarose_B,"list_Plates_B":list_Plates_B}

# write genus_VennDIS.txt with diffrent genera for each technique
for i in Technique_list.keys():
    print i
    print Technique_list[i]
    File_N = open("Results/genus_VennDIS.txt","a")
    file_VennDIS=str(i)+ "\n"+ str(Technique_list[i])+ "\n"
    File_N.write(file_VennDIS)
    File_N.close()


