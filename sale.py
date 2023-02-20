# This file is part sale_carrier module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool, PoolMeta
from trytond.model import fields

__all__ = ['Sale']


class Sale(metaclass=PoolMeta):
    __name__ = 'sale.sale'

    @staticmethod
    def default_carrier():
        Config = Pool().get('sale.configuration')
        config = Config(1)
        return config.sale_carrier.id if config.sale_carrier else None

    @fields.depends('party')
    def on_change_party(self):
        super(Sale, self).on_change_party()

        if self.party and self.party.carrier:
            self.carrier = self.party.carrier

    @fields.depends('party')
    def on_change_with_available_carriers(self, name=None):
        available_carriers = super(Sale, self).on_change_with_available_carriers(name)
        if self.party:
            if self.party.carriers:
                available_carriers += [c.id for c in self.party.carriers]
            if self.party.carrier:
                available_carriers += [self.party.carrier.id]
        return list(set(available_carriers))
