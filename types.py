#!/usr/bin/python3

'''
Types.

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

from enum import Enum

##########################################################

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

##########################################################
