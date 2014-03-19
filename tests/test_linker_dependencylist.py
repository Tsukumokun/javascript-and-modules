from jam_tool.linker.dependencylist import dependency_list


def sunny_day_is_working(output):
    for i in range(4):
        if not output[i] in ['e','h','c','d']:
            return False
    for i in range(4,6):
        if not output[i] in ['b','f']:
            return False
    for i in range(6,9):
        if not output[i] in ['a','i','g']:
            return False
    return True

def test_sunny_day():
    assert sunny_day_is_working(\
        dependency_list({       \
            'a':set(['b','c']), \
            'b':set(['c','d']), \
            'e':set([]),        \
            'f':set(['c','e']), \
            'g':set(['h','f']), \
            'i':set(['f'])      \
        }))


def test_simple_loop():
    assert \
        dependency_list({       \
            'a':set(['b']),     \
            'b':set(['a'])      \
        })                      \
            ==                  \
        {'a': set(['b']), 'b': set(['a'])}

def test_loop_with_separate_dependency():
    assert \
        dependency_list({       \
            'a':set(['b']),     \
            'b':set(['c']),     \
            'c':set(['a','d']), \
            'd':set(['e'])      \
        })                      \
            ==                  \
    {'a': set(['b']), 'c': set(['a']), 'b': set(['c'])}

def test_self_loop():
    assert \
        dependency_list({       \
            'a':set(['a']),     \
            'b':set(['a'])      \
        })                      \
            ==                  \
        {'a': set(['a'])}

def test_two_loops():
    assert \
        dependency_list({       \
            'a':set(['b']),     \
            'b':set(['a']),     \
            'c':set(['d']),     \
            'd':set(['c'])      \
        })                      \
            ==                  \
        {'a': set(['b']), 'c': set(['d']), 'b': set(['a']), 'd': set(['c'])}
