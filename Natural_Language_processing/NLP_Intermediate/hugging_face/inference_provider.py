from huggingface_hub import InferenceClient

client = InferenceClient(
    provider="together",
    api_key="4b7858ebc13fae18ce93db132b4a3f5fb012c69eb68f20d7ad32150a440cf378"
)

completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3",
    messages=[{"role": "user", "content": "What is the capital of Nepal?"}]
)

print(completion.choices[0].message)
