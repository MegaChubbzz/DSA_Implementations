"""Practicing using searching and sorting algorithms"""


# Linear search
def linear_search(sort_this, key):
    for i in range(len(sort_this)):
        if sort_this[i] == key:
            return i  # matching key
    return -1  # not found


# Binary search
def binary_search(sort_this, key):
    low = 0
    mid = len(sort_this) // 2
    high = len(sort_this - 1)
    while high >= low:
        mid = (high + low) // 2
        if sort_this[mid] < key:
            low = mid + 1
        elif sort_this[mid] > key:
            high = mid - 1
        else:
            return mid
    return -1  # not found


# Selection sort algorithm
def selection_sort(sort_this):
    for i in range(len(sort_this) - 1):
        index_smallest = i
        for j in range(i+1, len(sort_this)):
            if sort_this[j] < sort_this[index_smallest]:
                index_smallest = j
        temp = sort_this[i]
        sort_this[i] = sort_this[index_smallest]
        sort_this[index_smallest] = temp
    return sort_this


# Insertion sort algorithm
def insert_sort(sort_this):
    for i in range(1, len(sort_this)):
        j = i
        while j > 0 and sort_this[j] < sort_this[j - 1]:
            temp = sort_this[j]
            sort_this[j] = sort_this[j - 1]
            sort_this[j - 1] = temp
            j -= 1
    return sort_this


# Interleaved lists function for shell sort
def insert_sort_interleaved(sort_this, start_index, gap):
    for i in range(start_index + gap, len(sort_this), gap):
        j = i
        while (j - gap >= start_index) and (sort_this[j] < sort_this[j - gap]):
            temp = sort_this[j]
            sort_this[j] = sort_this[j - gap]
            sort_this[j - gap] = temp
            j = j - gap
    return sort_this


# Shell sort algorithm
def shell_sort(sort_this, gap_values): # Dont forget that (gap_values) needs to be a descending list where gap_values[max(index)] == 1
    for gap_value in gap_values:
        for i in range(gap_value):
            insert_sort_interleaved(sort_this, i, gap_value)
    return sort_this


# Partition function for quicksort
def partition(sort_this, start_index, end_index):
    midpoint = start_index + (end_index - start_index) // 2
    pivot = sort_this[midpoint]
    low = start_index
    high = end_index
    done = False
    while not done:
        while sort_this[low] < pivot:
            low = low + 1
        while pivot < sort_this[high]:
            high = high - 1
        if low >= high:
            done = True
        else:
            temp = sort_this[low]
            sort_this[low] = sort_this[high]
            sort_this[high] = temp
            low = low + 1
            high = high - 1
    return high

#Quickselect algorithm
def quickselect(numbers, start_index, end_index, k):
    if start_index >= end_index:
        return numbers[start_index]
    low_last_index = partition(numbers, start_index, end_index)
    if k <= low_last_index:
        return quickselect(numbers, start_index, low_last_index, k)
    return quickselect(numbers, low_last_index + 1, end_index, k)

# Quicksort algorithm
def quicksort(sort_this, start_index, end_index):
    if end_index <= start_index:
        return
    high = partition(sort_this, start_index, end_index)
    quicksort(sort_this, start_index, high)
    quicksort(sort_this, high + 1, end_index)
    return sort_this


# Merge function for merge sort algorithm
def merge(sort_this, i, j, k):
    merged_size = k - i + 1
    merged_sort_this = [0] * merged_size
    merge_pos = 0
    left_pos = i
    right_pos = j + 1
    while left_pos <= j and right_pos <= k:
        if sort_this[left_pos] <= sort_this[right_pos]:
            merged_sort_this[merge_pos] = sort_this[left_pos]
            left_pos += 1
        else:
            merged_sort_this[merge_pos] = sort_this[right_pos]
            right_pos += 1
        merge_pos = merge_pos + 1
    while left_pos <= j:
        merged_sort_this[merge_pos] = sort_this[left_pos]
        left_pos += 1
        merge_pos += 1
    while right_pos <= k:
        merged_sort_this[merge_pos] = sort_this[right_pos]
        right_pos = right_pos + 1
        merge_pos = merge_pos + 1
    for merge_pos in range(merged_size):
        sort_this[i + merge_pos] = merged_sort_this[merge_pos]


# Merge sort
def merge_sort(sort_this, i, k):
    j = 0
    if i < k:
        j = (i + k) // 2
        merge_sort(sort_this, i, j)
        merge_sort(sort_this, j + 1, k)
        merge(sort_this, i, j, k)
    return sort_this


# Get max length function for radix sort
def radix_get_max_length(sort_this):
    max_digits = 0
    for num in sort_this:
        digit_count = radix_get_length(num)
        if digit_count > max_digits:
            max_digits = digit_count
    return max_digits


# Get length function for radix sort
def radix_get_length(value):
    if value == 0:
        return 1
    digits = 0
    while value != 0:
        digits += 1
        value = int(value / 10)
    return digits


# Radix sort
def radix_sort(sort_this):
    buckets = []
    for i in range(10):
        buckets.append([])

    max_digits = radix_get_max_length(sort_this)

    pow_10 = 1
    for digit_index in range(max_digits):
        for num in sort_this:
            bucket_index = (abs(num) // pow_10) % 10
            buckets[bucket_index].append(num)
        sort_this.clear()
        for bucket in buckets:
            sort_this.extend(bucket)
            bucket.clear()
        pow_10 = pow_10 * 10

    negatives = []
    non_negatives = []
    for num in sort_this:
        if num < 0:
            negatives.append(num)
        else:
            non_negatives.append(num)
    negatives.reverse()
    sort_this.clear()
    sort_this.extend(negatives + non_negatives)
    return sort_this


# Get sorted run length function for natural merge sort
def get_sorted_run_length(sort_this, start_index, increment=0):
    increment = start_index
    if start_index > len(sort_this) - 1:
        start_index = 0
        return start_index
    else:
        for num in range(len(sort_this[start_index:])):
            if num < len(sort_this[start_index:]) - 1:
                if sort_this[increment] <= sort_this[increment + 1]:
                    increment += 1
                else:
                    start_index = num + 1
                    return start_index
            elif num == len(sort_this[start_index:]) - 1:
                start_index = num + 1
                return start_index
        return start_index


# Natural merge function for natural merge sort
def natural_merge(sort_this, left_first, left_last, right_last):
    merged_size = right_last - left_first + 1

    merged_sort_this = [None] * merged_size
    merge_pos = 0
    left_pos = left_first
    right_pos = left_last + 1

    while left_pos <= left_last and right_pos <= right_last:
        if sort_this[left_pos] <= sort_this[right_pos]:
            merged_sort_this[merge_pos] = sort_this[left_pos]
            left_pos += 1
        else:
            merged_sort_this[merge_pos] = sort_this[right_pos]
            right_pos += 1

        merge_pos += 1

    while left_pos <= left_last:
        merged_sort_this[merge_pos] = sort_this[left_pos]
        left_pos += 1
        merge_pos += 1

    while right_pos <= right_last:
        merged_sort_this[merge_pos] = sort_this[right_pos]
        right_pos += 1
        merge_pos += 1

    for merge_pos in range(merged_size):
        sort_this[left_first + merge_pos] = merged_sort_this[merge_pos]


# Natural merge sort
def natural_merge_sort(sort_this):
    i1 = 0
    run1_length = get_sorted_run_length(sort_this, i1)
    while run1_length < len(sort_this):
        i2 = i1 + run1_length
        if i2 == len(sort_this):
            i1 = 0
        else:
            run2_length = get_sorted_run_length(sort_this, i2)
            natural_merge(sort_this, i1, i2 - 1, i2 + run2_length - 1)
            i1 = i2 + run2_length
            if i1 == len(sort_this):
                i1 = 0
        run1_length = get_sorted_run_length(sort_this, i1)
    return sort_this


sort_this = [14, 3, 78, 52, 4, 9, 12, 10, 8, 33, 56, 27]
print(natural_merge_sort(sort_this))
