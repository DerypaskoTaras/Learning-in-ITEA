def bank(dep_count, years, percent):
    i = 1
    while i <= years:
        dep_percent = (dep_count / 100) * percent
        dep_count += dep_percent
        i += 1
    return dep_count
