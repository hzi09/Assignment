from transformers import AutoTokenizer, AutoModelForCausalLM

# LLaMA 모델 load
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat-hf")

# 입력 메시지
input_text = "What is the capital of England?"
inputs = tokenizer(input_text, return_tensors="pt")

# 응답 생성
outputs = model.generate(**inputs, max_new_tokens=100)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("outputs : ", response)


# LLaMA에게 번역 요청
translation_prompt = (
    "You are a professional translator who translates English to Korean.\n\n"
    "Translate the following English text into fluent and natural Korean:\n\n"
    f"English: {response}\n\n"
    "Korean:"
)
translation_inputs = tokenizer(translation_prompt, return_tensors="pt")

# 번역 실행
translated_tokens = model.generate(**translation_inputs, max_new_tokens=100)
korean_translation = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)

print("한국어로 번역 :", korean_translation)