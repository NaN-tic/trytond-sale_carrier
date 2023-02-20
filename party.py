# This file is part sale_carrier module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields, ModelSQL
from trytond.pool import PoolMeta


class Party(metaclass=PoolMeta):
    __name__ = 'party.party'
    carrier = fields.Many2One('carrier', 'Carrier')
    carriers = fields.Many2Many('party.party-carrier', 'party', 'carrier',
        'Carriers')


class PartyCarrier(ModelSQL):
    'Party - Carrier'
    __name__ = 'party.party-carrier'
    party = fields.Many2One('party.party', 'Party', ondelete='CASCADE',
        required=True)
    carrier = fields.Many2One('carrier', 'Carrier', ondelete='CASCADE',
        required=True)
