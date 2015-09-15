__author__ = 'Tom'
#first time ever building unit tests, yikes
import csv
import sys
import operator
import CSV_classes
import unittest

class TestFactorial(unittest.TestCase):
    n = CSV_classes.Neighborhood(77, 77, 77, 77, 77)

    def testAssignment(self):
         n = CSV_classes.Neighborhood(77, 77, 77, 77, 77)
        n.assertEqual(77, n.CommunityArea)
        n.assertEqual(77, n.CommunityAreaName)
        n.assertEqual(77, n.total_install)
        n.assertEqual(77, n.PerCapitaIncome)
        n.assertEqual(77, n.totalCrimes)

    def testSetter1(self):
        n = CSV_classes.Neighborhood(77, 77, 77, 77, 77)
        n.set_total_install(1)
        n.assertEqual(78, n.total_install)

    def testSetter2(self):
        n = CSV_classes.Neighborhood(77, 77, 77, 77, 77)
        n.set_total_crimes(1)
        n.assertEqual(78, n.totalCrimes)

