import numpy as np
import time

def loop_based_revenue(prices, quantities):
    """
    Calculate revenue using a Python loop.
    """
    revenue = []
    for i in range(len(prices)):
        revenue.append(prices[i] * quantities[i])
    return revenue


def numpy_vectorized_revenue(prices, quantities):
    """
    Calculate revenue using NumPy vectorization.
    """
    return prices * quantities

def benchmark_loops_vs_numpy(array_size=1_000_000):
    """
    Benchmark loop-based vs NumPy vectorized revenue calculation.
    """
    # Generate test data
    prices = np.random.randint(100, 10000, size=array_size)
    quantities = np.random.randint(1, 10, size=array_size)
    
    # Loop-based approach
    start = time.time()
    loop_result = loop_based_revenue(prices, quantities)
    loop_time = time.time() - start
    
    # NumPy vectorized approach
    start = time.time()
    numpy_result = numpy_vectorized_revenue(prices, quantities)
    numpy_time = time.time() - start
    
    # Calculate metrics
    speedup = loop_time / numpy_time
    improvement = ((loop_time - numpy_time) / loop_time) * 100
    
    # Verify results match
    results_match = np.allclose(loop_result[:1000], numpy_result[:1000])
    
    print("=== BENCHMARK RESULTS ===")
    print(f"Array size: {array_size:,}")
    print(f"Loop time: {loop_time:.4f}s")
    print(f"NumPy time: {numpy_time:.4f}s")
    print(f"Speedup: {speedup:.2f}x")
    print(f"Results match: {results_match}")
    
    return {
        "loop_time": loop_time,
        "numpy_time": numpy_time,
        "speedup": speedup,
        "improvement": improvement
    }
    
# exccute the function   
results = benchmark_loops_vs_numpy(1_000_000)





