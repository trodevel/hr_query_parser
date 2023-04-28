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
from common_types import HigherEducationLevel, LanguageWithLevel, JobFormat, Salary, RangeInt
from generic_str_helpers import list_to_str_w_size, optional_to_str, optional_to_str_w_brackets

##########################################################

class QueryParams:

    specializations: list[int]      = []
    qualifications: list[int]       = []
    skills: list[int]               = []
    language_skills: list[LanguageWithLevel] = None
    salary: Optional[Salary]        = None
    experience: Optional[RangeInt]  = None
    location: Optional[int]         = None
    age: Optional[RangeInt]         = None
    educations: list[HigherEducationLevel]  = []
    job_format: Optional[JobFormat] = None

    def __init__( self, specializations, qualifications, skills, language_skills, salary, experience, location, age, educations, job_format ):
        self.specializations   = specializations
        self.qualifications    = qualifications
        self.skills            = skills
        self.language_skills   = language_skills
        self.salary            = salary
        self.experience        = experience
        self.location          = location
        self.age               = age
        self.educations        = educations
        self.job_format        = job_format

    def __str__(self):
        return list_to_str_w_size( self.specializations ) + ";" + list_to_str_w_size( self.qualifications ) + ";" + list_to_str_w_size( self.skills ) \
            + ";" + list_to_str_w_size( self.language_skills ) \
            + ";" + optional_to_str_w_brackets( self.salary ) \
            + ";" + optional_to_str_w_brackets( self.experience ) \
            + ";" + optional_to_str_w_brackets( self.location ) \
            + ";" + optional_to_str_w_brackets( self.age ) \
            + ";" + list_to_str_w_size( self.educations ) \
            + ";" + optional_to_str_w_brackets( self.job_format )

##########################################################
