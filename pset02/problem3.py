import sys

class Tree:
    def __init__(self, left=None, right=None):
        self.right = right
        self.left = left

    def children(self):
        """
        Ill return the children's node
        """
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        """
        Return the child's nodes in a string
        """
        return "%s__%s" % (self.left, self.right)

def huffman_encoding(data):
    pass

def huffman_decoding(data,tree):
    pass

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))