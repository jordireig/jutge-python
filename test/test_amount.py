from __future__ import unicode_literals
import jutge


def test_1():
    source = open('./test/text/source3.txt', 'r')
    expected = range(1, 13)
    input_gen = jutge.read(int, file=source, amount=12)
    assert all(next(input_gen) == val for val in expected)
