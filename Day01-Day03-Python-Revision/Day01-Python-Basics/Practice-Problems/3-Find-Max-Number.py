# Find Maximum Number in a List

'''Question:

Write a function that takes a list of numbers and returns the largest value in the list.
Example Input: 
Expected Output: 8
'''

def Method1(numbers):
    if not numbers:
        return ValueError
    return max(numbers)

def Method2(numbers):
    # by sorting method we'll find max num
    if not numbers:
        return ValueError
    
    sorted_numbers = sorted(numbers, reverse=True)
    return sorted_numbers[0]

num = [1,2,5,8,3,2]
maxNum = Method1(num)
maxNum2 = Method2(num)
print(f'Max num with method1 is : {maxNum}')
print(f'Max num with method2 is : {maxNum2}')