from conversation import Conversation_RAG
from vector_index import *

class ModelSetup:
    def __init__(self, embedding_model_repo_id, llm_repo_id):

        #self.hf_token = hf_token
        self.embedding_model_repo_id = embedding_model_repo_id
        self.llm_repo_id = llm_repo_id

    def setup(self):

        conv_rag = Conversation_RAG(self.embedding_model_repo_id, self.llm_repo_id)

        # self.model, self.tokenizer, self.vectordb = conv_rag.load_model_and_tokenizer()
        self.vectordb = conv_rag.create_vectordb()
        self.pipeline = conv_rag.create_pipeline()

        return "Model Setup Complete"