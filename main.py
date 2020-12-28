
def binarySearch(arr, l, r, x):
    global folds
    folds += 1
    if r >= l: 
        mid = l + (r - l) // 2
        if arr[mid] == x: 
            return mid
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
        else: 
            return binarySearch(arr, mid + 1, r, x) 
    else:
        return -1

def main():
    
    global folds
    folds = 0

    value = input("Enter a password: ").strip()
    f = open("sorted.txt", "r")
    passwords = f.read().splitlines()
    result = binarySearch(passwords, 0 , len(passwords)-1, value)

    if result != -1:
        print(f"Binary search was took {folds} folds \nPassword is on {result + 1}th line in sorted file.")
    else:
        print(f"Password <{value}> was not found.")

if __name__ == "__main__":
    main()