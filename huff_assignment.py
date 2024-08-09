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
            return "EOF " + str(self.weight)
        elif self.value:
            return "LEAF " + self.value + " " + str(self.weight)
        else:
            return "INODE " + str(self.weight)



### Encoding Logic ###
def huff_encode(filename):
    with open(filename, 'r') as file:
       text = file.read()

    def build_freq(text): # DONE
        freq = {}
        for symbol in text:
            if symbol in freq:
                freq[symbol] += 1
            else:
                freq[symbol] = 1
        return freq

    freq = build_freq(text) 
    forest = [] 

    def build_forest_from_frequencies(forest, freq): # DONE
        for symbol in freq:
            heappush(forest, TreeNode(symbol, freq[symbol]))

    build_forest_from_frequencies(forest, freq)  
    # append a pseudo-eof marker to the heap with the lowest weight (0)
    heappush(forest, TreeNode('\udddd', 0)) # "\udddd" is an invalid unicode character! We use it as a pseudo-eof marker

    # merge smallest pairs from forest until down to one big tree
    # the forest is a heap, so the smallest trees are at the top
    # pop the top two trees, merge them, and push the result back into the heap
    def merge_trees(forest): # DONE
        while len(forest) > 1:
            left = heappop(forest) # pop the smallest tree
            right = heappop(forest) # pop the next smallest tree
            heappush(forest, TreeNode(None, left.weight + right.weight, left, right)) # push the merged tree back into the heap
        return heappop(forest) # return the last tree in the heap, you can also return forest[0]

    encoding_tree = merge_trees(forest)

    # set up buffer for the output
    encoded_data = BitBuffer() # this is the buffer for the header

    # store the tree into the buffer as the header using append("0"),
    # append("1") and append_chr(tree.value) methods in the traversal function

    # The encode_into_header function is a recursive function that traverses the tree and
    # encodes the tree into the header.  The encoded data is stored in the encoded_data
    # buffer.  The encoded data is a sequence of bits, where a "0" indicates a node
    # and a "1" indicates a leaf.  The leaf value is stored in the next 16 bits.
    # The traversal is preorder, so the root is encoded first, then the left subtree,
    # then the right subtree.  The traversal is recursive, so you need to pass the
    # encoded_data buffer to the recursive calls.
    def encode_into_header(tree, encoded_data):
        if tree.value:
            encoded_data.append("1")
            encoded_data.append_chr(tree.value)
        else:
            encoded_data.append("0")
            encode_into_header(tree.left, encoded_data)
            encode_into_header(tree.right, encoded_data)

    encode_into_header(encoding_tree, encoded_data) # DONE (described as option 3)

    # first parameter is input, second is for the output
    # create the encoding code table (i.e. dictionary) from the tree (recursively)
    code_table = {} # this is the dictionary of symbol:code pairs

    def build_code_table(tree, path, code_table): # DONE 5
        if tree.value: # This is a leaf node
            code_table[tree.value] = path # add the path to the code table
        else: # This is an internal node
            build_code_table(tree.left, path + "0", code_table) # add a 0 to the path and call the left child
            build_code_table(tree.right, path + "1", code_table) # add a 1 to the path and call the right child

    build_code_table(encoding_tree, "", code_table) # DONE 
    # first parameter initially passed the root of the tree
    # second parameter records the path as you recursively traverse the tree
    # when you get to the leaf, that path is the encoding for the leaf's value
    # so when calling down for a child, add to the path
    # at the leaf, add an entry to the code_table

    # encode the input
    for symbol in text:
       encoded_data.append(code_table[symbol])
    encoded_data.append(code_table['\udddd']) # add the pseudo-eof character

    # output the result
    with open(filename + '.huff.txt', 'wb') as file:
       file.write(bytes(encoded_data))  # padding to get to full bytes is automatic


# the decoding logic
def huff_decode(filename):
    with open(filename + '.huff.txt', 'rb') as file:
       coded = BitBuffer(file.read()) # reading binary file into the buffer

    # reconstruct a decode tree from the header data using pop_bit() and pop_chr()

    def rebuild_tree(coded): # DONE
        if coded.pop_bit() == "1": # if the next bit is a 1, then this is a leaf node
            return TreeNode(coded.pop_chr(), 0) # pop the next 16 bits and return a leaf node, the weight is 0 because we don't need it for decoding
        else:
            return TreeNode(None, 0, rebuild_tree(coded), rebuild_tree(coded)) # pop the next bit and recursively call rebuild_tree for the left and right subtrees

    decode_tree = rebuild_tree(coded) # DONE  (all weights can be zero this time)

    # prepare for the decode cycle
    result = "" # a simple character buffer to hold the decoded data
    t = decode_tree    # we haven't read any real data so start at he top of the tree
    while True:
        # TODO 7 decode cycle
        # pop a bit and traverse down the tree appropriately
        # if you land on the pseudo-eof character, you're done
        # if you land on any other leaf node, store the value and move t back to the top.
        bit = coded.pop_bit()
        if bit == "0":
            t = t.left
        else: 
            t = t.right
        if t.value:
            if t.value == '\udddd':
                break
            result += t.value 
            t = decode_tree

    # after you've seen the pseudo-eof you can output the translated result
    with open(filename + '.out.txt', 'w') as file:
       file.write(result)



huff_encode("test.txt") 

huff_decode("test.txt")

