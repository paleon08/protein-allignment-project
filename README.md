# 단백질 서열 정렬 알고리즘 구현 README  
(3.3, 4.1, 4.2, 4.3, 6.1 담당용)

---

## 0. 이 폴더에서 하는 일 & 보고서 연결

이 디렉터리에서 나오는 결과로 채울 보고서 파트:

- **3.3 정렬 알고리즘 구현**
- **4.1 알고리즘별 정렬 결과**
- **4.2 Gap penalty 변화에 따른 결과 비교**
- **4.3 BLAST 결과와의 비교**
- **6.1 정렬 알고리즘의 장점/한계**

이 README에 적힌 파일·코드만 만들고 실행하면,  
위 5개 섹션에 들어갈 **정렬 결과/표/비교자료**가 다 나온다고 생각하면 됨.

---

## 1. 폴더 구조

alignment/
├─ README.md                # 이 파일
├─ data/
│  ├─ example_pair.txt      # 예시 서열 1쌍
│  ├─ example_pair2.txt     # (선택) 두 번째 서열 쌍
│  └─ blast_alignment.txt   # BLAST 결과에서 복붙한 alignment 텍스트
├─ src/
│  ├─ alignment.py          # 정렬 알고리즘 함수 (Smith–Waterman 필수, NW 선택)
│  ├─ run_example.py        # 예시 서열 정렬(3.3, 4.1용)
│  ├─ run_gap_penalty.py    # gap penalty 실험(4.2용)
│  └─ run_blast_compare.py  # BLAST 결과와 비교(4.3용)
└─ results/
   ├─ example_alignment.txt         # 예시 정렬 결과
   ├─ gap_penalty_results.csv       # gap 설정별 결과 표
   └─ blast_comparison.txt          # BLAST vs 우리 정렬 비교 결과


---

## 2. 준비물

* Python 3.x (3.8 이상 권장)
* 별도 라이브러리 필요 없음 (표는 CSV, 결과는 텍스트로만 저장)

공통 실행 예:
cd alignment
python src/run_example.py

---

## 3. 데이터 파일 포맷 (`data/`)

### 3.1 `example_pair.txt` (필수)

예시 서열 1쌍을 **두 줄**로 저장:

HEAGAWGHEE
PAWHEAE

* 1줄: `seq1`
* 2줄: `seq2`
  FASTA 형식 아니고, 그냥 plain text 두 줄.

보고서에서 이 서열 쌍이
3.3, 4.1, 4.2, 4.3 전체에 공통으로 쓰여도 됨.

### 3.2 `example_pair2.txt` (선택)

추가로 한 쌍 더 필요하면 위와 같은 포맷으로 저장.
필수는 아님.

### 3.3 `blast_alignment.txt` (필수)

BLAST 웹 결과에서 **alignment 부분만** 복사해서 붙여넣기.

예시(실제 내용은 BLAST 결과 그대로):


Query  10  AAWGH-EE
            || |  |
Sbjct   5   AAWGHPEE


이 파일은 나중에 `run_blast_compare.py`에서
우리 정렬 결과와 같이 출력하는 용도.

---

## 4. 코드 파일 역할 (`src/`)

### 4.1 `alignment.py` – 정렬 알고리즘 함수 구현

> 정렬 알고리즘 함수만 모아두는 파일.

최소 이 함수 하나는 있어야 함:

```python
def smith_waterman(seq1: str, seq2: str,
                   match: int,
                   mismatch: int,
                   gap: int):
    """
    입력:
      seq1, seq2: 두 서열 문자열
      match, mismatch, gap: 점수 설정
    반환:
      score_matrix: 2차원 리스트 또는 None (필요시)
      aligned_seq1: gap('-') 포함 정렬 결과 문자열
      aligned_seq2: gap('-') 포함 정렬 결과 문자열
      max_score: 최종 점수 (int)
    """
    ...
```

(선택) 전역 정렬도 구현할 경우:

```python
def needleman_wunsch(seq1: str, seq2: str,
                     match: int,
                     mismatch: int,
                     gap: int):
    ...
```

* **필수:** `smith_waterman`
* **선택:** `needleman_wunsch` (시간 없으면 안 만들어도 됨)

이후 다른 스크립트들은 이 함수들을 import 해서 사용.

#### 보고서에서 쓸 것 (3.3)

* “우리가 구현한 정렬 함수 이름과 입력·출력 형식”
* “match/mismatch/gap 점수 설정 값”
* “Smith–Waterman를 사용했다는 점”
  (필요하면 NW는 이론 설명만)

---

### 4.2 `run_example.py` – 예시 정렬 실행 (3.3, 4.1용)

> 예시 서열 1쌍에 대해 정렬 돌리고, 결과를 파일로 저장.

해야 할 작업:

1. `data/example_pair.txt` 읽어서 `seq1`, `seq2` 가져오기
2. 기본 점수 설정으로 `smith_waterman` 호출

   * 예: `match=2, mismatch=-1, gap=-2`
3. (선택) `needleman_wunsch`도 호출
4. 정렬 결과를 콘솔과 `results/example_alignment.txt`에 저장

출력 예(파일 내용 예시):

```text
=== Smith-Waterman (Local) ===
seq1: H-EAGAWGHEE
seq2: HPE-AW-G-EE
score: 10

=== Needleman-Wunsch (Global, 선택) ===
seq1: HEAGAWGHEE
seq2: -HPEAWG-EE
score: 7
```

#### 보고서에서 쓸 것

* **3.3 정렬 알고리즘 구현**

  * “어떤 서열 쌍에 대해 SW를 적용했는지” (example_pair 내용)
  * “정렬 결과 예시(위와 같은 두 줄 alignment와 점수)”
* **4.1 알고리즘별 정렬 결과**

  * SW 정렬 결과 그림/텍스트
  * (NW 구현했다면) NW 결과와 간단 비교
    → “전역은 양 끝 gap, 국소는 motif 부분만 정렬” 같은 설명에 사용.

---

### 4.3 `run_gap_penalty.py` – gap penalty 실험 (4.2용)

> 같은 서열 쌍에 대해 gap penalty만 바꿔가며 정렬 실행.

해야 할 작업:

1. `data/example_pair.txt`에서 `seq1`, `seq2` 읽기
2. 여러 gap 값에 대해 반복 (예: -1, -3, -5)
3. 각 설정마다 `smith_waterman` 실행

   * 최종 점수(`max_score`)
   * alignment 안에서 gap 개수
   * alignment 안에서 mismatch 개수
     를 계산해서 리스트에 저장
4. 결과를 `results/gap_penalty_results.csv`로 저장

CSV 예시:

```csv
match,mismatch,gap,total_score,num_gaps,num_mismatches
2,-1,-1,10,8,1
2,-1,-3,6,4,4
2,-1,-5,2,2,7
```

콘솔 출력 예:

```text
gap=-1 -> score=10, gaps=8, mismatches=1
gap=-3 -> score=6, gaps=4, mismatches=4
gap=-5 -> score=2, gaps=2, mismatches=7
```

#### 보고서에서 쓸 것 (4.2)

* `gap_penalty_results.csv` 내용을 표로 옮기기

  * 각 설정별 gap 개수/score/mismatch 개수
* 관찰 문장:

  * gap penalty가 커질수록 gap 수가 줄고 mismatch가 늘어나는 식의 패턴 정리

---

### 4.4 `run_blast_compare.py` – BLAST와 비교 (4.3용)

> 우리 SW 정렬 결과 vs BLAST alignment 텍스트를 한 파일에 정리.

해야 할 작업:

1. `data/example_pair.txt`에서 `seq1`, `seq2` 읽기
2. `smith_waterman` 실행 (3.3에서 쓴 것과 같은 점수 설정 사용)
3. `data/blast_alignment.txt` 읽어서 문자열로 보관
4. `results/blast_comparison.txt`에 아래 형식으로 저장:

```text
=== Our Smith-Waterman Alignment ===
seq1: H-EAGAWGHEE
seq2: HPE-AW-G-EE
score: 10

=== BLAST Alignment (raw copy) ===
(여기에 blast_alignment.txt 내용 그대로)

=== Notes (간단 메모) ===
- 보존된 구간 위치/길이 비교
- gap 위치 차이 간단 메모
- BLAST가 양 끝 일부를 잘라낸 경우 등
```

자동 분석까지는 필요 없고,
**두 결과를 한 눈에 비교할 수 있게 정리**하는 게 목적.

#### 보고서에서 쓸 것 (4.3)

* `blast_comparison.txt`의 내용 기반으로:

  * SW와 BLAST alignment의 공통점/차이점 몇 가지 정리

    * 예: core motif는 거의 동일, 끝부분 처리/gap 배치 차이 등
  * “BLAST는 seed 기반 휴리스틱이라 완전한 DP와 약간 다를 수 있다”는 설명에 활용

---

## 5. 결과 폴더 (`results/`)와 보고서 섹션 연결

최종적으로 보고서에서 참고해야 하는 파일:

* **3.3 정렬 알고리즘 구현**

  * `results/example_alignment.txt`
  * * `src/alignment.py`의 함수 이름/입출력 설명 요약

* **4.1 알고리즘별 정렬 결과**

  * `results/example_alignment.txt`
    (SW 정렬 결과, NW도 구현했다면 둘 다)

* **4.2 Gap penalty 변화에 따른 결과 비교**

  * `results/gap_penalty_results.csv`

* **4.3 BLAST 결과와의 비교**

  * `results/blast_comparison.txt`

* **6.1 정렬 알고리즘의 장점/한계**

  * 위 세 결과 파일을 보면서:

    * DP 정렬의 특성 (최적 정렬, gap/mismatch 트레이드오프)
    * gap penalty 영향
    * SW와 BLAST 차이/계산량 관점 정리
      → **추가 코드 없이 해석만 하면 됨**

---

## 6. 실행 순서 요약 (팀원용)

1. `alignment.py`

   * `smith_waterman` 함수 구현 (필수)
   * (시간 남으면 `needleman_wunsch`도 구현)

2. `run_example.py` 실행

   * `data/example_pair.txt` 읽어서 예시 정렬 수행
   * `results/example_alignment.txt` 생성

3. `run_gap_penalty.py` 실행

   * gap penalty 여러 값으로 정렬
   * `results/gap_penalty_results.csv` 생성

4. BLAST 웹에서 검색 → alignment 부분 복사 → `data/blast_alignment.txt`에 저장

5. `run_blast_compare.py` 실행

   * `results/blast_comparison.txt` 생성

여기까지 하면,
3.3 / 4.1 / 4.2 / 4.3 / 6.1에 필요한 **정렬 결과 및 비교 데이터가 모두 준비된 상태**가 된다.

```
```
