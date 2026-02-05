import numpy as np

# Generate large arrays for benchmarking
prices = np.random.randint(100, 10000, size=1_000_000)
quantities = np.random.randint(1, 10, size=1_000_000)

print(f"Array size: {len(prices):,} elements")
print(f"Prices range: {prices.min()} - {prices.max()}")
print(f"Quantities range: {quantities.min()} - {quantities.max()}")

#Create a loop-based function:
def loop_based_revenue(prices, quantities):
    """
    Calculate revenue using a Python loop.
    """
    revenue = []
    for i in range(len(prices)):
        revenue.append(prices[i] * quantities[i])
    return revenue

#test the function 
# Test with small array first
test_prices = prices[:10]
test_quantities = quantities[:10]
#test loop based function
test_result = loop_based_revenue(test_prices, test_quantities)
print("Test result (first 5):", test_result[:5])

#Measure execution time using %timeit:
# Note: %timeit is a Jupyter magic command
# If using a script, use time.time() instead

# In Jupyter Notebook:
# %timeit loop_based_revenue(prices, quantities)

# In Python script, use:
import time

start_time = time.time()
loop_result = loop_based_revenue(prices, quantities)
loop_time = time.time() - start_time

print(f"Loop-based calculation time: {loop_time:.4f} seconds")

#NumPy vectorized calculation
#Create a vectorized function:
def numpy_vectorized_revenue(prices, quantities):
    """
    Calculate revenue using NumPy vectorization.
    """
    return prices * quantities
# again test this function : with small test array values
test_result_numpy = numpy_vectorized_revenue(test_prices, test_quantities)
print("NumPy test result (first 5):", test_result_numpy[:5])

# measure execution time
start_time = time.time()
numpy_result = numpy_vectorized_revenue(prices, quantities)
numpy_time = time.time() - start_time

print(f"NumPy vectorized calculation time: {numpy_time:.4f} seconds")

#verify results match
# Compare results (first 1000 elements for speed)
comparison = np.allclose(loop_result[:1000], numpy_result[:1000])
print(f"Results match: {comparison}")

# Calculate speedup factor:
speedup = loop_time / numpy_time
print("=== PERFORMANCE COMPARISON ===")
print(f"Loop-based time: {loop_time:.4f} seconds")
print(f"NumPy vectorized time: {numpy_time:.4f} seconds")
print(f"Speedup factor: {speedup:.2f}x faster")

#Calculate percentage improvement:
improvement = ((loop_time - numpy_time) / loop_time) * 100
print(f"Performance improvement: {improvement:.1f}%")

#Analyze why NumPy is faster:
print("\n=== WHY NUMPY IS FASTER ===")
print("1. NumPy operations are implemented in C (compiled code)")
print("2. Vectorized operations process multiple elements simultaneously")
print("3. No Python loop overhead (interpreted code)")
print("4. Better memory access patterns")
print("5. Optimized for numerical computations")

#Document findings:
# Create performance summary
performance_summary = {
    "array_size": len(prices),
    "loop_time_seconds": loop_time,
    "numpy_time_seconds": numpy_time,
    "speedup_factor": speedup,
    "improvement_percent": improvement
}

print("\n=== PERFORMANCE SUMMARY ===")
for key, value in performance_summary.items():
    print(f"{key}: {value}")

#Create a markdown document with findings.
#Create performance comparison document:
markdown_content = f"""# Performance Comparison: Loops vs NumPy

## Test Configuration
- Array size: {len(prices):,} elements
- Operation: Revenue calculation (price × quantity)

## Results

### Loop-Based Approach
- Execution time: {loop_time:.4f} seconds
- Method: Python for loop with list append

### NumPy Vectorized Approach
- Execution time: {numpy_time:.4f} seconds
- Method: Element-wise array multiplication

## Performance Analysis

### Speedup
- **Speedup factor:** {speedup:.2f}x faster
- **Performance improvement:** {improvement:.1f}%

### Why NumPy is Faster

1. **Compiled Code**: NumPy operations are implemented in C, which is much faster than interpreted Python code.

2. **Vectorization**: NumPy processes multiple elements simultaneously using CPU vectorization (SIMD instructions).

3. **No Loop Overhead**: Python loops have significant overhead for each iteration. NumPy eliminates this overhead.

4. **Memory Efficiency**: NumPy uses contiguous memory blocks, which improves cache performance.

5. **Optimized Algorithms**: NumPy uses highly optimized BLAS/LAPACK libraries for numerical operations.

## Conclusion

For large-scale data processing, NumPy vectorization provides significant performance benefits over Python loops. The speedup of {speedup:.2f}x demonstrates why vectorization is essential in data engineering workflows.

## Recommendations

- Always prefer NumPy vectorized operations over Python loops for numerical computations
- Use vectorization even for small arrays to maintain code consistency
- Consider NumPy when processing datasets with 10,000+ elements
"""

print(markdown_content)

#save to markdown file
with open("performance_comparison.md", "w") as f:
    f.write(markdown_content)

print("\nSaved: performance_comparison.md")



