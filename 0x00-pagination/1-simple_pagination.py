#!/usr/bin/env python3
"""
Pagination module to work with a dataset of popular baby names.
"""

import csv
from math import ceil
from typing import List, Tuple


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a page of the dataset.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            List[List]: A list of rows corresponding to the page and page_size.
        """
        assert isinstance(page, int) and page > 0, "Page must be an integer"
        "greater than 0."
        assert isinstance(page_size, int) and page_size > 0, "Page size must"
        "be an integer greater than 0."

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        # Return the subset of the dataset or an empty list if out of range
        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]
