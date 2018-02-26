from a2 import game1
from a2 import game2
from a2 import game3
from a2 import win
from a2 import validBoard
from a2 import validmove
from a2 import SampleState
from a2 import takeNaiveMove
from a2 import BS
from a2 import *

import unittest

class testpoint(unittest.TestCase):
	
	def test_game1(self):
		self.assertAlmostEqual(game1(10000),0.58,delta=0.03)
		self.assertAlmostEqual(game1(5000),0.58,delta=0.03)
		self.assertAlmostEqual(game1(30000),0.58,delta=0.03)
	

	def test_game2(self):
		self.assertAlmostEqual(game2(2000), 0.18, delta=0.03)
		self.assertAlmostEqual(game2(1500), 0.18, delta=0.03)
		self.assertAlmostEqual(game2(30000), 0.18, delta=0.03)

	def test_game3(self):
		self.assertAlmostEqual(game3(2500), 0.39, delta=0.03)
		self.assertAlmostEqual(game3(10000), 0.39, delta=0.03)
		self.assertAlmostEqual(game3(3500), 0.39, delta=0.03)


	def test_validBoard(self):
		SS=SampleState(1)
		self.assertFalse(validBoard())
		
		SS=SampleState(2)
		self.assertFalse(validBoard())

		SS=SampleState(3)
		self.assertTrue(validBoard())
	
	def test_win(self):
		
		SS=SampleState(4)
		self.something(SS)
		self.assertEqual(win(),0)

		SS=SampleState(5)
		self.something(SS)
		self.assertEqual(win(),2)

		SS=SampleState(6)
		self.something(SS)
		self.assertEqual(win(),1)

	def test_takeNaiveMove(self):
		SS=SampleState(7)
		self.something(SS)
		self.assertEqual(takeNaiveMove(),8)
		
		SS=SampleState(8)
		self.something(SS)
		self.assertEqual(takeNaiveMove(),4)
		
		SS=SampleState(9)
		self.something(SS)
		self.assertEqual(takeNaiveMove(),2)

	def test_validmove(self):
		SS=SampleState(4)
		self.something(SS)
		self.assertTrue(validmove(tile4))
		
		SS=SampleState(5)
		self.something(SS)
		self.assertFalse(validmove(tile4))
		
		SS=SampleState(6)
		self.something(SS)
		self.assertFalse(validmove(tile4))
		
	def something(self,BS):
		
		global tile1,tile2,tile3, tile4, tile5, tile6, tile7, tile8, tile9
		tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9=int(BS[0]),int(BS[1]),int(BS[2]),int(BS[3]),int(BS[4]),int(BS[5]),int(BS[6]),int(BS[7]),int(BS[8])
		

if __name__=='__main__':
	unittest.main()


