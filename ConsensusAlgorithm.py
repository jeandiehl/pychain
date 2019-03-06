class ConsensusAlgorithm(object):
    def __init__(self, hash_algorithm, settings):
        self.hash_algorithm = hash_algorithm
        self.settings = settings

    def calculate_proof(self, block_hash):
        pass

    def is_proof_valid(self, block):
        pass


class ProofOfWorkAlgorithm(ConsensusAlgorithm):
    def __init__(self, hash_algorithm, settings):
        super(ProofOfWorkAlgorithm, self).__init__(hash_algorithm, settings)

    def calculate_proof(self, block_hash):
        difficulty = self.settings.mining_difficulty
        nonce = 0
        proof = self.hash_algorithm.digest('{}{}'.format(block_hash, nonce))

        while proof[:difficulty] != '0' * difficulty:
            nonce += 1
            proof = self.hash_algorithm.digest('{}{}'.format(block_hash, nonce))

        return proof, nonce

    def is_proof_valid(self, block):
        proof_check = self.hash_algorithm.digest('{}{}'.format(block.hash, block.nonce))
        return proof_check == block.proof
