import streamlit as st
import pandas as pd
import plotly.express as px

# ==============================
# CONFIG PAGE
# ==============================
st.set_page_config(
    page_title="Dashboard Kuesioner",
    layout="wide"
)

st.title("📊 Dashboard Visualisasi Data Kuesioner")

# ==============================
# UPLOAD FILE
# ==============================
uploaded_file = st.file_uploader(
    "Upload File CSV Kuesioner",
    type=["csv"]
)

if uploaded_file is not None:

    # Baca data
    df = pd.read_csv(uploaded_file)

    # Ambil hanya kolom numerik (agar aman)
    df = df.select_dtypes(include="number")

    st.subheader("Preview Data")
    st.dataframe(df.head())

    # ==============================
    # 1️⃣ DISTRIBUSI KESELURUHAN
    # ==============================
    st.subheader("1️⃣ Distribusi Jawaban Keseluruhan")

    all_values = df.to_numpy().flatten()
    distribusi = pd.Series(all_values).value_counts().sort_index()

    fig1 = px.bar(
        x=distribusi.index,
        y=distribusi.values,
        labels={"x": "Skor Jawaban", "y": "Jumlah"},
        title="Distribusi Jawaban Keseluruhan"
    )

    st.plotly_chart(fig1, use_container_width=True)

    # ==============================
    # 2️⃣ PIE CHART PROPORSI
    # ==============================
    st.subheader("2️⃣ Proporsi Jawaban Keseluruhan")

    fig2 = px.pie(
        values=distribusi.values,
        names=distribusi.index,
        title="Proporsi Jawaban"
    )

    st.plotly_chart(fig2, use_container_width=True)

    # ==============================
    # 3️⃣ STACKED BAR PER PERTANYAAN
    # ==============================
    st.subheader("3️⃣ Distribusi Jawaban per Pertanyaan")

    df_melt = df.melt(
        var_name="Pertanyaan",
        value_name="Skor"
    )

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
        title="Distribusi Jawaban per Pertanyaan",
        barmode="stack"
    )

    st.plotly_chart(fig3, use_container_width=True)

    # ==============================
    # 4️⃣ RATA-RATA SKOR
    # ==============================
    st.subheader("4️⃣ Rata-rata Skor per Pertanyaan")

    rata_rata = df.mean().reset_index()
    rata_rata.columns = ["Pertanyaan", "Rata-rata"]

    fig4 = px.bar(
        rata_rata,
        x="Pertanyaan",
        y="Rata-rata",
        text="Rata-rata",
        title="Rata-rata Skor per Pertanyaan"
    )

    fig4.update_traces(
        texttemplate="%{text:.2f}",
        textposition="outside"
    )

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

    kategori_series = pd.Series(all_values).apply(kategori)
    kategori_count = kategori_series.value_counts()

    fig5 = px.bar(
        x=kategori_count.index,
        y=kategori_count.values,
        labels={"x": "Kategori", "y": "Jumlah"},
        title="Distribusi Positif, Netral, Negatif"
    )

    st.plotly_chart(fig5, use_container_width=True)

else:
    st.info("Silakan upload file CSV untuk menampilkan dashboard.")
