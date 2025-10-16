# AgriChatbot



## Introduction
Farmers and agricultural workers, especially in remote or underserved regions, often face challenges accessing timely and reliable information on crop management, soil health, pest control, and sustainable farming practices. Traditional information dissemination methods can be slow or unsuitable for users with limited literacy or internet access.

This project develops an **agriculture-specific chatbot** to assist farmers by providing concise, actionable advice through natural language conversation. The chatbot is built on the **T5 Transformer architecture**, fine-tuned on the **KisanVaani agriculture QA dataset** (22,615 question-answer pairs). Users can interact via a **Streamlit web interface**, ensuring easy access to agricultural knowledge.



## Dataset Cleaning
The dataset has been cleaned by removing duplicates, handling missing values, standardizing text, and removing outliers.

## Video Demo
Watch the demo on YouTube: [https://youtu.be/Rn1yqRJSnzU](https://youtu.be/Rn1yqRJSnzU)


## Dataset Collection and Preprocessing
- **Dataset:** [KisanVaani agriculture QA dataset](https://huggingface.co/datasets/KisanVaani/agriculture-qa-english-only)  
- **Size:** 22,615 question-answer pairs  
- **Split:** 18,092 training samples (80%), 4,523 validation samples (20%)  

**Preprocessing steps:**
1. Loaded **T5 tokenizer (`t5-small`)** for WordPiece tokenization.  
2. Truncated and padded input/output sequences to **64 tokens**.  
3. Shifted decoder tokens to align with encoder-decoder framework.  
4. Masked padding token IDs with `-100` to ignore during loss calculation.  
5. Converted datasets to **TensorFlow batched datasets** for efficient training.



## Model Fine-Tuning and Training
- **Model:** TensorFlow T5 initialized with PyTorch weights  
- **Training:** 3 epochs, batch size 8, Adam optimizer, learning rate ~3e-4  
- **Custom loss:** Masked sparse categorical crossentropy to ignore padding  
- **Training time:** ~258–315 seconds per epoch  

**Loss progression:**
- Epoch 1: `train_loss=2.50`, `val_loss=1.19`  
- Epoch 2: `train_loss=1.25`, `val_loss=0.52`  
- Epoch 3: `train_loss=0.72`, `val_loss=0.34`  

*Loss curves show rapid convergence, indicating effective learning.*  



## Performance Evaluation
- Performance validated through **qualitative interactions**:  

**Examples:**
- Q: *Why is crop rotation important?*  
  A: *Prevents soil erosion and depletion, helps control pests and diseases.*  
- Q: *What are the different methods of irrigation?*  
  A: *Surface irrigation, drip irrigation, and sprinkler irrigation.*  
- Q: *What causes soil degradation?*  
  A: *Erosion, compaction, and nutrient depletion.*  

> The chatbot consistently provides relevant, concise answers in a short QA style, ideal for farmers seeking quick insights.



## User Interface and Features
- **Light/Dark Mode:** Switchable themes to reduce eye strain.
  <img width="1911" height="880" alt="image" src="https://github.com/user-attachments/assets/0d0dacf4-daf1-468e-a575-2d80d25d816a" />
  <img width="1907" height="887" alt="image" src="https://github.com/user-attachments/assets/68b9301d-cebb-493e-bac2-2a8e51463090" />
- **Settings Menu:** Customize chatbot behavior, notifications, and interface options.
  <img width="1908" height="883" alt="image" src="https://github.com/user-attachments/assets/0fb9a36c-24a2-4dd4-9045-8ce909f942ea" />

- **Profile Management:** Track past queries and personalize interaction history.
<img width="1907" height="883" alt="image" src="https://github.com/user-attachments/assets/49f27aa6-e494-4aca-a69b-dfe499263c71" />

- **Language Selection:** Kiswahili, English, French for wider accessibility.
  <img width="1914" height="882" alt="image" src="https://github.com/user-attachments/assets/cb545eb4-3d5a-4936-b366-965fe2379469" />

- **Chat:** Chat with the AgriChatbot

  <img width="1901" height="884" alt="image" src="https://github.com/user-attachments/assets/ba9df9f9-52f0-4c3c-b7e6-d37f175ca87a" />



## Chatbot Usage
- Access the chatbot via **Streamlit web interface**.  
- Enter a question and receive concise agricultural advice.  
- Switch themes or languages as needed for comfort and comprehension.  


## Conclusion and Future Directions
The AgriChatbot effectively assists farmers by transforming complex agricultural knowledge into actionable advice. Training loss reduction and qualitative testing demonstrate reliability and domain relevance.  

**Future improvements:** 
- Support multi-turn conversations for richer dialogue  
- Deploy on mobile platforms for broader accessibility  
- Implement out-of-domain query detection for robustness  


## References
- [KisanVaani agriculture QA dataset](https://huggingface.co/datasets/KisanVaani/agriculture-qa-english-only)  
- T5 Transformer: [Text-to-Text Transfer Transformer](https://arxiv.org/abs/1910.10683)  

