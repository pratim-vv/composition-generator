import itertools

rhythyms = [1, 3/4, 1/2, 3/8, 1/4, 3/16, 1/8, 1/16]

def subset_sum(numbers, target, partial=[]):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target: 
        print(partial)
    if s >= target:
        return  # if we reach the number why bother to continue
    
    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, partial + [n]) 
   

if __name__ == "__main__":
    subset_sum([1, 3/4, 1/2, 3/8, 1/4, 3/16, 1/8, 1/16],1)


