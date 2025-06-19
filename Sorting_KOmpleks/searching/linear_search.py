import time

def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

def measure_time(arr, target):
    start = time.time()
    linear_search(arr, target)
    end = time.time()
    return end - start

if __name__ == "__main__":
    import random
    arr = [random.randint(0, 100) for _ in range(20)]
    target = arr[random.randint(0, 19)]
    print("Data:", arr)
    print("Target:", target)
    start = time.time()
    idx = linear_search(arr, target)
    end = time.time()
    if idx != -1:
        print(f"Target ditemukan pada indeks {idx}")
    else:
        print("Target tidak ditemukan")
    print(f"Waktu eksekusi: {end - start:.6f} detik")
