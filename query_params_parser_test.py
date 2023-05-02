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

import query_params_parser

gl_parser = None

##########################################################

def get_parser():

    global gl_parser

    if not gl_parser:
        gl_parser = query_params_parser.QueryParamsParser()

    return gl_parser

##########################################################

def test_01():

    p = get_parser()

    d = p.parse( "node js" )

    print( f'test_01: {d}' )

##########################################################

def test():

    test_01()
    #test_02()
    #test_03()
    #test_04()

##########################################################

if __name__ == "__main__":
   test()

##########################################################
