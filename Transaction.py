import datetime

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5


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
        # TODO remove concrete hashing function
        rsa_public_key = RSA.import_key(self.sender)
        verifier = PKCS1_v1_5.new(rsa_public_key)
        return verifier.verify(self.get_hash(), self.signature)

    def get_hash(self):
        transaction_hash = SHA256.new()
        transaction_hash.update('sender: {}, receiver: {}, self.amount: {}, self.timestamp: {}'.format(self.sender, self.receiver, self.amount, self.timestamp).encode('utf8'))
        return transaction_hash

    def __eq__(self, other):
        return self.sender == other.sender and self.receiver == other.receiver and self.amount == other.amount and self.signature == other.signature and self.timestamp == other.timestamp

    def __ne__(self, other):
        return self.sender != other.sender or self.receiver != other.receiver or self.amount != other.amount or self.signature != other.signature or self.timestamp != other.timestamp


class GenesisTransaction(Transaction):
    def __init__(self, sender, receiver, amount):
        self.amount = amount
        self.sender = sender
        self.receiver = receiver
        self.signature = ''

        self.timestamp = datetime.datetime.now(datetime.timezone.utc)


class MiningRewardTransaction(Transaction):
    def __init__(self, receiver, amount):
        self.amount = amount
        self.sender = None
        self.receiver = receiver
        self.signature = None

        self.timestamp = datetime.datetime.now(datetime.timezone.utc)

    def is_signature_valid(self):
        return False
