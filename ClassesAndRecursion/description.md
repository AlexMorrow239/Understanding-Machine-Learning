# Understanding Python Classes and Recursion with a Taxonomy Tree Example

In this blog post, we'll delve into two fundamental concepts in Python programming: classes and recursion. By examining a practical example—a script that constructs and manipulates a taxonomy tree—we'll see how these concepts can be applied to manage complex data structures effectively.

## Python Classes

Python classes provide a way to bundle data and functionality together. By defining classes, we can create more complicated data structures that encapsulate both data and operations on that data. Let's look at the classes defined in our example script.

### TaxonomyNode Class

The `TaxonomyNode` class represents a node in a taxonomy tree. Each node holds information about a biological classification such as "Animalia" or "Chordata."

```python
class TaxonomyNode:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.children = []

    def addChild(self, name, category):
        newChild = TaxonomyNode(name, category)
        self.children.append(newChild)
        self.children.sort(key=lambda x: x.name)

    def hasChild(self, name, category):
        return any(child.name == name and child.category == category for child in self.children)

    def getChild(self, name, category):
        for child in self.children:
            if child.name == name and child.category == category:
                return child
        return None
```

### TaxonomyTree Class

The `TaxonomyTree` class manages the entire taxonomy tree, starting from a root node which is initially empty.

```python
class TaxonomyTree:
    def __init__(self):
        self.root = TaxonomyNode("", "")

    def addSpecies(self, names, categories):
        current = self.root
        for name, category in zip(names, categories):
            if not current.hasChild(name, category):
                current.addChild(name, category)
            current = current.getChild(name, category)

    def print(self):
        self._print_internal(self.root, 1, "", "")
```

## Recursion

Recursion is a method where a function calls itself to solve smaller instances of the same problem. In our script, recursion is used to navigate and manipulate the taxonomy tree.

### Recursive Operations

- **Printing the Tree:** The tree is printed using a recursive method that navigates through all nodes and formats their display based on their depth in the tree.

```python
def _print_internal(self, node, lineno, number_str, name_str):
    if node.name:
        print(f"{lineno:<10}{number_str:<30} {name_str}{node.name}.")
        lineno += 1
    for i, child in enumerate(node.children):
        new_number_str = number_str + str(i+1) + "."
        new_name_str = name_str + (node.name + '.' if node.name else '')
        lineno = self._print_internal(child, lineno, new_number_str, new_name_str)
    return lineno
```

- **Listing Names:** Another recursive method collects and prints all names stored in the tree.

```python
def _listScientificNames_internal(self, node):
    if not node.children:
        return [node.name]
    names = []
    for child in node.children:
        names.extend(self._listScientificNames_internal(child))
    return names
```

## Conclusion

This script showcases how Python classes can be used to model complex structures like a biological taxonomy tree, while recursion helps in efficiently performing operations that require traversing or manipulating these structures. By combining these two powerful concepts, the script manages a hierarchical data model effectively, demonstrating the practical application of object-oriented programming and recursive algorithms in Python.

## Running The Project

All you need to run this project is a taxonomy.csv file (like the one on this repository) in the working directory.

There are no dependencies required for this script.

Simply run Python directly from the terminal:

```bash
python ClassesAndRecursion.py
```
