# -*- coding: utf-8 -*-
# @Time    : 2020/10/19 14:49
# @Author  : hongji
# @FileName: deci.py
import decimal

a = 2.3
b = 2.1
print(a-b)

a1 = decimal.Decimal(a)
b1 = decimal.Decimal(b)

print(a1-b1)