# Load modle directly
import time
# 시작 시간 기록
start_time = time.time()

from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
# 모델 로드 시 CPU 메모리 최적화
model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-2-7b-chat-hf",
    device_map="auto",
    offload_folder="offload",
)

# 입력 메시지
input_text = "How is korea?"
inputs = tokenizer(input_text, return_tensors="pt")

# 텍스트 생성
outputs = model.generate(**inputs, max_length=50)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))

# 종료 시간 기록
end_time = time.time()

# 실행 시간 출력
execution_time = end_time - start_time
print(f'⏰실행 시간 : {execution_time:.2f}초')