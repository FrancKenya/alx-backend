#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Exclude header

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return a dictionary with deletion-resilient pagination."""
        assert index is not None and 0 <= index < len(
            self.indexed_dataset()), "Index out of range"

        dataset = self.indexed_dataset()
        data = []
        current_index = index
        count = 0

        # Collect the required number of rows while skipping deleted indices
        while count < page_size and current_index < len(dataset):
            if current_index in dataset:
                data.append(dataset[current_index])
                count += 1
            current_index += 1

        # Calculate the next index
        next_index = current_index if current_index < len(dataset) else None

        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data,
        }
