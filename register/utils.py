def invert(dictionary: dict) -> dict:
    return {value: key for key, value in dictionary.items()}
