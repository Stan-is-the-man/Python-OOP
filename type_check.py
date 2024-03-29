def type_check(type_of_var):
    def decorator(func_ref):
        def wrapper(param):
            if not isinstance(param, type_of_var):
                return "Bad Type"
            return func_ref(param)

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))
