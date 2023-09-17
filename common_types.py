#!/usr/bin/python3

'''
Types.

Copyright (C) 2023 Dr. Sergey Kolevatov

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

'''

from enum import Enum
from languages.languages import Language
from currencies.currencies import Currency
from typing import Optional
from hr_query_parser.generic_str_helpers import optional_to_str

##########################################################

class RangeInt:
    value_from: Optional[int]     = None
    value_to:   Optional[int]     = None

    def __init__( self, value_from, value_to ):
        self.value_from     = value_from
        self.value_to       = value_to

    def __str__(self):
        return optional_to_str( self.value_from ) + ";" + optional_to_str( self.value_to )


class RangeFloat:
    value_from: Optional[float]   = None
    value_to:   Optional[float]   = None

class Salary:
    salary: RangeInt          = None
    currency: Currency        = None

    def __init__( self, salary, currency ):
        self.salary     = salary
        self.currency   = currency

    def __str__(self):
        return optional_to_str( self.salary ) + ";" + optional_to_str( self.currency )


##########################################################
