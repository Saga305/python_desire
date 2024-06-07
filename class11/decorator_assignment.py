from time import time

def time_calculate(unit='sec'):
    def outer_wrapper(func):
        def inner_wrapper(*args):
            start_time = time()
            result = func(*args)
            end_time = time()
            time_taken = end_time - start_time

            if unit == 'sec' or unit not in ["sec", "min", "hrs"]:
                print (f"execution time: {time_taken} seconds.")
            elif unit == 'min':
                time_taken = time_taken / 60
                print (f"execution time: {time_taken} minutes.")
            elif unit == 'hrs':
                time_taken = time_taken / 3600
                print (f"execution time: {time_taken} hours.")
            return result
        return inner_wrapper
    return outer_wrapper


@time_calculate()
def time_pass_seconds(count):
    sum = 0
    for i in range(count):
        sum += i
    return sum

@time_calculate('min')
def time_pass_minutes(count):
    sum = 0
    for i in range(count):
        sum += i
    return sum

@time_calculate('hrs')
def time_pass_hours(count):
    sum = 0
    for i in range(count):
        sum += i
    return sum

counts = 1300000000
time_pass_seconds(counts)
time_pass_minutes(counts)
time_pass_hours(counts)

# DELL@The-Great-Saga MINGW64 /e/python_desire/class11 (main)
# $ python3.12.exe decorator_assignment.py 
# execution time: 4.297041416168213 seconds.
# execution time: 0.08266960382461548 minutes.
# execution time: 0.0012422674894332886 hours.

