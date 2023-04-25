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

##########################################################

def bool_to_str( v: bool ) -> str:
    if v:
        return "1"
    return "0"

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
        return str( QueryParams.VERSION ) + ";" + self.specializations + ";" + self.qualifications + ";" + str( self.skills ) \
            + ";" + bool_to_str( self.language_skills ) + ";" + bool_to_str( self.salary ) + ";" + str( self.experience ) \
            + ";" + str( self.location )

##########################################################
