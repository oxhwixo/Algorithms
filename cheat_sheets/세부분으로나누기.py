n = "12345"

for i in range(1, len(n)):
    for j in range(i + 1, len(n)):
        part1 = n[:i]
        part2 = n[i:j]
        part3 = n[j:]

        print(part1, part2, part3)