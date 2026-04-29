# Air Quality Dashboard ✨

## Aotizhongxin Station, Beijing (2013–2017)

---

## Deskripsi Proyek

Proyek ini merupakan submission akhir dari materi analisis data.
Proyek ini melakukan analisis mendalam terhadap data kualitas udara dari stasiun pemantau
Aotizhongxin, Beijing, untuk menjawab dua pertanyaan bisnis utama terkait pola polusi PM2.5
dan pengaruh kondisi cuaca terhadap kualitas udara.

---

## Pertanyaan Bisnis

1. Bagaimana tren rata-rata tingkat polusi PM2.5 secara bulanan selama periode observasi (2013–2017), dan pada bulan apa saja kualitas udara biasanya mencapai titik terburuk?
2. Bagaimana pengaruh kondisi cuaca, khususnya curah hujan (RAIN) dan kecepatan angin (WSPM), terhadap fluktuasi konsentrasi PM2.5 di udara selama periode 2013–2017?

---

## Struktur Proyek

```
submission
├───dashboard
│   ├───main_data.csv
│   └───dashboard.py
├───data
│   └───PRSA_Data_Aotizhongxin_20130301-20170228.csv
├───notebook.ipynb
├───README.md
├───requirements.txt
└───url.txt
```

---

## Setup Environment - Anaconda

```
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

## Setup Environment - Shell/Terminal

```
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

---

## Run Streamlit App

```
cd dashboard
streamlit run dashboard.py
```

Dashboard akan otomatis terbuka di browser pada `http://localhost:8501`

---

## Dataset

- **Sumber:** [PRSA Data - Beijing Multi-Site Air Quality](https://github.com/marceloreis/HTI)
- **Stasiun:** Aotizhongxin
- **Periode:** 1 Maret 2013 – 28 Februari 2017
- **Jumlah Data:** 35.064 baris, 18 kolom

---

## Hasil Analisis

- Polusi PM2.5 mencapai puncaknya di bulan **Desember** dan terendah di bulan **Agustus**
- **Kecepatan angin (WSPM)** adalah faktor cuaca paling berpengaruh dalam menurunkan konsentrasi PM2.5 (korelasi: -0.275)
- **Curah hujan (RAIN)** hampir tidak berpengaruh secara signifikan (korelasi: -0.013)

---

## Author

- **Nama:** Sultan Abdul Fatah
- **Email:** sultan.fatahhh@gmail.com
- **ID Dicoding:** sultvnnnn
