import sys
def maxElement(input:list[int])->int:
    '''
    This method returns the max element of an array and returns an int.
    By default it returns 0.
    '''
    retval = 0
    for i in input:
        if i > retval:
            retval = i
    return retval

def main():
    if len(sys.argv) > 1:
        # cast inputs to int.
        input = [int(i) for i in sys.argv[1:]]
        print(f'the max element in {input} is {maxElement(input)}')
    else: 
        print('python maxElement.py <array of ints>')

if __name__ == '__main__':
    main()