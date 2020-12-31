from page import Page
from cluster import cluster
from os import walk
from zipfile import ZipFile
import os
from os.path import basename

def zipFiles(dirName):
   # create a ZipFile object
   with ZipFile('zippedPages/pages.zip', 'w') as zipObj:
      # Iterate over all the files in directory
      for folderName, subfolders, filenames in os.walk(dirName):
         for filename in filenames:
            # create complete filepath of file in directory
            filePath = os.path.join(folderName, filename)
            # Add file to zip
            zipObj.write(filePath, basename(filePath))


def unzipFiles(path_to_file):
   with ZipFile(path_to_file, 'r') as zip_ref:
      zip_ref.extractall("pages")



def test_clustering():
   fileNames = []
   for (dirpath, dirnames, filenames) in walk("pages/"):
      fileNames.extend(filenames)

   pages = []
   for name in fileNames:
      p = Page("pages/" + name)
      pages.append(p)

   print(cluster(pages))




if __name__ == '__main__':
   test_clustering()
