def print_repeated_numbers(n):
    """
    n개의 숫자를 좌우로 n번 반복하여 출력합니다.

    Args:
        n (int): 반복할 숫자 개수
    """
    for i in range(n):  # n번 반복
        if i % 2 == 0:  # 짝수 번째 행 (12345)
            for j in range(1, n + 1):
                print(j, end="")
            print()  # 줄바꿈
        else:  # 홀수 번째 행 (54321)
            for j in range(n, 0, -1):
                print(j, end="")
            print()  # 줄바꿈

# 사용자 입력
n = int(input())

# 결과 출력
print_repeated_numbers(n)