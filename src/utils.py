import csv
import os
from typing import Any, List


def annuity_total(mortgage_value, rate, N):
    return N * rate * mortgage_value/ (1 - (1 + rate) ** (-N))


def interest_only_total(mortgage_value, rate, N):
    return mortgage_value * (rate * N + 1)


def partial_interest_only_total(mortgage_value, rate, N, N_interest_only):
    annuity_term = N - N_interest_only
    io_interest = mortgage_value * rate * N_interest_only
    if annuity_term > 0:
        annuity_paid = annuity_total(mortgage_value, rate, annuity_term)
    else:
        annuity_paid = mortgage_value
    return io_interest + annuity_paid


def write_to_file(filename: os.PathLike, labels: List[str], data: List[Any]):
    with open(filename, 'w') as f:
        file_writer = csv.writer(f, delimiter=',')
        file_writer.writerow(labels)
        file_writer.writerow(data)
