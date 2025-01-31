import re
import sqlite3
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd
from collections import Counter
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForSeq2SeqLM

font_path = "C:/Windows/Fonts/malgun.ttf"

font_prop = fm.FontProperties(fname=font_path)
plt.rc("font", family=font_prop.get_name())


db = sqlite3.connect("C:/Users/hzi28/hyunji/github/Assignment/CH4_Assignment/LLM_llma_01/chatbot.db")

# 객체 생성
cursor = db.cursor()

"""
CREATE TABLE : 새로운 테이블을 생성할 때 사용(conversations 이라는 테이블의 이름을 생성)
IF NOT EXISTS : 동일한 테이블이 존재하면 새로 만들지 않음
id : 컬럼이 기본 키(Primary Key) 역할을 함
INTEGER PRIMARY KEY: 고유한 값을 가지는 정수형 기본 키
AUTOINCREMENT: 새로운 행이 추가될 때 자동으로 1씩 증가하는 고유 값

INTEGER NOT NULL: 정수값이며, 반드시 값이 있어야 함 (NULL 허용 X)
TEXT NOT NULL: 문자열 데이터를 저장하며, 반드시 값이 있어야 함 (NULL 허용 X)
CHECK(speaker IN ('user', 'computer'))
- speaker 값이 'user' 또는 'computer'만 허용됨
- 다른 값 ('bot', 'admin', 'guest') 등은 입력 불가능

created_at TIMESTAMP: 날짜 및 시간  자동 저장
DEFAULT CURRENT_TIMESTAMP
- 새 데이터가 삽입될 때 현재 시간을 자동으로 저장
- 사용자가 시간을 따로 입력하지 않아도 자동 입력됨
"""

cursor.execute("""
    CREATE TABLE IF NOT EXISTS conversations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    conversation_id INTEGER NOT NULL,
    speaker TEXT NOT NULL CHECK(speaker IN ('user', 'computer')),
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS word_counts (
    word TEXT PRIMARY KEY,
    count INTEGER DEFAULT 1
)
""")

db.commit

# LLaMA 모델 load
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat-hf")

# 번역 모델 로드 (M2M100)
translator_tokenizer = AutoTokenizer.from_pretrained("facebook/m2m100_418M")
translator_model = AutoModelForSeq2SeqLM.from_pretrained("facebook/m2m100_418M")

# 대화 ID
conversation_id = 1 

# 입력 메시지
input_text = """
    You are a kind Korean guide. I want to go on a trip to Korea. Where should I go?
    """

# 대화 데이터 DB 저장(사용자)
cursor.execute("INSERT INTO conversations (conversation_id, speaker, message) VALUES (?, ?, ?)", (conversation_id, 'user', input_text))
db.commit()

inputs = tokenizer(input_text, return_tensors="pt")

# 응답 생성
outputs = model.generate(**inputs, max_length=500)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("outputs : ", response)

# 대화 데이터 DB 저장(컴퓨터)
cursor.execute("INSERT INTO conversations (conversation_id, speaker, message) VALUES (?, ?, ?)", (conversation_id, 'computer', response))
db.commit()


# 번역을 위한 입력 준비
translator_inputs = translator_tokenizer(response, return_tensors="pt")
translator_inputs["forced_bos_token_id"] = translator_tokenizer.get_lang_id("ko")  # 한국어 번역

# 번역 실행
translated_tokens = translator_model.generate(**translator_inputs)
korean_translation = translator_tokenizer.decode(translated_tokens[0], skip_special_tokens=True)

cursor.execute("INSERT INTO conversations (conversation_id, speaker, message) VALUES (?, ?, ?)", (conversation_id, 'computer', korean_translation))
db.commit()

# 단어 추출 및 카운팅
def extract_korean_words(text):
    return re.findall(r"[가-힣]+", text)

words = extract_korean_words(korean_translation)
word_counts = Counter(words)

# 단어 데이터 삽입 및 업데이트
for word, count in word_counts.items():
    cursor.execute("INSERT INTO word_counts (word, count) VALUES (?, ?) ON CONFLICT(word) DO UPDATE SET count = count + ?",(word, count, count))

db.commit()

# 상위 10개 단어 조회
cursor.execute("SELECT word, count FROM word_counts ORDER BY count DESC LIMIT 10;")
top_words = cursor.fetchall()

# 데이터프레임 변환
df = pd.DataFrame(top_words, columns=["Word", "Count"])

# 그래프 생성
plt.figure(figsize=(10, 5))
plt.bar(df["Word"], df["Count"], color="skyblue")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Top 10 Most Frequent Words")
plt.xticks(rotation=45)
plt.show()

# SQLite 연결 닫기
cursor.close()
db.close()

print("번역된 한국어 응답:", korean_translation)