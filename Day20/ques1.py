#Capacity To Ship Packages Within D Days
def shipWithinDays(weights, D):
    lo, hi = max(weights), sum(weights)  
    while lo < hi:
        mid = (lo + hi) // 2  
        days = 1  
        current_load = 0  
        for weight in weights:
            if current_load + weight > mid:
                days += 1  
                current_load = 0 
            current_load += weight  
        if days <= D:
            hi = mid  
        else:
            lo = mid + 1 
    return lo 
