import time

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def measure_time(arr):
    start = time.time()
    merge_sort(arr.copy())
    end = time.time()
    return end - start

if __name__ == "__main__":
    import random
    arr = [random.randint(0, 10000) for _ in range(20)]
    print("Data sebelum sorting:", arr)
    start = time.time()
    sorted_arr = arr.copy()
    merge_sort(sorted_arr)
    end = time.time()
    print("Data setelah sorting:", sorted_arr)
    print(f"Waktu eksekusi: {end - start:.6f} detik")
