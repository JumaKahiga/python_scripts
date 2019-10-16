import json
from itertools import combinations, permutations


class SearchByTag:

    def __init__(self, data_file, query_tag):
        with open(data_file) as data_file:
            self._data = json.load(data_file)
        self.query = query_tag

    def search(self):
        if not self.query or not self._data:
            raise StopIteration
        
        try:
            self._data['items']
        except KeyError:
            raise StopIteration
    
        for item in self._data['items']:
            if not item:
                raise StopIteration
            
            thing = item.get('tags', None)
            
            if not thing:
                continue
            
            if self.query in thing:
                yield item
    

    def first(self):
        return self.search().__next__()


def solution(M, A):
    N = len(A)
    count = [0] * (M + 1)
    maxOccurence = 1
    index = -1
    for i in range(N):
        print(count[A[i]], 'here')
        if count[A[i]] > 0:
            tmp = count[A[i]]
            if tmp > maxOccurence:
                maxOccurence = tmp
                index = i
            count[A[i]] = tmp + 1
        else:
            count[A[i]] = 1
    print(index)
    return A[index]


def solutionB(M, A):
    N = len(A)
    maxOccurence = 1
    index = -1
    for i in range(N):
        pass


numbers = [1, 2, 3, 3, 1, 3, 1, 3, 5]


items = [
            1, 2, 6, 7, 8, 10, 11, 12, 13, 15, 16, 18, 19,
            20, 21, 0, 22, 27, 28, 30, 32, 33, 38, 40, 43,
            44, 46, 49, 50, 51, 54, 55, 57, 58, 60, 63, 64,
            65, 66, 67, 70, 72, 73, 74, 76, 78, 82, 83, 84,
            85, 86, 87, 88, 92, 93, 96, 101, 103, 106, 107,
            108, 115, 116, 119, 122, 123, 124, 127, 128, 130,
            131, 135, 137, 138, 140, 141, 143, 145, 149, 150,
            151, 152, 153, 154, 155, 156, 162, 166, 168, 172,
            175, 176, 177, 178, 180, 188, 193, 194, 196, 198,
            199, 200, 201, 202, 203, 204, 206, 210, 214, 215,
            216, 220, 221, 222, 223, 224, 228, 229, 230, 231,
            233, 234, 235, 239, 240, 243, 245, 248, 249, 250,
            251, 252, 254, 255, 256, 257, 258, 259, 260, 261,
            262, 263, 264, 266, 267, 269, 270, 271, 272, 274, 275]


S = 'aabcaabcabda'

mine = 'babada'

yangu = [mine[i:j] for i, j in combinations(range(len(mine) +1), r=2)]

zangu = set(mine)

a_thing = 'dab'

result = [S[i: i + 2] for i in range(len(S) - 2 + 1)]


def check_eligibility(A):
    if sum(A)%3 != 0:
        return False

    sub_total = sum(A)/3
    result = [n for i in range(len(A), 0, -1) for n in combinations(A, i) if sum(n) == sub_total]
    print(result)


A = [1,3,4,5,2]
print(list(combinations(A, 3)), 'p')
numbers = A
print(check_eligibility(A), 'he')

mwa = A


numbers = [1, 2, 3, 7, 7, 9, 10]
sub_total = sum(numbers)%3
numbers = A
result = [seq for i in range(len(numbers), 0, -1) for seq in combinations(numbers, i) if sum(seq) == 10]
print(result)

print(2 << 10)
