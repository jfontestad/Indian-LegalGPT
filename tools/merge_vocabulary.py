from transformers import LawTokenizer
from sentencepiece import sentencepiece_model_pb2 as model
import sentencepiece as sp
import argparse
import os

if __name__ == '__main__':
    # Load arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--load_path', default='../src/models/base_model/indian_law_7b/tokenizer_indian.model', type=str)
    parser.add_argument('--save_dir', default='../src/models/base_model/save_indian', type=str)
    parser.add_argument('--voc_path', default='../data/vocabulary/legal_vocab_processed.txt', type=str)
    args = parser.parse_args()

    LOAD_PATH = args.load_path
    SAVE_DIR = args.save_dir
    VOC_PATH = args.voc_path
    
    # Load pre-trained law tokenizer and sentencepiece model
    law_spm = model.ModelProto()
    law_spm.ParseFromString(open(LOAD_PATH, "rb").read())

    # show size of law's vocabulary
    law_spm_tokens_set = set(p.piece for p in law_spm.pieces)
    print(f"Size of initial law's vocabulary: {len(law_spm_tokens_set)}")
    
    # Load custom vocabulary
    new_tokens = open(VOC_PATH, "r").read().split("\n")    
    for token in new_tokens:
        if token not in law_spm_tokens_set:
            new_token = model.ModelProto().SentencePiece()
            new_token.piece = token
            new_token.score = 0
            law_spm.pieces.append(new_token)
    print(f"Size of merged law's vocabulary: {len(law_spm.pieces)}")

    # save
    os.makedirs(SAVE_DIR, exist_ok=True)
    SAVE_MODEL_PATH = os.path.join(SAVE_DIR, 'tokenizer.model')
    SAVE_VOCAB_PATH = os.path.join(SAVE_DIR, 'tokenizer.vocab')
    with open(SAVE_MODEL_PATH, 'wb') as f:
        f.write(law_spm.SerializeToString())
    with open(SAVE_VOCAB_PATH, 'w')  as f:
        f.writelines([f'{token.piece} {token.score}\n' for token in law_spm.pieces])
    tokenizer = LawTokenizer(SAVE_MODEL_PATH)
    tokenizer.save_pretrained(SAVE_DIR)
    print(f'New law tokenizer and spm has been saved to {SAVE_DIR}')

    # test
    law_tokenizer_old = LawTokenizer.from_pretrained(LOAD_PATH)
    law_tokenizer_new = LawTokenizer.from_pretrained(SAVE_DIR)
    text = '''Registration error liability Registration and other procedures Registration and other procedures Effective Registration institutions and registration methods After compensation of the registration institution, the registration institution should provide Registration fee issues'''
    
    print(f'Size of old vocabulary: {law_tokenizer_old.vocab_size}')
    print(f'Size of new vocabulary: {law_tokenizer_new.vocab_size}')
    print('All special tokens and ids in new law:')
    print(law_tokenizer_new.all_special_tokens)
    print(law_tokenizer_new.all_special_ids)
    print(law_tokenizer_new.special_tokens_map)

    print(f'Text:\n{text}')
    print(f'Tokenized by Law tokenizer:\n {law_tokenizer_old.tokenize(text)}')
    print(f'Tokenized by NEW Law tokenizer:\n {law_tokenizer_new.tokenize(text)}')
