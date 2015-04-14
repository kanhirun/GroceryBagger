import pytest
from unittest import TestCase

from grocery_bagger import GroceryBagger


class TestGroceryBagger(TestCase):

  def test1(self):
    groceryBagger = GroceryBagger()

    strength  = 0
    itemTypes = ["DAIRY", "DAIRY", "PRODUCE", "PRODUCE", "PRODUCE", "MEAT"]

    minimumBags = groceryBagger.minimumBags(strength, itemTypes)

    self.assertEqual(4, minimumBags)


  def test2(self):
    groceryBagger = GroceryBagger()

    strength  = 3
    itemTypes = ["DAIRY", "DAIRY", "PRODUCE", "PRODUCE", "PRODUCE", "MEAT"]

    minimumBags = groceryBagger.minimumBags(strength, itemTypes)

    self.assertEqual(3, minimumBags)


  def test3(self):
    groceryBagger = GroceryBagger()

    strength  = 10
    itemTypes = []

    minimumBags = groceryBagger.minimumBags(strength, itemTypes)

    self.assertEqual(0, minimumBags)


  def test4(self):
    groceryBagger = GroceryBagger()

    strength  = 5
    itemTypes = ["CANNED", "CANNED", "PRODUCE", "DAIRY", "MEAT", "BREAD",
                 "HOUSEHOLD", "PRODUCE", "FROZEN", "PRODUCE", "DAIRY"]

    minimumBags = groceryBagger.minimumBags(strength, itemTypes)

    self.assertEqual(7, minimumBags)


  def test5(self):
    groceryBagger = GroceryBagger()

    strength  = 2
    itemTypes = ["CANNED", "CANNED", "PRODUCE", "DAIRY", "MEAT", "BREAD",
                 "HOUSEHOLD", "PRODUCE", "FROZEN", "PRODUCE", "DAIRY"]

    minimumBags = groceryBagger.minimumBags(strength, itemTypes)

    self.assertEqual(8, minimumBags)


