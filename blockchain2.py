##
## Youtube video
##Blockchain-2

import hashlib


class Block():
    def _init_(self,index, timestamp, data, previousHash =''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previousHash = previousHash
        self.hash = calculateHash()
        
    def calculateHash(self):
          
        return hashlib.sha256(str(self.index, self.timestamp, str(self.data)))
class Blockchain:
    def _init_(self):
        self.chain = [self.createGenesisBlock()]
        
    def createGenesisBlock(self):
        
        return Block(0, "1/1/2010","5", "Genesis Block", "0")

    def getLatestBlock(self):
        return self.chain[self.chain.length-1]

    def addBlock(self, newBlock):
        newBlock.previousHash = self.getLatestBlock().hash
        newBlock.hash = newBlock.calculateHash()
        self.chain.append(newBlock)
#instantiate
test = Blockchain();
test.addBlock(Block(1, "09/06/18", "6", "test block", "1"))
test.addBlock(Block(2, "09/08/18", "7", "testlock", "2"))
print(str(test))

              

        
        
    
