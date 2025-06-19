import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def measure_time(arr):
    start = time.time()
    bubble_sort(arr.copy())
    end = time.time()
    return end - start

if __name__ == "__main__":
    import random
    arr = [random.randint(0, 100) for _ in range(20)]
    print("Data sebelum sorting:", arr)
    start = time.time()
    sorted_arr = bubble_sort(arr.copy())
    end = time.time()
    print("Data setelah sorting:", sorted_arr)
    print(f"Waktu eksekusi: {end - start:.6f} detik")
