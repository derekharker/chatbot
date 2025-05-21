from langchain.text_splitter import RecursiveCharacterTextSplitter
from pathlib import Path
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

# Configure text splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=50,
)

# Read all text files and generate chunks
texts = [] # this is where the text chunks will be stored
metadatas = [] # this will keep track of which text chunks belong to which text file
folder = Path("vectorstore/txt_files/")
for f in folder.glob("*.txt"):
    doc = f.read_text(encoding="utf8")
    chunks = splitter.split_text(doc)
    texts.extend(chunks) # store text chunks in texts
    metadatas.extend([{"source": f.name}] * len(chunks)) # store file name in metadatas

# Initialize OpenAI embeddings
embeddings = OpenAIEmbeddings()

# Build or load FAISS vector store
vectorstore = FAISS.from_texts(
    texts,
    embeddings,
    metadatas
)

# Persist to disk
vectorstore.save_local("vectorstore")