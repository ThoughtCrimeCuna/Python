# HUFF OUTLINE

from heapq import heappush, heappop

from BitBuffer import BitBuffer

# A simple tree node structure for the Huffman Coding algorithms
class TreeNode():

    # constructor for the nodes
    def __init__(self, value=None, weight=None, left=None, right=None):
        self.value = value
        self.weight = weight
        self.left = left
        self.right = right

    # comparison operator for < so the heap knows how to sort the nodes
    def __lt__(self, other):
        if self.weight != other.weight: # primary sorting is based on weight
            return self.weight < other.weight
        else: # secondary sort on letter values in code-point order
            return (self.value or '\udddd') < (other.value or '\udddd')
            # '\udddd' is my choice for pseudo-eof, it's big and illegal

    # maybe not really needed, but good to implement along with __lt__
    def __eq__(self, other):
        return self.weight == other.weight

    # this only converts a node to a string, not the entire tree recursively
    def __str__(self):
        if self.value == '\udddd':
            return "EOF " + str(weight)
        elif self.value:
            return "LEAF " + self.value + " " + str(weight)
        else:
            return "INODE " + str(weight)



## the encoding logic
#def huff_encode(filename):
    #with open(filename, 'r') as file:
    #    text = file.read()

    #freq = build_freq(text)  # TODO

    ## make a tree node for each symbol and push it into the forest heap
    #forest = [] # this will be our heap (i.e. priority queue) of trees
    ##build_forest_from_frequencies(forest, freq)  # TODO
    ## append a pseudo-eof marker to the heap with the lowest weight (0)
    #heappush(forest, HuffTree('\udddd', 0)) # "\udddd" is an invalid unicode character!

    ## merge smallest pairs from forest until down to one big tree
    #encoding_tree = merge_trees(forest) # TODO

    ## set up buffer for the output
    #encoded_data = BitBuffer()
    ## store the tree into the buffer as the header using append("0"),
    ## append("1") and append_chr(tree.value) methods in the traversal function
    #encode_into_header(encoding_tree, encoded_data) # TODO (described as option 3)
    ## first parameter is input, second is for the output

    ## create the encoding code table (i.e. dictionary) from the tree (recursively)
    #code_table = {}
    #build_code_table(encoding_tree, "", code_table) # TODO
    ## first parameter initially passed the root of the tree
    ## second parameter records the path as you recursively traverse the tree
    ## when you get to the leaf, that path is the encoding for the leaf's value
    ## so when calling down for a child, add to the path
    ## at the leaf, add an entry to the code_table

    ## encode the input
    #for symbol in text:
    #    encoded.append(code_table[symbol])
    #encoded.append(code_table['\udddd']) # add the pseudo-eof character

    ## output the result
    #with open(filename + '.huff.txt', 'wb') as file:
    #    file.write(bytes(encoded))  # padding to get to full bytes is automatic


## the decoding logic
#def huff_decode(filename):
    #with open(filename + '.huff.txt', 'rb') as file:
    #    coded = BitBuffer(file.read()) # reading binary file into the buffer

    ## reconstruct a decode tree from the header data using pop_bit() and pop_chr()
    #decode_tree = rebuild_tree(coded) # TODO  (all weights can be zero this time)

    ## prepare for the decode cycle
    #result = "" # a simple character buffer to hold the decoded data
    #t = decode_tree    # we haven't read any real data so start at he top of the tree
    #while True:
        ## TODO decode cycle
        ## pop a bit and traverse down the tree appropriately
        ## if you land on the pseudo-eof character, you're done
        ## if you land on any other leaf node, store the value and move t back to the top.

    ## after you've seen the pseudo-eof you can output the translated result
    #with open(filename + '.out.txt', 'w') as file:
    #    file.write(result)



#huff_encode("huff_outline.py")

#huff_decode("huff_outline.py")


## A test of the bit buffer
encoded = BitBuffer()
encoded.append('0001')
encoded.append_chr('T')
encoded.append('00000001')
encoded.append('0000000001010101')
encoded.append('00')

with open('bitbuffer_test_file.txt', 'wb') as file:
    file.write(bytes(encoded))  # padding to get to full bytes is automatic

with open('bitbuffer_test_file.txt', 'rb') as file:
    coded = BitBuffer(file.read()) # reading binary file into the buffer

while coded:
    while coded and coded.pop_bit() == '0':
        print("Zero")
    if coded:
        print(coded.pop_chr())
