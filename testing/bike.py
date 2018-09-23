import unittest
from bikeshare.entities import BikeState, Bike
from bikeshare import Logger
from testing import mocks

class TestBikeStateMachine(unittest.TestCase):

	def test_states(self):
		Logger.on = False
		bikeshare = mocks.MockBikeShare()

		bike = bikeshare.bike

		# Typical use
		self.assertEqual(bike.state, BikeState.ACTIVE_NO_USER)

		bike.on_swipe(0)

		self.assertEqual(bike.state, BikeState.ACTIVE_USER)

		bike.on_swipe(1)

		self.assertEqual(bike.state, BikeState.ACTIVE_USER)

		bike.on_swipe(0)

		self.assertEqual(bike.state, BikeState.ACTIVE_NO_USER)

		bike.on_swipe(1)

		self.assertEqual(bike.state, BikeState.ACTIVE_USER)

		bike.on_swipe(1)

		self.assertEqual(bike.state, BikeState.ACTIVE_NO_USER)


		# Out of order

		bike.on_deactivate()

		self.assertEqual(bike.state, BikeState.OUT_OF_ORDER_NO_USER)

		bike.on_swipe(1)

		self.assertEqual(bike.state, BikeState.OUT_OF_ORDER_NO_USER)

		bike.on_activate()

		self.assertEqual(bike.state, BikeState.ACTIVE_NO_USER)

		bike.on_swipe(1)

		self.assertEqual(bike.state, BikeState.ACTIVE_USER)

		bike.on_deactivate()

		self.assertEqual(bike.state, BikeState.OUT_OF_ORDER_USER)

		bike.on_swipe(0)

		self.assertEqual(bike.state, BikeState.OUT_OF_ORDER_USER)

		bike.on_swipe(1)

		self.assertEqual(bike.state, BikeState.OUT_OF_ORDER_NO_USER)

		bike.on_activate()

		self.assertEqual(bike.state, BikeState.ACTIVE_NO_USER)

		bike.on_swipe(1)

		self.assertEqual(bike.state, BikeState.ACTIVE_USER)

		bike.on_deactivate()

		self.assertEqual(bike.state, BikeState.OUT_OF_ORDER_USER)

		bike.on_activate()

		self.assertEqual(bike.state, BikeState.ACTIVE_USER)


