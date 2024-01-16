#!/usr/bin/env python3
"""module for Async Generator"""
import asyncio
import random
from typing import List, AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Async Generator
    Returns: list of floats
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
