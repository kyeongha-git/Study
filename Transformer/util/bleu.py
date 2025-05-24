import math
from collections import Counter
import numpy as np

def bleu_stats(hypothesis, reference):
    """Compute statistics for BLEU."""
    stats = []
    stats.append(len(hypothesis))
    stats.append(len(reference))
    for n in range(1, 5):
        s_ngrams = Counter([tuple(hypothesis[i:i + n]) for i in range(len(hypothesis) + 1 - n)])
        r_ngrams = Counter([tuple(reference[i:i + n]) for i in range(len(reference) + 1 - n)])

        match = sum((s_ngrams & r_ngrams).values())
        total = max(len(hypothesis) + 1 - n, 1)  # avoid division by 0
        stats.append(match)
        stats.append(total)
    return stats

def bleu(stats):
    """Compute BLEU given n-gram statistics."""
    if np.any(np.array(stats[2:]) == 0):
        return 0.0
    c, r = stats[:2]
    log_bleu_prec = sum(
        math.log(float(x) / y) for x, y in zip(stats[2::2], stats[3::2])
    ) / 4.0
    brevity_penalty = min(0, 1 - float(r) / c) if c > 0 else -1e9
    return math.exp(brevity_penalty + log_bleu_prec)

def get_bleu(hypotheses, reference):
    """Get BLEU score between single or multiple sentences"""
    # 단일 문장일 경우 감쌈
    if isinstance(hypotheses[0], str):
        hypotheses = [hypotheses]
    if isinstance(reference[0], str):
        reference = [reference]

    stats = np.zeros(10)
    for hyp, ref in zip(hypotheses, reference):
        stats += np.array(bleu_stats(hyp, ref))

    return 100 * bleu(stats)

def idx_to_word(x, vocab):
    words = []
    for i in x:
        word = vocab.lookup_token(i)
        if '<' not in word:  # <pad>, <eos> 등 제외
            words.append(word)
    return " ".join(words)
