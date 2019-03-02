from Crypto.Hash import SHA256
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

import datetime


class Transaction(object):
    def __init__(self, sender, receiver, amount):
        if amount <= 0.0:
            msg = 'Transaction amount can only be a positive value.'
            raise ValueError(msg)

        self.amount = amount
        self.sender = sender
        self.receiver = receiver
        self.signature = ''

        self.timestamp = datetime.datetime.now(datetime.timezone.utc)

    def set_signature(self, signature):
        self.signature = signature

    def is_signature_valid(self):
        if self.signature == '':
            msg = "Signature is empty and has value =''"
            raise ValueError(msg)

        rsa_public_key = RSA.import_key(self.sender)
        verifier = PKCS1_v1_5.new(rsa_public_key)
        return verifier.verify(self.get_hash(), self.signature)

    def get_hash(self):
        transaction_hash = SHA256.new()
        transaction_hash.update('sender: {}, receiver: {}, self.amount: {}, self.timestamp: {}'.format(self.sender, self.receiver, self.amount, self.timestamp).encode('utf8'))
        return transaction_hash
