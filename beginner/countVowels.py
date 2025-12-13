import sys

VOWELS = ['a','e','i','o','u']

def countVowels(input:str)->int:
    '''
    This method counts the number of vowels in the input and returns an 
    integer count, or 0 by default. 

    NOTE: the question did not specify that we have to count the number of distinct
    vowels, so this method counts duplicate vowels.
    '''

    retval = 0
    for i in input:
        if i in VOWELS:
            retval += 1
    return retval

def main():
    if len(sys.argv) == 2:
        input = str(sys.argv[1])
        print(f'the number of vowels in {input} is {countVowels(input)}')
    else:
        print('python countVowels.py <string>')

if __name__ == '__main__':
    main()