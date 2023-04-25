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
from languages import Language
from currencies import Currency
from typing import Optional

##########################################################

class JobFormat(int, Enum):
    UNDEF = 0
    OFFICE_ONLY = 1
    OFFICE_AND_REMOTE = 2
    REMOTE_ONLY = 3

class Qualification(int, Enum):
    undef = 0
    intern = 1
    junior = 2
    middle = 3
    senior = 4
    lead = 5

class HigherEducationLevel(int, Enum):
    UNDEF = 0
    BACHELOR = 1
    MASTER = 2
    PHD = 3

class LanguageLevel(int, Enum):
    undef = 0
    beginner = 1
    intermediate = 2
    advanced = 3
    native = 4

class LanguageWithLevel:
    language: Language        = None
    level: LanguageLevel      = None

class RangeInt:
    r_from: Optional[int]     = None
    r_to:   Optional[int]     = None

class RangeFloat:
    r_from: Optional[float]   = None
    r_to:   Optional[float]   = None

class Salary:
    salary: RangeInt          = None
    currency: Currency        = None

##########################################################
