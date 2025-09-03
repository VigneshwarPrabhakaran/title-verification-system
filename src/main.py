import os
import pandas as pd
from fuzzywuzzy import fuzz
from sentence_transformers import SentenceTransformer
from soundex import Soundex

# ===== Paths =====
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXISTING_TITLES_FILE = os.path.join(BASE_DIR, '../data/sample_titles.csv')
LOGS_FILE = os.path.join(BASE_DIR, '../data/logs.txt')

# ===== Configuration =====
DISALLOWED_WORDS = ["Police", "Crime", "Corruption", "CBI", "CID", "Army"]
DISALLOWED_PREFIXES = ["The", "India"]
DISALLOWED_SUFFIXES = ["News", "Samachar", "Daily", "Weekly", "Monthly"]
SEMANTIC_SIM_THRESHOLD = 0.65  # 65Daily Da%
PHONETIC_SIM_THRESHOLD = 0.8  # 80%

# ===== Load existing titles =====
df_titles = pd.read_csv(EXISTING_TITLES_FILE)
existing_titles = df_titles['title'].tolist()

# ===== Initialize models =====
model = SentenceTransformer('all-MiniLM-L6-v2')
soundex = Soundex()

# ===== Helper Functions =====
def is_disallowed_word(title):
    return any(word.lower() in title.lower() for word in DISALLOWED_WORDS)

def has_disallowed_prefix_suffix(title):
    words = title.split()
    if words[0] in DISALLOWED_PREFIXES or words[-1] in DISALLOWED_SUFFIXES:
        return True
    return False

def phonetic_similarity(title, existing_title):
    return soundex.soundex(title) == soundex.soundex(existing_title)

def semantic_similarity(title, existing_title):
    embeddings = model.encode([title, existing_title])
    from numpy import dot
    from numpy.linalg import norm
    cos_sim = dot(embeddings[0], embeddings[1]) / (norm(embeddings[0]) * norm(embeddings[1]))
    return cos_sim

# ===== Main Verification =====
print("=== Title Verification Prototype ===")
new_title = input("Enter a new title: ").strip()

status = "Accepted"
reason = "Passed all checks"
verification_probability = 100.0

for existing_title in existing_titles:
    # Exact or fuzzy match
    fuzzy_score = fuzz.ratio(new_title.lower(), existing_title.lower())
    if fuzzy_score >= 85:
        status = "Rejected"
        reason = f"Too similar to existing title: '{existing_title}' (score={fuzzy_score})"
        verification_probability = 100 - fuzzy_score
        break
    # Phonetic similarity
    if phonetic_similarity(new_title, existing_title):
        status = "Rejected"
        reason = f"Phonetically too similar to existing title: '{existing_title}'"
        verification_probability = 20
        break
    # Semantic similarity
    if semantic_similarity(new_title, existing_title) >= SEMANTIC_SIM_THRESHOLD:
        status = "Rejected"
        reason = f"Semantically too similar to existing title: '{existing_title}'"
        verification_probability = 30
        break

# Disallowed words / prefix / suffix
if is_disallowed_word(new_title):
    status = "Rejected"
    reason = "Contains disallowed word(s)"
    verification_probability = 0

if has_disallowed_prefix_suffix(new_title):
    status = "Rejected"
    reason = "Contains disallowed prefix/suffix"
    verification_probability = 0

# ===== Output =====
print(f"\nStatus: {status}")
print(f"Reason: {reason}")
print(f"Verification Probability: {verification_probability:.2f}%")

# ===== Log submission =====
with open(LOGS_FILE, 'a', encoding='utf-8') as f:
    f.write(f"{new_title} | {status} | {reason} | Probability={verification_probability:.2f}%\n")

print("\n✅ Submission logged successfully!")
