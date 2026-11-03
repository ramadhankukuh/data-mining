# Data Mining: IBM Machine Learning Professional Certificate

Repositori ini berisi notebook dan dataset dari **IBM Machine Learning Professional Certificate** di Coursera, dikerjakan sebagai tugas mata kuliah **Data Mining** di Universitas Dian Nuswantoro (UDINUS), Semarang.

Sertifikat: [IBM Machine Learning Professional Certificate (Coursera × UDINUS)](https://www.coursera.org/organizations/udinus/professional-certificates/ibm-machine-learning)

Semua penjelasan di dalam notebook sudah diterjemahkan ke bahasa Indonesia, dan setiap notebook diawali sel **Catatan Belajar** yang merangkum konsep utama serta dataset yang dipakai.

## Daftar Kursus

| No | Kursus | Folder | Status |
|----|--------|--------|--------|
| 1 | Exploratory Data Analysis for Machine Learning | [`Course-1`](Course-1/) | ✅ Selesai |
| 2 | Supervised Machine Learning: Regression | [`Course-2`](Course-2/) | ✅ Selesai |
| 3 | Supervised Machine Learning: Classification | `Course-3` | ⏳ Segera |
| 4 | Unsupervised Machine Learning | `Course-4` | ⏳ Segera |
| 5 | Deep Learning and Reinforcement Learning | `Course-5` | ⏳ Segera |
| 6 | Specialized Models: Time Series and Survival Analysis | `Course-6` | ⏳ Segera |

## Struktur Repositori

```
data-mining/
├── README.md
├── Course-1/
│   ├── data/
│   └── 01_… sampai 06_… (.ipynb)
├── Course-2/
│   ├── data/
│   ├── helper.py
│   └── 01_… sampai 06_… (.ipynb)
└── Course-3/ … Course-6/   (menyusul)
```

Setiap folder kursus berdiri sendiri: notebook dan folder `data/` berada sejajar, sehingga path data di notebook berupa `data/nama_file`. Jalankan notebook dari dalam folder kursus masing-masing.

## Ringkasan Materi

### Course 1: Exploratory Data Analysis for Machine Learning

| No | Notebook | Topik | Dataset |
|----|----------|-------|---------|
| 01 | `01_demo_reading_data` | Membaca data dari database SQL (SQLite + pandas) | `classic_rock.db` |
| 02 | `02_lab_reading_data` | Lab membaca file database | `baseball.db` |
| 03 | `03_lab_eda_iris` | EDA: statistik deskriptif, groupby, scatter, histogram, boxplot, pairplot | `iris_data.csv` |
| 04 | `04_demo_feature_engineering` | Transformasi log, fitur polinomial, interaksi, one-hot encoding | `Ames_Housing_Data.tsv` |
| 05 | `05_demo_hypothesis_testing` | Hipotesis nol vs alternatif, p-value, distribusi binomial | Simulasi lemparan koin |
| 06 | `06_final_project_megastore_sales` | Proyek akhir: EDA, cleaning, feature engineering, uji hipotesis | `supermarket_sales.csv` |

### Course 2: Supervised Machine Learning: Regression

| No | Notebook | Topik | Dataset |
|----|----------|-------|---------|
| 01 | `01_lab_transforming_target` | Uji normalitas target; transformasi log, akar kuadrat, Box-Cox; transformasi invers | `boston_housing_clean.pickle` |
| 02 | `02_lab_regression_train_test_split` | One-hot encoding, train-test split, overfitting, scaling | `Ames_Housing_Sales.csv` |
| 03 | `03_demo_cross_validation` | `KFold`, `Pipeline`, `cross_val_predict`, `GridSearchCV` | `boston_housing_clean.pickle` |
| 04 | `04_demo_regularization_gradient_descent` | Ridge, Lasso, ElasticNet, Stochastic Gradient Descent | `X_Y_Sinusoid_Data.csv`, `Ames_Housing_Sales.csv` |
| 05 | `05_lab_regularization` | Standardisasi, Lasso vs Ridge, scaling dengan train/test split | `boston_housing_clean.pickle` |
| 06 | `06_final_assignment_insurance` | Proyek akhir: prediksi biaya asuransi dengan berbagai model regresi | `insurance.csv` |

### Course 3 sampai Course 6

Akan ditambahkan seiring pengerjaan.

## Cara Menjalankan

1. Clone repositori ini:

   ```bash
   git clone https://github.com/ramadhankukuh/data-mining.git
   cd data-mining
   ```

2. Buat environment dan pasang library yang dibutuhkan:

   ```bash
   python -m venv .venv
   source .venv/bin/activate        # Windows: .venv\Scripts\activate
   pip install pandas numpy scipy matplotlib seaborn scikit-learn jupyter
   ```

3. Masuk ke folder kursus lalu buka Jupyter:

   ```bash
   cd Course-1        # atau Course-2, dst.
   jupyter notebook
   ```

Catatan: kode lama dari materi asli sudah disesuaikan agar berjalan di versi library terbaru (pandas, numpy, dan scikit-learn). Pada Course 2, `helper.py` membaca data Boston dari `data/boston_housing_clean.pickle`, karena `load_boston` sudah dihapus dari scikit-learn versi baru.

## Penulis

- Nama: _Kukuh Ramadhan Prastiyo_
- NIM: _A11.2024.15680_
- Program Studi: Informatika, Universitas Dian Nuswantoro
- GitHub: [@ramadhankukuh](https://github.com/ramadhankukuh)

## Sumber dan Atribusi

Materi lab dan dataset berasal dari kursus **IBM Machine Learning Professional Certificate** di Coursera (© IBM Corporation). Struktur awal repositori ini bersumber dari repositori [AI-MOO/IBM-Machine-Learning-Professional-Certificate](https://github.com/AI-MOO/IBM-Machine-Learning-Professional-Certificate), lalu disesuaikan untuk keperluan tugas kuliah (struktur folder, penamaan file, penjelasan dalam bahasa Indonesia, catatan belajar, dan perbaikan kompatibilitas kode).

Repositori ini hanya digunakan untuk tujuan pembelajaran.
