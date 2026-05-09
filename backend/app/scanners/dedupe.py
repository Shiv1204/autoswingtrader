def unique_symbols(symbols):
    seen = set()
    result = []
    for symbol in symbols:
        symbol = symbol.strip().upper()
        if symbol and symbol not in seen:
            seen.add(symbol)
            result.append(symbol)
    return result
