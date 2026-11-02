import re

def make_text_clean(text):
    #Replace tabs and spaces with single space
    text = re.sub(r"[ \t]+", " ",text)

    # Remove spaces around line breaks
    text = re.sub(r" *\n *", "\n", text)

    # Replace excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Remove unnecessary spaces at the beginning and end
    text = text.strip()

    return text


def convert_to_chunks(text, max_len=3000):
    sentences = re.split(r"(?<=[.!?])\s+",text)
    chunks = []
    current_chunk = ""
    for sentence in sentences:
        if len(sentence) > max_len:
            if current_chunk:
                chunks.append(current_chunk)
                current_chunk = ""

            words = sentence.split()

            for word in words:
                if current_chunk and len(current_chunk) + len(word) + 1 > max_len:
                    chunks.append(current_chunk)
                    current_chunk = word
                else:
                    if current_chunk:
                        current_chunk += " " + word
                    else:
                        current_chunk = word
        else:
            proposed_chunk = (current_chunk + " " +sentence).strip()

            if len(proposed_chunk) <= max_len:
                current_chunk = proposed_chunk
            else:
                if current_chunk:
                    chunks.append(current_chunk)
                current_chunk = sentence
    if current_chunk:
        chunks.append(current_chunk)

    return chunks


