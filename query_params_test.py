#!/usr/bin/python3

'''
fuzzydict test.

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

import query_params
from languages import Language
from currencies import Currency
from common_types import HigherEducationLevel, LanguageLevel, LanguageWithLevel, JobFormat, Salary, RangeInt

##########################################################

def test_01():

    d = query_params.QueryParams( [ 111, 222 ], [ 777, 888 ], [ 999 ], \
        [ LanguageWithLevel( Language.en, LanguageLevel.advanced ) ],
        Salary( RangeInt( 0, 200000 ), Currency.EUR ),
        RangeInt( 0, 2 ),
        555,
        RangeInt( 20, 50 ),
        [ HigherEducationLevel.BACHELOR ],
        JobFormat.OFFICE_AND_REMOTE )

    print( f'test_01: {d}' )

##########################################################

def test_02():

    d = query_params.QueryParams( [ ], [ ], [ ], \
        [ LanguageWithLevel( Language.en, LanguageLevel.advanced ) ],
        None,
        None,
        None,
        None,
        [ ],
        None )

    print( f'test_02: {d}' )

##########################################################

def test_03():

    d = query_params.QueryParams( [ 111, 222 ], [ 777, 888 ], [ 999 ], \
        [ LanguageWithLevel( Language.en, LanguageLevel.advanced ), \
             LanguageWithLevel( Language.de, LanguageLevel.beginner ) ],
        Salary( RangeInt( 0, 85000 ), Currency.EUR ),
        RangeInt( 0, 2 ),
        555,
        RangeInt( 20, 50 ),
        [ HigherEducationLevel.MASTER ],
        JobFormat.OFFICE_AND_REMOTE )

    print( f'test_03: {d}' )

##########################################################

def test():

    test_01()
    test_02()
    test_03()

##########################################################

if __name__ == "__main__":
   test()

##########################################################
