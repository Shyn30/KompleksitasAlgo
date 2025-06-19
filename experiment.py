import random
import time
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from sorting.bubble_sort import bubble_sort
from sorting.insertion_sort import insertion_sort
from sorting.merge_sort import merge_sort
from sorting.quick_sort import quick_sort
from searching.linear_search import linear_search
from searching.binary_search import binary_search

sizes = [100, 1000, 10000]
sorting_algorithms = {
    'Bubble Sort': bubble_sort,
    'Insertion Sort': insertion_sort,
    'Merge Sort': merge_sort,
    'Quick Sort': quick_sort
}
searching_algorithms = {
    'Linear Search': linear_search,
    'Binary Search': binary_search
}

sort_results = {alg: [] for alg in sorting_algorithms}
search_results = {alg: [] for alg in searching_algorithms}

for size in sizes:
    arr = [random.randint(0, size) for _ in range(size)]
    arr_sorted = sorted(arr)
    target = arr[size // 2]
    for name, func in sorting_algorithms.items():
        arr_copy = arr.copy()
        start = time.time()
        if name == 'Merge Sort':
            func(arr_copy)
        else:
            func(arr_copy)
        end = time.time()
        sort_results[name].append(end - start)
    for name, func in searching_algorithms.items():
        if name == 'Binary Search':
            search_arr = arr_sorted
        else:
            search_arr = arr
        start = time.time()
        func(search_arr, target)
        end = time.time()
        search_results[name].append(end - start)

# Plot sorting
plt.figure(figsize=(10,5))
for name, times in sort_results.items():
    plt.plot(sizes, times, marker='o', label=name)
plt.title('Sorting Algorithms Execution Time')
plt.xlabel('Number of Elements')
plt.ylabel('Time (seconds, log scale)')
plt.yscale('log')
plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.6f'))
plt.legend()
plt.grid(True, which="both", ls="--")
plt.savefig('sorting_comparison.png')
plt.show()

# Plot searching
plt.figure(figsize=(10,5))
for name, times in search_results.items():
    plt.plot(sizes, times, marker='o', label=name)
plt.title('Searching Algorithms Execution Time')
plt.xlabel('Number of Elements')
plt.ylabel('Time (seconds, log scale)')
plt.yscale('log')
plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.6f'))
plt.legend()
plt.grid(True, which="both", ls="--")
plt.savefig('searching_comparison.png')
plt.show()
