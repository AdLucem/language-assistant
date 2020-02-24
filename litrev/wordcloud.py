from os import listdir
from os.path import isfile, join
import sys
from document import Document

FILEPATH = "/home/adlucem/.data/coal"


class DocNode:

    def __init__(self, name):

        self.name = name
        self.subdirs = []
        self.docs = []

    def add_subdir(self, subdir):

        self.subdirs.append(subdir)

    def add_document(self, document):

        self.docs.append(document)

    def show(self):

        print("========== " + self.name + " ==========")
        print("-------- Subdirectories ---------")
        for subdir in self.subdirs:
            print(subdir.name)
        print("------------- Files -------------")
        for doc in self.docs:
            print(doc.name)
        print("=================================")


def show_level(nodes, level):

    if level == 0:
        for node in nodes:
            node.show()
    else:
        subnodes = []
        for node in nodes:
            subnodes.extend(node.subdirs)
        if subnodes == []:
            print("Tree depth exceeded.")
        else:
            show_level(subnodes, level - 1)


def get_all_files(nodes, level):

    files = []
    if level == 0:
        for node in nodes:
            files.extend(node.docs)
    else:
        subnodes = []
        for node in nodes:
            subnodes.extend(node.subdirs)
        if subnodes == []:
            print("Tree depth exceeded.")
        else:
            show_level(subnodes, level - 1)

    return files


def mk_dir_tree(fpath):

    subdirs = [join(fpath, d) for d in listdir(fpath)
               if (not isfile(join(fpath, d)))]
    files = [join(fpath, f) for f in listdir(fpath)
             if isfile(join(fpath, f))]

    root = DocNode(fpath)
    if subdirs == []:
        for file in files:
            doc = Document(file)
            root.add_document(doc)
        return root
    else:
        for subdir in subdirs:
            subnode = mk_dir_tree(subdir)
            root.add_subdir(subnode)
        return root


root = mk_dir_tree(FILEPATH)
files = get_all_files([root], int(sys.argv[1]))

print("yes")
print(files)
for file in files:
    print(file.name)
    print(file.summarize())
