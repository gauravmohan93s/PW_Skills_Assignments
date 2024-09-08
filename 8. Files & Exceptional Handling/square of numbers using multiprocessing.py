import multiprocessing
import time

# Function to calculate the square of a number
def square(n):
    return n * n

# Function to handle multiprocessing with custom task submission
def compute_squares_with_pool(pool_size):
    # List of numbers to compute squares for
    numbers = list(range(1, 11))

    # Start the timer
    start_time = time.time()

    # Create a pool of workers
    pool = multiprocessing.Pool(processes=pool_size)

    # Submit the tasks to the pool and collect the results
    results = pool.map(square, numbers)

    # Close the pool and wait for the workers to complete
    pool.close()
    pool.join()

    # End the timer
    end_time = time.time()

    # Calculate total time taken
    total_time = end_time - start_time

    return results, total_time

# Main entry point to ensure correct behavior in Jupyter
if __name__ == '__main__':
    pool_sizes = [2, 4, 8]  # Different pool sizes

    for pool_size in pool_sizes:
        results, total_time = compute_squares_with_pool(pool_size)
        print(f"Pool Size: {pool_size}")
        print(f"Results: {results}")
        print(f"Time Taken: {total_time:.4f} seconds\n")    