import csv
import os
from typing import Any, List


def annuity_total(mortgage_value, rate, N):
    return N * rate * mortgage_value/ (1 - (1 + rate) ** (-N))


def write_to_file(filename: os.PathLike, labels: List[str], data: List[Any]):
    with open(filename, 'w') as f:
        file_writer = csv.writer(f, delimiter=',')
        file_writer.writerow(labels)
        file_writer.writerow(data)
