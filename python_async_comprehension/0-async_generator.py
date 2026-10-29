#!/usr/bin/env python3
"""
This module provides an asynchronous generator function designed to yield
random float values. It demonstrates how to perform controlled background
operations with periodic delays inside a loop using python's asyncio.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Loops exactly ten times and asynchronously waits for one second during
    each iteration before yielding a random floating-point value.

    Yields:
        float: A random floating-point number between 0 and 10 inclusive.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
