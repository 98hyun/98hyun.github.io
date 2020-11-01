title: google analytics , git 
author: 98hyun
published: 2020-11-01
tags:[GA, git]

### google analytics 

google analytics의 목적은 log tracking 이다.  

이벤트, 트래픽 등 누가 어떤 경로를 통해 왔는지 마케팅에서 많이 쓰인다.  

이 블로그의 목적은 광고가 아니다. 내 글이 누군가에게 도움이 됐으면 하는 마음에서 썼다.  

그래서 미래에 어떤 글이 인기가 많을까? 하는 궁금에서 시작했다.  

[위 주소](https://cloud.google.com/appengine/docs/flexible/python/integrating-with-analytics) 를 보면 자세히 나와있다.  

바로 아래 `client`에 따른 방법을 제시한다. 나는 웹이니까 `analytics.js` 를 선택했다.  

클릭하니까 설명이 나온다. javascripts library고 ... ``<head>`` 를 넣어야하고 ...  

참고로 본인도 토익 못보고, javascripts 만질 줄 모른다. 모르면 번역기 돌리면서 몇번 보면  

`이 코드는 tag 고 head 밑에 넣는 거 구나. 저기 UA-XXXXX-Y 에는 내 id를 넣으면 되겠구나.` 가 보인다.  

그리고 이제 이 tag의 의미를 아는 것이다. `이 tag가 log tracking을 해서 data를 google analytics에 보내구나.`  

본인도 이 블로그의 인기가 높아지면 그때 여러가지 ga 함수의 기능을 이용 할 생각이다.  

### git 

이 글을 쓰는 이유는 처음 해본 pull request 와 branch 작업이기 때문이다. 그래서 정리하고 싶었다.  

정리하면, 먼저 branch를 생성한 후 수정한 후 push. 여기서 잠시 혹시나 아직도 `git push origin master`만 할까봐.  

git은 python의 pip, conda 의 conda 터미널과 소통하기 위한 시작 언어고 push a b 는 a에 b 를 push 한다는 명령이다.  

그래서 origin master는 origin 이라는 remote 저장소에 master branch를 넣는다는 뜻이다.  

쉽게 말해, 처음 `git remote add origin <path>` 할 때 origin 이 `retmoe alias(별명)`이다.  

master는 처음만들어지는 branch 이름은 master로 정해진다. 그래서 branch 이름을 맘대로 정할 수 있다.  

그래서 branch를 origin 에 넣으면 줄기가 2개가 있다는 뜻이니 github이 헷갈릴 수 있다.  

이때 master branch 와 push 한 branch를 merge를 하기 위해선 `요청(request)`가 필요하다.  

pull request 는 위 역할을 한다. 후에 사용한 branch는 자른다. 그게 `delete`고.  

`fork(clone) - add(commit) - push <remote> <branch> - pull request - merge - delete branch`  

큰 순서는 위와 같다.  

### 오늘의 공부

git merge와 pull request, branch 까지 처음 만져서 신기했다.  

직접 만지면서 경험하는게 제일 좋은 것 같다.  