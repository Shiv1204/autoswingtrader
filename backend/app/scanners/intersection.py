def common_stocks(scanner1, scanner2):

    return list(
        set(scanner1) & set(scanner2)
    )