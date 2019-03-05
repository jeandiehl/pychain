import datetime

import Block


class ChainSettings(object):
    def __init__(self):
        self.max_block_size = 1048576
        self.mining_reward = 10.0
        self.mining_difficulty = 3


class Blockchain(object):
    def __init__(self, consensus_mechanism, hash_algorithm, settings):
        self._blocks = []
        self.pending_transactions = []
        self.consensus_mechanism = consensus_mechanism
        self.hash_algorithm = hash_algorithm
        self.settings = settings
        self._generate_genesis_block()

    def add_transaction(self, transaction):
        if not transaction.is_signature_valid():
            msg = 'Transaction has no valid signature!'
            raise ValueError(msg)

        if not self.is_transaction_valid(transaction):
            msg = 'Transaction is not valid'
            raise ValueError(msg)

        self.pending_transactions.append(transaction)

    def _get_transactions_with_receiver(self, address):
        for block in self._blocks:
            for transaction in block.transactions:
                if transaction.receiver == address:
                    yield transaction

    def _get_transactions_with_sender(self, address):
        for block in self._blocks:
            for transaction in block.transactions:
                if transaction.receiver == address:
                    yield transaction

    def is_transaction_valid(self, transaction):
        pass

    def get_last_block(self):
        return self._blocks[-1]

    def _generate_genesis_block(self):
        genesis_block = Block.GenesisBlock()

        self.mine_block(genesis_block)
        self._blocks = [genesis_block]

    def generate_new_block(self, transactions):
        last_block = self.get_last_block()

        # new_block = Block.Block(last_block.index + 1, None, )

    def mine_block(self, block):
        # TODO implement mining
        hash = self.hash_algorithm.digest(block.get_combined_transaction_bash())
        difficulty = self.settings.mining_difficulty

        while hash[:difficulty] != '0' * difficulty:
            block.nonce += 1
            hash = self.hash_algorithm.digest(block.get_combined_transaction_bash())
        block.timestamp = datetime.datetime.now()
        block.hash = hash
