import torch
from torchtext.datasets import Multi30k
from torchtext.data.utils import get_tokenizer
from torchtext.vocab import build_vocab_from_iterator
from torch.utils.data import DataLoader

# 1. 토크나이저 정의
tokenizer_en = get_tokenizer('spacy', language='en_core_web_sm')
tokenizer_de = get_tokenizer('spacy', language='de_core_news_sm')

# 2. vocab 빌드 (generator는 매번 새로 생성)
def yield_tokens(data_iter, tokenizer, index):
    for pair in data_iter:
        yield tokenizer(pair[index])

vocab_de = build_vocab_from_iterator(
    yield_tokens(Multi30k(split='train', language_pair=('de', 'en')), tokenizer_de, 0),
    specials=["<unk>", "<pad>", "<bos>", "<eos>"]
)
vocab_en = build_vocab_from_iterator(
    yield_tokens(Multi30k(split='train', language_pair=('de', 'en')), tokenizer_en, 1),
    specials=["<unk>", "<pad>", "<bos>", "<eos>"]
)
vocab_de.set_default_index(vocab_de["<unk>"])
vocab_en.set_default_index(vocab_en["<unk>"])

# 3. 데이터셋 준비 (generator를 리스트로 변환)
train_pairs = list(Multi30k(split='train', language_pair=('de', 'en')))
valid_pairs = list(Multi30k(split='valid', language_pair=('de', 'en')))
test_pairs  = list(Multi30k(split='test',  language_pair=('de', 'en')))

# 4. 데이터 전처리 함수
def process(pair):
    src, tgt = pair
    src_tensor = torch.tensor([vocab_de["<bos>"]] + [vocab_de[token] for token in tokenizer_de(src)] + [vocab_de["<eos>"]])
    tgt_tensor = torch.tensor([vocab_en["<bos>"]] + [vocab_en[token] for token in tokenizer_en(tgt)] + [vocab_en["<eos>"]])
    return src_tensor, tgt_tensor

train_data = [process(pair) for pair in train_pairs]
valid_data = [process(pair) for pair in valid_pairs]
test_data  = [process(pair) for pair in test_pairs]

# 5. DataLoader 정의 (batch_first=True 옵션 추가 가능)
def collate_fn(batch):
    src_batch, tgt_batch = [], []
    for src_sample, tgt_sample in batch:
        src_batch.append(src_sample)
        tgt_batch.append(tgt_sample)
    src_batch = torch.nn.utils.rnn.pad_sequence(src_batch, padding_value=vocab_de["<pad>"], batch_first=True)
    tgt_batch = torch.nn.utils.rnn.pad_sequence(tgt_batch, padding_value=vocab_en["<pad>"], batch_first=True)
    return src_batch, tgt_batch

train_loader = DataLoader(train_data, batch_size=32, shuffle=True, collate_fn=collate_fn)
valid_loader = DataLoader(valid_data, batch_size=32, shuffle=False, collate_fn=collate_fn)
test_loader  = DataLoader(test_data,  batch_size=32, shuffle=False, collate_fn=collate_fn)
