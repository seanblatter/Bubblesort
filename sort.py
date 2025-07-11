"""Simple sorting algorithms demo."""

def bubble_sort(arr):
    """Sorts the list using bubble sort and returns it."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def insertion_sort(arr):
    """Sorts the list using insertion sort and returns it."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def main():
    data = [5, 2, 9, 1, 5, 6]
    print("Original:", data)
    print("Bubble sort:", bubble_sort(data[:]))
    print("Insertion sort:", insertion_sort(data[:]))


if __name__ == "__main__":
    main()
