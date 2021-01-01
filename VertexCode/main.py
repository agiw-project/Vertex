from page import Page
from cluster import cluster
import os
import time
import re


def test_clustering():
   start_time = time.time()

   print("...Start reading the directory")

   filePaths = []
   for root, dirs, files in os.walk("pages"):
      for name in files:
         filePaths.append(os.path.join(root, name))

   print("...Start loading the HTML content")

   pages = []
   for path in filePaths:
      tokens = re.split("\\\\", path)
      page = Page(path, tokens[1])
      pages.append(page)


   print("Number of pages loaded:{0}".format(len(pages)))

   start_time_execution = time.time()

   print("---CLUSTERING RESULTS---\n")
   size = 0
   for group in cluster(pages):
      print(group)
      size += len(group)

   print("\n")
   print("Number of pages processed:{0}".format(size))
   print("--- Clustering execution time %s seconds ---" % (time.time() - start_time_execution))
   print("--- Total execution time %s seconds ---" % (time.time() - start_time))









if __name__ == '__main__':
   test_clustering()
