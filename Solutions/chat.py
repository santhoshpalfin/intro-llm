from ctransformers import AutoModelForCausalLM

llm = AutoModelForCausalLM.from_pretrained("santhoshpalfin/orca_mini_3B-GGUF", model_file="orca-mini-3b.q4_0.gguf")

prompt = " Hello! What is your dogs"

print(llm(prompt))
