---
title: "오늘의 배움: 기말고사 보안시스템구축"
date: 2026-06-06 12:00:00 +0900
categories: [TIL, network]
tags: [기말고사]
permalink: /posts/network-my-first-til/
---

# 기말고사
## 보안시스템 구축


![alt text](image-17.png)
**(요구사항 1)**
![alt text](image-18.png)
우분투에 ssh를 설치한다.

**(요구사항 2)**
![alt text](image-19.png)
![alt text](image-20.png)
ssh를 실행시키고 nano에 들어가 
![alt text](image-21.png)
![alt text](image-22.png)
![alt text](<스크린샷 2026-06-14 141630.png>)
ssh_config 상태를 느슨하게 한다

**(요구사항 3)**
![alt text](image-23.png)
칼리에서 우분투(192.169.0.30)으로 들어간다
![alt text](<스크린샷 2026-06-14 140545.png>)
kali@kali에서 우분투 계정으로 접속한걸 볼수있다
![alt text](image-24.png)
같은 ip라도 존재하지않는 계정명으로 들어가면 실패하는걸 볼수있다

**(요구사항 4)**
![alt text](image-25.png)
우분투 로그를 살펴보면 
칼리에서 들어간 Accepted password 즉 계정접속 성공이 뜨고
다른 계정명으로 들어간건 Fail 이 뜨는걸 볼수있다

**(요구사항 5)**
이 상태가 왜 위험하냐면 id와 password 만 있으면 접속이 가능해
무차별 대입공격으로 쉽게 뚫릴가능성이 높다.
**방어방법 1** 기본포트인 22대신 2222를 사용하여 자동화된 공격을 스캔한다
**방어방법 2** PasswordAuthentication no로 설정하여 비밀번호 접속을 완전히 막고, 미리 등록된 안전한 SSH 키 쌍을 통해서만 접속을 허용한다


![alt text](image-26.png)

**(요구사항 6)**
![alt text](image-27.png)
![alt text](image-28.png)

**(요구사항 7)**
![alt text](image-29.png)
![alt text](image-30.png)
ketgen(키를 생성하겠다)
-t (type)
ed25519 (요즘 쓰는 키)

**(요구사항 8)**
![alt text](image-31.png)

**(요구사항 9)**

![alt text](image-32.png)
ssh 2222포트가 안열린걸 볼수있는데 다시 ssh를 켜주면

![alt text](image-33.png)

우분투에 ssh 포트가 2222로 된걸 볼수있다 
다시 칼리에서 우분투로 접속해보면

![alt text](image-35.png)
개인키 접속이 성공한걸 볼수있다

![alt text](image-36.png)
비밀번호 방식은 실패


**(요구사항 10)**
![alt text](image-37.png)


![alt text](image-38.png)

**(요구사항 11)**
![alt text](image-39.png)
![alt text](image-40.png)
fail2ban 설치 및 활성화

**(요구사항 12)**
![alt text](image-41.png)

**(요구사항 13)**
![alt text](image-42.png)

**(요구사항 14)**
![alt text](image-43.png)

**(요구사항 15)**
![alt text](image-44.png)
192.168.0.10 칼리의 ip 가 차단먹은걸 볼수있다
![alt text](image-45.png)
baneed ip list 에서 칼리 ip 가 없어진걸 볼수있다

![alt text](image-46.png)

**(요구사항 16)**
![alt text](image-47.png)

**(요구사항 17)**
![alt text](image-48.png)

**(요구사항 18)**
![alt text](image-49.png)

**(요구사항 19)**
![alt text](image-50.png)

**(요구사항 20)**
![alt text](image-51.png)
![alt text](image-54.png)


**(요구사항 21)**
![alt text](image-53.png)


![alt text](image-55.png)


**(요구사항 22)**
![alt text](image-56.png)

**(요구사항 23)**
![alt text](image-57.png)
![alt text](image-58.png)

**(요구사항 24)**
![alt text](image-60.png)

**(요구사항 25)**
![alt text](image-61.png)

**(요구사항 26)**
![alt text](image-62.png)



![alt text](image-63.png)
**(요구사항 27)**
![alt text](image-64.png)
보안레벨 low 설정

**(요구사항 28)**
![alt text](image-65.png)

**(요구사항 29)**
![alt text](image-66.png)

**(요구사항 30)**
네트워크 방화벽은 IP 주소와 포트 번호같은 OSI 3·4계층 정보만 확인하고 통과시키는데 SQL Injection 공격은 이미 허용된 80번 포트를 통해 정상적인 HTTP 요청의 내용물에 악성 코드를 실어 보내기 때문이다

![alt text](image-67.png)

**(요구사항 31)**
![alt text](image-70.png)

**(요구사항 32)**
![alt text](image-69.png)

**(요구사항 33)**
![alt text](image-73.png)
![alt text](image-72.png)

**(요구사항 34)**
![alt text](image-74.png)

**(요구사항 35)**
거짓 양성은 공격이 아닌 일반 사용자의 정상적인 요청을 웹방화벽이 악성 공격으로 잘못 인식해 차단하는것이다

![alt text](image-76.png)

**(요구사항 36)**
![alt text](image-75.png)
인터페이스 이름 enp0s3을 확인
![alt text](image-77.png)
snort 설치

**(요구사항 37)**
![alt text](image-78.png)

**(요구사항 38)**
![alt text](image-79.png)
![alt text](image-80.png)
검증 성공

**(요구사항 39)**
![alt text](image-81.png)


![alt text](image-83.png)


**(요구사항 40)**
![alt text](image-82.png)


**(요구사항 41)**
![alt text](image-84.png)

**(요구사항 42)**
![alt text](image-85.png)



**(요구사항 43)**
![alt text](image-86.png)

**(요구사항 44)**
![alt text](image-87.png)

drop 은 패킷차단할떄 아무런 응답없이 통째로 차단
reject 는 패킷차단후 차단 안내 패킷이 나옴
sdrop 은 drop과 비슷하게 아무 응답없이 버리지만 로그파일에 기록조차 남기지않음


![alt text](image-88.png)



**5) 위협 담당 방어 계층 매핑 표**

| 공격/위협 유형                             | 담당 방어 계층        |
| :----------------------------------------- | :-------------------- |
| **SSH 무차별 대입 공격**                   | 시스템 및 인증 계층   |
| **허용되지 않은 포트 스캔 및 서비스 접근** | 네트워크 계층         |
| **SQL Injection, XSS 등 웹 취약점 공격**   | 애플리케이션 계층     |
| **비정상 네트워크 트래픽 및 ICMP 플러딩**  | 네트워크 및 감시 계층 |

다층 방어란 계층별로 독립적인 방어벽을 만들어 하나의 방어 체계가 뚫리더라도 다음 계층에서 공격을 차단하여 전체적인 안전성을 보장하는것이다.

