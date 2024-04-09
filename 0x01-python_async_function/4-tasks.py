#!/usr/bin/env python3
""" Module to run multiple coroutines at the same time with async"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Function that returns the list of all the delays (float values).
        The list of the delays should be in ascending order without
        using sort() because of concurrency."""

    # Create a list to hold the results
    delays = []

    async def _task(index: int):
        # Call the task_wait_random coroutine
        delay = await task_wait_random(max_delay)
        # Insert the delay at the correct position in ascending order
        for i, d in enumerate(delays):
            if delay < d:
                delays.insert(i, delay)
                break
        else:
            delays.append(delay)  # Append if delay is larger than all in list

    # Create tasks and gather them
    await asyncio.gather(*[_task(i) for i in range(n)])

    return delays
