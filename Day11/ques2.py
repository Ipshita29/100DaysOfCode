#Repair cars
def repairCars(ranks, cars):
    def canRepairInTime(time):
        total_cars = 0
        for r in ranks:
            total_cars += int((time // r) ** 0.5)  
            if total_cars >= cars: 
                return True
        return total_cars >= cars

    left, right = 1, min(ranks) * cars * cars  
    
    while left < right:
        mid = (left + right) // 2
        if canRepairInTime(mid):  
            right = mid
        else:  
            left = mid + 1
    
    return left  
