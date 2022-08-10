## deque

스택과 큐 기능을 모두 가진 양방향 큐. 앞, 뒤 양쪽 방향에서 요소를 추가하거나 삭제할 수 있다. deque는 그냥 queue에 비해서 양 끝 요소의 append와 pop이 압도적으로 빠르다. 일반적인 리스트는 삽입과 삭제에 O(n)이 소요되는 데, 데크(deque)는 O(1)이 소요된다.

```python
from collections import deque

deq = deque()

# Add element to the start
deq.appendleft(10)

# Add element to the end
deq.append(0)

# Pop element from the start
deq.popleft()

# Pop element from the end
deq.pop()
```
