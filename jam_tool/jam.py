#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The jam library utils module file.
"""

__author__     = "Christopher Kelley (Tsukumo Chiaki)"
__copyright__  = "Copyright 2014, Christopher Kelley"
__credits__    = []
__license__    = "http://creativecommons.org/licenses/by-nc-nd/4.0/deed.en_US"
__version__    = "0.0.1"
__maintainer__ = "Christopher Kelley"
__email__      = "tsukumokun@icloud.com"
__status__     = "Development"


class Jam:
    """
    @brief The interface which should be used to interact with the tool.

    This class will do all the needed steps to perform the task correctly.
    Which includes:
        - parsing and providing command line arguments
    """

    # 'private' member


    # 'private' methods
    def _configure(self):
        """
        @brief This method will do the internal configuration of the class.

        Within this method we will perform the following steps:
            - pass

        @param[in] self The current instance.
        """
        pass

    # 'public' methods
    def __init__(self):
        """
        @brief The constructor for this class.

        The constructor will configure the current instance of the
        class by calling the private 'configure' method.

        @param[in] self The current instance
        """
        # Configure the instance.
        self._configure()


    def run(self):
        """
        @brief This method will run all configured checks on all found files.

        Run the checks on the files, correct them if configured and exit
        correctly.

        @param[in] self The current instance.
        """
        # Verify process is working #< TEMPORARY
        print ('Jam is running')
