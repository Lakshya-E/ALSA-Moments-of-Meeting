# from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS, Chroma


def chroma_vector_store(chunks):
    """
    This function embeds the given chunks using specified
    embedding model and stores in vector database and returns
    the retriever
    """
    embeddings = OpenAIEmbeddings()
    db = Chroma.from_texts(chunks, embeddings)

    retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 2})
    return retriever


def embed_n_vectorstore(chunks):
    """
    This function embeds the given chunks using specified
    embedding model and stores in vector database and returns
    to the user
    """
    embeddings = OpenAIEmbeddings()
    # embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")

    vector_store = FAISS.from_texts(
        texts=chunks,
        embedding=embeddings
    )

    return vector_store
