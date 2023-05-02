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
from fuzzydict_loader import fuzzydict_loader
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

        specializations: list[int]      = []
        qualifications: list[int]       = []
        skills = _parse_tokens( tokens, self.skills, self.similarity_pct )
        language_skills: list[LanguageWithLevel] = None
        salary: Optional[Salary]        = None
        experience: Optional[RangeInt]  = None
        location: Optional[int]         = None
        age: Optional[RangeInt]         = None
        educations: list[HigherEducationLevel]  = []
        job_format: Optional[JobFormat] = None

        res = QueryParams( specializations, qualifications, skills, language_skills, salary, experience, location, age, educations, job_format )

        return res

    def _parse_tokens( tokens, d: fuzzydict, similarity_pct: int ) -> list:

        res = []

        for t in tokens:
            res_iter = d.find_all_elems( t, similarity_pct )
            res += res_iter

        return res

    def _parse_token( token: str, d: fuzzydict, similarity_pct: int  ) -> list:
        res = d.find_all( t, similarity_pct )
        return res

##########################################################
