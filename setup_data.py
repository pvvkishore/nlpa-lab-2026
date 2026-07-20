"""
Post-install setup for NLPA Lab 2026.

Downloads all data files that pip cannot install directly:
  - NLTK tokenizer data (punkt_tab)
  - spaCy English model (en_core_web_sm)
  - Stanza English models
  - HuggingFace tokenizer files for BERT, GPT-2, T5, Qwen

Run once after `conda env create -f environment.yml`:
    conda activate nlpa_2026
    python setup_data.py
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
announce("1/4", "Downloading NLTK tokenizer data...")
import nltk
nltk.download('punkt_tab', quiet=False)

# 2. spaCy English model
announce("2/4", "Downloading spaCy English model...")
run(f'"{sys.executable}" -m spacy download en_core_web_sm')

# 3. Stanza English models
announce("3/4", "Downloading Stanza English models (~500 MB, patient please)...")
import stanza
stanza.download('en')

# 4. HuggingFace tokenizer files
announce("4/4", "Caching HuggingFace tokenizers (BERT, GPT-2, T5, Qwen)...")
from transformers import AutoTokenizer
for model in ['bert-base-uncased', 'gpt2', 't5-small',
              'Qwen/Qwen2.5-Coder-7B-Instruct']:
    print(f"  Loading {model}...")
    AutoTokenizer.from_pretrained(model)

print("\n" + "=" * 60)
print("Setup complete. All tokenizers are ready to use offline.")
print("=" * 60)