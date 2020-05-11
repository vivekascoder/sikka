from Crypto import Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from binascii import hexlify
import datetime
from collections import OrderedDict

__information__ = """
Group(Transactions) -> ...
Group(...) -> Block
Group(Block) -> BlockChain
Group(BlockChain) -> CryptoCurrency
"""

class Client:
    def __init__(self, username):
        # start generating the RSA private, public key pairs.
        self._private_key = RSA.generate(1024, Random.new().read)
        self._public_key = self._private_key.publickey()
        self._user_name = self.username
    @property
    def key(self):
        return hexlify(self._public_key).decode('ascii')
    @property
    def username(self):
        return self._user_name

class Transaction:
    def __init__(self, sender, reciever, amount):
        self.sender = sender
        self.reciever = reciever
        self.amount = amount
        self.timestamp = datetime.datetime.now()
        self.data = OrderedDict({
            'sender_name': self.sender.username,
            'sender_key': self.sender.key,
            'reciever_name': self.reciever.username,
            'amount': self.amount,
            'timestamp': self.timestamp
        })
        # It's time for signing the Transaction.
        


