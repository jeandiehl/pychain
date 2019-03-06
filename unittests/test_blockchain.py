from unittest import TestCase

import Blockchain
import ConsensusAlgorithm
import HashAlgorithm
import Wallet


class TestBlockchain(TestCase):
    def setUp(self):
        self.settings = Blockchain.ChainSettings()
        self.ha = HashAlgorithm.SHA256HashAlgorithm()
        self.ca = ConsensusAlgorithm.ProofOfWorkAlgorithm(self.ha, self.settings)
        self.bc = Blockchain.Blockchain(self.ca, self.ha, self.settings)

        self.wallet1 = Wallet.Wallet('geheim')
        self.wallet2 = Wallet.Wallet('other')
        self.wallet3 = Wallet.Wallet('bla')

    def test_add_transaction(self):
        new_block = self.bc.generate_new_block([])
        self.bc.mine_block(new_block, self.wallet1)
        self.bc.append_block(new_block)
        new_block = self.bc.generate_new_block([])
        self.bc.mine_block(new_block, self.wallet1)
        self.bc.append_block(new_block)
        new_block = self.bc.generate_new_block([])
        self.bc.mine_block(new_block, self.wallet2)
        self.bc.append_block(new_block)

        trans1 = self.wallet1.create_transaction(self.wallet3.get_public_address(), 5.0)
        trans2 = self.wallet1.create_transaction(self.wallet2.get_public_address(), 3.0)
        trans3 = self.wallet1.create_transaction(self.wallet3.get_public_address(), 4.0)
        trans4 = self.wallet1.create_transaction(self.wallet3.get_public_address(), 2.0)
        trans5 = self.wallet2.create_transaction(self.wallet1.get_public_address(), 1.0)
        trans6 = self.wallet2.create_transaction(self.wallet1.get_public_address(), 6.0)

        self.bc.add_transaction(trans1)
        self.bc.add_transaction(trans2)
        self.bc.add_transaction(trans3)
        self.bc.add_transaction(trans4)
        self.bc.add_transaction(trans5)
        self.bc.add_transaction(trans6)
        # TODO mine pending transactions

    def test_generate_genesis_block(self):
        self.bc._generate_genesis_block()
        last_block = self.bc.get_last_block()
        # print(json.dumps(last_block, default=Json.serialize, indent=4))
        expected_proof = "00017b0f5e57287fc7afe6d2325847442aa63ce6f9495e642f2e26dc45a06881"
        self.assertEqual(expected_proof, last_block.proof)

    def test_mine_empty_block(self):
        new_block = self.bc.generate_new_block([])
        self.bc.mine_block(new_block, self.wallet1)
        self.bc.append_block(new_block)

        new_block = self.bc.generate_new_block([])
        self.bc.mine_block(new_block, self.wallet2)
        self.bc.append_block(new_block)

        new_block = self.bc.generate_new_block([])
        self.bc.mine_block(new_block, self.wallet1)
        self.bc.append_block(new_block)

        # Json.pprint(new_block)
        balance1 = self.bc.get_balance(self.wallet1.get_public_address())
        self.assertEqual(balance1, 20.0)
