#!/usr/bin/env python3
"""
This module contains the index_range function for pagination.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indexes for a page of data.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index (inclusive) and
                         the end index (exclusive) for the pagination.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
