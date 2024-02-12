import time

def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def factorize_list_sync(numbers):
    start_time = time.time()
    result = [factorize(number) for number in numbers]
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

numbers = [10, 20, 30, 40, 50]  # Example input list of numbers
result_sync, execution_time_sync = factorize_list_sync(numbers)
print("Synchronous version:")
print("Results:", result_sync)
print("Execution time:", execution_time_sync, "seconds")