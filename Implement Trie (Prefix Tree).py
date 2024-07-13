class Trinode:
    def __init__(self):
        self.end=None
        self.key={}

class Trie(object):

    def __init__(self):
        self.root="Root"
        self.tree=Trinode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        def DFS(i,node):
            if i==len(word):
                node.end=True
                return
            if word[i] not in node.key :
                node.key[word[i]]=Trinode()
                DFS(i+1,node.key[word[i]])
            else:
                DFS(i+1,node.key[word[i]])
        DFS(0,self.tree)

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def DFS(i,node):
            if i==len(word) and node.end:
                return True
            if i==len(word):
                return False
            if word[i] not in node.key:
                return False
            return DFS(i+1,node.key[word[i]])
        
        return DFS(0,self.tree)
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        def DFS(i,node):
            if i==len(prefix):
                return True
            if prefix[i] not in node.key:
                return False
            return DFS(i+1,node.key[prefix[i]])
            
        return DFS(0,self.tree)

trie=Trie()
trie.insert("apple")
print(trie.search("apple"))   # return True
print(trie.search("app"))     # return False
print(trie.startsWith("app")) # return True
trie.insert("app")
print(trie.search("app"))
trie.insert("adil")
print(trie.startsWith("adil"))

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)