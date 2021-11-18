def medians(nums1, nums2):
            
        
        #return (left_digit_shorter, right_digit_shorter, left_digit_longer, right_digit_longer)
    def indices(right_digit_shorter, shorter_nums, longer_nums):
        indexmiddle = (len(shorter_nums) + len(longer_nums)) // 2
        right_digit_longer = indexmiddle - right_digit_shorter
        return (right_digit_shorter - 1, right_digit_shorter, right_digit_longer - 1, right_digit_longer)

        #making sure the index says inside the array(noyt reaching the end or beggining)
    def CheckEnds(arr, i):
        if i == -1:
            return float('-inf')
        if i == len(arr):
            return float('inf')
        return arr[i]
        
        #getting direction and deciding to go left or right
    def leftorright(left_digit_shorter, right_digit_shorter, left_digit_longer, right_digit_longer, shorter_nums, longer_nums):
        if CheckEnds(shorter_nums, left_digit_shorter) > CheckEnds(longer_nums, right_digit_longer):
            return -1
        elif CheckEnds(longer_nums, left_digit_longer) > CheckEnds(shorter_nums, right_digit_shorter):
            return 1
        else:
            return 0
        
        #getting result by calculating median
    def actmedian(left_digit_shorter, right_digit_shorter, left_digit_longer, right_digit_longer, shorter_nums, longer_nums):
        odd = (len(shorter_nums) + len(longer_nums)) % 2
        if odd:
            return min(CheckEnds(longer_nums, right_digit_longer), CheckEnds(shorter_nums, right_digit_shorter))
        else:
            return (max(CheckEnds(shorter_nums, left_digit_shorter), CheckEnds(longer_nums, left_digit_longer)) 
                        + min(CheckEnds(shorter_nums, right_digit_shorter), CheckEnds(longer_nums, right_digit_longer))) / 2.0
        
        
        #introducing some variables 
    left_digit_shorter = right_digit_shorter = left_digit_longer = right_digit_longer = direction = 1

    #finding the shorter and longer array
    shorter_nums = nums1
    longer_nums = nums2
    if len(nums1) > len(nums2):
        shorter_nums = nums2
        longer_nums = nums1
                
        #the actual, one and only, binary search, that didn't want to work, but we made it   
    go_left = 0
    go_right = len(shorter_nums)
    while direction != 0:
        middle = (go_left + go_right) // 2
            #determening indices from our middle
        left_digit_shorter, right_digit_shorter, left_digit_longer, right_digit_longer = indices(middle, shorter_nums, longer_nums)
            #finding the actual direction
        direction = leftorright(left_digit_shorter, right_digit_shorter, left_digit_longer, right_digit_longer, shorter_nums, longer_nums)
        if direction < 0:
            go_right = middle - 1
        elif direction > 0:
            go_left = middle + 1
        
        #calculate median
    return actmedian(left_digit_shorter, right_digit_shorter, left_digit_longer, right_digit_longer, shorter_nums, longer_nums)


