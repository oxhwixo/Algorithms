def solution(users, emoticons):
    answer = []
    
    discount = [10, 20, 30, 40]
    check = [0] * len(emoticons)

    def dfs(depth):
        if depth == len(emoticons):
            count = 0
            result = 0
            for percent, money in users:
                sum = 0
                for i in range(len(check)):
                    if percent <= check[i]:
                        sum += emoticons[i] - int(emoticons[i] * (check[i] / 100))
                if sum >= money:
                    count += 1
                    result -= sum
                result += sum
            answer.append([count, result])
            return
        
        for i in range(len(discount)):
            check[depth] = discount[i]
            dfs(depth + 1)
    
    dfs(0)
    answer.sort(reverse=True)
    return answer[0]