from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import chroma



def chroma_embed(chunks):
    collection = client.create_collection(name="my_collection", embedding_function=emb_fn)

    collection.add(
        documents=chunks,
    )
    return client


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
