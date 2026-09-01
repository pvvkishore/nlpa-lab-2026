"""
Post-install setup for NLPA Lab 2026.

Downloads all data files that pip cannot install directly:
  - NLTK tokenizer data (punkt_tab)
  - spaCy English model (en_core_web_sm)
  - Stanza English models
  - HuggingFace tokenizer files for BERT, GPT-2, T5, Qwen
  - Pretrained embedding models for Lab 05
    (Word2Vec Google News 300d, GloVe 6B 100d, Sentence-BERT MiniLM)

Run once after `conda env create -f environment.yml`:
    conda activate nlpa_2026
    python setup_data.py

Total download: ~2.3 GB. Word2Vec alone is 1.5 GB.
Expect 20-40 minutes on a typical connection.
"""

import sys
import subprocess


def announce(step, msg):
    print(f"\n[{step}] {msg}\n" + "-" * 60)


def run(cmd):
    """Run a shell command and stream its output."""
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"  WARNING: command failed: {cmd}")
        return False
    return True


# 1. NLTK
announce("1/5", "Downloading NLTK tokenizer data...")
import nltk
nltk.download('punkt_tab', quiet=False)


# 2. spaCy English model
announce("2/5", "Downloading spaCy English model...")
run(f'"{sys.executable}" -m spacy download en_core_web_sm')


# 3. Stanza English models
announce("3/5", "Downloading Stanza English models (~500 MB, patient please)...")
import stanza
stanza.download('en')


# 4. HuggingFace tokenizer files
announce("4/5", "Caching HuggingFace tokenizers (BERT, GPT-2, T5, Qwen)...")
from transformers import AutoTokenizer
for model in ['bert-base-uncased', 'gpt2', 't5-small',
              'Qwen/Qwen2.5-Coder-7B-Instruct']:
    print(f"  Loading {model}...")
    AutoTokenizer.from_pretrained(model)


# 5. Lab 05 pretrained embeddings
announce("5/5", "Downloading Lab 05 pretrained embeddings (~1.7 GB)...")

print("  [a] Word2Vec Google News 300d (~1.5 GB, may take 10-25 min)...")
import gensim.downloader as api
api.load('word2vec-google-news-300')
print("      Word2Vec cached.")

print("  [b] GloVe 6B 100d (~130 MB)...")
api.load('glove-wiki-gigaword-100')
print("      GloVe cached.")

print("  [c] Sentence-BERT all-MiniLM-L6-v2 (~80 MB)...")
from sentence_transformers import SentenceTransformer
SentenceTransformer('all-MiniLM-L6-v2')
print("      Sentence-BERT cached.")


print("\n" + "=" * 60)
print("Setup complete. All models are ready to use offline.")
print("Total downloaded: ~2.3 GB")
print("=" * 60)