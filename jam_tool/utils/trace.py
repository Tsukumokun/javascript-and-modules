#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Retained Description:
 This module provides tracing functionality.

 It provides the possibility to print information for the user in four
 different ways. Each of them react differently on settings and will print
 the information to different destinations.

Modification Description:
 Adds additional functionality for more types of tracing messages
 including code output as well as color support.
"""

__author__     = ["Christopher Kelley (Tsukumo Chiaki)",
                  "Original: Till Smejkal"]
__copyright__  = ["Copyright 2014, Christopher Kelley",
                  "Copyright 2014, Till Smejkal"]
__credits__    = ["Till Smejkal, original concept design"]
__license__    = ["http://creativecommons.org/licenses/by-nc-nd/4.0/deed.en_US",\
                  "MIT"]
__version__    = "0.0.1"
__maintainer__ = "Christopher Kelley"
__email__      = "tsukumokun@icloud.com"
__status__     = "Development"


# python language imports
import sys
from inspect import stack, getframeinfo

# project internal imports
#import jam_tool.utils.termcaps as color
import termcaps as color

# These variables are used to globally turn
# on or off debug or info messages.
_debug = False
_quiet = False


def _location():
    """
    @brief Add additional information to the message.

    This method will reuturn the file name, the function name and the line number
    of the calling method to the message.

    >>> def test():print(_location())
    >>> test()
    <doctest __main__._location[1]> - <module> (1) -- \


    @returns A combination of information such as the file name,
             line number and function name of the invoking method.
    """
    # As we are called by the tracing method we have to go two levels up in
    # the stack frames. The information we are interested in is the first
    # element in the stack frame.
    frame = stack()[2][0]

    # Get the information from the stack frame of interest.
    info = getframeinfo(frame)

    # Construct the location information
    location = ("{fileName} - {functionName} ({lineNumber}) -- ").format(
        fileName = info.filename,
        functionName = info.function,
        lineNumber = info.lineno
    )

    return location

def init(debugEnabled, quietEnabled):
    """
    @brief Initialize the tracing functionality.

    This method will set the debug and quiet flags which are used internally
    to the given values.

    >>> init(True,False)

    @param[in] debugEnabled Whether debug output is allowed or not.
    @param[in] quietEnabled Whether info output is forbidden or not.
    """
    global _debug
    global _quiet

    _debug = debugEnabled
    _quiet = quietEnabled


def error(message):
    """
    @brief Print the error message and exit the program.

    The message will be printed to stderr and the program will exit with exit
    code 3 after that.

    >>> color.make_boring()
    >>> bak = sys.stderr
    >>> sys.stderr = sys.stdout
    >>> error('msg')
    trace.py: error: msg
    >>> sys.stderr = bak
    >>> color.make_exciting()

    @param[in] message The message which should be displayed.
    """
    print("".join([sys.argv[0],": ",color.start("red"),"error: ",
        color.default(),message]), file=sys.stderr)


def warning(message):
    """
    @brief Print the warning message but don't exit the program.

    The message will also be printed to stderr but the program will continue
    after the call to this method.

    >>> color.make_boring()
    >>> bak = sys.stderr
    >>> sys.stderr = sys.stdout
    >>> warning('msg')
    trace.py: warning: msg
    >>> sys.stderr = bak
    >>> color.make_exciting()

    @param[in] message The message which should be displayed.
    """
    print("".join([sys.argv[0],": ",color.start("yellow"),"warning: ",
        color.default(),message]), file=sys.stderr)


def debug(message):
    """
    @brief Print the debug message if debug is enabled.

    The message will be printed out to stderr but just if debug output was
    enabled.

    >>> debug('msg')

    @param[in] message The message which should be displayed.
    """
    if _debug:
        print("".join([_location(),color.start("green"),"debug: ",
            color.default(),message]), file=sys.stderr)


def info(message):
    """
    @brief Print a message for the user if debug is enabled or quiet disabled.

    The message will be printed out to stdout but just if debug is enabled or
    quiet disabled.

    >>> info('msg')
    msg

    @param[in] message The message which should be displayed.
    """
    if not _quiet or _debug:
        print(message, file=sys.stdout)


def highlight(message):
    """
    @brief Print a message for the user if debug is enabled or quiet disabled.

    The message will be printed out to stdout but just if debug is enabled or
    quiet disabled. Also prints with a blue color to make the message stand out.

    >>> color.make_boring()
    >>> highlight('msg')
    msg
    >>> color.make_exciting()

    @param[in] message The message which should be displayed.
    """
    if not _quiet or _debug:
        print("".join([color.start("blue"),message,
            color.default()]), file=sys.stdout)


def _code_message(level,message,code,file,line,char,hint):
    """
    @brief Print a message for the user and point to a line of code.

    The message will be printed the same as a normal message but will
    be followed by the offending line of code and perhaps a character
    position marker.

    >>> color.make_boring()
    >>> bak = sys.stderr
    >>> sys.stderr = sys.stdout
    >>> _code_message('level','message','code','file',8,6,'hint')
    file:8:6: levelmessage
        code
        -----^
              hint
    >>> sys.stderr = bak
    >>> color.make_exciting()

    @param[in] level The level of message being displayed
    @param[in] message The message which should be displayed.
    @param[in] file The file where the message was produced.
    @param[in] code The offending line of code to be displayed.
    @param[in] char The character position where the message starts.
    @param[in] hint Some hint about the message.
    """
    # Default information to unspecified
    # Important to do here so the user may pass in NoneType
    file = file or "unspecified"
    line = line or "unspecified"
    char = char or "unspecified"

    # Format the information to be printed
    info = "{file}:{line}:{char}: ".format(file=file,line=line,char=char)

    # Print the information, a warning label, and the message
    print("".join([info,level,message]), file=sys.stderr)

    # Print the code prefixed by a 4 space gutter
    print(" "*4+code, file=sys.stderr)

    # If a character was specified print a marker
    if char != "unspecified":
        print("".join([" "*4,"-"*(char-1),color.start("green"),"^",
            color.default()]), file=sys.stderr)
        # If a hint was specified with a character print the
        # hint with that offset
        if hint != None:
            print("".join([" "*(char+4),color.start("green"),hint,
                color.default()]), file=sys.stderr)
    # Otherwise if there is a hint just print it
    elif hint != None:
            print("".join([color.start("green"),hint,
                color.default()]), file=sys.stderr)


def code_warning(message,code,file=None,line=None,char=None,hint=None):
    """
    @brief Print a message for the user and point to the line of code.

    The message will be printed the same as a normal warning but will
    be followed by the offending line of code and perhaps a character
    position marker.

    >>> color.make_boring()
    >>> bak = sys.stderr
    >>> sys.stderr = sys.stdout
    >>> code_warning('message','code','file',8,6,'hint')
    file:8:6: warning: message
        code
        -----^
              hint
    >>> sys.stderr = bak
    >>> color.make_exciting()

    @param[in] message The message which should be displayed.
    @param[in] file The file where the warning was produced.
    @param[in] code The offending line of code to be displayed.
    @param[in] char The character position where the warning starts.
    @param[in] hint Some hint to fix the warning.
    """
    _code_message("".join([color.start("yellow"),"warning: ",
        color.default()]),message,code,file,line,char,hint)

def code_error(message,code,file=None,line=None,char=None,hint=None):
    """
    @brief Print a message for the user and point to the line of code.

    The message will be printed the same as a normal error but will
    be followed by the offending line of code and perhaps a character
    position marker.

    >>> color.make_boring()
    >>> bak = sys.stderr
    >>> sys.stderr = sys.stdout
    >>> code_error('message','code','file',8,6,'hint')
    file:8:6: error: message
        code
        -----^
              hint
    >>> sys.stderr = bak
    >>> color.make_exciting()

    @param[in] message The message which should be displayed.
    @param[in] file The file where the error was produced.
    @param[in] code The offending line of code to be displayed.
    @param[in] char The character position where the error starts.
    @param[in] hint Some hint to fix the error.
    """
    _code_message("".join([color.start("red"),"error: ",
        color.default()]),message,code,file,line,char,hint)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
