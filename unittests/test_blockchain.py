from unittest import TestCase

import HashAlgorithm
import ConsensusAlgorithm
import Blockchain
import Wallet


class TestBlockchain(TestCase):
    def setUp(self):
        ha = HashAlgorithm.HashAlgorithm()
        ca = ConsensusAlgorithm.ConsensusAlgorithm()
        bc = Blockchain.Blockchain(ca, ha)
        wallet1 = Wallet.Wallet('geheim')
        wallet2 = Wallet.Wallet('other')
        wallet3 = Wallet.Wallet('bla')

        trans1 = wallet1.create_transaction(wallet3.get_public_address(), 100.0)
        trans2 = wallet1.create_transaction(wallet2.get_public_address(), 10.0)
        trans3 = wallet1.create_transaction(wallet3.get_public_address(), 500.0)
        trans4 = wallet1.create_transaction(wallet3.get_public_address(), 150.0)
        trans5 = wallet2.create_transaction(wallet1.get_public_address(), 220.0)
        trans6 = wallet2.create_transaction(wallet1.get_public_address(), 12.0)

    def test_add_transaction(self):

