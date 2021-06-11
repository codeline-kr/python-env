## 가상환경 만들기

```bash
python -m venv .venv
```

## 가상환경 activate

```bash
# windows
.venv/Scripts/activate

# 다른 os
source .venv/Scripts/activate

# pip 설치
python -m pip install --upgrade pip
```

## 라이브러리 install

```bash
pip install -r requirements.txt
```

## 라이브러리 출력

```bash
pip freeze > requirements.txt
```
