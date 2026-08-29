# Deep Learning from Scratch 6

『밑바닥부터 시작하는 딥러닝 6』 학습 코드를 정리하는 프로젝트입니다.

## 구조

```text
src/
├── ch01/
├── ch02/
└── common/
```

장별 예제는 `src/chXX`에, 여러 장에서 함께 사용하는 코드는 `src/common`에 둡니다.
필요한 디렉터리는 학습을 진행하면서 추가합니다.

## 환경 설정

```bash
uv sync
```

## 실행

Python 파일은 프로젝트 루트에서 다음과 같이 실행합니다.

```bash
uv run python src/ch01/sample.py
```

Zed에서는 `# %%`로 구분된 셀을 Python 커널로 실행할 수도 있습니다.
