# 1057 토너먼트
# 실버 4

n, kim, lim = map(int, input().split())
cnt = 0

# 승리할 때 마다 승자의 번호 = 승자의 번호 - 승자의 번호 / 2 로 갱신된다.
# kim과 Lim이 같은 승자의 번호를 갖게되는 때 서로 승부를 치룬 것.

# if kim == 8 and lim == 9
#                   (1) --> kim == lim 같은 승자의 번호를 갖게되는 때
#            (1              2)
#      (1           2)      (3)
#   (1     2)   (3     4)   (5) 
#  (1 2) (3 4) (5 6) (7 8) (9 10)

while kim != lim:
    kim -= kim // 2
    lim -= lim // 2
    cnt += 1

print(cnt)