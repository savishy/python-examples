import sys
def evenOrOdd(i:int)->bool:
    '''
    This method returns true if the input is even, or else odd.
    '''
    return i % 2 == 0
    
def main():
    if len(sys.argv) == 2:
        input = int(sys.argv[1])
        print(f'{input} is {"even" if evenOrOdd(input) else "odd"}')
    else:
        print('python evenOrOdd.py <int>')
if __name__ == '__main__':
    main()