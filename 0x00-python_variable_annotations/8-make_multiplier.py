#!/usr/bin/env python3
"""
Complex types - functions
"""
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """
    function make_multiplier that takes a float multiplier as argument and
    returns a function that multiplies a float by multiplier.
    """
    def multiplier_function(x: float) -> float:
        """
        function that multiplies a float by multiplier.
        """
        return x * multiplier
    return multiplier_function
