import copy
import csv
from datetime import datetime
import os
from typing import Any, List, Optional


def annuity_total(mortgage_value, rate, N, rcl, n_start = 0, Ntot = None):
    if rcl is None:
        return N * rate * mortgage_value/ (1 - (1 + rate) ** (-N))
    else:
        rate_change_list = copy.deepcopy(rcl)
        total_cost = 0
        balance = mortgage_value
        N_left = N
        n_total = 0
        for n_months, rate_value in rate_change_list:
            n_total += n_months
        if Ntot is not None:
            n_final = Ntot - n_total
        else:
            n_final = N - n_total
        rate_change_list[-1] = (n_final, rate_change_list[-1][1])

        full_date_list = []
        for n_months, rate_value in rate_change_list:
            for i in range(n_months):
                full_date_list.append(rate_value)

        previous_rate = 0
        balance = mortgage_value
        for new_rate in full_date_list[n_start:]:
            payment = annuity_payment(balance, new_rate, N_left)
            balance -= (payment - balance * new_rate)
            N_left -= 1
            total_cost += payment
        return total_cost


def interest_only_total(mortgage_value, rate, N, rcl):
    if rcl is None:
        return mortgage_value * (rate * N + 1)
    else:
        rate_change_list = copy.deepcopy(rcl)
        n_total = 0
        total_cost = 0
        for n_months, rate_value in rate_change_list:
            n_total += n_months
        n_final = N - n_total
        rate_change_list[-1] = (n_final, rate_change_list[-1][1])
        for n_months, rate_value in rate_change_list:
            total_cost += mortgage_value * (rate_value * n_months)
        return total_cost + mortgage_value


def partial_interest_only_total(mortgage_value, rate, N, N_interest_only, rcl):
    annuity_term = N - N_interest_only
    io_interest = interest_only_total(mortgage_value, rate, N_interest_only, rcl) - mortgage_value
    if annuity_term > 0:
        annuity_paid = annuity_total(mortgage_value, rate, annuity_term, rcl, n_start=N_interest_only, Ntot=N)
    else:
        annuity_paid = mortgage_value
    return io_interest + annuity_paid


def write_to_file(filename: os.PathLike, labels: List[str], data: List[Any], rate_change_list: Optional[List[Any]]):
    with open(filename, 'w') as f:
        file_writer = csv.writer(f, delimiter=',')
        file_writer.writerow(labels)
        file_writer.writerow(data)
        if rate_change_list is not None:
            file_writer.writerow([])
            file_writer.writerow(['Date', 'Interest Rate'])
            for date, new_rate in rate_change_list:
                file_writer.writerow([date, new_rate])


def date_difference(date_1: datetime, date_2: datetime):
    return (date_1.year - date_2.year) * 12 + date_1.month - date_2.month


def annuity_payment(p, i, N):
    return p * (i * (1 + i) ** N) / ((1 + i) ** N - 1)
