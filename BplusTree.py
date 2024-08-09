# This is the beginning of a Python translation of the JAVA
# code which is embedded in triple-quoted string comments below.
# Your task is to finish the translation.

''' Java version:    
    class BTreeNode {
        public int keys[];
        public BTreeNode children[];
        public int numKeys = 1; 
        public boolean isLeaf = true;
        public BTreeNode parent = null;
        public BTreeNode next = null;

        public BTreeNode() {
            keys = new int[treeDegree];
            children = new BTreeNode[treeDegree+1];
        }
    }
'''
class BTreeNode:

    # This isn't nested in the BPlusTree class, so in this 
    # implementation, the constructor needs to be passed the degree
    # Calls to the constructor need to be altered (see fill)
    def __init__(this, degree):  # constructor for the nodes
        this.keys = [None for number in range(degree)]
        this.children = [None for number in range(degree+1)]
        this.numKeys = 1
        this.isLeaf = True
        this.parent = None
        this.next = None

''' Java version
A single-file implementation of a B+Tree

import java.util.Scanner;

public class BPlusTree {

        private int treeDegree = 3;
        private BTreeNode treeRoot = null;
    
'''
class BPlusTree:

    ''' Java version
        public BPlusTree(int degree) {
            treeDegree = degree;
        }
    '''
    def __init__(self,degree=3): # constructor for the tree
        self.treeDegree = degree
        self.treeRoot = None


    ''' No Java equivalent for fill '''
    def fill(self): # this is just for testing the show function
        # but notice how every use of treeRoot requires self.
        self.treeRoot = BTreeNode(self.treeDegree)
        self.treeRoot.keys = [4,9,None,None,None]
        self.treeRoot.numKeys = 2
        self.treeRoot.isLeaf = False
        self.treeRoot.children[0] = BTreeNode(self.treeDegree)
        self.treeRoot.children[0].keys = [1,2,3,None,None]
        self.treeRoot.children[0].numKeys = 3
        self.treeRoot.children[0].parent = self.treeRoot
        self.treeRoot.children[1] = BTreeNode(self.treeDegree)
        self.treeRoot.children[1].keys = [4,6,None,None,None]
        self.treeRoot.children[1].numKeys = 2
        self.treeRoot.children[1].parent = self.treeRoot
        self.treeRoot.children[2] = BTreeNode(self.treeDegree)
        self.treeRoot.children[2].keys = [9,10,11,12,None]
        self.treeRoot.children[2].numKeys = 4
        self.treeRoot.children[2].parent = self.treeRoot
        self.treeRoot.children[0].next = self.treeRoot.children[1]
        self.treeRoot.children[1].next = self.treeRoot.children[2]


    ''' Java version
        private int max_keys() {
            return treeDegree - 1;
        }
    '''
    def max_keys(self): # self gets used often in Python
        return self.treeDegree - 1


    ''' Java version
        private int min_keys() {
            return (int)((treeDegree + 1) / 2) - 1;
        }
    '''
    def min_keys(self): # note the integer division operator
        return ((self.treeDegree + 1) // 2) - 1


    ''' Java version
        private int split_index() {
            return (int)(treeDegree / 2);
        }
    '''
    def split_index(self):
        return self.treeDegree // 2


    ''' Java version
        public void clear() {
            deleteTree(treeRoot);
            treeRoot = null;
        }
    '''
    # ToDo
    def clear(self):
        self.deleteTree(self.treeRoot)
        self.treeRoot = None


    ''' Java version
        private void deleteTree(BTreeNode tree) {
            if (tree != null) {
                if (!tree.isLeaf) {
                    for (int i = 0; i <= tree.numKeys; i++) {
                        deleteTree(tree.children[i]);
                        tree.children[i] = null;
                    }
                }
            }
        }
    '''
    # ToDo
    def deleteTree(self, tree):
        if tree != None:
            if tree.isLeaf == False:
                for i in range(tree.numKeys):
                    self.deleteTree(tree.children[i])
                    tree.children[i] = None


    ''' Java version
        public void show() {
            BTreeNode tree = treeRoot;
            int height = 1;
            while (tree != null) {
                tree = tree.children[0];
                height++;
            }
            String lines[] = new String[height];
            for (int i = 0; i < height; i++) {
                lines[i] = "";
            }
            lines = showTree(treeRoot, 0, lines);
            for (int i = 0; i < height; i++) {
                System.out.println(lines[i]);
            }
        }
    '''
    def show(self): # output the tree in a readable form
        tree = self.treeRoot
        height = 1
        while tree != None:
            tree = tree.children[0]
            height = height + 1
        lines = ["" for number in range(height)]
        lines = self.showTree(self.treeRoot, 0, lines)
        for i in range(height):
            print(lines[i])


    ''' Java version
        private String[] showTree(BTreeNode tree, int level, String lines[]) {
            if (tree != null) {
                for (int i = 0; i < tree.numKeys; i++) {
                    if (!tree.isLeaf)
                        lines = showTree(tree.children[i], level + 1, lines);
                    int lenChildren = 0;
                    for (int j = level + 1; j < lines.length; j++) {
                        lenChildren = Integer.max(lenChildren, lines[j].length());
                    }
                    if (i == 0) 
                        lenChildren = lenChildren - 1;
                    String lenChild = Integer.toString(Integer.min(-1,-lenChildren+4));
                    String leftEdge = "";
                    String rightEdge = "";
                    if (i == 0)
                        leftEdge = "[ ";
                    if (i == tree.numKeys - 1)
                        rightEdge = " ]    ";
                    lines[level] = String.format("%"+lenChild+"s%s%d%s ",lines[level], leftEdge, tree.keys[i], rightEdge);
                }
                if (!tree.isLeaf)
                    lines = showTree(tree.children[tree.numKeys], level + 1, lines);
            }
            return lines;
        }
    '''
    def showTree(self, tree, level, lines):
        if tree != None:
            for i in range(tree.numKeys):
                if not tree.isLeaf:
                    lines = self.showTree(tree.children[i], level + 1, lines)
                lenChildren = 0
                for j in range(level + 1, len(lines)):
                    lenChildren = max(lenChildren, len(lines[j]))
                if i == 0:
                    lenChildren = lenChildren - 1;
                lenChild = str(min(-1,-lenChildren+4))
                leftEdge = ""
                rightEdge = ""
                if i == 0:
                    leftEdge = "[ "
                if i == tree.numKeys - 1:
                    rightEdge = " ]    "
                lines[level] = ("%"+lenChild+"s%s%d%s ") % (lines[level], leftEdge, tree.keys[i], rightEdge)
            if not tree.isLeaf:
                lines = self.showTree(tree.children[tree.numKeys], level + 1, lines)
        return lines


    ''' Java version
        public void insert(int val) {
            if (treeRoot == null) {
                treeRoot = new BTreeNode();
                treeRoot.keys[0] = val;
            } else {
                insertIntoTree(treeRoot, val);                    
            }
        }
    '''
    #ToDo
    def insert(self, val):
        if self.treeRoot == None:
            self.treeRoot = BTreeNode(self.treeDegree)
            self.treeRoot.keys[0] = val
        else:
            self.insertIntoTree(self.treeRoot, val)

    ''' Java version
        private void insertIntoTree(BTreeNode tree, int insertValue) {
            if (tree.isLeaf) {
                int insertIndex = tree.numKeys;
                tree.numKeys++;
                while (insertIndex > 0 && tree.keys[insertIndex - 1] > insertValue) {
                    tree.keys[insertIndex] = tree.keys[insertIndex - 1];
                    insertIndex--;
                }
                tree.keys[insertIndex] = insertValue;
                insertRepair(tree);
            } else {
                int findIndex = 0;
                while (findIndex < tree.numKeys && tree.keys[findIndex] < insertValue) {
                    findIndex++;                    
                }                
                insertIntoTree(tree.children[findIndex], insertValue);                
            }
        }
    '''
    #ToDo
    def insertIntoTree(self, tree, insertValue):
        if tree.isLeaf == True:
            insertIndex = tree.numKeys
            tree.numKeys+=1
            while insertIndex > 0 and tree.keys[insertIndex - 1] > insertValue:
                tree.keys[insertIndex] = tree.keys[insertIndex - 1]
                insertIndex -= 1
            tree.keys[insertIndex] = insertValue
            self.insertRepair(tree)
        else:
            findIndex = 0
            while findIndex < tree.numKeys and tree.keys[findIndex] < insertValue:
                findIndex += 1
            self.insertIntoTree(tree.children[findIndex], insertValue)



    ''' Java version
        private void insertRepair(BTreeNode tree) {
            if (tree.numKeys <= max_keys()) {
                return;
            } else if (tree.parent == null) {
                treeRoot = splitNode(tree);
                return;
            } else {
                insertRepair(splitNode(tree));
            }            
        }
    '''
    #ToDo
    def insertRepair(self, tree):
        if tree.numKeys <=self.max_keys():
            return
        elif tree.parent == None:
            self.treeRoot = self.splitNode(tree)
            return
        else:
            self.insertRepair(self.splitNode(tree))



    ''' Java version
        private BTreeNode splitNode(BTreeNode tree) {
            BTreeNode rightNode = new BTreeNode();
            
            int risingNode = tree.keys[split_index()];
            
            int i;
            int parentIndex;
            if (tree.parent != null) {
                BTreeNode currentParent = tree.parent;
                for (parentIndex = 0; parentIndex < currentParent.numKeys + 1 && currentParent.children[parentIndex] != tree; parentIndex++);
                if (parentIndex == currentParent.numKeys + 1) {
                    throw new Error("Couldn't find which child we were!");
                }
                for (i = currentParent.numKeys; i > parentIndex; i--) {
                    currentParent.children[i+1] = currentParent.children[i];
                    currentParent.keys[i] = currentParent.keys[i-1];
                }
                currentParent.numKeys++;
                currentParent.keys[parentIndex] = risingNode;
                currentParent.children[parentIndex+1] = rightNode;
                rightNode.parent = currentParent;
            }
            
            int rightSplit = split_index() + 1;
            
            if (tree.isLeaf) {
                rightSplit = split_index();
                rightNode.next = tree.next;
                tree.next = rightNode;
            }
            
            rightNode.numKeys = tree.numKeys - rightSplit;
            
            for (i = rightSplit; i < tree.numKeys + 1; i++) {
                rightNode.children[i - rightSplit] = tree.children[i];
                if (tree.children[i] != null) {
                    rightNode.isLeaf = false;
                    if (tree.children[i] != null) {
                        tree.children[i].parent = rightNode;
                    }
                    tree.children[i] = null;
                }
            }
            for (i =rightSplit; i < tree.numKeys; i++) {
                rightNode.keys[i - rightSplit] = tree.keys[i];
            }
            BTreeNode leftNode = tree;
            leftNode.numKeys = split_index();
            if (tree.parent != null) {
                return tree.parent;
            } else {
                treeRoot = new BTreeNode();
                treeRoot.keys[0] = risingNode;
                treeRoot.children[0] = leftNode;
                treeRoot.children[1] = rightNode;
                leftNode.parent = treeRoot;
                rightNode.parent = treeRoot;
                treeRoot.isLeaf = false;
                return treeRoot;
            }
        }
    '''
    #ToDo
    def splitNode(self, tree):
        rightNode = BTreeNode(self.treeDegree)
        risingNode = tree.keys[self.split_index()]

        i = int()
        parentIndex = int()
        if tree.parent:
            currentParent = tree.parent
            while parentIndex < currentParent.numKeys + 1 and currentParent.children[parentIndex] != tree:
                parentIndex += 1
            if parentIndex == currentParent.numKeys + 1:
                Exception('Couldn\'t find which child we were!')
            for i in range(currentParent.numKeys, parentIndex, -1):
                currentParent.children[i+1] = currentParent.children[i]
                currentParent.keys[i] = currentParent.keys[i-1]
            currentParent.numKeys += 1
            currentParent.keys[parentIndex] = risingNode
            currentParent.children[parentIndex+1] = rightNode
            rightNode.parent = currentParent

        rightSplit = self.split_index() + 1

        if tree.isLeaf:
            rightSplit = self.split_index()
            rightNode.next = tree.next
            tree.next = rightNode

        rightNode.numKeys = tree.numKeys - rightSplit

        for i in range(rightSplit, tree.numKeys + 1):
            rightNode.children[i - rightSplit] = tree.children[i]
            if tree.children[i]:
                rightNode.isLeaf = False
                if tree.children[i]:
                    tree.children[i].parent = rightNode
                tree.children[i] = None
        for i in range(rightSplit, tree.numKeys):
            rightNode.keys[i - rightSplit] = tree.keys[i]
        leftNode = tree
        leftNode.numKeys = self.split_index()
        if tree.parent:
            return tree.parent
        else:
            self.treeRoot = BTreeNode(self.treeDegree)
            self.treeRoot.keys[0] = risingNode
            self.treeRoot.children[0] = leftNode
            self.treeRoot.children[1] = rightNode
            leftNode.parent = self.treeRoot
            rightNode.parent = self.treeRoot
            self.treeRoot.isLeaf = False
            return self.treeRoot






    ''' Java version
        public void delete(int val)
        {
            deleteFromTree(treeRoot, val);
            if (treeRoot.numKeys == 0) {
                treeRoot = treeRoot.children[0];
                treeRoot.parent = null;
            }
        }
    '''
    #ToDo
    def delete(self, val):
        self.deleteFromTree(self.treeRoot, val)
        if self.treeRoot.numKeys == 0:
            self.treeRoot = treeRoot.children[0]
            if self.treeRoot.parent != None:
                self.treeRoot.parent = None

    ''' Java version
        private void deleteFromTree(BTreeNode tree, int val) {
            if (tree != null) {
                int i;
                for (i = 0; i < tree.numKeys && tree.keys[i] < val; i++);
                if (i == tree.numKeys) {
                    if (!tree.isLeaf) {
                        deleteFromTree(tree.children[tree.numKeys], val);
                    }
                } else if (!tree.isLeaf && tree.keys[i] == val) {
                    deleteFromTree(tree.children[i+1], val);
                } else if (!tree.isLeaf) {
                    deleteFromTree(tree.children[i], val);            
                } else if (tree.isLeaf && tree.keys[i] == val) {
                    for (int j = i; j < tree.numKeys - 1; j++) {
                        tree.keys[j] = tree.keys[j+1];
                    }
                    tree.numKeys--;
                    
                    // Bit of a hack -- if we remove the smallest element in a leaf, then find the *next* smallest element
                    //  (somewhat tricky if the leaf is now empty!), go up our parent stack, and fix index keys
                    if (i == 0 && tree.parent != null) {
                        int nextSmallest = Integer.MIN_VALUE;
                        BTreeNode parentNode = tree.parent;
                        int parentIndex;
                        for (parentIndex = 0; parentNode.children[parentIndex] != tree; parentIndex++);
                        if (tree.numKeys == 0) {
                            if (parentIndex == parentNode.numKeys) {
                                nextSmallest = Integer.MIN_VALUE;
                            } else {
                                nextSmallest = parentNode.children[parentIndex+1].keys[0];            
                            }
                        } else {
                            nextSmallest = tree.keys[0];
                        }
                        while (parentNode != null) {
                            if (parentIndex > 0 && parentNode.keys[parentIndex - 1] == val) {
                                parentNode.keys[parentIndex - 1] = nextSmallest;
                            }
                            BTreeNode grandParent = parentNode.parent;
                            for (parentIndex = 0; grandParent != null && grandParent.children[parentIndex] != parentNode; parentIndex++);
                            parentNode = grandParent;
                            
                        }
                    }
                    repairAfterDelete(tree);
                }
            }
        }
    '''
    #ToDo
    #nextSmallest = -inf
    def deleteFromTree(self, tree, val):
        if tree != None:
            i = 0
            while i < tree.numKeys and tree.keys[i] < val:
                i += 1
            if i == tree.numKeys:
                if not tree.isLeaf:
                    self.deleteFromTree(tree.children[tree.numKeys], val)
            elif not tree.isLeaf and tree.keys[i] == val:
                self.deleteFromTree(tree.children[i+1], val)
            elif not tree.isLeaf:
                self.deleteFromTree(tree.children[i], val)
            elif tree.isLeaf and tree.keys[i] == val:
                j = i
                while j < (tree.numKeys - 1):
                    tree.keys[j] = tree.keys[j+1]
                    j += 1
                tree.numKeys -= 1
                if i == 0 and tree.parent != None:
                    nextSmallest = -2147483648
                    parentNode = tree.parent
                    parentIndex = 0
                    while parentNode.children[parentIndex] != tree:
                        parentIndex += 1
                    if tree.numKeys == 0:
                        if parentIndex == parentNode.numKeys:
                            nextSmallest = -2147483648
                        else:
                            nextSmallest = parentNode.children[parentIndex+1].keys[0]
                    else:
                        nextSmallest = tree.keys[0]
                    while parentNode != None:
                        if parentIndex > 0 and parentNode.keys[parentIndex - 1] == val:
                            parentNode.keys[parentIndex - 1] = nextSmallest
                        grandParent = parentNode.parent
                        parentIndex = 0
                        while grandParent != None and grandParent.children[parentIndex] != parentNode:
                            parentIndex += 1
                        parentNode = grandParent
                self.repairAfterDelete(tree)



    ''' Java version
        private BTreeNode mergeRight(BTreeNode tree) 
        {
            BTreeNode parentNode = tree.parent;
            int parentIndex = 0;
            for (parentIndex = 0; parentNode.children[parentIndex] != tree; parentIndex++);
            BTreeNode rightSib = parentNode.children[parentIndex+1];
            
            if (!tree.isLeaf) {
                tree.keys[tree.numKeys] = parentNode.keys[parentIndex];
            }
            
            int i;
            for (i = 0; i < rightSib.numKeys; i++) {
                int insertIndex =  tree.numKeys + 1 + i;
                if (tree.isLeaf) {
                    insertIndex -= 1;
                }
                tree.keys[insertIndex] = rightSib.keys[i];
            }
            if (!tree.isLeaf) {
                for (i = 0; i <= rightSib.numKeys; i++) {
                    tree.children[tree.numKeys + 1 + i] = rightSib.children[i];
                    tree.children[tree.numKeys + 1 + i].parent = tree;
                }
                tree.numKeys = tree.numKeys + rightSib.numKeys + 1;
            } else {
                tree.numKeys = tree.numKeys + rightSib.numKeys;
                tree.next = rightSib.next;
            }
            for (i = parentIndex+1; i < parentNode.numKeys; i++) {
                parentNode.children[i] = parentNode.children[i+1];
                parentNode.keys[i-1] = parentNode.keys[i];
            }
            parentNode.numKeys--;
            
            return tree;
        }
    '''
    #ToDo
    def mergeRight(self, tree):
        parentNode = tree.parent
        parentIndex = 0
        while parentNode.children[parentIndex] != tree:
            parentIndex+=1
        rightSib = parentNode.children[parentIndex+1]
        if tree.isLeaf == False:
            tree.keys[tree.numKeys] = parentNode.keys[parentIndex]
        for i in range(rightSib.numKeys):
            insertIndex = tree.numKeys + 1 + i
            if tree.isLeaf == True:
                insertIndex -= 1
            tree.keys[insertIndex] = rightSib.keys[i]
        if tree.isLeaf == False:
            for i in range(rightSibNumKeys + 1):
                tree.chldren[tree.numKeys + 1 + i] = rightSib.children[i]
                tree.children[tree.numkeys + 1+ i].parent = tree
            tree.numKeys = tree.numKeys + rightSib.numKeys + 1
        else:
            tree.numKeys = tree.nmKeys + rightSib.numKeys
            tree.next = rightSib.next
        for i in range((parentIndex+1), parentNode.numKeys):
            parentNode.children[i] = parentNode.children[i+1]
            parentnode.keys[i-1] = parentNode.keys[i]
        parentNode.numKeys-=1
        return tree


    ''' Java version
        private BTreeNode stealFromRight(BTreeNode tree, int parentIndex) 
        {
            // Steal from right sibling
            BTreeNode parentNode = tree.parent;
            
            BTreeNode rightSib = parentNode.children[parentIndex + 1];
            tree.numKeys++;
            
            if (tree.isLeaf) {
                tree.keys[tree.numKeys - 1] = rightSib.keys[0];
                parentNode.keys[parentIndex] = rightSib.keys[1];
            } else {
                tree.keys[tree.numKeys - 1] = parentNode.keys[parentIndex];
                parentNode.keys[parentIndex] = rightSib.keys[0];
            }
            
            if (!tree.isLeaf) {
                tree.children[tree.numKeys] = rightSib.children[0];
                tree.children[tree.numKeys].parent = tree;
                
                for (int i = 1; i < rightSib.numKeys + 1; i++) {
                    rightSib.children[i-1] = rightSib.children[i];
                }
                
            }
            for (int i = 1; i < rightSib.numKeys; i++) {
                rightSib.keys[i-1] = rightSib.keys[i];
            }
            rightSib.numKeys--;
            
            return tree;
            
        }
    '''
    #ToDo
    def stealfromRight(self, tree, parentIndex):
        parentNode = tree.parent
        rightSib = self.parentNode.children[parentIndex + 1]
        tree.numKeys+=1
        if tree.isLeaf == True:
            tree.keys[tree.numKeys - 1] = rightSib.keys[0]
            parentNode.keys[parentIndex] = rightSib.keys[0]
        if tree.isLeaf == False:
            tree.children[tree.numKeys] = rightSib.children[0]
            tree.children[tree.numKeys].parent = tree
            for i in range(1, (rightSib.numKeys + 1)):
                rightSib.children[i-1] = rightSib.children[i]
        for i in range(1, rightSib.numKeys):
            rightSib.keys[i-1] = rightSib.keys[i]
        rightSib.numKeys-=1
        return tree



    ''' Java version
        private BTreeNode stealFromLeft(BTreeNode tree, int parentIndex) {
            BTreeNode parentNode = tree.parent;
            // Steal from left sibling
            tree.numKeys++;
            
            for (int i = tree.numKeys - 1; i > 0; i--) {
                tree.keys[i] = tree.keys[i-1];
            }
            BTreeNode leftSib = parentNode.children[parentIndex -1];
            
            if (tree.isLeaf) {
                tree.keys[0] = leftSib.keys[leftSib.numKeys - 1];
                parentNode.keys[parentIndex-1] = leftSib.keys[leftSib.numKeys - 1];
            } else {
                tree.keys[0] = parentNode.keys[parentIndex - 1];
                parentNode.keys[parentIndex-1] = leftSib.keys[leftSib.numKeys - 1];                
            }

            if (!tree.isLeaf) {
                for (int i = tree.numKeys; i > 0; i--) {
                    tree.children[i] = tree.children[i-1];
                }
                tree.children[0] = leftSib.children[leftSib.numKeys];
                leftSib.children[leftSib.numKeys] = null;
                tree.children[0].parent = tree;
            }
            
            leftSib.numKeys--;
            
            return tree;
        }
    '''
    #ToDo
    def stealFromLeft(self, tree, parentIndex):
        parentNode = tree.parent
        tree.numKeys+=1
        i = tree.numKeys
        while i > 0:
            tree.keys[i] = tree.keys[i-1]
            i-=1
        leftSib = parentNode.children[parentIndex - 1]
        if tree.isLeaf == True:
            tree.keys[0] = leftSib.keys[leftSib.numKeys - 1]
            parentNode.keys[parentIndex-1] = leftSib.keys[leftSib.numKeys-1]
        else:
            tree.keys[0] = parentNode.keys[parentIndex - 1]
            parentNode.keys[parentIndex-1] = leftSib.keys[leftSib.numKeys - 1]
        if tree.isLeaf == False:
            i = tree.numKeys
            while i > 0:
                tree.children[i] = tree.children[i-1]
            tree.children[0] = leftSib.children[leftSib.numKeys]
            leftSib.children[leftSib.numkeys] = None
            tree.children[0].parent = tree
        leftSib.numKeys-=1
        return tree


    ''' Java version
        private void repairAfterDelete(BTreeNode tree)
        {
            if (tree.numKeys < min_keys()) {
                if (tree.parent == null) {
                    if (tree.numKeys == 0) {
                        treeRoot = tree.children[0];
                        if (treeRoot != null)
                            treeRoot.parent = null;
                    }
                } else {
                    BTreeNode parentNode = tree.parent;
                    int parentIndex;
                    for (parentIndex = 0; parentNode.children[parentIndex] != tree; parentIndex++);
                    if (parentIndex > 0 && parentNode.children[parentIndex - 1].numKeys > min_keys()) {
                        stealFromLeft(tree, parentIndex);
                    } else if (parentIndex < parentNode.numKeys && parentNode.children[parentIndex + 1].numKeys > min_keys()) {
                        stealFromRight(tree,parentIndex);
                    } else if (parentIndex == 0) { // Merge with right sibling
                        BTreeNode nextNode = mergeRight(tree);
                        repairAfterDelete(nextNode.parent);            
                    } else { // Merge with left sibling
                        BTreeNode nextNode = mergeRight(parentNode.children[parentIndex-1]);
                        repairAfterDelete(nextNode.parent);            
                    }
                }
            }
        }
    }
    '''
    #ToDo
    def repairAfterDelete(self, tree):
        if tree.numKeys < self.min_keys():
            if tree.parent == None:
                if tree.numKeys == 0:
                    treeRoot = tree.children[0]
                    if treeRoot != None:
                        treeRoot.parent = null

                else:
                    parentNode = tree.parent
                    parentIndex = 0
                    while parentNode.children[parentIndex] != tree:
                        parentIndex+=1
                    if parentIndex > 0 and parentNode.children[parentIndex - 1].numKeys > self.min_keys():
                        selff.stealFromLeft(tree, parentIndex)
                    elif parentIndex < parentNode.numkeys and parentNode.children[parentIndex + 1].numKeys > self.min_keys():
                       self.stealFromRight(tree, parentIndex)
                    elif parentIndex == 0:
                        nextNode = self.mergeRight(tree)
                        self.repairAfterDelete(nextNode.parent)
                    else:
                        nextNode = self.mergeRight(parentNode.children[parentIndex-1])
                        self.repairAfterDelete(nextNode.parent)

''' Java version
    public static void main(String[] args) {

        BPlusTree myTree = new BPlusTree(5);

        System.out.println("Enter numbers to insert values, Enter D followed by a number to delete a value.");
        Scanner scanner = new Scanner(System.in);
        String data = scanner.nextLine();
        while (data.length() > 0) {
            if(data.matches("\\d+")) {
                int val = Integer.decode(data);
                myTree.insert(val);
            } else if (data.matches("D\\d+")) {
                int val = Integer.decode(data.substring(1));
                myTree.delete(val);
            }
            myTree.show();
            System.out.println();
            data = scanner.nextLine();
        }
        scanner.close();
    }
'''
#ToDo

myTree = BPlusTree(5)
print("Enter Numbers to insert values, Enter D followed by number to delete a value.")
data = "hi"
while len(data) > 0:
    data = input("Enter: ")
    if data.isdigit():
        myTree.insert(int(data))
    elif data[1:].isdigit():
        myTree.delete(int(data[1:]))
    myTree.show()
print("\n")


''' --------------------------------------------------------------------------------- 
    Here's the complete version of the Java code without interruptions.

A single-file implementation of a B+Tree

import java.util.Scanner;

public class BPlusTree {

    private int treeDegree = 3;
    private BTreeNode treeRoot = null;
    
    public BPlusTree(int degree) {
        treeDegree = degree;
    }
    
    class BTreeNode {
        public int keys[];
        public BTreeNode children[];
        public int numKeys = 1; 
        public boolean isLeaf = true;
        public BTreeNode parent = null;
        public BTreeNode next = null;

        public BTreeNode() {
            keys = new int[treeDegree];
            children = new BTreeNode[treeDegree+1];
        }
    }
    
    private int max_keys() {
        return treeDegree - 1;
    }
    private int min_keys() {
        return (int)((treeDegree + 1) / 2) - 1;
    }
    private int split_index() {
        return (int)(treeDegree / 2);
    }

    public void clear() {
        deleteTree(treeRoot);
        treeRoot = null;
    }

    private void deleteTree(BTreeNode tree) {
        if (tree != null) {
            if (!tree.isLeaf) {
                for (int i = 0; i <= tree.numKeys; i++) {
                    deleteTree(tree.children[i]);
                    tree.children[i] = null;
                }
            }
        }
    }
    

    public void show() {
        BTreeNode tree = treeRoot;
        int height = 1;
        while (tree != null) {
            tree = tree.children[0];
            height++;
        }
        String lines[] = new String[height];
        for (int i = 0; i < height; i++) {
            lines[i] = "";
        }
        lines = showTree(treeRoot, 0, lines);
        for (int i = 0; i < height; i++) {
            System.out.println(lines[i]);
        }
    }

    private String[] showTree(BTreeNode tree, int level, String lines[]) {
        if (tree != null) {
            for (int i = 0; i < tree.numKeys; i++) {
                if (!tree.isLeaf)
                    lines = showTree(tree.children[i], level + 1, lines);
                int lenChildren = 0;
                for (int j = level + 1; j < lines.length; j++) {
                    lenChildren = Integer.max(lenChildren, lines[j].length());
                }
                if (i == 0) 
                    lenChildren = lenChildren - 1;
                String lenChild = Integer.toString(Integer.min(-1,-lenChildren+4));
                String leftEdge = "";
                String rightEdge = "";
                if (i == 0)
                    leftEdge = "[ ";
                if (i == tree.numKeys - 1)
                    rightEdge = " ]    ";
                lines[level] = String.format("%"+lenChild+"s%s%d%s ",lines[level], leftEdge, tree.keys[i], rightEdge);
            }
            if (!tree.isLeaf)
                lines = showTree(tree.children[tree.numKeys], level + 1, lines);
        }
        return lines;
    }

    public void insert(int val) {
        if (treeRoot == null) {
            treeRoot = new BTreeNode();
            treeRoot.keys[0] = val;
        } else {
            insertIntoTree(treeRoot, val);                    
        }
    }


    private void insertIntoTree(BTreeNode tree, int insertValue) {
        if (tree.isLeaf) {
            int insertIndex = tree.numKeys;
            tree.numKeys++;
            while (insertIndex > 0 && tree.keys[insertIndex - 1] > insertValue) {
                tree.keys[insertIndex] = tree.keys[insertIndex - 1];
                insertIndex--;
            }
            tree.keys[insertIndex] = insertValue;
            insertRepair(tree);
        } else {
            int findIndex = 0;
            while (findIndex < tree.numKeys && tree.keys[findIndex] < insertValue) {
                findIndex++;                    
            }                
            insertIntoTree(tree.children[findIndex], insertValue);                
        }
    }

    private void insertRepair(BTreeNode tree) {
        if (tree.numKeys <= max_keys()) {
            return;
        } else if (tree.parent == null) {
            treeRoot = splitNode(tree);
            return;
        } else {
            insertRepair(splitNode(tree));
        }            
    }

    private BTreeNode splitNode(BTreeNode tree) {
        BTreeNode rightNode = new BTreeNode();
        
        int risingNode = tree.keys[split_index()];
        
        int i;
        int parentIndex;
        if (tree.parent != null) {
            BTreeNode currentParent = tree.parent;
            for (parentIndex = 0; parentIndex < currentParent.numKeys + 1 && currentParent.children[parentIndex] != tree; parentIndex++);
            if (parentIndex == currentParent.numKeys + 1) {
                throw new Error("Couldn't find which child we were!");
            }
            for (i = currentParent.numKeys; i > parentIndex; i--) {
                currentParent.children[i+1] = currentParent.children[i];
                currentParent.keys[i] = currentParent.keys[i-1];
            }
            currentParent.numKeys++;
            currentParent.keys[parentIndex] = risingNode;
            currentParent.children[parentIndex+1] = rightNode;
            rightNode.parent = currentParent;
        }
        
        int rightSplit = split_index() + 1;
        
        if (tree.isLeaf) {
            rightSplit = split_index();
            rightNode.next = tree.next;
            tree.next = rightNode;
        }
        
        rightNode.numKeys = tree.numKeys - rightSplit;
        
        for (i = rightSplit; i < tree.numKeys + 1; i++) {
            rightNode.children[i - rightSplit] = tree.children[i];
            if (tree.children[i] != null) {
                rightNode.isLeaf = false;
                if (tree.children[i] != null) {
                    tree.children[i].parent = rightNode;
                }
                tree.children[i] = null;
            }
        }
        for (i =rightSplit; i < tree.numKeys; i++) {
            rightNode.keys[i - rightSplit] = tree.keys[i];
        }
        BTreeNode leftNode = tree;
        leftNode.numKeys = split_index();
        if (tree.parent != null) {
            return tree.parent;
        } else {
            treeRoot = new BTreeNode();
            treeRoot.keys[0] = risingNode;
            treeRoot.children[0] = leftNode;
            treeRoot.children[1] = rightNode;
            leftNode.parent = treeRoot;
            rightNode.parent = treeRoot;
            treeRoot.isLeaf = false;
            return treeRoot;
        }
    }

    public void delete(int val)
    {
        deleteFromTree(treeRoot, val);
        if (treeRoot.numKeys == 0) {
            treeRoot = treeRoot.children[0];
            treeRoot.parent = null;
        }
    }


    private void deleteFromTree(BTreeNode tree, int val) {
        if (tree != null) {
            int i;
            for (i = 0; i < tree.numKeys && tree.keys[i] < val; i++);
            if (i == tree.numKeys) {
                if (!tree.isLeaf) {
                    deleteFromTree(tree.children[tree.numKeys], val);
                }
            } else if (!tree.isLeaf && tree.keys[i] == val) {
                deleteFromTree(tree.children[i+1], val);
            } else if (!tree.isLeaf) {
                deleteFromTree(tree.children[i], val);            
            } else if (tree.isLeaf && tree.keys[i] == val) {
                for (int j = i; j < tree.numKeys - 1; j++) {
                    tree.keys[j] = tree.keys[j+1];
                }
                tree.numKeys--;
                
                // Bit of a hack -- if we remove the smallest element in a leaf, then find the *next* smallest element
                //  (somewhat tricky if the leaf is now empty!), go up our parent stack, and fix index keys
                if (i == 0 && tree.parent != null) {
                    int nextSmallest = Integer.MIN_VALUE;
                    BTreeNode parentNode = tree.parent;
                    int parentIndex;
                    for (parentIndex = 0; parentNode.children[parentIndex] != tree; parentIndex++);
                    if (tree.numKeys == 0) {
                        if (parentIndex == parentNode.numKeys) {
                            nextSmallest = Integer.MIN_VALUE;
                        } else {
                            nextSmallest = parentNode.children[parentIndex+1].keys[0];            
                        }
                    } else {
                        nextSmallest = tree.keys[0];
                    }
                    while (parentNode != null) {
                        if (parentIndex > 0 && parentNode.keys[parentIndex - 1] == val) {
                            parentNode.keys[parentIndex - 1] = nextSmallest;
                        }
                        BTreeNode grandParent = parentNode.parent;
                        for (parentIndex = 0; grandParent != null && grandParent.children[parentIndex] != parentNode; parentIndex++);
                        parentNode = grandParent;
                        
                    }
                }
                repairAfterDelete(tree);
            }
        }
    }



    private BTreeNode mergeRight(BTreeNode tree) 
    {
        BTreeNode parentNode = tree.parent;
        int parentIndex = 0;
        for (parentIndex = 0; parentNode.children[parentIndex] != tree; parentIndex++);
        BTreeNode rightSib = parentNode.children[parentIndex+1];
        
        if (!tree.isLeaf) {
            tree.keys[tree.numKeys] = parentNode.keys[parentIndex];
        }
        
        int i;
        for (i = 0; i < rightSib.numKeys; i++) {
            int insertIndex =  tree.numKeys + 1 + i;
            if (tree.isLeaf) {
                insertIndex -= 1;
            }
            tree.keys[insertIndex] = rightSib.keys[i];
        }
        if (!tree.isLeaf) {
            for (i = 0; i <= rightSib.numKeys; i++) {
                tree.children[tree.numKeys + 1 + i] = rightSib.children[i];
                tree.children[tree.numKeys + 1 + i].parent = tree;
            }
            tree.numKeys = tree.numKeys + rightSib.numKeys + 1;
        } else {
            tree.numKeys = tree.numKeys + rightSib.numKeys;
            tree.next = rightSib.next;
        }
        for (i = parentIndex+1; i < parentNode.numKeys; i++) {
            parentNode.children[i] = parentNode.children[i+1];
            parentNode.keys[i-1] = parentNode.keys[i];
        }
        parentNode.numKeys--;
        
        return tree;
    }


    private BTreeNode stealFromRight(BTreeNode tree, int parentIndex) 
    {
        // Steal from right sibling
        BTreeNode parentNode = tree.parent;
        
        BTreeNode rightSib = parentNode.children[parentIndex + 1];
        tree.numKeys++;
        
        if (tree.isLeaf) {
            tree.keys[tree.numKeys - 1] = rightSib.keys[0];
            parentNode.keys[parentIndex] = rightSib.keys[1];
        } else {
            tree.keys[tree.numKeys - 1] = parentNode.keys[parentIndex];
            parentNode.keys[parentIndex] = rightSib.keys[0];
        }
        
        if (!tree.isLeaf) {
            tree.children[tree.numKeys] = rightSib.children[0];
            tree.children[tree.numKeys].parent = tree;
            
            for (int i = 1; i < rightSib.numKeys + 1; i++) {
                rightSib.children[i-1] = rightSib.children[i];
            }
            
        }
        for (int i = 1; i < rightSib.numKeys; i++) {
            rightSib.keys[i-1] = rightSib.keys[i];
        }
        rightSib.numKeys--;
        
        return tree;
        
    }


    private BTreeNode stealFromLeft(BTreeNode tree, int parentIndex) {
        BTreeNode parentNode = tree.parent;
        // Steal from left sibling
        tree.numKeys++;
        
        for (int i = tree.numKeys - 1; i > 0; i--) {
            tree.keys[i] = tree.keys[i-1];
        }
        BTreeNode leftSib = parentNode.children[parentIndex -1];
        
        if (tree.isLeaf) {
            tree.keys[0] = leftSib.keys[leftSib.numKeys - 1];
            parentNode.keys[parentIndex-1] = leftSib.keys[leftSib.numKeys - 1];
        } else {
            tree.keys[0] = parentNode.keys[parentIndex - 1];
            parentNode.keys[parentIndex-1] = leftSib.keys[leftSib.numKeys - 1];                
        }

        if (!tree.isLeaf) {
            for (int i = tree.numKeys; i > 0; i--) {
                tree.children[i] = tree.children[i-1];
            }
            tree.children[0] = leftSib.children[leftSib.numKeys];
            leftSib.children[leftSib.numKeys] = null;
            tree.children[0].parent = tree;
        }
        
        leftSib.numKeys--;
        
        return tree;
    }


    private void repairAfterDelete(BTreeNode tree)
    {
        if (tree.numKeys < min_keys()) {
            if (tree.parent == null) {
                if (tree.numKeys == 0) {
                    treeRoot = tree.children[0];
                    if (treeRoot != null)
                        treeRoot.parent = null;
                }
            } else {
                BTreeNode parentNode = tree.parent;
                int parentIndex;
                for (parentIndex = 0; parentNode.children[parentIndex] != tree; parentIndex++);
                if (parentIndex > 0 && parentNode.children[parentIndex - 1].numKeys > min_keys()) {
                    stealFromLeft(tree, parentIndex);
                } else if (parentIndex < parentNode.numKeys && parentNode.children[parentIndex + 1].numKeys > min_keys()) {
                    stealFromRight(tree,parentIndex);
                } else if (parentIndex == 0) { // Merge with right sibling
                    BTreeNode nextNode = mergeRight(tree);
                    repairAfterDelete(nextNode.parent);            
                } else { // Merge with left sibling
                    BTreeNode nextNode = mergeRight(parentNode.children[parentIndex-1]);
                    repairAfterDelete(nextNode.parent);            
                }
            }
        }
    }

    
    public static void main(String[] args) {

        BPlusTree myTree = new BPlusTree(5);

        System.out.println("Enter numbers to insert values, Enter D followed by a number to delete a value.");
        Scanner scanner = new Scanner(System.in);
        String data = scanner.nextLine();
        while (data.length() > 0) {
            if(data.matches("\\d+")) {
                int val = Integer.decode(data);
                myTree.insert(val);
            } else if (data.matches("D\\d+")) {
                int val = Integer.decode(data.substring(1));
                myTree.delete(val);
            }
            myTree.show();
            System.out.println();
            data = scanner.nextLine();
        }
        scanner.close();
    }
}
'''
