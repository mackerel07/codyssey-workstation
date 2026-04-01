# codyssey-workstation
## 1. 프로젝트 개요

본 프로젝트는 Docker를 활용하여 개발 워크스테이션 환경을 구축하는 것을 목표로 한다.

Git과 GitHub를 이용한 버전 관리 환경을 구성하고,  
Docker를 통해 컨테이너 기반의 실행 환경을 직접 구성 및 실습하였다.

이를 통해 이미지와 컨테이너의 개념, 그리고 격리된 실행 환경의 특징을 이해하고자 한다.

---

## 2. 실행 환경

- OS: macOS (MacBook Air)
- 터미널: macOS 기본 터미널
- Git: Git CLI
- 원격 저장소: GitHub
- 컨테이너 환경: OrbStack (Docker Engine)
- Docker 버전: 28.5.2
## 터미널 기본 명령

## 수행 체크리스트

- [O] 터미널 기본 조작 및 폴더 구성
- [O] 권한 변경 실습
- [O] Docker 설치 및 점검
- [O] hello-world 및 ubuntu 실행
- [O] Dockerfile 빌드 및 실행
- [O] 포트 매핑 접속
- [O] 바인드 마운트 반영
- [O] 볼륨 영속성 검증
- [O] Git 설정 및 GitHub 연동

```bash
sam@yeon-eowamaeche-ui-MacBookAir codyssey-workstation % pwd
/Users/sam/Documents/GitHub/codyssey-workstation
sam@yeon-eowamaeche-ui-MacBookAir codyssey-workstation % ls
README.md
# 현재 위치 확인
sam@yeon-eowamaeche-ui-MacBookAir ~ % pwd
/Users/sam

# 폴더 생성 및 이동
sam@yeon-eowamaeche-ui-MacBookAir ~ % mkdir terminal_test
sam@yeon-eowamaeche-ui-MacBookAir ~ % cd terminal_test

# 빈 파일 생성 및 목록 확인 (숨김 파일 포함)
sam@yeon-eowamaeche-ui-MacBookAir terminal_test % touch empty_file.txt
sam@yeon-eowamaeche-ui-MacBookAir terminal_test % ls -la
total 0
drwxr-xr-x   3 sam  staff   96  3 30 21:00 .
drwxr-x---+ 85 sam  staff 2720  3 30 21:00 ..
-rw-r--r--   1 sam  staff    0  3 30 21:00 empty_file.txt

# 파일 내용 작성 및 확인
sam@yeon-eowamaeche-ui-MacBookAir terminal_test % echo "Hello Codyssey!" > text_file.txt
sam@yeon-eowamaeche-ui-MacBookAir terminal_test % cat text_file.txt
Hello Codyssey!

# 파일 복사
sam@yeon-eowamaeche-ui-MacBookAir terminal_test % cp text_file.txt copy_file.txt

# 이동/이름 변경
sam@yeon-eowamaeche-ui-MacBookAir terminal_test % mv copy_file.txt rename_file.txt

# 상위 폴더로 이동 후 삭제
sam@yeon-eowamaeche-ui-MacBookAir terminal_test % cd ..
sam@yeon-eowamaeche-ui-MacBookAir ~ % rm -r terminal_test

# 실습 대상 생성
sam@yeon-eowamaeche-ui-MacBookAir ~ % touch perm_test.txt
sam@yeon-eowamaeche-ui-MacBookAir ~ % mkdir perm_test_dir

# [변경 전] 권한 확인
sam@yeon-eowamaeche-ui-MacBookAir ~ % ls -l perm_test.txt
-rw-r--r--  1 sam  staff  0  3 30 21:05 perm_test.txt
sam@yeon-eowamaeche-ui-MacBookAir ~ % ls -ld perm_test_dir
drwxr-xr-x  2 sam  staff  64  3 30 21:05 perm_test_dir

# 권한 변경 수행 (파일: 755, 폴더: 700)
sam@yeon-eowamaeche-ui-MacBookAir ~ % chmod 755 perm_test.txt
sam@yeon-eowamaeche-ui-MacBookAir ~ % chmod 700 perm_test_dir

# [변경 후] 권한 비교
sam@yeon-eowamaeche-ui-MacBookAir ~ % ls -l perm_test.txt
-rwxr-xr-x  1 sam  staff  0  3 30 21:05 perm_test.txt
sam@yeon-eowamaeche-ui-MacBookAir ~ % ls -ld perm_test_dir
drwx------  2 sam  staff  64  3 30 21:05 perm_test_dir
결과 확인:
perm_test.txt 파일은 -rw-r--r-- (644)에서 -rwxr-xr-x (755)로 변경되어 소유자, 그룹, 기타 사용자 모두에게 실행(x) 권한이 추가되었습니다.
perm_test_dir 디렉토리는 drwxr-xr-x (755)에서 drwx------ (700)으로 변경되어 소유자만 읽기/쓰기/실행이 가능하고 다른 사용자의 접근이 완벽히 차단되었음을 확인하였습니다.

## Git 설정 및 GitHub 연동

### 1. Git 기본 설정

```bash
$ git config --global user.name "mackerel07"
$ git config --global user.email "b*********70@gmail.com"
$ git config --global init.defaultBranch main

$ git init
$ git remote add origin https://github.com/mackerel07/codyssey-workstation.git
sam@yeon-eowamaeche-ui-MacBookAir codyssey-workstation % git remote -v
origin  https://github.com/mackerel07/codyssey-workstation.git (fetch)
origin  https://github.com/mackerel07/codyssey-workstation.git (push)

$ touch README.md
$ git add .

sam@yeon-eowamaeche-ui-MacBookAir codyssey-workstation % git status
On branch main
Your branch is based on 'origin/main', but the upstream is gone.
  (use "git branch --unset-upstream" to fixup)

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   README.md
sam@yeon-eowamaeche-ui-MacBookAir codyssey-workstation % git add README.md 
sam@yeon-eowamaeche-ui-MacBookAir codyssey-workstation % git commit -m "feat: chore README.md"
[main abe5c36] feat: chore README.md
 1 file changed, 1 insertion(+)

**트러블슈팅**

### 1. GitHub push 인증 실패

#### 1) 문제
git push 실행 시 아래와 같은 인증 오류가 발생하였다.

#### 2) 원인 가설
GitHub에서 더 이상 비밀번호 기반 인증을 지원하지 않기 때문에 발생한 문제라고 판단하였다.
#### 3) 확인
GitHub 정책을 확인한 결과, HTTPS 방식에서는 비밀번호 대신 Personal Access Token 또는 외부 인증 방식이 필요함을 확인하였다.
#### 4) 해결 / 대안
Visual Studio Code에서 GitHub 계정 로그인을 수행하여 인증을 완료하였다.
이후 git push 명령이 정상적으로 수행되었다.

$ git push
Username for 'https://github.com': mackerel07
Password for 'https://mackerel07@github.com':
remote: Invalid username or token. Password authentication is not supported for Git operations.
fatal: Authentication failed

sam@yeon-eowamaeche-ui-MacBookAir codyssey-workstation % git push
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 10 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (9/9), 707 bytes | 707.00 KiB/s, done.
Total 9 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/mackerel07/codyssey-workstation.git
 * [new branch]      main -> main

 ## ✔️ Git 역할

- 로컬에서 버전 관리 수행
- GitHub를 통해 원격 저장소에 코드 공유

### 2.Docker 기본 실행
sam@yeon-eowamaeche-ui-MacBookAir codyssey-workstation % docker --version
Docker version 28.5.2, build ecc6942
sam@yeon-eowamaeche-ui-MacBookAir codyssey-workstation % docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.
##### Docker가 정상적으로 설치되고 컨테이너 실행이 성공적으로 이루어졌음을 확인하였다.

### 3. Ubuntu 컨테이너 실행
sam@yeon-eowamaeche-ui-MacBookAir codyssey-workstation % docker run -it ubuntu bash
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
86790fc5660d: Pull complete 
Digest: sha256:186072bba1b2f436cbb91ef2567abca677337cfc786c86e107d25b7072feef0c
Status: Downloaded newer image for ubuntu:latest
root@6599e567239e:/# ls
bin  boot  dev  etc  home  lib  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@6599e567239e:/# echo hello
hello
#### 컨테이너 내부에서 명령어가 정상적으로 실행되며, 호스트와 분리된 환경임을 확인하였다.

### 4. Docker 상태 확인
sam@yeon-eowamaeche-ui-MacBookAir codyssey-workstation % docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED              STATUS              PORTS     NAMES
6599e567239e   ubuntu    "bash"    About a minute ago   Up About a minute             interesting_meninsky
sam@yeon-eowamaeche-ui-MacBookAir codyssey-workstation % docker ps -a
CONTAINER ID   IMAGE         COMMAND    CREATED              STATUS                      PORTS     NAMES
6599e567239e   ubuntu        "bash"     About a minute ago   Up About a minute                     interesting_meninsky
ec0b5630d21c   hello-world   "/hello"   2 minutes ago        Exited (0) 2 minutes ago              thirsty_pike
fdc88053091b   hello-world   "/hello"   12 minutes ago       Exited (0) 12 minutes ago             goofy_moore
fd30b82f5713   hello-world   "/hello"   12 minutes ago       Exited (0) 12 minutes ago             stoic_brattain
sam@yeon-eowamaeche-ui-MacBookAir codyssey-workstation % docker images
REPOSITORY    TAG       IMAGE ID       CREATED       SIZE
hello-world   latest    eb84fdc6f2a3   6 days ago    5.2kB
ubuntu        latest    e3847ac055b4   4 weeks ago   101MB
sam@yeon-eowamaeche-ui-MacBookAir codyssey-workstation % docker info
Client:
 Version:    28.5.2
 Context:    orbstack
 Debug Mode: false
 Plugins:
  buildx: Docker Buildx (Docker Inc.)
    Version:  v0.29.1
    Path:     /Users/sam/.docker/cli-plugins/docker-buildx
  compose: Docker Compose (Docker Inc.)
    Version:  v2.40.3
    Path:     /Users/sam/.docker/cli-plugins/docker-compose
...이하 생략

sam@yeon-eowamaeche-ui-MacBookAir web % docker stats
CONTAINER ID   NAME               CPU %     MEM USAGE / LIMIT    MEM %     NET I/O           BLOCK I/O         PIDS 
5d886db78b60   my-web-container   0.00%     7.48MiB / 7.807GiB   0.09%     2.81kB / 1.18kB   10.2MB / 8.19kB   11 

sam@yeon-eowamaeche-ui-MacBookAir web % docker logs 5d886db78b60
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
이하생략...
#### 실행 중인 컨테이너와 종료된 컨테이너 상태를 확인하였다.

### exec vs attach 차이 정리
sam@yeon-eowamaeche-ui-MacBookAir web % docker exec 5d886db78b60 ls
bin
dev
docker-entrypoint.d
docker-entrypoint.sh
이하 생략...
sam@yeon-eowamaeche-ui-MacBookAir web % docker attach 5d886db78b
>둘다 컨테이너에 접속하는 명령어지만, attach는 컨테이너에 직접 연결하여 제어하고, exec는 컨테이너 내부에 새로운 프로세서를 실행하여 접속한다

### 바인드 마운트 전후 변경

#### 호스트에서 확인
sam@yeon-eowamaeche-ui-MacBookAir ~ % mkdir bind-test
sam@yeon-eowamaeche-ui-MacBookAir ~ % cd bind-test
sam@yeon-eowamaeche-ui-MacBookAir bind-test % echo "hello" > test.txt
sam@yeon-eowamaeche-ui-MacBookAir bind-test % cat test.txt
hello

#### 컨테이너에서 확인
sam@yeon-eowamaeche-ui-MacBookAir web % docker run -v $(pwd):/app -it ubuntu
<$(pwd) : 현재 내 컴퓨터 폴더
/app : 컨테이너 내부 경로
즉 → 내 폴더 = 컨테이너 /app과 연결됨>
root@28c86dae2666:/# cat /app/test.txt
hello

#### 컨테이너 종료 후 호스트에서 파일 수정
root@28c86dae2666:/# exit
exit

sam@yeon-eowamaeche-ui-MacBookAir bind-test % echo "changed" > test.txt
sam@yeon-eowamaeche-ui-MacBookAir bind-test % cat test.txt
changed

#### 컨테이너 접속 후 확인
sam@yeon-eowamaeche-ui-MacBookAir bind-test % docker run -it -v $(pwd):/app ubuntu bash
root@28c86dae2666::/# cat /app/test.txt
changed
<바인드 마운트를 사용하여 호스트 디렉토리를 컨테이너에 연결하였다.
호스트에서 파일 내용을 변경한 후 컨테이너에서 확인한 결과, 변경 사항이 즉시 반영되는 것을 확인하였다.
이를 통해 바인드 마운트는 호스트와 컨테이너 간에 동일한 파일 시스템을 공유함을 알 수 있다.>

## **트러블슈팅**: 바인드 마운트 경로 오류
문제
바인드 마운트를 사용하여 컨테이너를 실행했으나,
컨테이너 내부 `/app` 디렉토리에 파일이 보이지 않는 문제가 발생하였다.

원인/가설
* 호스트 경로가 잘못 지정되었을 가능성
* 존재하지 않는 디렉토리를 마운트했을 가능성

확인 과정

```bash
docker run -it -v /bind-test:/app ubuntu bash
root@28c86dae2666:/# ls /app

결과:
(출력 없음)
→ `/app` 디렉토리가 비어있는 것을 확인

해결 방법
호스트의 실제 경로를 정확히 지정하도록 수정

```bash
docker run -it -v $(pwd):/app ubuntu bash
 

<바인드 마운트 사용 시 호스트 경로가 정확하지 않으면 파일이 보이지 않는 문제가 발생한다.
`$(pwd)`를 사용하여 현재 디렉토리를 지정함으로써 문제를 해결할 수 있다.>

### Docker 개념 정리
- Docker Image는 컨테이너 실행을 위한 설계도이다.
- Container는 이미지를 기반으로 실행된 독립적인 환경이다.
- 컨테이너 내부는 호스트 시스템과 격리되어 있다.

### 5.Dockerfile 기반 웹 서버 실행
```bash
sam@yeon-eowamaeche-ui-MacBookAir codyssey-workstation % mkdir web
sam@yeon-eowamaeche-ui-MacBookAir codyssey-workstation % ls
README.md	web
sam@yeon-eowamaeche-ui-MacBookAir codyssey-workstation % cd web
sam@yeon-eowamaeche-ui-MacBookAir web % mkdir site
sam@yeon-eowamaeche-ui-MacBookAir web % touch site/index.html   
sam@yeon-eowamaeche-ui-MacBookAir web % touch Dockerfile
sam@yeon-eowamaeche-ui-MacBookAir web % nano
sam@yeon-eowamaeche-ui-MacBookAir web % nano site/index.html
####사이트 코드 작성
<h1>Hello Docker</h1>

sam@yeon-eowamaeche-ui-MacBookAir web % ls  
Dockerfile	site
sam@yeon-eowamaeche-ui-MacBookAir web % ls   
Dockerfile	site
sam@yeon-eowamaeche-ui-MacBookAir web % nano Dockerfile
sam@yeon-eowamaeche-ui-MacBookAir web % docker build -t my-web:1.0 .
[+] Building 8.9s (7/7) FINISHED                                                                                                 docker:orbstack
 => [internal] load build definition from Dockerfile                                                                                        0.0s
 => => transferring dockerfile: 90B                                                               
 ...이하 생략
sam@yeon-eowamaeche-ui-MacBookAir web % docker run -d -p 8080:80 --name my-web-container my-web:1.0              
d886db78b607e9cad9ce88bb089600b0114b51f9f6ffa13010a6a413d897445

### 웹사이트 접속
브라우저에 http://localhost:8080 접속 후, Hello Docker을 확인함
>웹 서버가 정상적으로 실행되고 포트 매핑이 이루어졌음을 확인하였다

###제작 결과
기존 Dockerfile 기반 커스텀 이미지 제작
본 작업은 제시된 방식 중 (A) 웹 서버 베이스 이미지 활용 + 정적 콘텐츠 교체 방식을 선택하여 진행하였다

1) 선택한 기존 베이스 이미지 및 Dockerfile 구성
베이스 이미지: nginx:latest (웹 서버 베이스 이미지)

선택 이유: 별도의 웹 서버 설정 없이 NGINX 베이스 이미지의 기본 웹 루트 디렉토리에 커스텀 HTML 파일만 덮어쓰는 방식으로 빠르고 간편하게 정적 웹사이트를 배포할 수 있기 때문임.
2) 적용한 커스텀 포인트 및 각각의 목적
커스텀 포인트 1: site/index.html 파일 작성

목적: NGINX 기본 웰컴 페이지 대신, "Hello Docker"라는 문구가 출력되는 나만의 커스텀 정적 웹 화면을 제공하기 위함.

커스텀 포인트 2: Dockerfile 내 COPY 명령어 사용

목적: 호스트에서 작성한 커스텀 index.html 파일을 컨테이너 이미지 내부의 NGINX 기본 웹 서비스 디렉토리(/usr/share/nginx/html/)로 복사하여 기존 파일을 교체하기 위함

### 6.볼륨 영속성 검증

#### 볼륨 생성하기
sam@yeon-eowamaeche-ui-MacBookAir web % docker volume create mydata
mydata

#### 컨테이너 실행 및 볼륨 연결
am@yeon-eowamaeche-ui-MacBookAir web % docker run -d --name vol-test1 -v mydata:/data ubuntu sleep infinity
ea1adb6f419ba06cb28652bb185617c472ffc7762d571e058fff0688a5d7404c
sam@yeon-eowamaeche-ui-MacBookAir web % docker exec -it vol-test1 bash -c "echo 'Volume Data Safe!' > /data/hello.txt && cat /data/hello.txt"
Volume Data Safe!
(내부에 접속해서 hello.txt에 글자쓰기 및 확인 {>을 통해 파일생성})

#### 컨테이너 삭제
sam@yeon-eowamaeche-ui-MacBookAir web % docker rm -f vol-test1
vol-test1

#### 두 번째 컨테이너 실행
sam@yeon-eowamaeche-ui-MacBookAir web % docker run -d --name vol-test2 -v mydata:/data ubuntu sleep infinity
ad90c8ff11601ae9454f60f32ed71088991358549a915b0eb6712fc2c9b714ab

#### 데이터 확인(영속성 검증)
sam@yeon-eowamaeche-ui-MacBookAir web % docker exec -it vol-test2 bash -c "cat /data/hello.txt"
Volume Data Safe!
<위 과정을 통해 첫 번째 컨테이너(vol-test1) 내부에 생성한 데이터가 컨테이너 강제 삭제 후에도 유실되지 않음을 직접 확인하였다.
완전히 새로운 두 번째 컨테이너(vol-test2)를 실행하여 동일한 볼륨(mydata)을 마운트했을 때, 이전 컨테이너에서 작성했던 데이터(hello.txt)를 그대로 조회할 수 있었다.
이를 통해 컨테이너의 생명주기(생성/삭제)와는 독립적으로 호스트에 데이터를 안전하게 보존하는 Docker 볼륨의 영속성(Persistence) 특징을 성공적으로 검증하였다.>

### 7.Git 설정 및 Github 연동 증거
sam@yeon-eowamaeche-ui-MacBookAir web % git config --list
credential.helper=osxkeychain
init.defaultbranch=main
filter.lfs.clean=git-lfs clean -- %f
filter.lfs.smudge=git-lfs smudge -- %f
filter.lfs.process=git-lfs filter-process
filter.lfs.required=true
user.name=mackerel07
user.email=b*********170@gmail.com
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
core.ignorecase=true
core.precomposeunicode=true
submodule.active=.
remote.origin.url=https://github.com/mackerel07/codyssey-workstation.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
branch.main.remote=origin
branch.main.merge=refs/heads/main
lfs.repositoryformatversion=0

### 8.보안 및 개인정보 보호 준수
본 기술 문서(README.md) 및 첨부된 모든 터미널 로그, 스크린샷 작성 시 아래의 보안 수칙을 철저히 준수하였습니다.

터미널 조작 로그 기록 중 발생할 수 있는 개인 토큰(PAT), 비밀번호, 인증 코드 등의 민감 정보는 문서에 포함하지 않았습니다.

GitHub Push 과정에서 발생한 인증 단계 기록 시, 민감한 자격 증명 정보가 텍스트나 이미지로 노출되지 않도록 주의하였으며, 안전한 VSCode OAuth 연동 방식을 채택하여 개인정보를 보호하였습니다.

결과에 나오는 본인의 실제 이메일은 개인정보에 해당하여 마스킹 처리 하였습니다.

기타링크:
웹사이트 포트매핑 검증: https://ibb.co/bjwHrRJP
깃허브 연동검증(git push): https://ibb.co/bjwHrRJP
깃허브 연동(로그인): https://ibb.co/yFptmj1s