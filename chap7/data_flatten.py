def flatten(data, prefix='', separator='.'):
    """Flattens a nested dict structure. """
    if not isinstance(data, dict):
        return {prefix: data} if prefix else data
    result = {}
    for (key, value) in data.items():
        result.update(flatten(value,_get_new_prefix(prefix, key, separator),separator=separator))
    return result

def _get_new_prefix(prefix, key, separator):
    return (separator.join((prefix, str(key))) if prefix else str(key))
