#This file is part sale_carrier module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.pool import Pool
from .party import *
from .sale import *


def register():
    Pool.register(
        Party,
        Sale,
        module='sale_carrier', type_='model')
