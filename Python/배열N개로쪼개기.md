```python
s = [1,2,3,4,5,6,7,8]

# 3개씩 자르기
split_s = [ s[j: j + 3] for j in range(0, len(s), 3)]
```
