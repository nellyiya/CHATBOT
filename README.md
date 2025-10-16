

```markdown
# Agriculture Chatbot Using T5

## Project Introduction

This project is a domain-specific chatbot focused on agriculture, aimed at providing helpful, relevant, and accurate answers to user queries related to farming, crop management, pest control, and more. The chatbot leverages a pre-trained Transformer model from Hugging Face, specifically T5-small, which is fine-tuned using the agriculture Q&A dataset to generate contextual and meaningful responses through generative question answering.

The goal is to gain hands-on experience in fine-tuning Transformer models with TensorFlow and implementing an interactive interface for end-users.

## Dataset

The fine-tuning dataset used is the [KisanVaani Agriculture Q&A English-only dataset](https://huggingface.co/datasets/KisanVaani/agriculture-qa-english-o) sourced from Hugging Face. It contains a broad variety of agriculture-related question-answer pairs, enabling the chatbot to generalize across multiple farming topics. The dataset was preprocessed through tokenization, normalization, and handling of noisy or missing data to prepare it suitably for Transformer input.

## Project Structure

```
├── agri_chatbot_t5/             # Trained T5 model files post fine-tuning
├── app.py                      # Streamlit-based chatbot user interface
├── training_notebook.ipynb     # Colab notebook: data preprocessing, fine-tuning, evaluation, and testing
├── README.md                   # This README file
├── requirements.txt            # Python dependencies for the project
```

## Technologies Used

- Python 3.x  
- TensorFlow (model fine-tuning and training)  
- Hugging Face Transformers (pre-trained T5 model)  
- Streamlit (interactive chatbot UI)  
- Git & Git Large File Storage (LFS) for versioning large model files  

## How to Run

### Locally

Clone the repository:

```
git clone https://github.com/nellyiya/CHATBOT.git
cd CHATBOT
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the chatbot UI:

```
streamlit run app.py
```

Open a browser at `http://localhost:8501` to interact with the chatbot.

### Using Google Colab

The notebook contains all steps including data preprocessing, model training, hyperparameter tuning, evaluation, and testing. You can also run the Streamlit app using ngrok tunneling if needed.

## Evaluation & Performance Metrics

- Hyperparameter tuning on learning rate, batch size, and epochs was performed to optimize performance.  
- Evaluation metrics include BLEU score, F1-score, perplexity, and qualitative conversational tests.  
- The chatbot accurately answers agriculture-related queries while appropriately handling or rejecting out-of-domain questions.

## User Interface

The interface is implemented in Streamlit, offering an intuitive text input box and clear display of generated answers. It is designed for smooth user interaction requiring minimal setup.

## Demo Video

A 5–10 minute video is included, showcasing training, evaluation, and live interaction with the chatbot illustrating its capabilities in agriculture Q&A.

## Contact

- Maintainer: nellyiya  
- Email: n.iyabikoze@alustudent.com  
- GitHub: https://github.com/nellyiya/CHATBOT

---

Thank you for exploring this Agriculture Chatbot project! Contributions, feedback, and collaboration are welcome.
```

***
