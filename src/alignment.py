"""
파일 이름
  alignment.py

역할
  단백질 서열 정렬에 사용할 알고리즘 함수들을 모아 두는 모듈이다.
  이 파일 안에는 실제 정렬 계산 로직만 두고,
  파일 입출력이나 화면 출력 같은 작업은 다른 스크립트에서 처리한다.

이 파일에서 구현할 함수

  smithWaterman
    목적
      두 단백질 서열에 대해 로컬 정렬을 수행하고
      갭이 포함된 정렬 결과와 정렬 점수를 계산한다.

    입력
      seqOne        첫 번째 단백질 서열, 문자열
      seqTwo        두 번째 단백질 서열, 문자열
      matchScore    두 서열 문자가 같을 때 더할 점수
      mismatchScore 두 서열 문자가 다를 때 더할 점수
      gapPenalty    갭 하나를 추가할 때 더하는 패널티 점수

    출력
      alignedOne    갭이 포함된 첫 번째 정렬 결과 문자열
      alignedTwo    갭이 포함된 두 번째 정렬 결과 문자열
      score         최종 정렬 점수 하나

    특징
      동적 계획법을 사용해 점수 표를 만든 뒤,
      가장 점수가 높은 지점에서 거꾸로 따라가며
      정렬 경로를 복원하는 방식을 사용한다.
      점수 표와 경로 복원 방식은 이 파일 안에서만 사용하고,
      다른 파일에서는 함수 이름과 입력과 출력만 알면 된다.

  needlemanWunsch   선택 사항
    목적
      필요하다면 전역 정렬 알고리즘도 함께 구현할 수 있다.
      입력과 출력 형식은 smithWaterman 와 동일하게 맞춘다.

이 모듈과 다른 파일의 관계
  run-example.py, run-gap-penalty.py, run-blast-compare.py 파일은
  이 모듈에 정의된 함수들을 불러서 실제 서열 정렬 실험을 수행한다.
  따라서 이 파일이 정렬 알고리즘의 핵심 엔진 역할을 한다.
"""

from typing import Tuple


def smithWaterman(
    seqOne: str,
    seqTwo: str,
    matchScore: int,
    mismatchScore: int,
    gapPenalty: int,
) -> Tuple[str, str, int]:
    """
    smithWaterman 함수의 골격만 정의해 둔 상태이다.

    나중에 이 안에 동적 계획법과 경로 복원 과정을 구현하면 된다.
    지금은 프로젝트 구조를 잡기 위한 자리 표시자 역할만 한다.
    """
    raise NotImplementedError("정렬 알고리즘 구현이 필요합니다.")


def needlemanWunsch(
    seqOne: str,
    seqTwo: str,
    matchScore: int,
    mismatchScore: int,
    gapPenalty: int,
) -> Tuple[str, str, int]:
    """
    needlemanWunsch 함수는 선택 사항이다.

    전역 정렬이 필요할 경우에만 이 함수를 구현하면 된다.
    입력과 출력 형식은 smithWaterman 와 같다.
    """
    raise NotImplementedError("전역 정렬 구현이 필요하면 이 함수를 완성하세요.")
