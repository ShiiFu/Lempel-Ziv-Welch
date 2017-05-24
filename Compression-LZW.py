#-*- coding:UTF-8 -*-
#Python 2.7 a ete utilise

class CompressionLZW:

    def __init__(self):
        """
        Constructor
        """
        self.content = None
		self.dictionnaire = []
		self.compress = []

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

if __name__ == '__main__':
    compress = CompressionLZW()
    compress.readFile("lorem.txt")
