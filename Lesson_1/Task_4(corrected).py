def bank(dep_count, years, percent):
    for i in range(1, years + 1):
        dep_percent = (dep_count / 100) * percent
        dep_count += dep_percent
    return dep_count
