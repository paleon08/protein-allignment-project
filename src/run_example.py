"""
파일 이름
  run-example.py

역할
  alignment 모듈에 정의한 정렬 함수를
  예시 단백질 서열 한 쌍에 적용해 보고,
  그 결과를 화면과 파일로 확인하는 실행용 스크립트이다.

이 파일에서 할 일

  하나, 예시 서열 읽기
    data 폴더의 example-pair.txt 파일에서
    첫 번째 줄과 두 번째 줄에 있는 단백질 서열을 읽어 온다.
    이 두 서열을 정렬 알고리즘의 입력으로 사용한다.

  둘, 정렬 알고리즘 실행
    alignment 모듈의 smithWaterman 함수를
    기본 점수 규칙
      예 matchScore 는 2, mismatchScore 는 마이너스 1, gapPenalty 는 마이너스 2
    로 한 번 호출해 정렬 결과를 얻는다.
    전역 정렬까지 구현했다면 needlemanWunsch 함수도 같은 서열에 대해 실행해 볼 수 있다.

  셋, 결과 출력과 저장
    얻은 정렬 결과 두 줄과 정렬 점수를
    화면에 보기 좋게 출력한다.
    같은 내용을 results 폴더의 example-alignment.txt 파일에도 기록해 둔다.
    이 파일은 나중에 보고서에 넣을 예시 그림과 표를 만들 때 참고 자료로 사용한다.

보고서와의 연결

  이 스크립트에서 얻은 정렬 예시는
  보고서의 정렬 알고리즘 구현 부분과
  알고리즘별 정렬 결과 부분에서
  실제로 어떻게 정렬이 되는지 보여 줄 때 사용한다.
"""

from alignment import smithWaterman, needlemanWunsch


def readExamplePair() -> tuple[str, str]:
    """
    data 폴더의 example-pair.txt 파일에서
    단백질 서열 두 줄을 읽어 온다.
    """
    path = "data/example-pair.txt"
    with open(path, "r", encoding="utf-8") as handle:
        lines = [line.strip() for line in handle.readlines() if line.strip()]
    if len(lines) < 2:
        raise ValueError("example-pair.txt 파일에는 두 줄의 서열이 필요합니다.")
    return lines[0], lines[1]


def main() -> None:
    seqOne, seqTwo = readExamplePair()

    matchScore = 2
    mismatchScore = -1
    gapPenalty = -2

    print("기본 점수 규칙으로 smithWaterman 정렬을 실행합니다.")
    alignedOne, alignedTwo, score = smithWaterman(
        seqOne,
        seqTwo,
        matchScore,
        mismatchScore,
        gapPenalty,
    )

    print()
    print("정렬 결과 예시")
    print("첫 번째 정렬 서열 ", alignedOne)
    print("두 번째 정렬 서열 ", alignedTwo)
    print("정렬 점수 ", score)

    outPath = "results/example-alignment.txt"
    with open(outPath, "w", encoding="utf-8") as handle:
        handle.write("SmithWaterman 예시 정렬 결과\n")
        handle.write("첫 번째 정렬 서열 " + alignedOne + "\n")
        handle.write("두 번째 정렬 서열 " + alignedTwo + "\n")
        handle.write("정렬 점수 " + str(score) + "\n")


main()
