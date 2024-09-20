def find_duplicate(nums):
    slow = nums[0]
    fast = nums[0]
    
    # step1
    while True:
        slow = nums[slow]          
        fast = nums[nums[fast]] 
        if slow == fast:      
            break

    # step2
    slow = nums[0]          
    while slow != fast:
        slow = nums[slow]       
        fast = nums[fast]       

    return fast                 

# Example 
if __name__ == "__main__":
    arr = [1, 3, 4, 2, 2]
    duplicate = find_duplicate(arr)
    print(duplicate)  
