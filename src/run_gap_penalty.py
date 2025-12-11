"""
파일 이름
  run-gap-penalty.py

역할
  같은 단백질 서열 쌍에 대해 갭 패널티 값을 여러 가지로 바꾸어 가며
  정렬 알고리즘을 반복 실행하고,
  각 설정에서 정렬 점수와 갭의 개수, 불일치 개수를 정리하는 스크립트이다.

이 파일에서 할 일

  하나, 예시 서열 읽기
    data 폴더의 example-pair.txt 파일에서
    예시로 사용할 단백질 서열 두 개를 읽어 온다.
    run-example.py 에서 사용한 것과 같은 서열을 사용한다.

  둘, 갭 패널티 설정 목록 정하기
    예를 들어 갭 패널티 값을 마이너스 1, 마이너스 3, 마이너스 5 와 같이 몇 가지 정해 둔다.
    일치 점수와 불일치 점수는 고정하고
    갭 패널티만 바꾸면서 실험한다.

  셋, 정렬 반복 실행
    설정한 각 갭 패널티 값에 대해
    alignment 모듈의 smithWaterman 함수를 호출해 정렬을 수행한다.
    각 결과에서 전체 정렬 점수,
    갭 문자의 개수,
    서로 다른 아미노산이 맞춰진 위치의 개수를 계산한다.

  넷, 결과를 표 형태로 저장
    설정 하나마다 얻은 숫자들을 한 줄로 정리하여
    results 폴더의 gap-penalty-results.csv 파일에 저장한다.
    이 파일은 나중에 보고서에서
    갭 패널티에 따른 정렬 결과 비교 표를 만들 때 그대로 사용할 수 있다.

보고서와의 연결

  이 스크립트에서 얻는 숫자 자료는
  보고서의 갭 패널티 변화에 따른 결과 비교 부분에서
  갭 패널티가 커질수록 갭이 줄고 불일치가 늘어나는지 등
  정렬 모양의 변화를 설명할 때 근거로 사용된다.
"""

import csv

from alignment import smithWaterman


def readExamplePair() -> tuple[str, str]:
    path = "data/example-pair.txt"
    with open(path, "r", encoding="utf-8") as handle:
        lines = [line.strip() for line in handle.readlines() if line.strip()]
    if len(lines) < 2:
        raise ValueError("example-pair.txt 파일에는 두 줄의 서열이 필요합니다.")
    return lines[0], lines[1]


def countGapsAndMismatches(alignedOne: str, alignedTwo: str) -> tuple[int, int]:
    if len(alignedOne) != len(alignedTwo):
        raise ValueError("정렬된 두 서열의 길이가 다릅니다.")
    gapCount = 0
    mismatchCount = 0
    for letterOne, letterTwo in zip(alignedOne, alignedTwo):
        if letterOne == "-" or letterTwo == "-":
            gapCount += 1
        elif letterOne != letterTwo:
            mismatchCount += 1
    return gapCount, mismatchCount


def main() -> None:
    seqOne, seqTwo = readExamplePair()

    matchScore = 2
    mismatchScore = -1

    gapList = [-1, -3, -5]

    rows = []

    for gapPenalty in gapList:
        alignedOne, alignedTwo, score = smithWaterman(
            seqOne,
            seqTwo,
            matchScore,
            mismatchScore,
            gapPenalty,
        )
        gapCount, mismatchCount = countGapsAndMismatches(alignedOne, alignedTwo)
        rows.append(
            {
                "matchScore": matchScore,
                "mismatchScore": mismatchScore,
                "gapPenalty": gapPenalty,
                "totalScore": score,
                "gapCount": gapCount,
                "mismatchCount": mismatchCount,
            }
        )

    outPath = "results/gap-penalty-results.csv"
    with open(outPath, "w", encoding="utf-8", newline="") as handle:
        fieldNames = [
            "matchScore",
            "mismatchScore",
            "gapPenalty",
            "totalScore",
            "gapCount",
            "mismatchCount",
        ]
        writer = csv.DictWriter(handle, fieldnames=fieldNames)
        writer.writeheader()
        writer.writerows(rows)


main()
