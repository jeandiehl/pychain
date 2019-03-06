import datetime


class Block(object):
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.transactions = transactions
        self.previous_hash = previous_hash

        self.nonce = 0
        self.proof = None
        self.timestamp = datetime.datetime.now()

        self.hash = None

    def calculate_hash(self, hash_algorithm):
        transactions = ''.join([str(t.get_hash()) for t in self.transactions])
        previous_hash = str(self.previous_hash)

        return hash_algorithm.digest('{}{}'.format(transactions, previous_hash))


class GenesisBlock(Block):
    def __init__(self):
        self.index = 0
        self.transactions = []
        self.previous_hash = 0

        self.nonce = 0
        self.proof = None
        self.timestamp = datetime.datetime.now()

        self.hash = None
