
def run():
    set1 = {1,2,3,4,5}
    print(f'set1: {set1}')
    set2 = {5,6,7,8,9}
    print(f'set2: {set2}')
    union = set1 | set2
    print(f'union: {union}')
    intersection = set1 & set2
    print(f'intersection: {intersection}')
    diff1 = set1 - set2
    print(f'diff1: {diff1}')
    diff2 = set2 - set1
    print(f'diff2: {diff2}')
    # Opposite to diff
    sym_diff = set1 ^ set2
    print(f'sym_diff: {sym_diff}')


if __name__ == '__main__':
    run()