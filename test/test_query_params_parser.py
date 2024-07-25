#!/usr/bin/python3

'''
test.

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

from hr_query_parser.query_params_parser import QueryParamsParser
from print_helpers.helpers import set_log_level, DEBUG

gl_parser = None

##########################################################

def get_parser():

    global gl_parser

    if not gl_parser:
        gl_parser = QueryParamsParser( '../assets' )

    return gl_parser

##########################################################

def test_kern( name: str, text: str ):

    p = get_parser()

    d = p.parse( text )

    print( f'{name}: \'{text}\' ==> {d}' )

##########################################################

def test_01():

    test_kern( "test_01", "node js" )

##########################################################

def test_02():

    test_kern( "test_02", "node js react" )

##########################################################

def test_03():

    test_kern( "test_03", "node js munich" )

##########################################################

def test_04():

    test_kern( "test_04", "node js ontario" )

##########################################################

def test_05():

    test_kern( "test_05", "node js ontario" )
    test_kern( "test_05", "node js ontario office" )
    test_kern( "test_05", "node js ontario remote" )
    test_kern( "test_05", "node js ontario office and remote" )
    test_kern( "test_05", "node js ontario hybrid" )

##########################################################

def test_06():

    test_kern( "test_06", "node js ontario backend" )
    test_kern( "test_06", "node js ontario backend developer" )
    test_kern( "test_06", "node js ontario fullstack" )

##########################################################

def test_07():

    test_kern( "test_07", "node js ontario junior" )
    test_kern( "test_07", "node js ontario middle" )
    test_kern( "test_07", "node js ontario senior" )
    test_kern( "test_07", "node js ontario lead" )

##########################################################

def test():

    set_log_level( DEBUG )

    test_01()
    test_02()
    test_03()
    test_04()
    test_05()
    test_06()
    test_07()

##########################################################

if __name__ == "__main__":
   test()

##########################################################
