#!/usr/bin/env python3
"""This module defines the function `wait_random`"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Asynchronous coroutine that waits for a random delay
        and eventually returns it

        Args:
            max_delay: int - with a default value of 10
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
