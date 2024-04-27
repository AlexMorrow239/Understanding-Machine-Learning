import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import bisect

#------------------------------------------
# The TaxonomyNode class
#------------------------------------------

class TaxonomyNode:
  def __init__(self,name,category):
    self.name = name           # The "name" of the node such as Animalia or Chordata 
	                           #   (i.e. the values of the csv table)
    self.category = category   # The "category" such as Kingdom or Phylum
	                           #   (i.e. the column headers of the csv table)
    self.children = []         # The list of children each of type TaxonomyNode

  def __lt__(self,other):
    return self.name < other.name

  def __eq__(self,other):
    return self.name == other.name

  def addChild(self,name,category):
    newChild = TaxonomyNode(name,category)
    self.children.append(newChild)
    self.children.sort(key=lambda x: x.name)
	
  def hasChild(self,name,category):
    for child in self.children:
      if child.name == name and child.category == category:
        return True
    return False

  def getChild(self,name,category):
    for child in self.children:
      if child.name == name and child.category == category:
        return child
    return None

#------------------------------------------
# The TaxonomyTree class
#------------------------------------------

class TaxonomyTree:
  def __init__(self):
    self.root = TaxonomyNode("","")

  def addSpecies(self,names,categories):
    current = self.root
    for i in range(len(categories)):
      if not current.hasChild(names[i],categories[i]):
        current.addChild(names[i],categories[i])
      current = current.getChild(names[i],categories[i])

  @staticmethod
  def print_internal(node, lineno, number_str, name_str):
      if node.name != '':
        print(f"{lineno:<10}{number_str:<30} {name_str}{node.name}.")
        lineno += 1

      # Recurse into the children
      for i, child in enumerate(node.children):
          new_number_str = number_str + str(i+1) + "."
          new_name_str = name_str + (node.name + '.' if node.name != '' else '')
          lineno = TaxonomyTree.print_internal(child, lineno, new_number_str, new_name_str)

      return lineno

  def print(self):
    TaxonomyTree.print_internal(self.root,1,"","")

  @staticmethod
  def listScientificNames_internal(node):

    if len(node.children) == 0:
      return [node.name]
    
    names = []

    for child in node.children:
      names.extend(TaxonomyTree.listScientificNames_internal(child))
    
    return names

  def printScientificNames(self):
    names = TaxonomyTree.listScientificNames_internal(self.root)
    names.sort()
    for name in names:
      print(name)

#------------------------------------------

def main():
  # Read the Pandas dataframe
  df = pd.read_csv("ClassesAndRecursion/taxonomy.csv")
  rows = df.shape[0]
  cols = df.shape[1]
  categories = list(df.columns)[1:cols]

  # Construct a Taxonomy Tree
  tree = TaxonomyTree()

  # Insert species into the tree row by row
  for r in range(rows):
    names = list(df.iloc[r,1:cols])
    tree.addSpecies(names,categories)

  # Print the contents of the TaxonomyTree
  tree.print()

  # Extra Credit: print all scientific names in alphabetical order
  tree.printScientificNames()

#------------------------------------------

main()
