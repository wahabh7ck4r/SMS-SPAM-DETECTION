# 📩 SMS Spam Detection App

This is a simple **Streamlit web app** that detects whether a given SMS message is **Spam** or **Not Spam** using a machine learning model trained on labeled data.

---

## 🚀 Live App

👉 [Click here to try the app](https://sms-spam-detection-nb3fdvxmxm2cnorpfr5mup.streamlit.app)

---
## 📁 Project Structure

| File/Folder         | Description                                        |
|---------------------|----------------------------------------------------|
| `app.py`            | 🎯 Main Streamlit application script               |
| `Model.pkl`         | 🧠 Trained machine learning model file             |
| `Vectorizer.pkl`    | 🧰 Vectorizer for transforming text data           |
| `nltk_data/`        | 📚 NLTK data folder containing `punkt`, `stopwords` |
| `download_nltk.py`  | 🔽 Script to download NLTK data locally           |
| `requirements.txt`  | 📦 Python dependencies required for the project    |
| `README.md`         | 📄 Project overview and documentation              |
| `.gitignore`        | 🚫 Specifies untracked files to ignore in Git      |
| `DataSet/`          | 📊 Dataset folder used for training                |
| `NoteBook/`         | 📓 Jupyter Notebooks with data analysis, model building, comparison, and final model saving |


---

## 🧠 Model Details

- **Algorithm:** Multinomial Naive Bayes
- **Text Preprocessing:** Tokenization, stopword removal
- **Vectorization:** CountVectorizer or TF-IDF
- **Libraries Used:** Scikit-learn, NLTK, Streamlit

---

## ⚙️ How to Run Locally

```bash
git clone https://github.com/wahabh7ck4r/SMS-SPAM-DETECTION.git
```
### Go to desire directory by using 
```bash
cd SMS-SPAM-DETECTION
```
### (optional) Create virtual environment and activate
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
````
### Install the Requirments by usign: 
```bash
pip install -r requirements.txt
```
### Run the Streamlit app
```bash
streamlit run app.py
```


