import numpy as np
import time

# Fungsi yang akan diintegrasikan
def f(x):
    return 4 / (1 + x**2)

# Implementasi metode integrasi trapezoid
def trapezoid_integration(f, a, b, N):
    h = (b - a) / N
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, N):
        integral += f(a + i * h)
    integral *= h
    return integral

# Kode testing
N_values = [10, 100, 1000, 10000]
pi_reference = 3.14159265358979323846
errors = []
execution_times = []

for N in N_values:
    start_time = time.time()
    pi_estimate = trapezoid_integration(f, 0, 1, N)
    end_time = time.time()
    
    # Menghitung galat RMS
    error = np.sqrt((pi_estimate - pi_reference)**2)
    errors.append(error)
    
    # Mengukur waktu eksekusi
    execution_time = end_time - start_time
    execution_times.append(execution_time)
    
    print(f"N: {N}, Estimasi Pi: {pi_estimate}, Galat RMS: {error}, Waktu Eksekusi: {execution_time} detik")

# Output hasil
for i in range(len(N_values)):
    print(f"Untuk N = {N_values[i]}, Galat RMS = {errors[i]}, Waktu Eksekusi = {execution_times[i]} detik")
