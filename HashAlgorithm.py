from Crypto.Hash import SHA256


class HashAlgorithm(object):
    def __init__(self):
        pass

    def digest(self, string):
        pass


class SHA256HashAlgorithm(HashAlgorithm):
    def __init__(self):
        super(SHA256HashAlgorithm, self).__init__()

    def digest(self, string):
        return SHA256.new(string.encode()).hexdigest()
