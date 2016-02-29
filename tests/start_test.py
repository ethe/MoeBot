# -*- coding:utf-8 -*-

import sys
sys.path.append("../moebot")


def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    test()
