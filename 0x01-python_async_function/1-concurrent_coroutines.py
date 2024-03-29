#!/usr/bin/env python3
"""This module defines the function `wait_n`"""
import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """spawn wait_random n number of times with the specified max_delay"""
    tasks = [wait_random(max_delay) for _ in range(n)]

    res = await asyncio.gather(*tasks)

    return sorted(res)
