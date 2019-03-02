import Transaction


class Block(object):
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.transactions = transactions
        self.nonce = ''
        self.previous_hash = previous_hash