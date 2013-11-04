#This file is part sale_carrier module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.pool import Pool, PoolMeta

__all__ = ['Sale']
__metaclass__ = PoolMeta


class Sale:
    __name__ = 'sale.sale'

    def on_change_party(self):
        carrier = None
        changes = super(Sale, self).on_change_party()

        if self.party and self.party.carrier:
            carrier = self.party.carrier.id
        if self.party and not self.party.carrier:
            Config = Pool().get('sale.configuration')
            config = Config(1)
            if config.sale_carrier:
                carrier = config.sale_carrier.id

        changes['carrier'] = carrier
        return changes
