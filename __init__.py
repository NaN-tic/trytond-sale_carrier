#This file is part sale_carrier module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.pool import Pool
import configuration
import party
import sale


def register():
    Pool.register(
        configuration.Configuration,
        party.Party,
        sale.Sale,
        module='sale_carrier', type_='model')
