# 그리디 알고리즘 (Greedy Algorithm, 탐욕법)

## 그리디 알고리즘 (Greedy Algorithm) 이란?

- 그리디 알고리즘은 어떤 문제를 '탐욕적'으로 푸는 알고리즘입니다.

  - 여기서 '탐욕적'이라는 말은 '현재 상황에서 지금 당장 좋은 것만 고르는 방법'을 의미합니다.
  - 즉, **선택을 해야할 때마다 당장 눈 앞에 놓인 최적의 상황만을 선택**하여 해답에 도달하는 방법입니다.

- **최적의 상황에 대한 기준**이 필요하므로, 그리디 알고리즘으로 풀 수 있는 문제들은 '가장 큰 순서대로', '가장 작은 순서대로 '같은 기준을 알게 모르게 제시해줍니다. 대체로 이 기준은 정렬 알고리즘을 사용했을 때 만족시킬 수 있습니다.

- 그런데, 순간마다 하는 최선의 선택이 **늘** 최선의 결과를 보장해주지는 않습니다.

  예시 그림에서, 선택지들을 합한 가장 큰 수를 찾는다고 가정해보겠습니다. 이 때, 출발점인 10에서 뻗어 나가는 선택지인 20과 30중에 더 큰 수인 30이 최적의 상황으로 선택됩니다. 하지만 결과적으로 30을 선택하여 얻는 합이 20을 선택하여 얻는 합보다 작습니다.
  따라서 그리디 알고리즘으로 문제의 해법을 찾았을 때는 그 해법이 정당한지 검토해야 합니다.

## 그리디 알고리즘을 적용시킬 수 있는 문제의 조건

- 탐욕적 선택 속성 (Greedy Choice Property): **이전의 선택이 이후의 선택에 영향을 주지 않아야 합니다.**
- 최적 부분 구조 (Optional Substructure): **부분 문제에 대한 최적의 결과가 전체에도 그대로 적용될 수 있어야 합니다.**

단, 이 두가지 조건을 문제가 완전히 만족하는지 증명하는 것은 쉽지 않기 때문에 우선 테스트 코드를 작성하여 동작을 확인하고 정당성을 확인하는 식으로 문제를 해결하는 경우가 많습니다.

## 그리디 알고리즘으로 해답을 찾는 방법

- 대부분의 그리디 알고리즘 문제는 문제 풀이를 위한 최소한의 **아이디어를 떠올리고, 이것이 정당한지 검토**할 수 있어야 답을 도출할 수 있습니다.
  - 선택 -> 정당성 검토 -> 해답 검토
- 어떤 문제를 만났을 때, 바로 문제 유형을 파악하기 어렵다면 그리디 알고리즘으로 문제를 해결할 수 있는지, 탐욕적인 해결법이 있는지 고민해봅니다.
- 만약 오랜 시간 고민해 보아도 해결 방법을 찾을 수 없다면 다이나믹 프로그래밍이나 그래프 알고리즘으로 문제를 해결할 수 있는지 고민해봅니다.

## 그리디 알고리즘 문제

> [백준 그리디 알고리즘 문제 모음](https://www.acmicpc.net/problemset?sort=ac_desc&algo=33)

- 백준 브론즈 문제
  - [거스름돈](https://www.acmicpc.net/problem/5585)
- 백준 실버 문제
  - [ATM](https://www.acmicpc.net/problem/11399)
  - [회의실 배정](https://www.acmicpc.net/problem/1931)
- 백준 골드 문제
  - [센서](https://www.acmicpc.net/problem/2212)
  - [강의실 배정](https://www.acmicpc.net/problem/11000)
  - [크게 만들기](https://www.acmicpc.net/problem/2812)
  - [보석 도둑](https://www.acmicpc.net/problem/1202)
  - [멀티탭 스케줄링](https://www.acmicpc.net/problem/1700)
