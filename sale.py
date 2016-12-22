#This file is part sale_carrier module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.pool import Pool, PoolMeta
from trytond.model import fields

__all__ = ['Sale']


class Sale:
    __metaclass__ = PoolMeta
    __name__ = 'sale.sale'

    @fields.depends('party')
    def on_change_party(self):
        super(Sale, self).on_change_party()

        self.carrier = None
        if self.party:
            if self.party.carrier:
                self.carrier = self.party.carrier
            else:
                Config = Pool().get('sale.configuration')
                configuration = Config(1)
                self.carrier = configuration.sale_carrier
