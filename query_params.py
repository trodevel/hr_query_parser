#!/usr/bin/python3

'''
QueryParams.

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

from typing import Optional
from enum import Enum

##########################################################

def bool_to_str( v: bool ) -> str:
    if v:
        return "1"
    return "0"

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

class SkillWithLevel:
    skill: int                = None
    level: int                = None

class RangeInt:
    r_from: Optional[int]     = None
    r_to:   Optional[int]     = None

class RangeFloat:
    r_from: Optional[float]   = None
    r_to:   Optional[float]   = None

class QueryParams:

    specializations: list[int]      = []
    qualifications: list[int]       = []
    educations: list[int]           = []
    skills: list[int]               = []
    language_skills: list[SkillWithLevel] = None
    salary: Optional[RangeInt]      = None
    salary_currency: Optional[int]  = None
    age: Optional[RangeInt]         = None
    experience: Optional[RangeInt]  = None
    location: Optional[int]         = None
    job_format: Optional[JobFormat] = None

    def __init__( self, ad_id, title, price, is_negotiable, is_shipping_offered, shipping_price, num_photos ):
        self.ad_id                  = ad_id
        self.title                  = title
        self.price                  = price
        self.is_negotiable          = is_negotiable
        self.is_shipping_offered    = is_shipping_offered
        self.shipping_price         = shipping_price
        self.num_photos             = num_photos
        self.description            = ""
        self.photo_filenames        = []

    def __str__(self):
        return str( QueryParams.VERSION ) + ";" + self.ad_id + ";" + self.title + ";" + str( self.price ) \
            + ";" + bool_to_str( self.is_negotiable ) + ";" + bool_to_str( self.is_shipping_offered ) + ";" + str( self.shipping_price ) \
            + ";" + str( self.num_photos )

##########################################################