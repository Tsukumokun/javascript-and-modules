#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module provides styled terminal printing functionality.
"""

__author__     = "Christopher Kelley (Tsukumo Chiaki)"
__copyright__  = "Copyright 2014, Christopher Kelley"
__credits__    = []
__license__    = "http://creativecommons.org/licenses/by-nc-nd/4.0/deed.en_US"
__version__    = "0.0.1"
__maintainer__ = "Christopher Kelley"
__email__      = "tsukumokun@icloud.com"
__status__     = "Development"


# python language imports
import os

# Defines the permissable colors for terminal output
_colors = {
    "black"     :"0", #< ANSI modifiers
    "red"       :"1",
    "green"     :"2",
    "yellow"    :"3",
    "blue"      :"4",
    "magenta"   :"5",
    "cyan"      :"6",
    "white"     :"7",
    "default"   :"9"
}

# Defines the permissable attributes for terminal output
_attribs = {
    "default"   :"0", #< ANSI modifiers
    "bold"      :"1",
    "dim"       :"2",
    "italic"    :"3",
    "underline" :"4",
    "blink"     :"5",
    "blink_fast":"6",
    "reverse"   :"7",
    "conceal"   :"8",
    "crossed"   :"9"
}

# Defines if these methods should return nothing
# used to turn off styled printing for the entire project
_boring = False

# Defines the escape sequence used to send colors
_escape = "\033["


def make_boring():
    """
    @brief Turn off styled printing.

    This method will set the boring flag which will be checked
    when a start or end termcap is requested. If boring is set
    to true then nothing will be returned and therefore there
    will be no style on the resulting text.

    >>> make_boring()
    >>> make_exciting()

    """
    global _boring

    _boring = True


def make_exciting():
    """
    @brief Turn on styled printing.

    This method will set the boring flag which will be checked
    when a start or end termcap is requested. If boring is set
    to false then the normal termcaps will be returned and
    therefore there will be style on the resulting text.

    >>> make_boring()
    >>> make_exciting()

    """
    global _boring

    _boring = False


def start(foreground=None,background=None,attribute=None):
    """
    @brief Starts a terminal style as specified

    >>> import sys
    >>> print(start("red","yellow",\
        "reverse")+"oooo"+default(),file=sys.stderr)

    @param[in] foreground Color to set the foreground to.
    @param[in] background Color to set the background to.
    @param[in] attribute Style to set the attribute to.

    @return the string needed to start the specified terminal style
    """
    if not os.getenv("ANSI_COLORS_DISABLED") is None or _boring:
        return ""

    # Begin the string with the escape sequence
    holder = _escape

    # If there is a foreground specified add it to the sequence
    if foreground != None:
        holder += "3"+_colors[foreground] #< ANSI foreground starts with 3
        # If either of the others are defined add a semi-colon for formatting
        if background != None or attribute != None:
            holder += ";"

    # If there is a background specified add it to the sequence
    if background != None:
        holder += "4"+_colors[background] #< ANSI background starts with 4
        # If there is also an attribute defined add a semi-color for formatting
        if attribute != None:
            holder += ";"

    # If there is an attribute specified add it to the sequence
    if attribute != None:
        holder += _attribs[attribute] #< ANSI attributes aren't prefixed

    # Add the modifier ending to the sequence
    holder += "m"

    return holder


def end(foreground=False,background=False,attribute=None):
    """
    @brief Ends a terminal style as specified

    >>> import sys
    >>> print(start("red","yellow",\
        "reverse")+"oo"+end(attribute="reverse")+"oo"+default(),\
        file=sys.stderr)

    @param[in] foreground Color to set the foreground to.
    @param[in] background Color to set the background to.
    @param[in] attribute Style to set the attribute to.

    @return the string needed to end the specified terminal style
    """
    if not os.getenv("ANSI_COLORS_DISABLED") is None or _boring:
        return ""

    # Begin the string with the escape sequence
    holder = _escape

    # If foreground true remove it by writing the default foreground color
    if foreground:
        holder += "3"+_colors["default"] #< ANSI foreground starts with 3
        # If either of the others are defined add a semi-colon for formatting
        if background or attribute != None:
            holder += ";"

    # If background true remove it by writing the default background color
    if background:
        holder += "4"+_colors["default"] #< ANSI background starts with 4
        # If there is also an attribute defined add a semi-color for formatting
        if attribute != None:
            holder += ";"

    # If there is an attribute specified add it to the sequence
    if attribute != None:
        holder += "2"+_attribs[attribute]

    # Add the modifier ending to the sequence
    holder += "m"

    return holder


def default():
    """
    @brief Ends all terminal styles

    >>> import sys
    >>> print(start("red","yellow",\
        "reverse")+"oo"+default()+"oo",\
        file=sys.stderr)

    @return the string needed to set the terminal style to default
    """
    if not os.getenv("ANSI_COLORS_DISABLED") is None or _boring:
        return ""

    # Return the default ANSI sequence of 0
    return _escape + "0m"


def clear():
    """
    @brief Clears the terminal screen

    disabled>>> import sys
    disabled>>> print(clear(),file=sys.stderr)

    @return the string needed to clear the terminal screen
    """
    # Return the clear ANSI sequence of 2J
    return _escape + "2J"

def move_cursor(x,y):
    """
    @brief Moves the cursor to the given x,y

    disabled>>> import sys
    disabled>>> print(move_cursor(50,50)+"oo",file=sys.stderr)

    @return the string needed to move the cursor to the specified position
    """
    # Return the make ANSI sequence
    return "".join([_escape, str(x), ";", str(y), "H"])

def reset_cursor():
    """
    @brief Resets the cursor to 0,0 on the screen

    disabled>>> import sys
    disabled>>> print(reset_cursor(),file=sys.stderr)

    @return the string needed to reset the cursor
    """
    # Return the blank cursor ANSI sequence of ;H
    return _escape + ";H"

def reset_screen():
    """
    @brief Clears the screen and resets the cursor to 0,0

    disabled>>> import sys
    disabled>>> print(reset_screen(),file=sys.stderr)

    @return the string needed to clear the screen and reset the cursor
    """
    # Return the clear and blank cursor ANSI sequences of 2j and ;H
    return _escape + "2J" + _escape + ";H"


def easter_egg(line):
    """
    @brief It's an easter egg!

    >>> import sys
    >>> print(easter_egg("easter egg"),\
        file=sys.stderr)

    @return the string needed to set the terminal style to default
    """
    modifier  = 1
    colors    = ["red","yellow","green",\
                 "cyan","blue","magenta"]
    where     = 0
    what      = ""
    for char in line:
        what += start(colors[where]) + char
        if where > 4:
            modifier = -1
        elif where < 1:
            modifier = 1
        where += modifier
    return what + default()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
