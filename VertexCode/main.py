from page import Page
from cluster import cluster
import os
import re


def test_clustering():
   filePaths = []
   for root, dirs, files in os.walk("pages"):
      for name in files:
         filePaths.append(os.path.join(root, name))


   pages = []
   for path in filePaths:
      tokens = re.split("\\\\", path)
      page = Page(path, tokens[1])
      pages.append(page)

   for group in cluster(pages):
      print(group)







if __name__ == '__main__':
   test_clustering()
