#!/usr/bin/env python3
"""
This module contains an asynchronous routine that utilizes task_wait_random
to spawn multiple asyncio Tasks concurrently. It gathers all the generated
delays and returns them in ascending order upon completion.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay value
    and collects the execution delays in an ascending sorted floating list.

    Args:
        n (int): The number of times to spawn the asynchronous task.
        max_delay (int): The maximum delay bound for the tasks.

    Returns:
        List[float]: A list of all execution delays sorted in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []

    for task in asyncio.as_completed(tasks):
        delay: float = await task
        delays.append(delay)

    return delays
