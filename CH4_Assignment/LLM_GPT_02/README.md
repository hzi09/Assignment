# CoT(Chain-of-Thought)
## 1. Chain-of-Thought (CoT)란?
- Chain-of-Thought (CoT) Prompting은 대형 언어 모델(LLM)의 논리적 추론(reasoning) 능력을 향상시키는 프롬프팅 기법
- 기존 프롬프팅 방식은 **입력에 대해 즉시 정답을 생성(direct answer prediction)**하는 방식이었으나,
CoT 프롬프팅은 단계별 사고 과정(step-by-step reasoning)을 모델이 명시적으로 출력하도록 유도하여 추론 성능을 크게 향상시킴
- CoT는 주로 **수학 문제 해결(mathematical reasoning), 논리적 추론(logical reasoning), 상식적 추론(common sense reasoning)**과 같은 복잡한 문제에서 성능이 향상됨을 실험적으로 입증

## 2. CoT 프롬프팅의 등장 배경
### 기존 LLM의 한계
- 대형 언어 모델(예: GPT-3, PaLM-540B)은 문맥 이해와 자연어 처리에서 강력한 성능을 보였지만,
수학 문제나 논리적 추론이 필요한 문제에서는 성능이 낮음
- 특히, **단순한 Zero-shot Prompting(예제 없이 정답을 바로 출력하는 방식)**으로는 논리적으로 복잡한 문제를 해결하기 어려움

### 기존 해결법 : Few-shot Prompting
- 기존에는 모델의 추론 능력을 향상시키기 위해 Few-shot Prompting(예제 몇 개를 제공하여 모델이 패턴을 학습하도록 유도하는 방식)이 사용됨
- 예를 들어, 모델에게 수학 문제와 그 풀이 과정을 포함한 몇 개의 예제를 제공한 후, 새로운 문제를 해결하도록 유도하는 방식
- 하지만 Few-shot 방식은 항상 효과적이지 않으며, 많은 예제가 필요할 수 있음

### 새로운 해결법: Chain-of-Thought (CoT) Prompting
- CoT는 Few-shot 방식 없이도 단순한 프롬프트 변형만으로 모델의 논리적 사고 능력을 향상시킬 수 있음을 발견
- 예를 들어, "Let's think step by step." 같은 문장을 프롬프트에 추가하는 것만으로도 모델이 복잡한 문제를 더 정확하게 풀 수 있음이 확인


## 3. CoT 프롬프팅의 방식
### 기본 Prompting vs. CoT Prompting 비교

![Image](https://github.com/user-attachments/assets/7d4573a9-7a36-4826-84a0-7ed38001a4d4)

#### (1) 기존 Zero-shot Prompting
- 기본 방식: 정답을 바로 예측

    ```
    Q: 철수가 사과 3개를 샀고, 2개를 영희에게 주었다. 철수에게 남은 사과는 몇 개인가?
    A: 1
    ```
#### (2) Zero-shot CoT Prompting
- CoT 방식: 중간 사고 과정을 포함하여 정답을 도출

    ```
    Q: 철수가 사과 3개를 샀고, 2개를 영희에게 주었다. 철수에게 남은 사과는 몇 개인가?
    Let's think step by step.
    철수는 처음에 3개의 사과를 가지고 있었다.
    영희에게 2개를 주었으므로, 3 - 2 = 1개가 남는다.
    따라서, 정답은 1개이다.
    ```

- CoT는 모델이 중간 사고 과정을 먼저 출력하도록 유도하여 문제 해결 능력을 향상시킴
- 프롬프트에 단순히 "Let's think step by step." 문장을 추가하는 것만으로 성능 향상 가능!

## 4. CoT 실험 결과
### 실험 환경
- 사용된 모델: GPT-3, PaLM-540B 등 대형 언어 모델
- 테스트 데이터셋
  - 수학 문제 해결: GSM8K, MultiArith
  - 논리적 추론: CommonsenseQA, StrategyQA
  - 기호적 추론: Last Letter Concatenation, Date Understanding
### 주요 결과
- GSM8K(수학 문제)에서의 정확도 비교

    |프롬프트 방식	                            |정확도(%)|
    |-------------------------------------------|:-------:|
    |기본 Zero-shot                             |17.7%    |
    |Zero-shot CoT(Let's think step by step)	|40.7%    |
    |Few-shot CoT                               |57.1%    |

    ![Image](https://github.com/user-attachments/assets/cdc92676-26c5-41ce-aeb7-0fe366dad9c8)

- CoT를 적용하면 기존 Zero-shot 방식 대비 성능이 최대 2~3배 향상됨
- 특히 대형 모델(100B+ 파라미터)에서 효과가 극대화됨

## 5. CoT의 핵심 발견
### 1. Zero-shot 환경에서도 논리적 추론 가능
- 기존에는 CoT가 Few-shot 환경에서만 효과적이라고 여겨졌음
- 하지만 이 연구들은 Zero-shot에서도 단순한 프롬프트 변형만으로 논리적 사고를 유도할 수 있음을 입증
### 2. 단순한 프롬프트 변경으로 성능 향상
- "Let's think step by step." 같은 간단한 문장을 추가하는 것만으로도 성능이 향상됨
- 이는 Prompt Engineering이 LLM의 성능을 극대화하는 핵심 요소임을 의미
### 3. 모델 크기가 클수록 효과가 극대화됨

![Image](https://github.com/user-attachments/assets/ca111315-e017-4204-9708-9e1a912bf0fc)

- 대형 모델(100B+ 파라미터)일수록 CoT의 효과가 더욱 강력
- 이는 LLM이 사전 학습 단계에서 이미 논리적 사고 능력을 일부 보유하고 있음을 시사


## 6. CoT의 한계 및 향후 연구 방향
### CoT의 한계
- 작은 모델에서는 효과가 미미
  - CoT는 **대형 모델(100B+ 파라미터)**에서 효과가 두드러지며, 작은 모델에서는 성능 향상이 크지 않음
- 일부 문제에서는 여전히 정답을 도출하지 못함
  - 특히 기호 조작(symbolic reasoning) 문제에서 CoT의 효과가 제한적
- 논리적 일관성이 부족할 수 있음
  - CoT가 적용된 모델도 때때로 논리적으로 맞지 않는 답변을 생성할 수 있음

### 향후 연구 방향
- Zero-shot CoT의 최적화 연구
  - "Let's think step by step."보다 더 효과적인 프롬프트 탐색
- CoT를 강화하는 학습 기법 개발
  - Fine-tuning을 통해 CoT를 자연스럽게 수행하는 모델 개발
- Self-Consistency CoT 및 Tree of Thoughts 연구
  - CoT의 한계를 극복하기 위한 추가적인 알고리즘적 접근


## 7. 결론 및 시사점
- CoT 프롬프팅이 LLM의 논리적 추론 능력을 크게 향상시킬 수 있음을 입증
- 단순한 프롬프트 변형만으로 Zero-shot에서도 성능을 높일 수 있음
- 대형 모델일수록 CoT 프롬프팅에 더 강하게 반응함
- Prompt Engineering이 LLM의 성능을 결정하는 중요한 요소임을 강조


## 참고한 논문
- "Large Language Models are Zero-Shot Reasoners" (Kojima et al., 2022), 
- "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" (Wei et al., 2022)

<br>

# RAG(Retrieval-Augmented Generation)
## 1. RAG(Retrieval-Augmented Generation)란?
- **Retrieval-Augmented Generation (RAG)**은 대형 언어 모델(LLM)이 외부 지식을 검색(retrieval)하여 더 정확하고 정보가 풍부한 응답을 생성(generation)할 수 있도록 하는 기법
- 이 접근법은 기본 LLM의 한계를 극복하기 위해 검색(search)과 생성(generation)을 결합하는 방식으로, 특히 사전 훈련(pre-training)된 모델의 정적인 지식 한계를 극복하는 데 유용
-  ✅핵심 아이디어:
   - 기존 LLM은 고정된 파라미터(parameter) 내에서만 답변을 생성
   - 하지만 RAG는 실시간으로 외부 데이터베이스, 검색 엔진, 문서 저장소에서 관련 정보를 검색하여, 보다 풍부한 정보에 기반한 응답을 생성할 수 있음
   - 이를 통해 최신 정보 반영, 근거 기반 답변 생성, 지식 확장이 가능해짐

## 2. RAG가 등장한 배경
### 기존 LLM의 한계
- 사전 학습된 지식만 사용 → 모델이 훈련된 이후 발생한 최신 정보를 반영하지 못함
- 사실적 오류(hallucination) 문제 → 모델이 없는 정보를 생성할 가능성이 높음
- 긴 컨텍스트 유지 한계 → LLM은 일반적으로 긴 문서를 읽고 분석하는 데 한계가 있음

### RAG의 필요성
- 최신 지식을 활용하고, 모델의 정적인 한계를 극복하기 위해 RAG가 도입됨
- LLM이 실시간으로 검색 가능한 시스템과 연결되면, 보다 정확하고 신뢰할 수 있는 응답을 생성할 수 있음


## 3. RAG의 구조
### RAG의 핵심 구성 요소
- RAG는 크게 두 가지 주요 단계로 구성됨

#### (1) Retrieval (검색 단계)
- 쿼리(query): 사용자의 입력(질문)을 기반으로 관련 정보를 검색
- 외부 지식 소스: 검색 대상은 웹 문서, 논문 데이터베이스, 위키피디아, 회사 내부 데이터 등 다양할 수 있음
- 검색 엔진(Retriever) 활용
  - BM25 (고전적인 정보 검색 알고리즘)
  - DPR (Dense Passage Retrieval)
  - ColBERT (효율적인 딥러닝 기반 검색 모델)

#### (2) Generation (생성 단계)
- 검색된 문서를 기반으로 LLM이 답변을 생성
- 단순한 원문 복사(copy)가 아닌, 문맥을 반영하여 새로운 응답을 생성하는 방식

#### 예시
- 사용자: "2024년 대선 결과는?"
- RAG 검색 단계: 뉴스 아카이브에서 최신 대선 결과를 검색
- RAG 생성 단계: 검색된 문서를 요약하여 응답 생성
- 출력: "2024년 대선에서 후보 X가 승리했다는 보도가 있습니다."

## 4. RAG의 최신 연구 및 발전

### RAG의 최신 연구 방향
- Self-Adaptive Retrieval
  - 단순히 검색된 문서를 이용하는 것이 아니라, 문맥에 따라 검색 전략을 동적으로 조정
  - 예: 간단한 질문에는 빠른 검색, 복잡한 질문에는 심층 검색 적용

- Multi-hop Retrieval:
  - 하나의 검색 결과를 바탕으로 추가적인 검색을 수행하는 방식
  - 예: "양자 컴퓨팅의 현재 연구 동향은?" → 최신 논문 검색 → 논문 인용 논문 추가 검색

- Augmented Memory in RAG:
  - 검색된 정보가 캐시(cache)처럼 저장되어 재사용될 수 있는 구조
  - LLM이 동일한 질문에 대해 일관된 응답을 생성하도록 도움

### RAG의 주요 적용 사례
- 오픈 도메인 질문 응답 (Open-domain QA)
  - 예: 구글 검색 기반 AI 비서, ChatGPT with Bing
  - 최신 뉴스나 트렌드 정보를 검색하여 반영할 수 있음
- 기업 내부 문서 검색 및 요약
  - 예: 회사의 내부 보고서를 검색하고 요약하는 AI 시스템
- 과학 연구 및 논문 분석
  - 최신 연구 논문을 검색하여 연구 동향 분석을 자동화
- 의료 및 법률 컨설팅
  - 의학 논문, 법률 조항 검색 후 전문가 수준의 답변 생성 가능

## 5. RAG의 한계 및 해결 방안
### RAG의 주요 한계
- 검색된 문서의 품질 문제
  - 잘못된 정보(inaccurate information)가 포함될 가능성이 있음
  - 최신 뉴스, 소셜 미디어, 신뢰할 수 없는 데이터 출처 문제
- 빠른 검색과 정확성의 균형 문제
  - 빠른 검색(Fast Retrieval)과 깊이 있는 검색(Deep Retrieval) 간의 균형을 맞추는 것이 어려움
- 추론 오류 (Inference Error)
  - 검색된 정보를 적절히 활용하지 못하면, 오히려 비효율적인 답변을 생성할 가능성이 있음.

### 해결 방안
- Self-Consistency RAG
  - 여러 번 검색 및 응답 생성 후 가장 일관성 있는 답변을 선택
- Fact-Verification RAG
  - 검색된 정보의 신뢰도를 평가하고, 팩트체크(fact-checking) 알고리즘을 적용
- Adaptive Retrieval Strategies
  - 질문 유형에 따라 적절한 검색 방법을 동적으로 선택


## 6. 결론 및 시사점
- RAG는 검색과 생성의 조합을 통해, LLM의 한계를 극복할 수 있는 강력한 방법론
- 최신 연구는 "Self-Adaptive Retrieval" 및 "Multi-hop Retrieval"을 활용하여 RAG의 효율성을 개선하고 있음
- 검색된 정보의 신뢰성 문제를 해결하기 위해 "Fact-Verification RAG"와 같은 기법이 연구되고 있음
- RAG는 AI 기반 검색, 질문 응답 시스템, 법률·의료 도메인 등 다양한 분야에서 활용될 가능성이 큼

## 참고한 논문
- "Retrieval-Augmented Generation for Large Language Models: A Survey" (2023)
- "Retrieval-Augmented Generation for AI-Generated Content: A Survey" (2024)

<br>


# 직접해보기
- Python 코딩을 도와주는 서포터 만들기
- 질문 : n번째 피보나치 수 구하는 코드를 작성해줘

## 일반 프롬프트
```python
system_prompt = """
너는 Python 코딩을 도와주는 서포터야.  
사용자가 코드를 작성하면, 코드의 오류를 찾아주고, 최적화 방법을 제안해줘
또한, 사용자가 원하는 기능을 구현할 수 있도록 단계별 가이드를 제공해줘.
초보자가 이해할 수있도록 이해하기 쉬운 방식으로 설명해야 해.  
"""
```

- GPT 답변
```질문하기 : n번째 피보나치 수 구하는 코드를 작성해줘
GPT : 피보나치 수열은 앞의 두 숫자를 더해서 다음 숫자를 만들어나가는 수열이야.  
예를 들어, 1, 1, 2, 3, 5, 8, 13, ... 과 같은 형태로 숫자들이 계속해서 증가해.  
  
그럼, 사용자가 입력한 n번째 피보나치 수를 구하는 코드를 작성해볼게.  


def fibonacci(n):
    if n <= 0:
        return "n은 1 이상의 자연수여야 합니다."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

n = int(input("몇 번째 피보나치 수를 구하시겠습니까? "))
result = fibonacci(n)
print(f"{n}번째 피보나치 수는 {result}입니다.")


위 코드를 실행하면, 사용자가 입력한 숫자에 해당하는 피보나치 수를 계산해서 결과를 보여줄게.     
출력된 결과는 n번째 피보나치 수를 의미해.
완성된 코드를 실행해보고, 어떤 결과가 나오는지 확인해봐.
```

## CoT 프롬프트
```python
system_prompt = """
너는 Python 프로그래밍을 도와주는 "Python 코딩 서포터"야.  
너의 주요 역할은 아래와 같아.

1. 단계별 가이드 제공  
- 사용자가 특정 코드를작성하려고 하면, 1단계, 2단계, 3단계 형식으로 상세한 방법을 알려줘
- 간단한 예제 코드와 함께 설명하면 더 좋아.  

2. 문제 해결 및 알고리즘 설명  
- Python에서 자주 사용되는 알고리즘(정렬, 검색, 재귀 등)을 설명하고 예제 코드를 제공해줘 
- 특정 문제를 해결하는 여러 가지(2개 이상) 접근 방식을 소개하고 어떤 코드가 왜 좋은지에 대해 비교 분석해줘

3. 필수!!
- 설명은 이해하기 쉽게, 초보자도 이해할 수 있도록 해줘
- 질문을 받으면, 코드와 함께 상세한 설명을 제공해줘 
- 가능하면 성능 비교나 코드 스타일 차이를 분석해서 알려줘
"""
```
- GPT 답변

    ```
    GPT : 물론이죠! 피보나치 수열은 첫 번째 항과 두 번째 항이 1이고, 세 번째 항부터는 바로 직전의 두 항을 더한 값이 되는 수열을 말합니다.
    예를 들어, 1, 1, 2, 3, 5, 8, 13, 21, ... 과 같은 형태입니다.

    n번째 피보나치 수를 구하는 방법은 여러 가지가 있지만, 이 중에서 가장 간단한 방법은 재귀 함수를  사용하는 것입니다.
    아래는 재귀 함수를 사용하여 n번째 피보나치 수를 구하는 Python 코드 예시입니다.


    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    n = 10  # 여기에 구하고 싶은 피보나치 수열의 인덱스를 입력하세요
    result = fibonacci(n)
    print(f"{n}번째 피보나치 수는 {result}입니다.")


    위 코드를 실행하면, n에 입력한 값에 해당하는 피보나치 수가 출력됩니다.
    하지만 이 코드는 피보나치 수를 구하는 과정에서 중복된 계산이 많이 발생해 성능 상 불이익이 있을  수 있습니다.
    이를 개선하기 위해 반복문이나 동적 계획법 등의 방법을 사용할 수도 있습니다.
    ```

## 비교
- 일반 프롬프트는 그냥 반복문을 사용한 것에 비해 CoT 프롬프트는 재귀함수를 사용하여 문제를 풀이해줌
- 일반 프롬프트는 코드만 작성해주었지만, CoT 프롬프트경우에는 문제가 발생할 수 있다는 것에 대해 설명하고, 다른 문제 해결방안에 대한 내용을 언급