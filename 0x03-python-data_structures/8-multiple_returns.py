#!/usr/bin/python3
# 8-multiple_returns.py
# clifford karimi<Ckarimi676@gmail.com>

def multiple_returns(sentence):
    """Returns the length of a string and its first character."""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
