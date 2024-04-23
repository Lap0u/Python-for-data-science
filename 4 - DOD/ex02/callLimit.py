def callLimit(limit: int):
    count = 0

    def callLimiter(function):

        def limit_function(*args: any, **kwds: any):
            nonlocal count
            if count >= limit:
                print(f"Error: {function} called too many times")
                return
            count += 1
            return function(*args, **kwds)

        return limit_function

    return callLimiter
