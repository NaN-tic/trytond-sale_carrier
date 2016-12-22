# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['Configuration']


class Configuration:
    __metaclass__ = PoolMeta
    __name__ = 'sale.configuration'
    sale_carrier = fields.Property(fields.Many2One('carrier', 'Carrier',
        domain=[('carrier_product.salable', '=', True)],
        ))
