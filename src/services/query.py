from groq import Groq
import os
from dotenv import load_dotenv

import services.ranker.bm25_ranker as bm25_ranker
import services.chroma_db as chroma_db
import services.ranker.reranker as reranker

CHOSEN_GROQ_MODEL = "qwen/qwen3-32b"
CHOSEN_GROQ_MODEL = "groq/compound"
CHOSEN_GROQ_MODEL = "groq/compound-mini"
CHOSEN_GROQ_MODEL = "openai/gpt-oss-20b"
CHOSEN_GROQ_MODEL = "openai/gpt-oss-safeguard-20b"
CHOSEN_GROQ_MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"
CHOSEN_GROQ_MODEL = "llama-3.1-8b-instant"
CHOSEN_GROQ_MODEL = "llama-3.3-70b-versatile"
CHOSEN_GROQ_MODEL = "openai/gpt-oss-120b"

load_dotenv()

groq_client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def rag_query(question):
    source_sentences = chroma_db.retrieve(question)
    source_sentences = bm25_ranker.rank_n_filter(question, source_sentences)
    source_sentences = reranker.rerank(question, source_sentences)

    prompt = f"""Answer the question based only on this context:

Context:
{chr(10).join(source_sentences)}

Question: {question}

Answer:"""

    # Generate response
    response = groq_client.chat.completions.create(
        model=CHOSEN_GROQ_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content, source_sentences
