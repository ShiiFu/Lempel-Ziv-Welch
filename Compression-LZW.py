#-*- coding:UTF-8 -*-
#Python 2.7 a ete utilise

class CompressionLZW:

    def __init__(self):
        """
        Constructor
        """
        self.content = None

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
        """

    def compress(self):
        w = Nul;
        for c in file:
           if(w + c existe dans le dictionnaire) in list():
               w = w + c;
           else
               ajouter w + c au dictionnaire;
               écrire le code de w;
               w = c;
           fin si
        fin tant que
        écrire le code de w;

if __name__ == '__main__':
    compress = CompressionLZW()
    compress.readFile("lorem.txt")
