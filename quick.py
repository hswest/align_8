def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def data(f):
    data = list(map(int, f.read().replace(",", " ").split()))[:100]
    sorted_result = quick_sort(data) 
    print(sorted_result)