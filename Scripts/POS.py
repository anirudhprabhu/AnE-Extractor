def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()

import spacy

nlp = spacy.load('en_core_web_lg')

# Process `text` with Spacy NLP Parser
text = read_file('/Users/anirudhprabhu/PycharmProjects/AnE-Extractor/Data/A Short History of Nearly Everything.txt')
processed_text = nlp(text)

# How many sentences are in the book (Pride & Prejudice)?
sentences = [s for s in processed_text.sents]
print(len(sentences))

# Print sentences from index 10 to index 15, to make sure that we have parsed the correct book
print(sentences[10:15])

# Extract all the personal names from Pride & Prejudice and count their occurrences.
# Expected output is a list in the following form: [('elizabeth', 622), ('darcy', 312), ('jane', 286), ('bennet', 266) ...].

from collections import Counter, defaultdict

def extract_finite_verb(doc):

    characters = Counter()

    for ent in processed_text.ents:
        print(ent)
        if ent.label_ == 'PERSON':
            characters[ent.lemma_] += 1

    return characters.most_common()

print(extract_finite_verb(processed_text)[:20])