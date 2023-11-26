# Project Title: Retrieval-Augmented Generation with Hugging Face Transformers and Gradio

## Overview

This project implements a retrieval-augmented generation system that seamlessly integrates local large language models from Hugging Face Transformers. By combining advanced language processing capabilities, the system intelligently retrieves relevant information and generates context-aware responses. The user interface is powered by Gradio, ensuring an interactive and user-friendly experience for input, retrieval, and generation interactions. To prioritize user privacy and security, the application is designed for local execution, giving users control over their data.

## Key Features

- **Cutting-edge Language Models:** Utilize state-of-the-art language models from Hugging Face Transformers for powerful natural language understanding and generation. The user can chose the pre-seted models or look for a model repository ID on 🤗 and add it in the gradio_app.py script.

- **Retrieval-Augmented Generation:** Combine retrieval and generation techniques for comprehensive and context-aware responses to user queries.

- **Gradio Integration:** Leverage Gradio to create an interactive and user-friendly interface, making the system accessible to a wide range of users. Set `Share=True` on the `gradio.launch()`. This generates a public, shareable link that you can send to anybody!

- **Local Execution:** Emphasizing privacy and security, the application is designed for local execution, empowering users with control over their data.

## Technologies Used

- Hugging Face Transformers
- Gradio
- Python
- Retrieval Augmented Generatrion
- LangChain
- Vector Store databases and indexes (FAISS and ChromaDB)

## Getting Started

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/matglima/Local-LLM-RAG-Transformers-App.git
    ```

2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application:**
    ```bash
    python gradio_app.py
    ```

4. **Open the Application:**
    Visit `http://localhost:7860` (you can set another port in the `gradio.launch()` function) in your web browser.

## Usage

1. Upload the pdf or csv for the knowledge retrieval, choose the embedding model and click create vector database.
2. Choose the LLM parameters or use the default ones.
3. Input your query into the provided interface.
4. Experience the system's intelligent retrieval and generation of context-aware responses.
5. Explore the capabilities of the application for natural language understanding and generation.

## Contribution

Contributions are welcome! If you'd like to contribute to the project, feel free to contact me.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Special thanks to Hugging Face, LangChain and the Gradio team for their exceptional libraries.

---
