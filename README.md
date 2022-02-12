# 2048_ML

## 기본 정보
사용 언어 : Python
사용 알고리즘 : Q-Learning

## Motive for Selection
 4차 산업혁명 세상을 살아가면서 자연스레 소프트웨어 분야에 관심을 가지게 되었다. 또한 정보제어와 지능시스템 세부전공을 선택하기 전 고민이 많이 되었고, 소프트웨어 작품을 한 번도 해보지 않아서 이번 작품으로 소프트웨어 작품을 하고 싶었다. 많은 분야 중에서도 머신러닝에 흥미가 생겼고 직접 공부해보고 싶다는 생각이 들었다. 그리고 평소 게임을 직접 만들어보고 싶다는 생각을 해왔었다. 그래서 두 분야를 융합하여 평소 즐겨하던 게임인 2048 게임을 머신러닝의 강화학습을 이용하여 학습시키는 작품으로 선정하게 되었다. 

## Development Goals
1. Python을 이용한 2048게임 제작
- pygame을 이용하여 게임을 제작하며 python언어를 공부한다.

2. 강화학습을 통한 게임 학습
- Q-learning을 통해 2048 게임을 학습 시킨다.

## Software Architecture
<img src="https://user-images.githubusercontent.com/53519801/153714688-042647b5-8a82-4e21-88df-5990a81bcfd3.png" width="200" height="400">

## System Architecture
<img src="https://user-images.githubusercontent.com/53519801/153714730-e5b65f10-4014-4c72-a090-d210c969a2fb.png" width="400" height="350">

## Project Contents
### 1. Python을 이용한 2048 게임 제작
![image](https://user-images.githubusercontent.com/53519801/153714944-994a533c-e190-463b-afd2-acf448d10752.png)

 - 4X4 크기의 게임판을 만들고 2 혹은 4의 숫자 상자를 랜덤으로 출력한다.
 - 키보드 방향키로 입력을 받아 방향키를 누르면 숫자 블록이 누른 방향키의 방향으로 쏠린다.
 - 이 때 만약 두 개의 같은 숫자가 붙어있는 상황에서 이동하면 두 숫자를 더한다. (숫자는 빈 공간에 계속 랜덤으로 출력)
 - 방향키로 숫자를 계속 합하여 2048 혹은 그 이상의 숫자를 만들어내면 승리한다.
 - 빈 공간이 없고 어떤 블럭도 이동할 수 없을 시 게임은 종료된다.

### 2. Q-Learning
ε-greedy 방식을 사용한다.

## Project Scenarios
1. 게임이 정상적으로 작동되는지 확인한다.
2-1. 2048 AI로 게임을 시작한다. 
2-2. 직접 게임을 한다.
3. 게임 결과를 출력한다.


## Project Schedule
![image](https://user-images.githubusercontent.com/53519801/153715101-b08dc467-ba8f-42ca-9d44-29f50afa6e75.png)
(2019년 일정입니다.)




