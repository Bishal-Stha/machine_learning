from transformers.pipelines import pipeline

gpt2_pipeline = pipeline(task="text-generation", model="openai-community/gpt2")
# output = gpt2_pipeline("The tallest mountain of the world is ")
# print(output)

results = gpt2_pipeline("What if AI",max_new_tokens=10, num_return_sequences=2)
# print(results)
for result in results:
    print(result["generated_text"])