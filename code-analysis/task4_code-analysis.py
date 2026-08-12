def sequnece_checker(s1, s2):
    if len(s1) != len(s2):
        return False
    return True

def calculate_mean(anysequence):
    total = 0
    count = 0
    for num in anysequence:
        total += num
        count += 1
    return total / count

def distance_fn(s1, s2): 
    squared_diff_sum = 0
    for i in range(len(s1)):
        squared_diff_sum += (s1[i] - s2[i]) ** 2
    return squared_diff_sum

# Example
s1 = [1, 2, 4, 5, 9]
s2 = [6, 7, 8, 9, 10]

cond = sequnece_checker(s1, s2)
if (cond): 
    me1 = calculate_mean(s1)
    me2 = calculate_mean(s2)
    distance = distance_fn(s1, s2)
    print("Mean of sequence 1:", me1)
    print("Mean of sequence 2:", me2)
    print("Distance between the sequences:", distance)
else: 
    print('Warning! Error.')