def chunk_sentences(text,chunk_size,overlap):
    sentences=text.split("\n")
    start=0
    step=chunk_size-overlap
    chunk=[]
    chunks=[]
    while start < len(sentences):
        chunk = sentences[start:start+chunk_size]
        chunks.append(chunk)
        start += step
    return chunks
