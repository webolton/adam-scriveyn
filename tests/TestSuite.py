import unittest
import tests
from tests import lib

def create_suite():
    test_suite = unittest.TestSuite()
    loader = unittest.TestSuite()

    test_suite.addTests(loader.loadTestsFromModule(lib))

    # test_suite.addTest(unittest.makeSuite(TestImageProcessor))

    return(test_suite)

if __name__ == '__main__':
    suite = create_suite()

    runner=unittest.TextTestRunner()
    runner.run(suite)
