import unittest

from main import sort


class TestSort(unittest.TestCase):

  def test_standard(self):
    self.assertEqual(sort(1, 1, 1, 1), "STANDARD")

  def test_special_bulky(self):
    self.assertEqual(sort(150, 1, 1, 1), "SPECIAL")
    self.assertEqual(sort(1, 150, 1, 1), "SPECIAL")
    self.assertEqual(sort(1, 1, 150, 1), "SPECIAL")
    self.assertEqual(sort(140, 140, 140, 1), "SPECIAL")

  def test_special_heavy(self):
    self.assertEqual(sort(1, 1, 1, 20), "SPECIAL")

  def test_rejected(self):
    self.assertEqual(sort(150, 1, 1, 20), "REJECTED")
    self.assertEqual(sort(140, 140, 140, 20), "REJECTED")

  def test_null_value(self):
     with self.assertRaises(TypeError):
       sort(None, 1, 1, 20)

  def test_invalid_value(self):
     with self.assertRaises(TypeError):
       sort("xpto", 1, 1, 20)
