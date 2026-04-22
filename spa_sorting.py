import random
import time

# -------------------------------
# Insertion Sort
# -------------------------------
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# -------------------------------
# Merge Sort
# -------------------------------
def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


# -------------------------------
# Quick Sort (Lomuto Partition)
# -------------------------------
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


# -------------------------------
# Timing Function
# -------------------------------
def measure_time(sort_func, arr, is_quick=False):
    arr_copy = arr.copy()
    start = time.time()

    if is_quick:
        sort_func(arr_copy, 0, len(arr_copy) - 1)
    else:
        result = sort_func(arr_copy)
        if result is not None:
            arr_copy = result

    end = time.time()
    return (end - start) * 1000  # milliseconds


# -------------------------------
# Dataset Generator
# -------------------------------
def generate_datasets():
    sizes = [1000, 5000, 10000]
    datasets = {}

    for size in sizes:
        random.seed(42)
        datasets[(size, "random")] = [random.randint(1, 100000) for _ in range(size)]
        datasets[(size, "sorted")] = list(range(size))
        datasets[(size, "reverse")] = list(range(size, 0, -1))

    return datasets


# -------------------------------
# Correctness Check
# -------------------------------
def check_correctness():
    test = [5, 2, 9, 1, 5, 6]

    arr1 = test.copy()
    insertion_sort(arr1)

    arr2 = merge_sort(test.copy())

    arr3 = test.copy()
    quick_sort(arr3, 0, len(arr3) - 1)

    print("Correctness Check:")
    print("Insertion:", arr1)
    print("Merge:", arr2)
    print("Quick:", arr3)
    print()


# -------------------------------
# Main Execution
# -------------------------------
def main():
    check_correctness()

    datasets = generate_datasets()

    print("Size\tType\t\tInsertion(ms)\tMerge(ms)\tQuick(ms)")
    print("-" * 70)

    for (size, dtype), data in datasets.items():
        t1 = measure_time(insertion_sort, data)
        t2 = measure_time(merge_sort, data)
        t3 = measure_time(quick_sort, data, is_quick=True)

        print(f"{size}\t{dtype:10}\t{t1:.2f}\t\t{t2:.2f}\t\t{t3:.2f}")


if __name__ == "__main__":
    main()
