import gc
from conversation import Conversation_RAG
from vector_index import *
from setup import ModelSetup
from torch import cuda

def load_models(embedding_model,llm):
    global conv_qa 
    conv_qa = Conversation_RAG(embedding_model, llm)
    global model_setup
    model_setup = ModelSetup(embedding_model, llm)
    success_prompt = model_setup.setup()
    return success_prompt

def get_chat_history(inputs):

    res = []
    for human, ai in inputs:
        res.append(f"Human:{human}\nAssistant:{ai}")
    return "\n".join(res)

def add_text(history, text):

    history = history + [[text, None]]
    return history, ""


def bot(history,
        instruction="Use the following pieces of context to answer the question at the end. Generate the answer based on the given context only if you find the answer in the context. If you do not find any information related to the question in the given context, just say that you don't know, don't try to make up an answer. Keep your answer expressive.",
        temperature=0.1,
        max_new_tokens=512,
        repetition_penalty=1.1,
        top_k=10,
        top_p=0.95,
        k_context=5,
        num_return_sequences=1,
        ):
    
    pipeline = conv_qa.create_pipeline(max_new_tokens=max_new_tokens,
                                  temperature=temperature, 
                                  repetition_penalty=repetition_penalty, 
                                  top_k=top_k, 
                                  top_p=top_p, 
                                  num_return_sequences=num_return_sequences)
                             
    qa = conv_qa.create_conversation(
                            #  model_setup.model,
                            #  model_setup.tokenizer,
                             pipeline=pipeline,
                             vectordb=model_setup.vectordb,
                             k_context=k_context,
                             
                             instruction=instruction
    )

    chat_history_formatted = get_chat_history(history[:-1])
    res = qa(
        {
            'question': history[-1][0],
            'chat_history': chat_history_formatted
        }
    )

    history[-1][1] = res['answer']
    return history

def reset_sys_instruction(instruction):

    default_inst = "Use the following pieces of context to answer the question at the end. Generate the answer based on the given context only if you find the answer in the context. If you do not find any information related to the question in the given context, just say that you don't know, don't try to make up an answer. Keep your answer expressive."
    return default_inst

def clear_cuda_cache():

    cuda.empty_cache()
    gc.collect()
    return None