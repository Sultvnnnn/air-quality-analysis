import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Air Quality Dashboard",
    page_icon=":cloud:",
    layout="wide"
)

st.title("💨 Air Quality Dashboard")
st.markdown("**Stasiun Aotizhongxin, Beijing | 2013–2017**")
st.divider()

@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/marceloreis/HTI/master/PRSA_Data_20130301-20170228/PRSA_Data_Aotizhongxin_20130301-20170228.csv"
    df = pd.read_csv(url)

    numeric_cols = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'TEMP', 'PRES', 'DEWP', 'RAIN', 'WSPM']
    for col in numeric_cols:
        df[col] = df[col].interpolate(method='linear', limit_direction='both')
    df['wd'] = df['wd'].ffill().bfill()
    
    return df

df = load_data()

# SIDEBAR
st.sidebar.header("Filter Data")

# filter bulan
selected_months = st.sidebar.multiselect(
    label="Pilih Bulan",
    options=list(range(1, 13)),
    default=list(range(1, 13)),
    format_func=lambda x: ["Jan","Feb","Mar","Apr","Mei","Jun","Jul","Agu","Sep","Okt","Nov","Des"][x-1]
)

# filter tahun
selected_years = st.sidebar.multiselect(
    label="Pilih Tahun",
    options=sorted(df['year'].unique()),
    default=sorted(df['year'].unique())
)

# terapkan filter ke dataframe
filtered_df = df[df['month'].isin(selected_months) & df['year'].isin(selected_years)]

st.sidebar.markdown(f"**Total data:** {len(filtered_df):,} baris")

# METRIC CARDS
st.subheader("📊 Ringkasan Statistik")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    label="Rata-rata PM2.5",
    value=f"{filtered_df['PM2.5'].mean():.1f}",
    delta="µg/m³"
)
col2.metric(
    label="PM2.5 Tertinggi",
    value=f"{filtered_df['PM2.5'].max():.1f}",
    delta="µg/m³"
)
col3.metric(
    label="Rata-rata Kec. Angin",
    value=f"{filtered_df['WSPM'].mean():.1f}",
    delta="m/s"
)
col4.metric(
    label="Rata-rata Curah Hujan",
    value=f"{filtered_df['RAIN'].mean():.2f}",
    delta="mm"
)

st.divider()

# VISUALISASI
# pertanyaan pertama
st.subheader("📈 Tren Rata-rata PM2.5 per Bulan")

monthly_pm25 = filtered_df.groupby('month')['PM2.5'].mean().reset_index()
month_labels = ["Jan","Feb","Mar","Apr","Mei","Jun","Jul","Agu","Sep","Okt","Nov","Des"]
monthly_pm25['month_name'] = monthly_pm25['month'].apply(lambda x: month_labels[x-1])

fig1, ax1 = plt.subplots(figsize=(10, 5))
sns.lineplot(
    x='month_name', y='PM2.5',
    data=monthly_pm25,
    marker='o', linewidth=2.5, color='firebrick', ax=ax1
)
ax1.set_title('Rata-rata Tingkat Polusi PM2.5 per Bulan\n(Stasiun Aotizhongxin)', fontsize=14, fontweight='bold')
ax1.set_xlabel('Bulan', fontsize=12)
ax1.set_ylabel('Rata-rata Konsentrasi PM2.5 (µg/m³)', fontsize=12)
ax1.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

st.pyplot(fig1)
st.caption("Kualitas udara cenderung memburuk di akhir tahun (puncak: Desember) dan terbaik di pertengahan tahun (Agustus).")

st.divider()

# pertanyaan kedua
st.subheader("🌤️ Pengaruh Cuaca terhadap PM2.5")

fig2, axes = plt.subplots(1, 2, figsize=(14, 5))

sns.scatterplot(x='WSPM', y='PM2.5', data=filtered_df, alpha=0.2, color='teal', ax=axes[0])
axes[0].set_title('Kecepatan Angin vs PM2.5', fontsize=13, fontweight='bold')
axes[0].set_xlabel('Kecepatan Angin (m/s)', fontsize=11)
axes[0].set_ylabel('Konsentrasi PM2.5', fontsize=11)

sns.scatterplot(x='RAIN', y='PM2.5', data=filtered_df, alpha=0.2, color='royalblue', ax=axes[1])
axes[1].set_title('Curah Hujan vs PM2.5', fontsize=13, fontweight='bold')
axes[1].set_xlabel('Curah Hujan (mm)', fontsize=11)
axes[1].set_ylabel('Konsentrasi PM2.5', fontsize=11)

plt.tight_layout()
st.pyplot(fig2)
st.caption("Angin kencang terbukti menurunkan PM2.5. Curah hujan berkorelasi sangat lemah terhadap polusi.")

st.divider()

# heatmap korelasi
st.subheader("🔥 Heatmap Korelasi Antar Variabel")

corr_cols = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'TEMP', 'RAIN', 'WSPM']
corr_matrix = filtered_df[corr_cols].corr()

fig3, ax3 = plt.subplots(figsize=(10, 7))
sns.heatmap(
    corr_matrix,
    annot=True, fmt=".2f",
    cmap='coolwarm', center=0,
    square=True, linewidths=0.5,
    ax=ax3
)
ax3.set_title('Matriks Korelasi Variabel Kualitas Udara & Cuaca', fontsize=13, fontweight='bold')
plt.tight_layout()

st.pyplot(fig3)
st.caption("Nilai mendekati 1 atau -1 menunjukkan korelasi kuat. Mendekati 0 berarti tidak ada korelasi signifikan.")