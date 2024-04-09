#!/usr/bin/env python3
""" Module to run multiple coroutines at the same time with async"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Function that returns the list of all the delays (float values).
        The list of the delays should be in ascending order without
        using sort() because of concurrency."""

    delays = [task_wait_random(max_delay) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
