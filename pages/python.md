title: python 3.9 version 특징 
author: 98hyun
published: 2020-10-31 
tags: [python ]

### remarkable python 3.9 version 

파이썬 3.7 부터 친숙했다. 그런데 누군가는 더 편하게 language 를 쓰기 위해서 개발을 한다.  

지금까지 파이썬 3.8 을 기본으로 썼지만, 당연히 3.8+a 이므로 언젠가 파이썬 3.9 를 사용할 것이다.  

이번엔 파이썬 3.9, 3.8에서 추가된 주목할 만한 특징을 살펴 보겠다.  

1. syntax 

학교에서 프로그래밍을 배운다. syntax 는 문법. 쉽게 말하면 hello 를 helo 라고 쓰면   

`사람`들은 알아들어도 `컴퓨터`는 못알아 듣는다. syntax 는 쉽게 말해 규칙이다.  

* collections, decorator and dict

주목할 만한 점은 union 기능이 dict 에도 추가 됐다.  

    :::python 
    x = {"key1": "value1 from x", "key2": "value2 from x"}
    y = {"key2": "value2 from y", "key3": "value3 from y"}
    print(y|x)
    # {'key2': 'value2 from x', 'key3': 'value3 from y', 'key1': 'value1 from x'}

2. built-in 

built-in 이 무슨 뜻인지 정확히는 모르겠지만 str, tuple, list 같은 자료 구조 느낌이 난다.  

* string (removesuffix, removeprefix)

이번 str 자료구조에서 사용할 수 있는 method가 추가 됐다.  

    :::python 
    a='98hyun'
    print(a.removeprefix('98'))
    print(a.removesuffix('hyun'))
    # 'hyun'
    # '98' 

3. improvement

파이썬의 모든 기능을 잘 알지 못하지만, 아래 문장이 눈에 들어 왔다.  

`a number of Python builtins (range, tuple, set, frozenset, list, dict) are now sped up using PEP 590 vectorcall`

뭔지는 모르겠지만, pep500 vectorcall 을 사용해서 자료구조들이 빨라졌다는 뜻이다.  

### 오늘의 공부 

대단하고 존경스럽다. 정말 기본을 위해서, 편리를 위해서 언어를 개발하는 것이.  

계속 파이썬 3.9 가 나왔다고 하길래 뭐가 어떻게 변했나 봤지만 역시 가까운 version update라 편의를 늘렸다.  

처음 파이썬을 분석해봤다. 알면 알 수록 심오한 것 같다.  

물론 이것저것 공부하고 싶지만, 집중해야 할 것은 일단 통계와 알고리즘이다.  

우선순위를 파악하는 것이 중요하다.  