"""
Pre-download the three pretrained models Lab 05 will use.
Run once, before the lab session, on a good internet connection.

Total download: ~1.7 GB
Total time: 15-30 minutes depending on your connection.
"""

import time

print("=" * 60)
print("Prefetching Lab 05 pretrained models")
print("=" * 60)

# 1. Word2Vec Google News 300d (~1.5 GB)
print("\n[1/3] Downloading Word2Vec Google News 300d (~1.5 GB)...")
print("      This is the biggest download. Get a coffee.")
start = time.time()
import gensim.downloader as api
w2v = api.load('word2vec-google-news-300')
print(f"      Done in {(time.time() - start) / 60:.1f} min.")
print(f"      Vector shape: {w2v['king'].shape} (300 dimensions)")

# 2. GloVe 6B 100d (~130 MB)
print("\n[2/3] Downloading GloVe 6B 100d (~130 MB)...")
start = time.time()
glove = api.load('glove-wiki-gigaword-100')
print(f"      Done in {(time.time() - start) / 60:.1f} min.")
print(f"      Vector shape: {glove['king'].shape} (100 dimensions)")

# 3. Sentence-BERT all-MiniLM-L6-v2 (~80 MB)
print("\n[3/3] Downloading sentence-BERT all-MiniLM-L6-v2 (~80 MB)...")
start = time.time()
from sentence_transformers import SentenceTransformer
sbert = SentenceTransformer('all-MiniLM-L6-v2')
test_embed = sbert.encode('The cat sat on the mat')
print(f"      Done in {(time.time() - start) / 60:.1f} min.")
print(f"      Embedding shape: {test_embed.shape} (384 dimensions)")

print("\n" + "=" * 60)
print("All three models cached locally. Lab 05 will run offline.")
print("=" * 60)