import unittest
import utility


class TestUtilityMethods(unittest.TestCase):

    def test_utility(self):
        self.assertTrue(utility.generate_thumb('./descarga.pdf'))
        self.assertTrue(utility.generate_thumb('descarga.pdf'))
        self.assertFalse(utility.generate_thumb('fichero.txt'))
        self.assertFalse(utility.generate_thumb('/home/vagrant/test.pdf'))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtilityMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
