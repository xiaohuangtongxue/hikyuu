#!/usr/bin/python
# -*- coding: utf8 -*-
# gb18030

#===============================================================================
# 作者：fasiondog
# 历史：1）20120221, Added by fasiondog
#===============================================================================

import unittest

from test_init import *
from hikyuu.trade_manage import *

class PythonTradeCost(TradeCostBase):
    def __init__(self):
        super(PythonTradeCost, self).__init__("PythonTradeCost")
        
    def getBuyCost(self, date, stock, price, num):
        return CostRecord(1.0, 1.0, 1.0, 1.0, 4.0)

    def getSellCost(self, date, stock, price, num):
        return CostRecord(2.0, 2.0, 2.0, 2.0, 8.0)
    
    def _clone(self):
        return PythonTradeCost();


class TradeCostTest(unittest.TestCase):
    def test_PythonTradeCost(self):
        stock = sm['sh000001']
        tc = PythonTradeCost()
        self.assertEqual(tc.name, "PythonTradeCost")
        cost = tc.getBuyCost(Datetime(201001010000), stock, 10.0, 100)
        self.assertEqual(cost, CostRecord(1,1,1,1,4))

        cost = tc.getSellCost(Datetime(201001010000), stock, 10.0, 100)
        self.assertEqual(cost, CostRecord(2,2,2,2,8))
        #print tc       
        
        clone_tc = tc.clone()
        self.assertEqual(clone_tc.name, "PythonTradeCost")
        cost = clone_tc.getBuyCost(Datetime(201001010000), stock, 10.0, 100)
        self.assertEqual(cost, CostRecord(1,1,1,1,4))
        cost = clone_tc.getSellCost(Datetime(201001010000), stock, 10.0, 100)
        self.assertEqual(cost, CostRecord(2,2,2,2,8))
        

    def test_ZeroTC(self):
        stock = sm['sh000001']
        tc = crtZeroTC()
        cost = tc.getBuyCost(Datetime(201001010000), stock, 10.0, 100)
        self.assertEqual(cost, CostRecord(0,0,0,0,0))
        cost = tc.getSellCost(Datetime(201001010000), stock, 10.0, 100)
        self.assertEqual(cost, CostRecord(0,0,0,0,0))   
        
        clone_tc = tc.clone()
        cost = clone_tc.getBuyCost(Datetime(201001010000), stock, 10.0, 100)
        self.assertEqual(cost, CostRecord(0,0,0,0,0))
        cost = clone_tc.getSellCost(Datetime(201001010000), stock, 10.0, 100)
        self.assertEqual(cost, CostRecord(0,0,0,0,0))   
        
    def test_FixedATC(self):
        stock = sm['sh000001']
        tc = crtFixedATC()
        cost = tc.getBuyCost(Datetime(200101010000), stock, 10.0, 2100)
        self.assertEqual(cost, CostRecord(37.8, 0, 2.1, 0, 39.9))
        cost = tc.getSellCost(Datetime(200101010000), stock, 10.0, 2100)
        self.assertEqual(cost, CostRecord(37.8, 0, 2.1, 0, 39.9))

        clone_tc = tc.clone()
        cost = clone_tc.getBuyCost(Datetime(200101010000), stock, 10.0, 2100)
        self.assertEqual(cost, CostRecord(37.8, 0, 2.1, 0, 39.9))
        cost = clone_tc.getSellCost(Datetime(200101010000), stock, 10.0, 2100)
        self.assertEqual(cost, CostRecord(37.8, 0, 2.1, 0, 39.9))
       
        
def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TradeCostTest)