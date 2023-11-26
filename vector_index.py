from langchain.vectorstores import FAISS, Chroma, DocArrayInMemorySearch
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os, shutil


# # This function loads a PDF of your chosing
# def create_vector_store_index(pdf_path, embedding_model_repo_id="sentence-transformers/all-roberta-large-v1"):
#     loaders = PyPDFLoader(pdf_path)
#     pages = loaders.load()

#     text_splitter = RecursiveCharacterTextSplitter(
#         chunk_size=1024,
#         chunk_overlap=128,
#     )
#     embedding_model_instance = HuggingFaceEmbeddings(
#         model_name=embedding_model_repo_id
#     )
#     docs = text_splitter.split_documents(pages)
#     # Return the vector database
#     vectordb = Chroma.from_documents(
#         docs,
#         embedding=embedding_model_instance,
#         persist_directory="./chroma_db"
#     )
#     return "Vector store index created."



def create_vector_store_index(file_path, embedding_model_repo_id="sentence-transformers/all-roberta-large-v1"):

    file_path_split = file_path.split(".")
    file_type = file_path_split[-1].rstrip('/')

    if file_type == 'csv':
        print(file_path)
        loader = CSVLoader(file_path=file_path)
        documents = loader.load()

    elif file_type == 'pdf':
        loader = PyPDFLoader(file_path)
        pages = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 512,
        chunk_overlap = 128,)

        documents = text_splitter.split_documents(pages)


    embedding_model = HuggingFaceEmbeddings(
        model_name=embedding_model_repo_id
        )

    vectordb = FAISS.from_documents(documents, embedding_model)
    file_output = "./db/faiss_index"
    vectordb.save_local(file_output)

    return "Vector store index is created."


def upload_and_create_vector_store(file,embedding_model_repo_id):

    # Save the uploaded file to a permanent location
    file_path = file
    split_file_name = file_path.split("/")
    file_name = split_file_name[-1]

    current_folder = os.getcwd()
    #root_folder = os.path.dirname(current_folder)
    data_folder = os.path.join(current_folder, "data")
    permanent_file_path = os.path.join(data_folder, file_name)
    
    # Create the directory if it doesn't exist
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    shutil.copy(file, permanent_file_path)

    # Access the path of the saved file
    print(f"File saved to: {permanent_file_path}")


    index_success_msg = create_vector_store_index(permanent_file_path,embedding_model_repo_id)
    return index_success_msg