import unittest

#
class Pair:




# None -> list
# This function takes no arguments and returns an empty list.
def empty_list():
    return Pair('mt', 'mt')
class Tests(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(empty_list(), 'mt')

