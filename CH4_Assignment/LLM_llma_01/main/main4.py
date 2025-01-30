from transformers import AutoTokenizer, AutoModelForCausalLM

# LLaMA 모델 load
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat-hf")

# 입력 메시지
input_text = """
    I want to develop an AI-powered web service and focus on three key areas: model development, web integration, and cloud deployment.
    Model Development: I want to train AI models and make them practical for real-world applications.
    Web Integration: I plan to integrate AI models into a web application using Django.
    Cloud Deployment: I aim to efficiently deploy my web service using platforms like AWS, Google Cloud, or Azure.
    Could you recommend learning resources that cover these topics?
    """
inputs = tokenizer(input_text, return_tensors="pt")

# 응답 생성
outputs = model.generate(**inputs, max_length=500)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("outputs : ", response)