#!/usr/bin/env python3
"""
Tasks
"""
import asyncio
import typing
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    task_wait_n should return the list of all the delays (float values).
    The list of the delays should be in ascending order
    """
    waitlist = [task_wait_random(max_delay) for _ in range(n)]
    completed = await asyncio.gather(*waitlist)
    return sorted(completed)
