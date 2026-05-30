# 🔬 ResearchLens — Research Paper Topic Clustering & Gap Analysis

A full-stack research intelligence dashboard that clusters academic papers by topic, identifies underexplored research areas, and visualises publication trends — built with Python, BERTopic, UMAP, and Streamlit.

---

## 📸 Dashboard Preview

| Tab | Description |
|---|---|
| 📊 Distribution | Bar chart + donut pie of papers per topic |
| 🔍 Gap Analysis | Bar / Treemap / Bubble + radar chart + badge table |
| 📈 Trends | Line chart + Year×Topic heatmap + cumulative area chart |
| ☁️ Word Clouds | Per-topic word clouds with dark background |
| 📄 Raw Data | Searchable table + CSV downloads |

---

## 🗂️ Project Structure

```
RESEARCH PAPER TOPIC/
│
├── app/
│   └── dashboard.py          # Streamlit dashboard (main entry point)
│
├── data/
│   ├── raw_papers.csv        # Original scraped/collected papers
│   ├── processed_papers.csv  # Cleaned + clustered papers (main input)
│   ├── embeddings.npy        # Sentence embeddings (numpy array)
│   ├── gap_report.csv        # Precomputed gap scores per topic
│   └── topic_info.csv        # Topic metadata (keywords, IDs)
│
├── notebooks/
│   ├── data_collection.ipynb # Scraping / API data collection
│   ├── preprocessing.ipynb   # Text cleaning & normalisation
│   ├── embedding.ipynb       # Sentence-BERT embeddings + UMAP
│   ├── clustering.ipynb      # BERTopic / KMeans clustering
│   └── gap_analysis.ipynb    # Gap score computation
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/research-paper-topic.git
cd research-paper-topic
```

### 2. Create a virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the dashboard
```bash
streamlit run app/dashboard.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 📋 Data Format

The dashboard reads `data/processed_papers.csv`. Required columns:

| Column | Type | Description |
|---|---|---|
| `title` | string | Paper title |
| `year` | integer | Publication year |
| `topic_name` | string | Assigned topic label |
| `clean_text` | string | Preprocessed text for word clouds |

Optional columns (auto-displayed if present):

| Column | Description |
|---|---|
| `abstract` | Paper abstract |
| `authors` | Author names |
| `citations` | Citation count |
| `venue` | Journal / conference name |
| `umap_x`, `umap_y` | 2D UMAP coordinates |
| `topic` | Numeric topic ID |
| `category` | Broader research category |

---

## 🧠 Pipeline Overview

```
Raw Papers (CSV / API)
        │
        ▼
  Preprocessing
  (clean, tokenise, remove stopwords)
        │
        ▼
  Sentence Embeddings
  (sentence-transformers / all-MiniLM-L6-v2)
        │
        ▼
  Dimensionality Reduction
  (UMAP → 2D for visualisation, 5D for clustering)
        │
        ▼
  Topic Clustering
  (BERTopic / HDBSCAN)
        │
        ▼
  Gap Analysis
  (gap_score = 1 / paper_count per topic)
        │
        ▼
  Streamlit Dashboard
```

---

## 📦 Requirements

```
streamlit>=1.32.0
pandas>=2.0.0
numpy>=1.26.0
plotly>=5.20.0
matplotlib>=3.8.0
wordcloud>=1.9.3
sentence-transformers>=2.7.0
bertopic>=0.16.0
umap-learn>=0.5.6
hdbscan>=0.8.33
scikit-learn>=1.4.0
```

Install all at once:
```bash
pip install -r requirements.txt
```


## 📄 License

MIT License — free to use, modify, and distribute.

---

## 🙋 Author

Built as a research analytics project.  
Feel free to open an issue or pull request for improvements.
