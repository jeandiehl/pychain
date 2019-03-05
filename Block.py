import datetime


class Block(object):
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.transactions = transactions
        self.nonce = 0
        self.previous_hash = previous_hash
        self.timestamp = datetime.datetime.now()
        self.hash = ''

    def get_combined_transaction_bash(self):
        return ''.join([t.get_hash() for t in self.transactions]) + str(self.nonce) + str(self.previous_hash)


class GenesisBlock(Block):
    def __init__(self):
        self.index = 0
        self.transactions = []
        self.nonce = 0
        self.previous_hash = ''
        self.timestamp = datetime.datetime.now()
        self.hash = ''
