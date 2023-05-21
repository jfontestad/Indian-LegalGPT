# LegalGPT

# 🏛️ Indian-LawGPT: A Large Language Model Based on Indian Legal Knowledge

Indian-LawGPT is a series of open-source large language models based on Indian legal knowledge.

These models expand on general Indian foundational models (such as Indian-LLaMA, ChatGLM, etc.) by adding a proprietary legal domain vocabulary and large-scale pre-training on Indian legal corpora, enhancing the base semantic understanding capabilities of large models in the legal field. On this basis, a legal dialogue question-and-answer dataset and an Indian judicial examination dataset are constructed for instruction fine-tuning, improving the model's understanding and execution capabilities for legal content.

Please refer to the technical report for more details.

This project is ongoing, and the legal domain datasets and series of models will be open-sourced in succession. Please stay tuned.

## 📅 Updates:
- 🌱 2023/05/15: Release of Awesome Indian Legal Resources and legal field vocabulary.
- 🌟 2023/05/13: Public release of Legal-Base-7B: a foundational legal model using 500,000 Indian judgment documents for secondary pre-training. Indian-LawGPT-7B-beta1.0: a legal dialogue model, constructed using 300,000 high-quality legal question and answer datasets based on Legal-Base-7B for instruction fine-tuning.
- 🌟 2023/04/12: Internal testing of Indian-LawGPT-7B-alpha: constructed directly on the Indian-LLaMA-7B using 300,000 legal question-and-answer datasets for instruction fine-tuning.

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

Indian-LawGPT
├── assets # Project static resources
├── data # Corpus and fine-tuning data
├── tools # Data cleaning tools
├── README.md
├── requirements.txt
└── src # Source code
├── finetune.py
├── generate.py
├── models # Base models and Lora weights
│ ├── base_models
│ └── lora_weights
├── outputs
├── scripts # Script files
│ ├── finetune.sh # Instructional fine-tuning
│ └── generate.sh # Service creation
├── templates
└── utils


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

Output examples:
- Question: Please give a judgment opinion.
- Question: Please introduce the definition of gambling crime.
- Question: How is overtime pay calculated?
- Question: What is the legal interest protected by the state for private lending?
- Question: Do you have to go to jail if you can't pay back the money you owe on a credit card?
- Question: Can you write a case description of the crime of robbery?

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

- Indian-LLaMA-Alpaca: https://github.com/ymcui/Indian-LLaMA-Alpaca
- LLaMA: https://github.com/facebookresearch/llama
- Alpaca: https://github.com/tatsu-lab/stanford_alpaca



