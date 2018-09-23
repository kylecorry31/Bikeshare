import unittest
from testing import bike, mocks
from testing.bike import *

def runTests(class_name):
	suite = unittest.TestLoader().loadTestsFromTestCase(class_name)
	unittest.TextTestRunner(verbosity=2).run(suite)


runTests(TestBikeStateMachine)