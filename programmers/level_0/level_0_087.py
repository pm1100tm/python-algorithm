"""
직각삼각형 출력하기

"*"의 높이와 너비를 1이라고 했을 때,
"*"을 이용해 직각 이등변 삼각형을 그리려고합니다.
정수 n 이 주어지면 높이와 너비가 n 인 직각 이등변 삼각형을 출력하도록 코드를 작성해보세요.

1 ≤ n ≤ 10

n = 3
*
**
***
"""
from utils import prvalue


if __name__ == '__main__':
    n = int(input())

    for i in range(1, n + 1):
        print(f"{'*' * i}")
