from chunker import chunk_sentences
from embedding import Embedding
from similarity import calculate_similarity
import json
from llm import llm_refinement
embedding=Embedding("all-MiniLM-L6-v2")

def get_chunks(file_path):
    with open(file_path,"r") as f:
        text=f.read()
        chunk_size=3
        overlap=1
        chunks=chunk_sentences(text,chunk_size,overlap)
        chunks=[''.join(chunk) for chunk in chunks]
        chunks=[{"sentence": chunk, "source":file_path} for chunk in chunks]
    return chunks

def get_vector_encodings():
    print("Initialising database")
    database=chunks=[]
    chunks=get_chunks("documents/python.txt")
    chunks+=get_chunks("documents/java.txt")
    chunks+=get_chunks("documents/spring.txt")
    for chunk in chunks: 
        text_embedding=get_embedding(chunk["sentence"])
        database.append({
            "sentence":chunk["sentence"],
            "embedding": text_embedding,
            "source": chunk["source"]
        })
    return database

def get_embedding(text):    
    embedding_value=embedding.encode(text)
    return embedding_value

def get_text_from_embedding(embedding):
    text=embedding.decode(embedding)
    return text

def get_best_match_chunk(question_embedding,vector_db):
    best=float('-inf')
    results=[]
    for vector in vector_db:
        similarity_score=calculate_similarity(question_embedding,vector["embedding"])
        if similarity_score>best:
            best_score=similarity_score
            results.append({
                "score": float(best_score),
                "sentence": vector["sentence"],
                "source": vector["source"]
            })
    results=sorted(results,key=lambda x: x["score"],reverse=True)
    return results

def store_results(results):
    with open("documents/results.json","w") as f:
            json.dump(results,f,indent=4,default=float)

        
if __name__=="__main__":
    vector_db=[]
    while True:
        if len(vector_db)==0:
            vector_db=get_vector_encodings()
        question=input("Ask a question [Press Q to exit]: ")
        if(question.strip().upper()=='Q'):
            break
        question_embedding=get_embedding(question)
        retrival_results=get_best_match_chunk(question_embedding,vector_db)
        store_results(retrival_results)
        print(json.dumps(retrival_results[:3],indent=4,default=float))
        response=llm_refinement(retrival_results[:3],question)
        print(response)

        

