#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 'jam' - is a compiler for javascript which allows for the
#         use of modules, providing a way to import and 
#         minify all of the source files.
# Copyright (C) 2014 Christopher Kelley <tsukumokun(at)icloud.com>
# 
# This work is licensed under the 
# Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 
# International License. To view a copy of this license, visit 
# http://creativecommons.org/licenses/by-nc-nd/4.0/deed.en_US.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.


"""
The jam library module file.
"""

__author__     = "Christopher Kelley (Tsukumo Chiaki)"
__copyright__  = "Copyright (C) 2014, Christopher Kelley"
__credits__    = []
__license__    = "Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International"
__version__    = "0.0.1"
__maintainer__ = "Christopher Kelley"
__email__      = "tsukumokun@icloud.com"
__status__     = "Development"


from jam_tool.jam_tool import jam


__all__ = ['jam']
