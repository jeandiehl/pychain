import os

from Crypto.Protocol.KDF import PBKDF2
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

import Transaction

KEY_SAVE_PATH = os.path.expanduser('~/PycharmProjects/pychain')
KEY_LENGTH = 1024
PKCS = 8
KEY_PROTECTION = 'scryptAndAES128-CBC'

SALT = 'PYCOIN'

master_key = ''


class Wallet(object):
    def __init__(self, seed):
        msg = 'Wallet seed value can not be an empty string'
        if seed == '':
            raise ValueError(msg)

        global master_key
        self.key = RSA
        master_key = PBKDF2(seed, SALT, count=10000)
        self.generate_new_key()

    def generate_new_key(self):
        my_rand.counter = 0
        self.key = RSA.generate(KEY_LENGTH, randfunc=my_rand)

    def get_public_address(self):
        return self.key.publickey().export_key()

    def calculate_signature(self, transaction):
        private_key = self.key.exportKey()
        rsa_private_key = RSA.importKey(private_key)
        return PKCS1_v1_5.new(rsa_private_key).sign(transaction.get_hash())

    def create_transaction(self, receiver_address, amount):
        if self.get_public_address() == receiver_address:
            msg = 'Receiver address can not be the same like sender address.'
            raise RuntimeError(msg)

        transaction = Transaction.Transaction(self.get_public_address(), receiver_address, amount)
        signature = self.calculate_signature(transaction)
        transaction.set_signature(signature)

        if transaction.is_signature_valid():
            return transaction
        else:
            msg = 'Can not create transaction, because signature could not be verified!'
            raise RuntimeError(msg)


def my_rand(n):
    my_rand.counter += 1
    return PBKDF2(master_key, "my_rand:%d" % my_rand.counter, dkLen=n, count=1)
