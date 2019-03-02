import Block
import Transaction


class Blockchain(object):
    def __init__(self, consensus_mechanism, hash_algorithm):
        self.blocks = []
        self.pending_transactions = []
        self.consensus_mechanism = consensus_mechanism
        self.hash_algorithm = hash_algorithm

    def add_transaction(self, transaction):
        if not transaction.is_signature_valid():
            msg = 'Transaction has no valid signature!'
            raise ValueError(msg)

        if not self.is_transaction_valid(transaction):
            msg = 'Transaction is not valid'
            raise ValueError(msg)

        self.pending_transactions.append(transaction)

    def _get_transactions_with_receiver(self, address):
        for block in self.blocks:
            for transaction in block.transactions:
                if transaction.receiver == address:
                    yield transaction

    def _get_transactions_with_sender(self, address):
        for block in self.blocks:
            for transaction in block.transactions:
                if transaction.receiver == address:
                    yield transaction

    def is_transaction_valid(self, transaction):
        pass
