import ollama
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

print("--- 1. Reading the ENTIRE Registration Act... ---")
loader = PyPDFLoader("./legal_docs/registrationActHindi.pdf") 
docs = loader.load()

print("--- 2. Breaking PDF into small chunks... ---")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_documents(docs)

print("--- 3. Creating Offline Search Database (ChromaDB)... ---")
# This creates a model that understands Hindi text meanings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
# This saves the chunks into a database folder
vector_db = Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory="./chroma_db")

def ask_gramin_nyaya(user_query):
    print("\n--- Searching the Database for the answer... ---")
    
    # 4. Search the entire PDF for the top 3 most relevant paragraphs
    relevant_chunks = vector_db.similarity_search(user_query, k=3)
    
    # Combine those specific paragraphs into one text block
    context_text = "\n\n".join([chunk.page_content for chunk in relevant_chunks])
    
    print("--- Generating Hindi Response... ---")
    # 5. Pass ONLY the relevant laws to Qwen
    response = ollama.chat(model='qwen2.5:1.5b', messages=[
        {
            'role': 'system', 
            'content': f'You are Gramin-Nyaya, a legal expert. Use ONLY the following legal text to answer the user in simple Hindi. If the answer is not in the text, say you do not know.\n\nLegal Text:\n{context_text}'
        },
        {'role': 'user', 'content': user_query},
    ])
    
    return response['message']['content']

if __name__ == "__main__":
    query = "दस्तावेजों के पंजीकरण के लिए क्या नियम हैं?"
    print("\nसवाल:", query)
    print("\nउत्तर:\n", ask_gramin_nyaya(query))