
def binary_search(num_arr, target):
    l = 0
    r = len(num_arr) - 1


    # condition l == r included so that last element on the binary search is considered. Ex: [1,2] target == 2
    while l <= r:
        mid = (l + r) // 2
        if num_arr[mid] > target:
            r = mid - 1
        elif num_arr[mid] < target:
            l = mid + 1
        else:
            return mid
    return -1

def main():
    num_arr = [1, 7, 11, 14, 19 , 100, 2000]
    target = 7
    index = binary_search(num_arr, target)
    
    print(f"{target} found at {index}")

if __name__ == "__main__":
    main()