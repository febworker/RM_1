import multiprocessing
import time

def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def factorize_list_parallel(numbers):
    start_time = time.time()
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    result = pool.map(factorize, numbers)
    pool.close()
    pool.join()
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

numbers = [10, 20, 30, 40, 50]  # Example input list of numbers
result_parallel, execution_time_parallel = factorize_list_parallel(numbers)
print("Parallel version:")
print("Results:", result_parallel)
print("Execution time:", execution_time_parallel, "seconds")