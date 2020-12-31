from vectorize_shingle import shingles_to_vectors
from bs4 import BeautifulSoup

class Page:
    def __init__(self, pathToFile):
        #read the html file
        file =  open(pathToFile,"r",encoding="utf8")
        self.name = pathToFile.replace("pages/","").replace(".html","")
        self.content = file.read()
        file.close()
        #extract the tags ordered
        self.tags = self.extract_tags()
        #each contiguous sequence of 10 tags within the page
        self.shingles = self.find_shingles()
        #the hash vector of the shingles
        self.shingle_vector =  tuple(shingles_to_vectors(self.shingles))

    def __repr__(self):
        return "Page({0})".format(self.name)

    def __str__(self):
        return "Page({0})".format(self.name)


    def extract_tags(self):
        soup = BeautifulSoup(self.content, "html.parser")
        #the list of tags within the page ordered
        return [tag.name for tag in soup.find_all()]

    def find_shingles(self):
        iterations = len(self.tags)-10+1
        if iterations <= 0:
            iterations = 1

        shingles = []
        start_index = 0
        for i in range(iterations):
            shingle = []
            current_step = 0
            while current_step < 10:
                shingle.append(self.tags[start_index + current_step])
                current_step += 1
            shingles.append(shingle)
            start_index += 1

        shingles = list(map(lambda l: tuple(l), shingles))

        return shingles

