#!/usr/bin/env python
# -*- coding: utf-8 -*-

def test_a():
    assert 'a' == 'a'

def b():
    assert 'b' == 'b'

class Two:
    def test_two(self):
        assert 'b' == 'b'

import nose

if __name__ == "__main__":
    nose.main()
