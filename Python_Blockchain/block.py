from time import time

class Block:
    def __init__(self, index, previous_hash, transactions, proof_of_work, time=time()):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = time
        self.transactions = transactions
        self.proof_of_work = proof_of_work