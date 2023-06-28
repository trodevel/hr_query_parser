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
from print_helpers.helpers import print_fatal, print_error, print_warning, print_info, print_debug
from query_params import QueryParams
from common_types import HigherEducationLevel, LanguageLevel, LanguageWithLevel, JobFormat, Salary, RangeInt

##########################################################

class QueryParamsParser:

    locations: fuzzydict       = None
    skills:    fuzzydict       = None
    job_formats: fuzzydict     = None
    specializations: fuzzydict = None
    qualifications: fuzzydict  = None
    similarity_pct: int        = None

    def __init__( self ):
        self.locations         = fuzzydict_loader.load_inverse( 'assets/locations/locations.en.csv', True )
        self.skills            = fuzzydict_loader.load_inverse_w_synonyms( 'assets/skills/skills.en.csv', True )
        self.job_formats       = fuzzydict_loader.load_inverse_w_synonyms( 'assets/job_formats/job_formats.en.csv', True )
        self.specializations   = fuzzydict_loader.load_inverse_w_synonyms( 'assets/specializations/specializations.en.csv', True )
        self.qualifications    = fuzzydict_loader.load_inverse_w_synonyms( 'assets/qualifications/qualifications.en.csv', True )
        self.similarity_pct    = 85

    def __str__(self):
        return f"len( self.locations );len( self.skills )"

    def parse( self, s: str ) -> QueryParams:

        tokens = s.split()
        unmatched_tokens = []

        print_debug( f"parse: skills" )
        skills, unmatched_tokens = QueryParamsParser._parse_tokens( tokens, self.skills, self.similarity_pct )
        language_skills: list[LanguageWithLevel] = []
        salary: Optional[Salary]        = None
        experience: Optional[RangeInt]  = None

        print_debug( f"parse: locations" )
        locations_list, unmatched_tokens = QueryParamsParser._parse_tokens( unmatched_tokens, self.locations, self.similarity_pct )
        location: Optional[int]         = None

        if len( locations_list ):
            location = locations_list[ 0 ]

        age: Optional[RangeInt]         = None
        educations: list[HigherEducationLevel]  = []
        print_debug( f"parse: job_format" )
        job_format, unmatched_tokens = QueryParamsParser._parse_tokens( unmatched_tokens, self.job_formats, self.similarity_pct )

        print_debug( f"parse: specialization" )
        specializations, unmatched_tokens = QueryParamsParser._parse_tokens( unmatched_tokens, self.specializations, self.similarity_pct )

        print_debug( f"parse: qualifications" )
        qualifications, unmatched_tokens = QueryParamsParser._parse_tokens( unmatched_tokens, self.qualifications, self.similarity_pct )

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

        print_debug( f"_group_and_parse_tokens: tokens {tokens}, similarity_pct {similarity_pct}, token_group_size {token_group_size}" )

        res = []
        unmatched_tokens = []

        num_tokens = len( tokens )

        print_debug( f"_group_and_parse_tokens: num_tokens {num_tokens}, token_group_size {token_group_size}" )

        if num_tokens < token_group_size:
            print_debug( f"_group_and_parse_tokens: num_tokens {num_tokens} < token_group_size {token_group_size}" )
            return [ res, tokens ]

        rng=range( 0, num_tokens ) # DEBUG
        print_debug( f"_group_and_parse_tokens: range {rng}" )

        i = 0
        while i < num_tokens:

            subset = tokens[ i : i + token_group_size ]

            t = QueryParamsParser._join_tokens( subset )

            res_iter = d.find_all( t, similarity_pct )

            print_debug( f"_group_and_parse_tokens: i {i}, t '{t}', res_iter {len(res_iter)}: {res_iter}" )

            if len( res_iter ) > 0:
                print_debug( f"_group_and_parse_tokens: MATCH: i {i}, t '{t}', res_iter {len(res_iter)}: {res_iter}" )
                res += res_iter
                i += token_group_size
            else:
                unmatched_tokens.append( tokens[ i ] )
                i += 1


        print_debug( f"_group_and_parse_tokens: result: res {len(res)}: {res}, unmatched_tokens {unmatched_tokens}" )
        return [ res, unmatched_tokens ]

    def _parse_token( token: str, d: fuzzydict, similarity_pct: int  ) -> list:
        res = d.find_all( t, similarity_pct )
        return res

##########################################################
