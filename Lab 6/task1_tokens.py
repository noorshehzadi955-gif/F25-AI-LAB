import re

# Six required examples from the lab manual
samples = [
    "AI, search!",                 # punctuation
    "I can't log in.",             # contraction
    "help@example.com",            # email
    "CS4944 version 2.1",          # course/code identifier
    "",                            # empty text
    "یہ ایک مثال ہے"                # Urdu text
]

for text in samples:
    whitespace_tokens = text.split()
    word_like_tokens = re.findall(r"\b\w+\b", text, flags=re.UNICODE)

    print("\nOriginal text:", repr(text))
    print("Whitespace tokens:", whitespace_tokens)
    print("Whitespace count:", len(whitespace_tokens))
    print("Word-like tokens:", word_like_tokens)
    print("Word-like count:", len(word_like_tokens))

# Optional: compare the model's subword tokenizer on two English examples.
# Install sentence-transformers to enable this part.
try:
    from sentence_transformers import SentenceTransformer

    model = SentenceTransformer(
        "sentence-transformers/all-MiniLM-L6-v2",
        device="cpu"
    )

    print("\nMODEL SUBWORD TOKENIZATION")
    for text in samples[:2]:
        print("Original:", text)
        print("Subword tokens:", model.tokenizer.tokenize(text))

except ImportError:
    print("\nOptional model tokenizer not run.")
    print("Install sentence-transformers if you want this comparison.")
