class Block(object):
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.transactions = transactions
        self.nonce = ''
        self.previous_hash = previous_hash

    def __str__(self):
        return "{{\n\t'index': {},\n\t,'transactions':{},\n\t'nonce': {},\n\t'previous_hash': {}\n\t  }}".format(
            self.index, str(self.transactions).replace('\n', '\n\t'), self.nonce, self.previous_hash)
