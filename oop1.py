"""
You are going to model a Forest with rain and a lumberjack who cuts tall trees.

Tree
Trees should have a height.
We should be able to create trees in two ways:
providing height
not providing height, in this case the height will be 0 by default.
It has an irrigate method which will increase the height of the tree. The implementation should depend on the type of the tree.
It has a getHeight method which returns the tree's height.
WhitebarkPine
This tree type grows by 2 units each time its irrigated.
FoxtailPine
This tree type grows by 1 unit each time its irrigated.
Lumberjack
You should be able to create a lumberjack without providing any parameters.

It has a canCut(tree) method which takes a tree as parameter and returns true if its taller than 4 units.
Forest
The Forest has Trees.
We should be able to create a forest by providing a list of trees.
It should have a getTrees() method returning every Tree in the Forest.
It has a rain() method which should irrigate every Tree in the Forest.
It has a cutTrees(lumberjack) which should remove all the trees which can be cut by the lumberjack. (It calls the canCut method on the lumberjack).
It has an isEmpty method which returns true if there is no tree in the forest.
It has a getStatus method which returns an array/list with status reports about each tree in the forest. For example:
[
  'There is a 3 tall WhitebarkPine in the forest.',
  'There is a 2 tall WhitebarkPine in the forest.',
  'There is a 4 tall FoxtailPine in the forest.'
]

Sample code to run
Using your solution, the following code should run without errors and print the expected results.


whitebark1 = WhitebarkTree()
whitebark2 = WhitebarkTree(5)
foxtail1 = FoxtailPine()
foxtail2 = FoxtailPine(4)
jack = Lumberjack()
hundred_acre_wood = Forest([whitebark1, whitebark2, foxtail1, foxtail2])
print(hundred_acre_wood.is_empty())
print(whitebark1.get_height())  # Should print: 0
print(whitebark2.get_height())  # Should print: 5
print(hundred_acre_wood.get_status()) # Should print: ['There is a 0 tall FoxtailPine in the forest.', 'There is a 5 tall FoxtailPine in the forest.', 'There is a 0 tall FoxtailPine in the forest.', 'There is a 4 tall FoxtailPine in the forest.']
hundred_acre_wood.cut_trees(jack)
print(hundred_acre_wood.get_status()) # Should print: ['There is a 0 tall FoxtailPine in the forest.', 'There is a 0 tall FoxtailPine in the forest.', 'There is a 4 tall FoxtailPine in the forest.']
hundred_acre_wood.rain()
hundred_acre_wood.cut_trees(jack)
print(hundred_acre_wood.get_status()) # Should print: ['There is a 2 tall FoxtailPine in the forest.', 'There is a 1 tall FoxtailPine in the forest.']
print(hundred_acre_wood.is_empty()) #Should print: False
"""

class Tree:
    def __init__(self, height=0):
        self.height = height

    def irrigate(self):
        pass

    def get_height(self):
        return self.height
    
class WhitebarkPine(Tree):
    def irrigate(self):
        self.height += 2

class FoxtailPine(Tree):
    def irrigate(self):
        self.height += 1

class Lumberjack:
    def can_cut(self, tree):
        return tree.get_height() > 4
    
class Forest:
    def __init__(self, trees):
        self.trees = trees

    def get_trees(self):
        return self.trees

    def rain(self):
        for tree in self.trees:
            tree.irrigate()

    def cut_trees(self, lumberjack):
        self.trees = [tree for tree in self.trees if not lumberjack.can_cut(tree)]

    def is_empty(self):
        return len(self.trees) == 0

    def get_status(self):
        return [f'There is a {tree.get_height()} tall {type(tree).__name__} in the forest.' for tree in self.trees]
    
whitebark1 = WhitebarkPine()
whitebark2 = WhitebarkPine(5)
foxtail1 = FoxtailPine()
foxtail2 = FoxtailPine(4)
jack = Lumberjack()
hundred_acre_wood = Forest([whitebark1, whitebark2, foxtail1, foxtail2])
print(hundred_acre_wood.is_empty())
print(whitebark1.get_height())  # Should print: 0
print(whitebark2.get_height())  # Should print: 5
print(hundred_acre_wood.get_status()) # Should print: ['There is a 0 tall FoxtailPine in the forest.', 'There is a 5 tall FoxtailPine in the forest.', 'There is a 0 tall FoxtailPine in the forest.', 'There is a 4 tall FoxtailPine in the forest.']
hundred_acre_wood.cut_trees(jack)
print(hundred_acre_wood.get_status()) # Should print: ['There is a 0 tall FoxtailPine in the forest.', 'There is a 0 tall FoxtailPine in the forest.', 'There is a 4 tall FoxtailPine in the forest.']
hundred_acre_wood.rain()
hundred_acre_wood.cut_trees(jack)
print(hundred_acre_wood.get_status()) # Should print: ['There is a 2 tall FoxtailPine in the forest.', 'There is a 1 tall FoxtailPine in the forest.']
print(hundred_acre_wood.is_empty()) #Should print: False


