import sys
def sumOfArray(numbers:list[int])->int:
    '''
    This method returns the sum of an array
    '''
    sum = 0
    for i in numbers:
        sum += int(i)
    return sum
    
def main():
    if len(sys.argv) > 1:
        inputs = sys.argv[1:]
        print(f'the sum of {inputs} is {sumOfArray(inputs)}')
    else:
        print('python sumOfArray.py <array of ints>')

if __name__ == '__main__':
    main()