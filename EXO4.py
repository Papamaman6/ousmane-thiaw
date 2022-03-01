import math
import time





class Poo:
    
    def Read(self,val):
        fich = open(val,"r")
        
        return int(fich.read())

    def Syracuse(self, number):
        val = "Etapes de Syracuse : \n"

        while(number!=1):
            val+=str(number)+"\n"
            
            if (number%2)==0:
                number=number/2
            else:
                number= number*3+1
        return val
        

    def Write(self,str,fichier):
        fich = open(fichier,"w")
        fich.write(str)
        fich.close

classe = Poo()
valeurRead = classe.Read("FichierIn.txt")
valeurWrite = classe.Syracuse(valeurRead)
classe.Write(valeurWrite,"FichierWrite.txt")