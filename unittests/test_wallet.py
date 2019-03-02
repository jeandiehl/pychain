import Wallet
import Transaction

from unittest import TestCase


class TestWallet(TestCase):

    def test_new_wallet(self):
        wallet = Wallet.Wallet('geheim')
        result = b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDlbor8kAc62jFaoivZGdArI9tY\nvKz1551t7i3j0s1j0KqwmLdIVI5fp5LYFcJ7iL9P1jsaotAw9QqdJuMu4x+ttOAT\nIqQ25TdyXA4FtRPLZ2zBbTmdklSlHNkekSpmE7nTOSl95S2FbLrDNuV3t1mPjfZB\nxq0HF0RamgLmE77gCwIDAQAB\n-----END PUBLIC KEY-----'
        self.assertEqual(result, wallet.get_public_address())

    def test_new_wallet_other(self):
        wallet = Wallet.Wallet('other')
        result = b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCeWC3lCcA7pPP1/7aQaW5iLSm+\nA9THkEvAvnILkVtF1UKxBkTN6x5Jz5kbTbi56lYIZydt3e+sg8r8BD5qMR6O193d\nreVKvp4eRQbQOi2Ys/0GyI5k8FsqoYSaEZ3mA/0QJWOQrYHcX99idqjon/Mzytu2\nvPQktEZV4eu+p2YV5wIDAQAB\n-----END PUBLIC KEY-----'
        self.assertEqual(result, wallet.get_public_address())

    def test_transaction_creation(self):
        wallet_sender = Wallet.Wallet('geheim')
        wallet_receiver = Wallet.Wallet('other')

        transaction = wallet_sender.create_transaction(wallet_receiver.get_public_address(), 100.0)

        transaction_compare = Transaction.Transaction(wallet_sender.get_public_address(), wallet_receiver.get_public_address(), 100.0)
        transaction_compare.signature = transaction.signature
        self.assertEqual(transaction, transaction_compare)
