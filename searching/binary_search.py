import time

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def measure_time(arr, target):
    start = time.time()
    binary_search(arr, target)
    end = time.time()
    return end - start

if __name__ == "__main__":
    import random
    arr = sorted([random.randint(0, 100) for _ in range(20)])
    target = arr[random.randint(0, 19)]
    print("Data:", arr)
    print("Target:", target)
    start = time.time()
    idx = binary_search(arr, target)
    end = time.time()
    if idx != -1:
        print(f"Target ditemukan pada indeks {idx}")
    else:
        print("Target tidak ditemukan")
    print(f"Waktu eksekusi: {end - start:.6f} detik")
