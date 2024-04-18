def count_in_list(list: list, toCount: str) -> int:
    """Returns the number of times toCount appears in list"""
    return len([word for word in list if word == toCount])
