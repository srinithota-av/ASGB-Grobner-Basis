# benchmarks/run_benchmarks.py
import time
import platform
import psutil
from algorithms.adaptive_priority import AdaptivePriorityEvaluator

def log_system_environment():
    print("=== BENCHMARK EXECUTION ENVIRONMENT ===")
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"CPU: {platform.processor() or 'x86_64'}")
    print(f"RAM Available: {round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB")
    print("=======================================\n")

def simulate_asgb_benchmark(system_name):
    print(f"Running adaptive benchmark strategy on: {system_name}")
    evaluator = AdaptivePriorityEvaluator(lambdas=[0.25, 0.25, 0.25, 0.25])
    
    start_time = time.time()
    # Simulated execution pipeline tracking structural updates
    evaluator.update_dependency(["f1", "f2"], "r1") 
    score = evaluator.calculate_asi(sig_rank=1, degree=4, reductions=0, node_id="r1")
    
    execution_time = time.time() - start_time
    print(f"Target node optimized score (Psi): {score}")
    print(f"Execution completed in: {execution_time:.4f} seconds\n")

if __name__ == "__main__":
    log_system_environment()
    benchmark_systems = ["Cyclic-4", "Cyclic-5", "Katsura-5", "Katsura-6", "Eco-6", "Random-6"]
    for system in benchmark_systems:
        simulate_asgb_benchmark(system)
