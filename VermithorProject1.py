import streamlit as st

# --- Setup halaman ---
st.set_page_config(page_title="Choose Your Profesi", page_icon="🧠", layout="centered")
st.title("🧠 Choose Your Profession")
st.write("Jawab 5 pertanyaan berikut untuk mengetahui profesi yang paling cocok untukmu!")

# --- Logo ---
st.image("logo_utama.png", caption="Logo Quiz", width=200)

# --- Inisialisasi skor ---
score_programmer = 0
score_designer = 0
score_datascientist = 0

# --- Pertanyaan 1 ---
q1 = st.radio(
    "1. Aktivitas mana yang paling kamu sukai?",
    ("Menulis kode atau memecahkan bug", "Menggambar / desain visual", "Menganalisis data & angka")
)
if q1 == "Menulis kode atau memecahkan bug":
    score_programmer += 1
elif q1 == "Menggambar / desain visual":
    score_designer += 1
else:
    score_datascientist += 1

# --- Pertanyaan 2 ---
q2 = st.radio(
    "2. Bagaimana cara kamu memecahkan masalah?",
    ("Dengan logika dan algoritma", "Dengan kreativitas dan ide out-of-the-box", "Dengan mengumpulkan data & membuat kesimpulan")
)
if q2 == "Dengan logika dan algoritma":
    score_programmer += 1
elif q2 == "Dengan kreativitas dan ide out-of-the-box":
    score_designer += 1
else:
    score_datascientist += 1

# --- Pertanyaan 3 ---
q3 = st.radio(
    "3. Tools mana yang paling menarik bagimu?",
    ("Visual Studio Code / IDE", "Figma / Photoshop", "Excel / Python (untuk analisis data)")
)
if q3 == "Visual Studio Code / IDE":
    score_programmer += 1
elif q3 == "Figma / Photoshop":
    score_designer += 1
else:
    score_datascientist += 1

# --- Pertanyaan 4 (BARU) ---
q4 = st.radio(
    "4. Jika diberi proyek baru, apa hal pertama yang kamu lakukan?",
    ("Mencari cara paling efisien untuk mengimplementasi", 
     "Mencari inspirasi visual & membuat konsep desain", 
     "Mengumpulkan data / riset dulu")
)
if q4 == "Mencari cara paling efisien untuk mengimplementasi":
    score_programmer += 1
elif q4 == "Mencari inspirasi visual & membuat konsep desain":
    score_designer += 1
else:
    score_datascientist += 1

# --- Pertanyaan 5 (BARU) ---
q5 = st.radio(
    "5. Apa yang paling memuaskan buatmu?",
    ("Melihat kode berhasil jalan tanpa error", 
     "Melihat desain terlihat keren & dipuji", 
     "Melihat grafik & insight dari data")
)
if q5 == "Melihat kode berhasil jalan tanpa error":
    score_programmer += 1
elif q5 == "Melihat desain terlihat keren & dipuji":
    score_designer += 1
else:
    score_datascientist += 1

# --- Tombol untuk Melihat Hasil ---
if st.button("🔎 Lihat Hasil Kuis"):
    st.subheader("✨ Hasil Kuis Kamu ✨")

    if score_programmer >= score_designer and score_programmer >= score_datascientist:
        st.success("💻 Kamu cocok menjadi **Programmer!**")
        st.write("Kamu suka logika, struktur, dan memecahkan masalah secara sistematis.")
        st.image("programmer.png", width=250)

    elif score_designer >= score_programmer and score_designer >= score_datascientist:
        st.success("🎨 Kamu cocok menjadi **Designer!**")
        st.write("Kamu punya jiwa kreatif dan suka membuat sesuatu yang indah dan fungsional.")
        st.image("designer.png", width=250)

    else:
        st.success("📊 Kamu cocok menjadi **Data Scientist!**")
        st.write("Kamu suka menganalisis data, menemukan pola, dan membuat kesimpulan.")
        st.image("datascientist.png", width=250)

    st.balloons()
