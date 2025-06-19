import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

def measure_time(arr):
    start = time.time()
    quick_sort(arr.copy())
    end = time.time()
    return end - start

if __name__ == "__main__":
    import random
    arr = [random.randint(0, 10000) for _ in range(20)]
    print("Data sebelum sorting:", arr)
    start = time.time()
    sorted_arr = quick_sort(arr.copy())
    end = time.time()
    print("Data setelah sorting:", sorted_arr)
    print(f"Waktu eksekusi: {end - start:.6f} detik")
