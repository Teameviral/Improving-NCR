import spacy
import neuralcoref

def resolve_coreference(text):
    # Load spaCy model with neural coreference resolution
    nlp = spacy.load('en_core_web_sm')
    neuralcoref.add_to_pipe(nlp)

    # Process the text with spaCy
    doc = nlp(text)

    # Resolve coreferences
    resolved_text = doc._.coref_resolved

    return resolved_text

# Example usage
text = "John is a great engineer. He loves his job. However, he wants to pursue higher studies."
resolved_text = resolve_coreference(text)

print("Original Text:")
print(text)
print("\nResolved Text:")
print(resolved_text)
