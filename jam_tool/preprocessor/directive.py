#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module defines the interface which must be implemented
by every class which wants to act as a preprocessor directive
inside the jam program preprocessor.
"""

__author__     = "Christopher Kelley (Tsukumo Chiaki)"
__copyright__  = "Copyright 2014, Christopher Kelley"
__credits__    = []
__license__    = "http://creativecommons.org/licenses/by-nc-nd/4.0/deed.en_US"
__version__    = "0.0.1"
__maintainer__ = "Christopher Kelley"
__email__      = "tsukumokun@icloud.com"
__status__     = "Development"


class Directive:
    """
    @brief This class defines the interface which must be implemented by
           every directive.

    Each directive must provide the functions which are defined in this class.
    If some functionality is not needed, a function can be left unimplemented
    and the default implementation defined here will be used.
    """

    def start(self,file_path):
        """
        @brief This method will be used to indicate that a new file will be
               processed.

        Directives can implement this method to clear any cached information
        they may be storing for the last file.

        @param[in] self      The current instance.
        @param[in] file_path The path of the new file.
        """
        pass

    def finish(self):
        """
        @brief This method will be used to indicate that a file has
               finished being processed.

        Directives can implement this method to return any information
        that should be output into the file for the linker.

        @param[in] self The current instance.
        @return any information needed by the linker as a string
        """
        return ""

    def process_line(self,line,line_number):
        """
        @brief This method will be used to process an indivdua.

        Directives can implement this method to return any information
        that should be output into the file for the linker.

        @param[in] self The current instance.
        @param[in] line The line being processed.
        @param[in] line_number The line number.
        @return true if this directive used the line, false otherwise.
        """
        return False


