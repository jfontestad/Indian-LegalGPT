## 🏛️ Indian-LawGPT: A Large Language Model Based on Indian Legal Knowledge
---

# Indian-LawGPT: Revolutionizing Indian Legal Domain with AI

Indian-LawGPT is a breakthrough in the intersection of artificial intelligence and law. It's an innovative series of open-source large language models (LLMs) finely-tuned to the nuances of Indian legal knowledge. Developed by Permissioned AI, this initiative aims to revolutionize the accessibility and understanding of Indian legal processes and legislation.

These models form an expansion of general Indian foundational models such as Indian-LLaMA, ChatGLM, among others. However, they are distinct due to their infusion of a proprietary legal domain vocabulary and their large-scale pre-training on an extensive Indian legal corpus. This novel approach amplifies the semantic understanding capabilities of large models, especially within the legal domain, thereby providing an in-depth understanding of complex legal terminologies, precedents, and cases.

The development process of the Indian-LawGPT includes the construction of a legal dialogue question-and-answer dataset and an Indian judicial examination dataset for instruction fine-tuning. This procedure refines the model's understanding of legal content and its execution capabilities, making it an invaluable tool in the realm of legal discourse and research.

## Applications of Indian-LawGPT

### Legal Research

Indian-LawGPT can be instrumental in legal research by helping researchers parse through extensive legal documents, understand intricate legal terms, and even predict potential outcomes based on legal precedents.

### Legal Education

This tool can be of immense help in legal education. It can aid in creating interactive educational content, answering legal queries, and even preparing students for judicial examinations.

### Legal Consultation

Indian-LawGPT can provide initial legal consultation by providing answers to legal queries based on Indian law, thereby enhancing access to legal services.

### Legal Document Review

Indian-LawGPT can review and understand legal documents, helping to identify key issues, analyze contracts, and even draft preliminary legal documents.

Please refer to the technical report for more details.

This project is ongoing, and the legal domain datasets and series of models will be open-sourced in succession. Please stay tuned.

## 📚 Project Timeline & Milestones:
- 📘  Announcement of the public release of Legal-Base-7B - a robust foundational legal model which has been trained using an impressive 500,000 Indian judgment documents for secondary pre-training. 
- 📝 : Completion of the internal testing phase for Indian-LawGPT-7B-alpha - a model constructed directly on the Indian-LLaMA-7B using 300,000 legal question-and-answer datasets for instruction fine-tuning. This signifies our commitment to continuous improvement and quality assurance, ensuring the best possible user experience. 🛠️

Stay tuned for more exciting updates as we continue to make strides in enhancing Indian-LawGPT! 📈👩‍💻👨‍💻

## ⚡ Quick Start:

Prepare code and create the environment:

git clone git@github.com:permissionedAI/Indian-LawGPT.git
cd Indian-LawGPT
conda activate indianlawgpt
pip install -r requirements.txt


### Merge model weights (optional):

If you want to use the Indian-LawGPT-7B-alpha model, you can skip this step and directly proceed to step 3.

If you want to use the Indian-LawGPT-7B-beta1.0 model:

As LLaMA and Indian-LLaMA have not open-sourced the model weights, this project can only release LoRA weights under the relevant open-source license and cannot release the complete model weights. Your understanding is appreciated.

This project provides a method to merge the weights. Please obtain the original weights and reconstruct the model yourself.

### Launch the example:

Start local service:

conda activate indianlawgpt
cd Indian-LawGPT
sh src/scripts/generate.sh

Connect to the service:

## 🏗️ Project Structure:

- Indian-LawGPT
  - assets # Project static resources
  - data # Corpus and fine-tuning data
  - tools # Data cleaning tools
  - README.md
  - requirements.txt
  - src # Source code
    - finetune.py
    - generate.py
    - models # Base models and Lora weights
      - base_models
      - lora_weights
    - outputs
    - scripts # Script files
      - finetune.sh # Instructional fine-tuning
      - generate.sh # Service creation
    - templates
    - utils

## 📚 Data Construction:

This project is based on publicly available legal document data from the Indian Judgments Online, judicial examination data, and other datasets. For details, please refer to Awesome Indian Legal Resources.

- Preliminary data generation: Dialogue question-and-answer data generated according to the Stanford_alpaca and self-instruct methods.
- Knowledge-guided data generation: Data generated based on structured Indian legal knowledge through the Knowledge-based Self-Instruct method.

## 🏋️ Model Training:

### Training Process:

The training process for the Indian-LawGPT series of models is divided into two stages:

1. Expand the legal field vocabulary and pre-train Indian-LLaMA on a large scale with legal documents and codes.
2. Construct a legal field dialogue question-and-answer dataset and fine-tune instructions on the basis of the pre-trained model.

### Secondary Training Process:

- Refer to src/data/example_instruction_train.json to construct a secondary training dataset.
- Run src/scripts/train_lora.sh.

### Instruction Fine-tuning Steps:

- Refer to src/data/example_instruction_tune.json to construct an instructional fine-tuning dataset.
- Run src/scripts/finetune.sh.

### Computational Resources:

8 Tesla V100-SXM2-32GB: The secondary training stage takes about 24h / epoch, and the fine-tuning stage takes about 12h / epoch.

## 📝 Model Evaluation:

- 1. Question: Please provide a judgment opinion on the case of [Case Name].

- 2. Question: Can you introduce the legal definition and elements of the crime of gambling in India?

- 3. Question: How is overtime pay calculated under Indian labor laws? Are there any specific regulations governing overtime wages?

- 4. Question: What is the legal interest rate protected by the state for private lending in India? Are there any limitations or guidelines regarding interest rates on private loans?

- 5. Question: In the context of credit card debt in India, if someone is unable to repay their outstanding balance, are they required to go to jail? What are the potential consequences or legal actions associated with unpaid credit card debt?

- 6. Question: Could you please provide a detailed case description of the crime of robbery under Indian law? Include relevant elements, penalties, and any key legal considerations.

Feel free to customize or modify these questions to suit your needs.

## ❗ Limitations:

Due to factors such as computational resources and data scale, Indian-LawGPT has many limitations at the current stage:

- Limited data resources and relatively small model capacity result in relatively weak model memory and language capabilities. Therefore, it may generate incorrect results when facing factual knowledge tasks.
- The model series has only undergone preliminary human intent alignment. Therefore, it may produce unpredictable harmful content and content that does not conform to human preferences and values.
- There are problems with self-awareness, and Indian understanding needs to be enhanced.

Please understand the above problems before using to avoid misunderstandings and unnecessary trouble.

## 👥 Collaborators:

The following people collaborated on this project (in alphabetical order): @permissionedAI, @govtAI, @lawAI.

## ❗ Disclaimer:

Please strictly adhere to the following:

- Any resources in this project are for academic research use only and commercial use is strictly prohibited.
- The model's output is influenced by various uncertain factors, and the project currently cannot guarantee its accuracy. It is strictly prohibited for use in real legal scenarios.
- The project does not bear any legal responsibility, nor does it take responsibility for any loss that may be caused by the use of related resources and output results.

## 💌 Feedback:

If you have any issues, please submit them in GitHub Issue.

Before submitting an issue, it is recommended to check the FAQ and past issues to see if they can solve your problem.
Please discuss politely and build a harmonious community.
As the collaborators advance the project in their spare time from research, due to limited manpower, it's difficult to provide real-time feedback. Your understanding is appreciated!

## 🙏 Acknowledgments:

This project is based on the following open-source projects, and we would like to express our sincere gratitude to the relevant projects and developers:

- Hugging Face
- LLaMA: https://github.com/facebookresearch/llama
- Alpaca: https://github.com/tatsu-lab/stanford_alpaca



