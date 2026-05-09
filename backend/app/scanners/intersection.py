from .dedupe import unique_symbols

def find_common(scanner1, scanner2):
    scanner1 = set(unique_symbols(scanner1))
    scanner2 = set(unique_symbols(scanner2))
    return sorted(list(scanner1.intersection(scanner2)))
