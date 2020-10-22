def annuity_total(mortgage_value, rate, N):
    return N * rate * mortgage_value/ (1 - (1 + rate) ** (-N))
