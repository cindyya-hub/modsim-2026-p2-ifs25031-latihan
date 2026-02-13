import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# ==============================
# CONFIG PAGE
# ==============================
st.set_page_config(
    page_title="Dashboard Kuesioner",
    layout="wide"
)

st.title("📊 Dashboard Visualisasi Data Kuesioner")

# ==============================
# UPLOAD FILE (EXCEL)
# ==============================
uploaded_file = st.file_uploader(
    "Upload File Excel Kuesioner",
    type=["xlsx"]
)

if uploaded_file is not None:

    df = pd.read_excel(uploaded_file)

    # Ambil hanya kolom pertanyaan (Q1–Q17)
    df_pertanyaan = df.iloc[:, 1:]

    st.subheader("Preview Data")
    st.dataframe(df.head())

    # ==============================
    # Mapping Skala ke Angka
    # ==============================
    mapping = {
        "STS": 1,
        "TS": 2,
        "CS": 3,
        "S": 4,
        "SS": 5
    }

    df_numeric = df_pertanyaan.replace(mapping)

    # Paksa semua jadi numeric
    df_numeric = df_numeric.apply(pd.to_numeric, errors='coerce')

    # ==============================
    # 1️⃣ DISTRIBUSI KESELURUHAN
    # ==============================
    st.subheader("1️⃣ Distribusi Jawaban Keseluruhan")

    all_values = df_numeric.to_numpy().flatten()

    # Bersihkan data
    series = pd.to_numeric(pd.Series(all_values), errors='coerce')
    series = series.dropna().astype(int)

    distribusi = series.value_counts().sort_index()

    fig1 = px.bar(
        x=distribusi.index.astype(str),
        y=distribusi.values,
        labels={"x": "Skor Jawaban", "y": "Jumlah"},
        title="Distribusi Jawaban Keseluruhan",
        height=400
    )

    st.plotly_chart(fig1, use_container_width=True)

    # ==============================
    # 2️⃣ PIE CHART
    # ==============================
    st.subheader("2️⃣ Proporsi Jawaban")

    fig2 = px.pie(
        values=distribusi.values,
        names=distribusi.index.astype(str),
        title="Proporsi Jawaban",
        height=400
    )

    st.plotly_chart(fig2, use_container_width=True)

    # ==============================
    # 3️⃣ STACKED BAR PER PERTANYAAN
    # ==============================
    st.subheader("3️⃣ Distribusi Jawaban per Pertanyaan")

    df_melt = df_numeric.melt(
        var_name="Pertanyaan",
        value_name="Skor"
    )

    df_melt = df_melt.dropna()
    df_melt["Skor"] = df_melt["Skor"].astype(int)

    distribusi_per_pertanyaan = (
        df_melt.groupby(["Pertanyaan", "Skor"])
        .size()
        .reset_index(name="Jumlah")
    )

    fig3 = px.bar(
        distribusi_per_pertanyaan,
        x="Pertanyaan",
        y="Jumlah",
        color="Skor",
        barmode="stack",
        height=500,
        title="Distribusi Jawaban per Pertanyaan"
    )

    fig3.update_layout(xaxis_tickangle=-45)

    st.plotly_chart(fig3, use_container_width=True)

    # ==============================
    # 4️⃣ RATA-RATA SKOR
    # ==============================
    st.subheader("4️⃣ Rata-rata Skor per Pertanyaan")

    rata_rata = df_numeric.mean().reset_index()
    rata_rata.columns = ["Pertanyaan", "Rata-rata"]

    fig4 = px.bar(
        rata_rata,
        x="Pertanyaan",
        y="Rata-rata",
        text="Rata-rata",
        height=500,
        title="Rata-rata Skor per Pertanyaan"
    )

    fig4.update_traces(
        texttemplate="%{text:.2f}",
        textposition="outside"
    )

    fig4.update_layout(xaxis_tickangle=-45)

    st.plotly_chart(fig4, use_container_width=True)

    # ==============================
    # 5️⃣ POSITIF / NETRAL / NEGATIF
    # ==============================
    st.subheader("5️⃣ Distribusi Kategori Jawaban")

    def kategori(skor):
        if skor >= 4:
            return "Positif"
        elif skor == 3:
            return "Netral"
        else:
            return "Negatif"

    kategori_series = series.apply(kategori)
    kategori_count = kategori_series.value_counts()

    fig5 = px.bar(
        x=kategori_count.index,
        y=kategori_count.values,
        labels={"x": "Kategori", "y": "Jumlah"},
        height=400,
        title="Distribusi Positif, Netral, Negatif"
    )

    st.plotly_chart(fig5, use_container_width=True)

else:
    st.info("Silakan upload file Excel (.xlsx)")