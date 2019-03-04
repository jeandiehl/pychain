from unittest import TestCase

import HashAlgorithm


class TestHashAlgorithm(TestCase):
    def test_SHA256HashAlgorithm(self):
        sha256 = HashAlgorithm.SHA256HashAlgorithm()
        calculated_hash = sha256.digest('test')
        expected_hash = '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08'
        self.assertEqual(expected_hash, calculated_hash)
