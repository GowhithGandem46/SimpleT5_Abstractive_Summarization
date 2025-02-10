# 🚀 **SimpleT5 Abstractive Summarization**  

✨ **Unlock the power of AI-generated summaries!** This project fine-tunes **T5 (Text-to-Text Transfer Transformer)** for **abstractive summarization**, enabling you to condense large text passages into meaningful summaries using deep learning. 📝✨  

---

## 🌟 **Features**
✅ **Abstractive Summarization** – Generates human-like summaries, not just extracts sentences.  
✅ **SimpleT5 Implementation** – Built with [SimpleT5](https://github.com/Shivanandroy/simpleT5) for streamlined fine-tuning.  
✅ **Pretrained T5 Models** – Leverages Hugging Face’s `t5-small`, `t5-base`, or `t5-large`.  
✅ **Scalable & Fast** – Optimized training with PyTorch Lightning.  
✅ **Easy-to-Use Notebook** – A step-by-step guide for training & inference.  

---

## 🏗 **Project Structure**
```bash
SimpleT5_Abstractive_Summarization/
├── 📜 README.md                   # Project documentation
├── 📂 data/                        # Dataset directory
├── 📂 models/                      # Trained model weights
├── 📂 images/                      # Project visuals/screenshots
├── 📂 notebooks/                   # Jupyter Notebook for training & inference
├── 📝 requirements.txt              # Required dependencies
├── 🔹 train.py                      # Model training script
├── 🔹 infer.py                      # Summarization script
└── 🔹 preprocess.py                  # Data preprocessing script
```

---

## 🚀 **Installation & Setup**
### 🔹 **1. Clone the Repository**
```bash
git clone https://github.com/GowhithGandem46/SimpleT5_Abstractive_Summarization.git
cd SimpleT5_Abstractive_Summarization
```

### 🔹 **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### 🔹 **3. Run the Jupyter Notebook**
```bash
jupyter notebook notebooks/SimpleT5_Abstractive_Summarization.ipynb
```
💡 **Tip**: Running the notebook will walk you through **loading data, training, and generating summaries!** 🎯  

---

## 🎯 **Training the Model**
Fine-tune **T5** on your dataset in just a few steps:

```python
from simplet5 import SimpleT5

model = SimpleT5()
model.from_pretrained("t5","t5-small")

model.train(train_df=df_train,
            eval_df=df_val,
            source_max_token_len=512,
            target_max_token_len=128,
            batch_size=8,
            max_epochs=3)
```

---

## 📝 **Generating Summaries**
Once trained, use the model for **text summarization**:

```python
summary = model.predict("Your long text goes here...")
print(summary)
```

🚀 **Transform lengthy paragraphs into concise, human-like summaries in seconds!**  

---

## 🎨 **UI Preview**
🔍 Example of a summarized text:

**Original:**  
*"Artificial Intelligence is revolutionizing industries, automating tasks, and enabling smarter decision-making through machine learning and deep learning techniques."*  

**Generated Summary:**  
*"AI is transforming industries with automation and smart decision-making."*  

---

## 📊 **Monitoring Training**
Use **TensorBoard** to track training progress:
```bash
tensorboard --logdir runs/
```

---

🚀 **Let’s summarize smarter!** 📝✨  

---
