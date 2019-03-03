from unittest import TestCase

import Blockchain
import ConsensusAlgorithm
import HashAlgorithm
import Wallet


class TestBlockchain(TestCase):
    def setUp(self):
        self.ha = HashAlgorithm.HashAlgorithm()
        self.ca = ConsensusAlgorithm.ConsensusAlgorithm()
        self.bc = Blockchain.Blockchain(self.ca, self.ha)

    def test_add_transaction(self):
        wallet1 = Wallet.Wallet('geheim')
        wallet2 = Wallet.Wallet('other')
        wallet3 = Wallet.Wallet('bla')

        trans1 = wallet1.create_transaction(wallet3.get_public_address(), 100.0)
        trans2 = wallet1.create_transaction(wallet2.get_public_address(), 10.0)
        trans3 = wallet1.create_transaction(wallet3.get_public_address(), 500.0)
        trans4 = wallet1.create_transaction(wallet3.get_public_address(), 150.0)
        trans5 = wallet2.create_transaction(wallet1.get_public_address(), 220.0)
        trans6 = wallet2.create_transaction(wallet1.get_public_address(), 12.0)
        self.fail()

    def test_generate_genesis_block(self):
        self.bc._generate_genesis_block()
        last_block = self.bc.get_last_block()
        print(last_block)
