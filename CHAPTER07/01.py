"""
우리가 리스트가 있어서
특정한 원소를 찾는다면[있는지, 없는지, index가 몇인지 등등]

1. 앞에서부터 차례대로 찾기
2. 반으로 쪼개면서 탐색하기.[정렬되어 있을 경우]
=> 일반적인 정렬이 아니라, 트리형태로 정렬이 되어있을 가능성이 있다.

먼저 순차탐색이다.

모든 원소를 다 확인하므로 최악의 경우 O(N) 수준
"""


def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i+1  # 인덱스가 아닌 몇 번째인지를 확인하고 싶은것.


print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()

print(sequential_search(n, target, array))
