from torch.utils.data import Dataset
import tqdm
import torch
import random


class BERTDataset(Dataset):
    # self.vocab은 Voab 객체 -> stoi, itos, unk_index, mask_index를 가짐.
    # stoi, itos는 단어 수만큼의 딕셔너리.
    # self.lines: 두 문장 문자 벡터. ex) [["The man went to the store", "He bought milk"], ["The sky is blue", "It looks beautiful today"]]
    # self.corpus_lindes: 라인 수 ex) 2
    def __init__(self, corpus_path, vocab, seq_len, encoding="utf-8", corpus_lines=None, on_memory=True):
        self.vocab = vocab
        self.seq_len = seq_len

        self.on_memory = on_memory
        self.corpus_lines = corpus_lines
        self.corpus_path = corpus_path
        self.encoding = encoding

        with open(corpus_path, "r", encoding=encoding) as f:
            if self.corpus_lines is None and not on_memory:
                for _ in tqdm.tqdm(f, desc="Loading Dataset", total=corpus_lines):
                    self.corpus_lines += 1

            if on_memory:
                self.lines = [line[:-1].split("\t")
                              for line in tqdm.tqdm(f, desc="Loading Dataset", total=corpus_lines)]
                self.corpus_lines = len(self.lines)

        if not on_memory:
            self.file = open(corpus_path, "r", encoding=encoding)
            self.random_file = open(corpus_path, "r", encoding=encoding)

            for _ in range(random.randint(self.corpus_lines if self.corpus_lines < 1000 else 1000)):
                self.random_file.__next__()

    def __len__(self):
        return self.corpus_lines
  
    def __getitem__(self, item):
        # item: line의 인덱스.
        t1, t2, is_next_label = self.random_sent(item)
        t1_random, t1_label = self.random_word(t1)
        t2_random, t2_label = self.random_word(t2)

        # [CLS] tag = SOS tag, [SEP] tag = EOS tag
        t1 = [self.vocab.sos_index] + t1_random + [self.vocab.eos_index] # [CLS] [Mask] like Hope [SEP] 이게 인덱스 형태로.
        t2 = t2_random + [self.vocab.eos_index] # I Don't Tennis NLP [SEP] (Tennis is masking word) 이게 인덱스 형태로.

        t1_label = [self.vocab.pad_index] + t1_label + [self.vocab.pad_index] 
        t2_label = t2_label + [self.vocab.pad_index]

        segment_label = ([1 for _ in range(len(t1))] + [2 for _ in range(len(t2))])[:self.seq_len]
        bert_input = (t1 + t2)[:self.seq_len]
        bert_label = (t1_label + t2_label)[:self.seq_len]

        padding = [self.vocab.pad_index for _ in range(self.seq_len - len(bert_input))]
        bert_input.extend(padding), bert_label.extend(padding), segment_label.extend(padding)
        
        # 이를 통해 bert_input은 MLM, SNP에 대한 전처리가 모두 완료되었고,
        # bert_label은 random_word에서 구하고 (MLM 레이블),
        # segment_label은 각 토큰이 어떤 문장에 속하는지에 대한 레이블 (Segment Embedding에 사용)
        # is_next는 두 문장이 원래 연결된 문장이 맞는지에 대한 레이블 (NSP 레이블)
        output = {"bert_input": bert_input,
                  "bert_label": bert_label,
                  "segment_label": segment_label,
                  "is_next": is_next_label}

        return {key: torch.tensor(value) for key, value in output.items()}

    def random_word(self, sentence):
        # tokens = ["I", "like", "NLP"]
        # after masking
        # tokens = [[Mask], "like", "Hope"]
        # output_label = [13, 0, 30] index: I -> 13, Hope -> 30
        tokens = sentence.split()
        output_label = []

        for i, token in enumerate(tokens):
            prob = random.random()
            if prob < 0.15:
                prob /= 0.15

                # 80% randomly change token to mask token
                if prob < 0.8:
                    tokens[i] = self.vocab.mask_index

                # 10% randomly change token to random token
                elif prob < 0.9:
                    tokens[i] = random.randrange(len(self.vocab))

                # 10% randomly change token to current token
                # vocab에서 token이 존재하면, stoi로 인덱스 저장. 없으면 unknown token으로 대체.
                else:
                    tokens[i] = self.vocab.stoi.get(token, self.vocab.unk_index)
                
                # label은 원래 token의 인덱스로 저장.
                output_label.append(self.vocab.stoi.get(token, self.vocab.unk_index))

            else:
                tokens[i] = self.vocab.stoi.get(token, self.vocab.unk_index)
                output_label.append(0)

        return tokens, output_label
  
    # NSP를 위해서, 문장의 50%는 원래 다음 문장(t2)로, 50%는 랜덤한 다른 문장으로 대체.
    def random_sent(self, index):
        # 해당 인덱스 라인의 문장 두 개를 t1, t2에 저장.
        # output: "I Like NLP", "I Don't Like NLP", 0 이런 식.
        t1, t2 = self.get_corpus_line(index)

        # output_text, label(isNotNext:0, isNext:1)
        if random.random() > 0.5:
            return t1, t2, 1
        else:
            return t1, self.get_random_line(), 0

    def get_corpus_line(self, item):
        if self.on_memory:
            return self.lines[item][0], self.lines[item][1]
        else:
            line = self.file.__next__()
            if line is None:
                self.file.close()
                self.file = open(self.corpus_path, "r", encoding=self.encoding)
                line = self.file.__next__()

            t1, t2 = line[:-1].split("\t")
            return t1, t2

    def get_random_line(self):
        if self.on_memory:
            return self.lines[random.randrange(len(self.lines))][1]

        line = self.file.__next__()
        if line is None:
            self.file.close()
            self.file = open(self.corpus_path, "r", encoding=self.encoding)
            for _ in range(random.randint(self.corpus_lines if self.corpus_lines < 1000 else 1000)):
                self.random_file.__next__()
            line = self.random_file.__next__()
        return line[:-1].split("\t")[1]
