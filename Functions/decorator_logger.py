"""
Create decorator logger. The decorator should print to the console information about function's name
and all its arguments separated with ',' for the function decorated with logger.
Create function concat with any numbers of any arguments which concatenates arguments and
apply logger decorator for this function.
For example
print(concat(2, 3)) display
Executing of function concat with arguments 2, 3...
23
print(concat('hello', 2)) display
Executing of function concat with arguments hello, 2...
hello2
print(concat (first = 'one', second = 'two')) display
Executing of function concat with arguments one, two...
onetwo
"""

def logger(func):
    def wrapper(*args, **kwargs):
        all_args = []
        for a in args:
            all_args.append(str(a))

        for k, v in kwargs.items():
            all_args.append(f"{v}")

        arg_str = ", ".join(all_args)

        result = func(*args, **kwargs)
        print(f'Executing of function {func.__name__} with arguments {arg_str}...')
        return result
    return wrapper

@logger
def concat(*args, **kwargs):
    args_part = "".join(map(str, args))
    kwargs_part = "".join(map(str, kwargs.values()))
    return args_part + kwargs_part

@logger
def print_arg(arg):
    print(arg)

print(concat(first = 'one', second = 'two')) #Executing of function concat with arguments one, two...\onetwo
print(concat('hello', 2)) # Executing of function concat with arguments hello, 2...\hello2
print(concat(2, 3)) #Executing of function concat with arguments 2, 3...\23
print(print_arg(2)) #2 \Executing of function print_arg with arguments 2...