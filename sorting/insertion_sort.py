import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def measure_time(arr):
    start = time.time()
    insertion_sort(arr.copy())
    end = time.time()
    return end - start

if __name__ == "__main__":
    import random
    arr = [random.randint(0, 10000) for _ in range(20)]
    print("Data sebelum sorting:", arr)
    start = time.time()
    sorted_arr = insertion_sort(arr.copy())
    end = time.time()
    print("Data setelah sorting:", sorted_arr)
    print(f"Waktu eksekusi: {end - start:.6f} detik")
