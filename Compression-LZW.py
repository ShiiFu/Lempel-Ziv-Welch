#-*- coding:UTF-8 -*-
#Python 2.7 a ete utilise

from array import array
import argparse
import sys
import re

class CompressionLZW:

    def __init__(self,):
        """
        Constructor
        """
        self.content = None
        self.dictionnaire = []
        self.compressed = []

    def setContent(self, content):
        """
        Définis le contenu à compresser.

        @param content Contenu à compresser
        """
        self.content = content

    def setFileName(self, fileName):
        """
        Définis le nom du fichier

        @param fileName Nom fichier
        """
        self.fileName = fileName

    def readFile(self, fileName):
        """
        Lis le contenus du fichier fileName.

        @param fileName Nom du fichier à lire
        """
        self.fileName = fileName
        self.file = open(self.fileName, 'r')
        self.content = self.file.read()


    def writeFileC(self, fileName):
        """
        Fonction permettant d'écrire les valeurs compresser dans un fichier binaire.
        @param self doit avoir comme paramètre un objet CompressionLZW
        @type self CompressionLZW
        """
        binaryString =  ""
        for i in self.compressed:
            binaryString += "{0:09b}".format(i)

        binaryArray = array("B")
        for i in range(0, len(binaryString), 8):
            binaryArray.append(int(binaryString[i:i+8], 2))
		
        fileCompressed = open(fileName + ".lzwly", "wb")
        binaryArray.tofile(fileCompressed)
		
    def writeFileD(self, fileName):
		"""
		Fonction permettant d'écrire les valeurs décompresser dans un fichier text standard.
		@param self doit avoir comme paramètre un objet CompressionLZW
		@type self CompressionLZW
		"""
		fileCompressed = open(fileName + ".txt", "wb")
		fileCompressed.write(self.content)

    def compress(self):
        """
        Fonction pour compresser un fichier texte. Il utilise un système d'association entre charactères ASCII qui sont positionné dans un tableau.

        """
        print "Compression du fichier", self.fileName,"\n"
        w = ""
        for c in self.content:
           if w + c in self.dictionnaire:
               w = w + c
           else:
               if w != "" :
                   self.dictionnaire.append(w + c)
                   if len(w) > 1:
                       self.compressed.append(self.dictionnaire.index(w) + 256)
                   else:
                       self.compressed.append(ord(w))
               w = c

    def decompress(self):
        """
        Fonction pour décompresser un fichier binaire. Il lis la valeur binaire (entre 256 et +++) pour pouvoir remplacer ce code par sa valeur il prend la valeur ou l'index
        de la liste et 256 - n ,  n étant la valeur binaire.
        """
        print "Décompression du fichier", self.fileName,"\n"
        w = self.content
        for c in self.content:
            if (c > 255) and self.dictionnaire[c] != None:
               ent = self.dictionnaire[c]
            elif c > 255 and self.dictionnaire[c] == None:
               ent = w + w[0]
            else:
               ent = c
            sortie = ent
            self.dictionnaire.append(w+ent[0])
            w = ent

#if __name__ == '__main__':
    #Compression d'un fichier
	# compress = CompressionLZW()
# #    compress.readFile("lorem.txt")
	# compress.readFile("toBe.txt")
	# compress.compress()
	# compress.writeFileC()
	
	# #Décompression de ce même fichier
	# decompress = CompressionLZW()
	# decompress.readFile("toBe.txt.lzwly")
	# decompress.decompress()
	# decompress.writeFileD()
	
	
def Compression(infile, outfile):
	fileD = CompressionLZW()
	fileD.readFile(infile)
	fileD.compress()
	fileD.writeFileC(outfile)

def Decompression(infile, outfile):
	fileD = CompressionLZW()
	fileD.readFile(infile)
	fileD.decompress()
	fileD.writeFileD(outfile)


"""
Documentation interne disponible écrite ci-dessous. 
Pour la lire exécutez le programme avec l'argument argument -h 
"""
parser = argparse.ArgumentParser(description='Compresse ou Décompresse un fichier avec la méthode Lempel-Ziv-Welch')
parser.add_argument('infile', nargs=1,
					help='Nom du fichier en entrée')
parser.add_argument('outfile', nargs='?', 
					help='Nom du fichier en sortie')
parser.add_argument("-d", dest='Decompression', action="store_true",
					help='Décompresse le fichier en entrée')
parser.add_argument("-c", dest='Compression', action="store_true",
					help='Compresse le fichier en entrée')


args = parser.parse_args()

m = re.split("'",str(args.infile))
infile = str(m[1])

if args.Compression==True and args.Decompression==False:
	Compression(infile, args.outfile)
elif args.Decompression==True and args.Compression==False:
	Decompression(infile, args.outfile)
else:
	print("Effectuez la commande -h pour l'aide")

