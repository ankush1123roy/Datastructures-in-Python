class Trie: 

# Create the Node Instance

    def __init__(self):
        self.next = {}
        self.Indicator = False
    
    def AddNode(self,string):
        # Check the word to be inserted
        if len(string) == 0:
            self.Indicator = True
            return 
        # See if any tree already exist
        key = string[0]
        string = string[1:]
        
        
        if key in self.next:
            self.next[key].AddNode(string)
        
        else: 
            node = Trie()
            self.next[key] = node
            node.AddNode(string)


T = Trie()
T.AddNode('Ammy')
T.AddNode('Amanda')

