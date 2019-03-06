import datetime

import Block
import Transaction


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
            msg = 'Transaction is not valid, because current balance is currently {} and smaller than transaction ' \
                  'amount.'.format(self.get_balance(transaction.sender))
            raise ValueError(msg)

        self.pending_transactions.append(transaction)

    def _get_transactions_with_receiver(self, address):
        for block in self._blocks:
            for transaction in block.transactions:
                if transaction.receiver == address:
                    yield transaction

        for transaction in self.pending_transactions:
            if transaction.receiver == address:
                yield transaction

    def _get_transactions_with_sender(self, address):
        for block in self._blocks:
            for transaction in block.transactions:
                if transaction.sender == address:
                    yield transaction

        for transaction in self.pending_transactions:
            if transaction.sender == address:
                yield transaction

    def get_balance(self, address):
        balance = 0.0
        sended_transactions = self._get_transactions_with_sender(address)
        received_transactions = self._get_transactions_with_receiver(address)

        for transaction in sended_transactions:
            balance -= transaction.amount

        for transaction in received_transactions:
            balance += transaction.amount
        return balance

    def is_transaction_valid(self, transaction):
        return self.get_balance(transaction.sender) - transaction.amount >= 0.0

    def get_last_block(self):
        return self._blocks[-1]

    def _generate_genesis_block(self):
        genesis_block = Block.GenesisBlock()

        self.mine_block(genesis_block)
        self._blocks = [genesis_block]

    def generate_new_block(self, transactions):
        # TODO check for valid transactions

        last_block = self.get_last_block()
        return Block.Block(last_block.index + 1, transactions, last_block.hash)

    def mine_block(self, block, miner_wallet=None):
        if miner_wallet:
            reward_transaction = Transaction.MiningRewardTransaction(miner_wallet.get_public_address(),
                                                                     self.settings.mining_reward)
            block.transactions.append(reward_transaction)

        block.hash = block.calculate_hash(self.hash_algorithm)

        block.proof, block.nonce = self.consensus_mechanism.calculate_proof(block.hash)
        block.timestamp = datetime.datetime.now()

    def is_connection_valid(self, block, next_block):
        if block.timestamp > next_block.timestamp:
            return False
        if block.index + 1 != next_block.index:
            return False
        if block.hash != next_block.previous_hash:
            return False
        if not self.consensus_mechanism.is_proof_valid(next_block):
            return False

        return True

    def append_block(self, block):
        if not self.is_connection_valid(self.get_last_block(), block):
            msg = 'The new block can not be appended, because the connection is not valid.'
            raise RuntimeError(msg)
        # TODO remove mined transactions from pending_transactions
        self._blocks.append(block)
