pos = -1

def search(arr, target):
    global pos
    l = 0
    u = len(arr) - 1

    while l <= u:
        mid = (l + u) // 2
        if arr[mid] == target:
            pos = mid
            return True
        elif arr[mid] < target:
            l = mid + 1
        else:
            u = mid - 1
    return False

my_list = [11, 22, 33, 44, 55, 66, 77, 88, 99, 12]
target_value = 55

if search(my_list, target_value):
    print("Found at index:", pos)
else:
    print("Not Found")
