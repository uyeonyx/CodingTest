같은 숫자는 싫어 
================
[문제링크](https://programmers.co.kr/learn/courses/30/lessons/12906)  
_연관태그: #배열_
***

## + 난이도: 1

## 문제 설명
배열 arr가 주어집니다. 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다.  
이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다.  
단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다.    
  
예를 들면,  

* arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.
* arr = [4, 4, 4, 3, 3] 이면 [4, 3] 을 return 합니다.
배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 완성해 주세요.

### 제한사항
* 배열 arr의 크기 : 1,000,000 이하의 자연수
* 배열 arr의 원소의 크기 : 0보다 크거나 같고 9보다 작거나 같은 정수

### 입출력 예
```
arr	answer
[1,1,3,3,0,1,1]	[1,3,0,1]
[4,4,4,3,3]	[4,3]
```

### 입출력 예 설명
입출력 예 #1,2

문제의 예시와 같습니다.

***

## 문제 풀이
반복문을 통해 배열의 원소를 하나씩 검사하며,  
직전 원소를 임시 변수에 저장하고 다음 원소와 비교한다.  
비교했을 때 같은 원소가 아닌 경우에만 정답 배열에 추가한다.

