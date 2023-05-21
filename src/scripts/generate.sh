
CUDA_VISIBLE_DEVICES=1 python generate.py
--load_8bit
--base_model 'minlik/indian-llama-7b-merged'
--lora_weights 'entity303/lawgpt-lora-7b'
--prompt_template 'indian_law_template'
--share_gradio
