import time
import os
from scanner import horspool, naive

def generate_large_file(filepath, lines=10000, pattern="SUPER_SECRET_PASSWORD"):
    """
    Generates a large mock file for benchmarking.
    """
    with open(filepath, "w", encoding="utf-8") as f:
        for i in range(lines):
            if i == lines // 2 or i == lines - 10:
                f.write(f"This is a line containing {pattern} inside it.\n")
            else:
                f.write(f"This is just a regular line of code number {i}.\n")

def run_benchmark():
    test_file = "test_10k_lines.txt"
    pattern = "SUPER_SECRET_PASSWORD"
    
    print("Generating large test file...")
    generate_large_file(test_file)
    
    with open(test_file, "r", encoding="utf-8") as f:
        text = f.read()

    print(f"\nBenchmarking search for '{pattern}' in file of {len(text)} characters.")
    
    # Benchmark Naive
    start = time.time()
    naive_res = naive.search(text, pattern)
    naive_time = time.time() - start
    
    # Benchmark Horspool
    start = time.time()
    horspool_res = horspool.search(text, pattern)
    horspool_time = time.time() - start

    print(f"Naive: found {len(naive_res)} matches in {naive_time:.5f}s")
    print(f"Horspool: found {len(horspool_res)} matches in {horspool_time:.5f}s")
    
    # Cleanup
    if os.path.exists(test_file):
        os.remove(test_file)

if __name__ == "__main__":
    run_benchmark()
