def indexing(keys, values, match):
    # match is a two- argument function,
    return {k: [v for v in values if match(key, v)] for k in keys }