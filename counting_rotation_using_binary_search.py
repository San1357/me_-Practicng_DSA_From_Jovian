def count_rotations_binary(nums):
    lo = 0
    hi = len(nums)-1
    
    while lo <= hi:
        mid = lo + (hi - lo)//2
        prev = (mid-1+len(nums))%len(nums)
        nex = (mid+1)%len(nums)
        
        # Uncomment the next line for logging the values and fixing errors.
        # print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)
        
        if nums[mid] < nums[prev] and nums[mid] <= nums[nex]:
            # The middle position is the answer
            return mid
        
        elif nums[mid] < nums[lo]:
            # Answer lies in the left half
            hi = mid-1  
        
        elif nums[mid] > nums[hi]:
            # Answer lies in the right half
            lo = mid+1
        else : 
            return 0
 
print(count_rotations_binary([5,1,2,3,4]))
