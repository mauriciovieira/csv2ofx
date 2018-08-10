# coding: utf-8

from __future__ import (
    absolute_import, division, print_function, unicode_literals)

from operator import itemgetter
from datetime import datetime


def get_date(transaction):
    """Parses date from correct field"""

    transaction_date = transaction['Transaction date']

    # 26.07.2018 12:09
    parsed_date = datetime.strptime(transaction_date, '%d.%m.%Y %H:%M')

    return parsed_date.strftime('%m/%d/%Y')


mapping = {
    'has_header': True,
    'currency': itemgetter('Currency'),
    'bank': 'Leupay',
    'account': 'Undefined',
    'date': get_date,
    'amount': itemgetter('Amount'),
    'desc': itemgetter('Description'),
    'payee': itemgetter('Naam tegenpartij'),
}
