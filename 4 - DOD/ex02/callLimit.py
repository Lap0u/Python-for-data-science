def callLimit(limit: int):
    """Decorator that limits the number of times a function can be called."""
    count = 0

    def callLimiter(function):
        """Inner function that limits the number of times a function can be called."""

        def limit_function(*args: any, **kwds: any):
            """Innermost function that limits the number of times a function can be called."""
            nonlocal count
            if count >= limit:
                print(f"Error: {function} called too many times")
                return
            count += 1
            return function(*args, **kwds)

        return limit_function

    return callLimiter
