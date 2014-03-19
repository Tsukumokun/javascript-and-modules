#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The jam library utils dependency list file.
"""

__author__     = "Christopher Kelley (Tsukumo Chiaki)"
__copyright__  = "Copyright 2014, Christopher Kelley"
__credits__    = []
__license__    = "http://creativecommons.org/licenses/by-nc-nd/4.0/deed.en_US"
__version__    = "0.0.1"
__maintainer__ = "Christopher Kelley"
__email__      = "tsukumokun@icloud.com"
__status__     = "Development"


def dependency_list(depdict):
    """
    @brief Given a dictionary of dependencies, returns the order
           in which they should be included as a list

    Requires:
        dictionary in the format of
        {
            file:Set(dependency[,dependency][,dep...]),
            file:Set(dep...),
            file...
        }
    Ensures:
        The returned list will be in any order given that this order
        ensures a file which another depends on will come before
        it in the list.
        If there was an error in making the list such as a dependency
        loop, a dictionary with the loop will be returned.

    Process:
        Loop through dependencies dictionary doing the following
        process until there are no more items in the dictionary.

        #1< Create a set of files which have no dependencies.
        #2< If this list is empty but the dictionary is not
            it means there is an issue, likely a dependency
            loop, so clean out the files which depend on the
            loop and return the rest as a dictionary.
        #3< Append this set to the list to be returned.
        #4< Go through the dictionary removing any files
            which have no dependencies left and removing the
            newly added files from the other dependency sets.

    @param[in] depdict Dictionary of dependencies as specified by
               Requires.
    @return a list of dependencies in the correct order to include as
            specified by Ensures or a dictionary specifying a failure
            due to a loop in the dependencies.

    """
    deplist=[]
    while depdict:
    #1< # Independent dependencies, values with no key
        nodep = set(dep for item in depdict.values() for dep in item)
        nodep = nodep - set(depdict.keys())

        # Independent dependencies, keys with no values
        for item in depdict:
            if not depdict[item]:
                nodep.add(item)

    #2< # Detect loop
        if not nodep:
            # Remove all keys which are not also values
            vals = set(val for item in depdict.values() for val in item)
            stor = { }
            for item in depdict:
                if item in vals:
                    stor[item] = depdict[item]
            return stor

    #3< # Add items without dependency
        deplist.append(nodep)

    #4< # Remove nodeps
        stor = { }
        for item in depdict:
            if depdict[item]:
                stor[item] = depdict[item] - nodep
        depdict = stor

    return list(dep for item in deplist for dep in item)

if __name__=='__main__':
    import doctest
    doctest.testmod()
