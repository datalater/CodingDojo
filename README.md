### pyenv
1. 설명
    1. 파이썬 프로젝트 별로 각각 맞는 다양한 python 버전으로 실행해 볼 수 있도록 환경 제공
    2. 참고: https://jiyeonseo.github.io/2016/07/27/install-pyenv/)
2. 설치
    1. $ brew install pyenv
    2. $ brew upgrade pyenv
3. PATH 설정
    1. $ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile 
    2. $ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile 
    3. $ echo 'eval "$(pyenv init -)"' >> ~/.bash_profile $ source ~/.bash_profile
4. 설치할 수 있는 목록 확인
    1. $ pyenv install --list
5. 원하는 python 버전 설치
    1. $ pyenv install 3.6.0
6. 설치된 버전 확인
    1. $ pyenv versions
7. 원하는 python 버전 선택
    1. $ vi .python-version
    2. 3.6.0
    3. $ pyenv versions
8. path가 잘 안 잡힐 때
    1. $ source ~/.bash_profile


### virtualenv
1. 설치
    1. $ pip install virtualenv
2. 생성
    1. $ virtualenv venv
3. 진입
    1. $ source venv/bin/activate


### pytest 및 pytest-watch
1. 설치
    1. $ pip install pytest
    2. $ pip install pytest-watch


### vim code highlighting 
1. $ vi ~/.vimrc 
2. syntax on 
3. :wq


### vim tab setting
1. $ vi ~/.vimrc
2. set smartindent
set tabstop=4
set expandtab
set shiftwidth=4
3. :wq
















END
