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
from fuzzydict import fuzzydict_loader
from query_params import QueryParams
from common_types import HigherEducationLevel, LanguageLevel, LanguageWithLevel, JobFormat, Salary, RangeInt

##########################################################

class QueryParamsParser:

    locations: fuzzydict       = None
    skills:    fuzzydict       = None
    similarity_pct: int        = None

    def __init__( self ):
        self.locations         = fuzzydict_loader.load( 'resources/locations.eng.csv' )
        self.locations.set_caseinsensitive( True )
        self.skills            = fuzzydict_loader.load( 'resources/skills.eng.csv' )
        self.skills.set_caseinsensitive( True )
        self.similarity_pct    = 85

    def __str__(self):
        return f"len( self.locations );len( self.skills )"

    def parse( self, s: str ) -> QueryParams:

        tokens = s.split()
        unmatched_tokens = []

        specializations: list[int]      = []
        qualifications: list[int]       = []
        skills, unmatched_tokens = QueryParamsParser._parse_tokens( tokens, self.skills, self.similarity_pct )
        language_skills: list[LanguageWithLevel] = []
        salary: Optional[Salary]        = None
        experience: Optional[RangeInt]  = None

        locations_list, unmatched_tokens = QueryParamsParser._parse_tokens( unmatched_tokens, self.locations, self.similarity_pct )
        location: Optional[int]         = None

        if len( locations_list ):
            location = locations_list[ 0 ]

        age: Optional[RangeInt]         = None
        educations: list[HigherEducationLevel]  = []
        job_format: Optional[JobFormat] = None

        res = QueryParams( specializations, qualifications, skills, language_skills, salary, experience, location, age, educations, job_format )

        return res

    def _parse_tokens( tokens, d: fuzzydict, similarity_pct: int ) -> [ list, list ]:

        res = []
        unmatched_tokens = []

        res_iter, unmatched_tokens = QueryParamsParser._group_and_parse_tokens( tokens, d, similarity_pct, 3 )
        res += res_iter

        res_iter, unmatched_tokens = QueryParamsParser._group_and_parse_tokens( unmatched_tokens, d, similarity_pct, 2 )
        res += res_iter

        res_iter, unmatched_tokens = QueryParamsParser._group_and_parse_tokens( unmatched_tokens, d, similarity_pct, 1 )
        res += res_iter

        return [ res, unmatched_tokens ]

    def _join_tokens( tokens_subset ) -> str:

        res = ' '.join( str(e) for e in tokens_subset )

        return res


    def _group_and_parse_tokens( tokens, d: fuzzydict, similarity_pct: int, token_group_size: int ) -> [ list, list ]:

        print( f"DEBUG: _group_and_parse_tokens: tokens {tokens}, similarity_pct {similarity_pct}, token_group_size {token_group_size}" )

        res = []
        unmatched_tokens = []

        for i in range( 0, len( tokens ), token_group_size ):

            subset = tokens[ i : i + token_group_size ]

            t = QueryParamsParser._join_tokens( subset )

            res_iter = d.find_all_elems( t, similarity_pct )

            print( f"DEBUG: _group_and_parse_tokens: t '{t}', res_iter {res_iter}" )

            if not len( res_iter ):
                unmatched_tokens = subset

            res += res_iter

        return [ res, unmatched_tokens ]

    def _parse_token( token: str, d: fuzzydict, similarity_pct: int  ) -> list:
        res = d.find_all( t, similarity_pct )
        return res

##########################################################
