#!/usr/bin/python3

'''
QueryParamsParser.

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

from fuzzydict import fuzzydict
from query_params import QueryParams

##########################################################

class QueryParamsParser:

    locations: fuzzydict       = None
    skills:    fuzzydict       = None

    def __init__( self ):
        self.locations         = locations
        self.skills            = skills

    def __str__(self):
        return f"len( self.locations );len( self.skills )"

##########################################################
