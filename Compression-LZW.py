#-*- coding:UTF-8 -*-
#Python 2.7 a ete utilise

class Compression-LZW:

    def __init__(self, fileName):
        """
        Constructor
        """
        self.content = None
		self.dictionnaire = []
		self.compress = []

    def readFile(self, fileName):
        """
        """
        self.fileName = fileName

    def writeFile(self):
        """
		Fonction permettant d'écrire les valeurs compresser dans un fichier binaire.
		@param self doit avoir comme paramètre un objet CompressionLZW
		@type self CompressionLZW
        """

    def compress(self):
		"""
		Fonction pour compresser un fichier texte. Il utilise un système d'association entre charactères ASCII qui sont positionné dans le tableau.
		
		"""
        for c in self.content:
           if(w + c existe dans le dictionnaire) in self.dictionnaire():
               w = w + c
           else
               self.dictionnaire.append(w + c)
               self.compress = w
               w = cu
		self.compress = w
        self.writeFile();

	def decompress(self):
		"""
		Fonction pour décompresser un fichier binaire. Il lis la valeur binaire (entre 256 et +++) pour pouvoir remplacer ce code par sa valeur il prend la valeur ou l'index
		de la liste et 256 - n ,  n étant la valeur binaire.
		"""