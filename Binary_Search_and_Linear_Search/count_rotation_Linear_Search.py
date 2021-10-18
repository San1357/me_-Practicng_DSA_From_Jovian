def count_rotations_linear(nums):
    position = 0               # What is the intial value of position?
    
    while position <= len(nums)-1:                     # When should the loop be terminated?
        
        # Success criteria: check whether the number at the current position is smaller than the one before it
        if position > 0 and nums[position] < nums[position-1]:   # How to perform the check?
            return position
        
        # Move to the next position
        position += 1


    else:
        return -1  

print(count_rotations_linear([6,7,8,9,10, 1, 2, 3]))