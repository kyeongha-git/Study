#!/usr/bin/env python
# coding: utf-8

from conf import *
from util.data_loader import train_loader, valid_loader, test_loader, vocab_de, vocab_en

# vocab���� pad, sos, eos �ε��� ����
src_pad_idx = vocab_de["<pad>"]
trg_pad_idx = vocab_en["<pad>"]
src_sos_idx = vocab_de["<bos>"]   # <sos> ��� <bos> ���
trg_sos_idx = vocab_en["<bos>"]
src_eos_idx = vocab_de["<eos>"]
trg_eos_idx = vocab_en["<eos>"]

enc_voc_size = len(vocab_de)
dec_voc_size = len(vocab_en)
