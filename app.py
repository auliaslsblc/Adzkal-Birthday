import streamlit as st
import base64
import requests

# --- Kode untuk Memutar Musik dari URL ---
def play_audio_from_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            audio_bytes = response.content
            audio_b64 = base64.b64encode(audio_bytes).decode()
            audio_html = f"""
            <audio autoplay loop>
              <source src="data:audio/mp3;base64,{audio_b64}" type="audio/mp3">
            </audio>
            """
            st.markdown(audio_html, unsafe_allow_html=True)
        else:
            st.error(f"Error: Gagal memuat file audio dari URL. Status Code: {response.status_code}")
    except Exception as e:
        st.error(f"Error: Terjadi kesalahan saat memuat audio. {e}")

# --- Panggil Fungsi Musik ---
# Gunakan URL mentah dari file MP3 di GitHub
audio_url = "https://raw.githubusercontent.com/auliaslsblc/Adzkal-Birthday/5f9c598805b3d77fe5ddfb66cdf48c13c8d4d006/lagu_ulang_tahun.mp3"
play_audio_from_url(audio_url)

# --- Pengaturan Halaman dan Judul ---
st.set_page_config(
    page_title="Happy 22nd Birthday, Askal!",
    page_icon="🎂",
    layout="wide"
)

# --- Kode CSS untuk Background Warna ---
st.markdown(
    """
    <style>
    .stApp {
        background-color: #89CFF0;
    }
    </style>
    """, unsafe_allow_html=True
)

# --- Header Foto di Atas Halaman ---
# Ganti "header_foto.jpg" dengan nama file fotomu
st.image("header_foto.jpg", use_column_width=True)

# --- Judul dan Efek Visual ---
st.title("🎂 Happy 22nd Birthday to My Favorite Person, Askal! 🎂")
st.balloons()
st.subheader("It's so amazing to see you grow and become an even better person everyday. Hope this year brings you so much joy and happiness.")
st.write("---")

# --- Bagian Pesan Pertama ---
st.markdown(
    """
    <div style="font-size: 1.15em; line-height: 1.5; text-align: justify;">
    Life has been tough, but you never gave up.
    <br><br>
    Terima kasih ya sudah berjuang sejauh ini. Thank you for being such an amazing person and for all the little things you do.
    <br><br>
    Semangat yaa sekolah sama kerjanya pasti itu cape banget kan tapi liat diri kamu sekarang, kamu keren! keep up the good work and never stop chasing your dreams ya kal so excited to see all the great things you'll accomplish to the next step hihi&gt;⩊&lt;
    <br><br>
    Always Proud of you ya♡
    </div>
    """, unsafe_allow_html=True
)
st.write("---")

# --- Bagian Pesan Spiritual ---
st.markdown(
    """
    <div style="font-size: 1.15em; line-height: 1.5; text-align: justify;">
    Semoga Allah selalu melindungimu dari hal-hal yang buruk dan semoga hidupmu selalu penuh dengan berkah ya. May God bless you and keep you safe, always.
    <br><br>
    jangan tinggalin solat dan ngajinya yaaaa(˶˃ ᵕ ˂˶)
    </div>
    """, unsafe_allow_html=True
)
st.write("---")

# --- Bagian Pesan Dukungan ---
st.markdown(
    """
    <div style="font-size: 1.15em; line-height: 1.5; text-align: justify;">
    aku tahu belakangan ini kamu lagi banyak hal masalah. mungkin ada saat-saat kamu mau nyerah but I want you to know how proud I am of you. Aku liat semua perjuangan kamu dan semua kerja keras kamu.
    <br><br>
    Remember that it's okay to not be okay. Take a break, breathe, and know that you are not alone. Kamu adalah orang yang luar biasa, dan aku percaya kamu bisa melewati ini semua. Keep your head up, everything will be okay. I'm here for you, always kal♡
    <br><br>
    Thank you for being you, for being my support system, and for loving me ya!
    </div>
    """, unsafe_allow_html=True
)
st.write("---")

# --- Penutup ---
st.markdown(
    """
    <div style="font-size: 1.25em; text-align: center; font-weight: bold;">
    Wishing you a year full of success and happiness. Stay awesome!
    </div>
    """, unsafe_allow_html=True
)
st.write("---")

# --- Galeri Foto Kenangan ---
st.subheader("our memories ꉂ(˵˃ ᗜ ˂˵)")
st.caption("semoga kita bisa berjumpa di real life ya jangan virtual mulu hahah ૮₍ ˶ᵔ ᵕ ᵔ˶ ₎ა")

col1, col2, col3 = st.columns(3)
with col1:
    # Ganti dengan nama file fotomu 
    st.image("https://github.com/auliaslsblc/Adzkal-Birthday/blob/71b704114fae6d339269bec60fd686af9a17ce33/foto_kita_1.JPG")
with col2:
    st.image("https://github.com/auliaslsblc/Adzkal-Birthday/blob/71b704114fae6d339269bec60fd686af9a17ce33/foto_kita_2.JPG")
with col3:
    st.image("https://github.com/auliaslsblc/Adzkal-Birthday/blob/71b704114fae6d339269bec60fd686af9a17ce33/foto_kita_3.jpg")
    
# --- Tanda Tangan ---
st.write("---")
st.markdown(
    """
    <div style="font-size: 1.25em; text-align: right; font-weight: bold;">
    miss you askal<br>
    love you, always
    </div>
    """, unsafe_allow_html=True
)

st.markdown(
    """
    <div style="font-size: 1.5em; text-align: right; font-weight: bold;">
    aul,
    </div>
    """, unsafe_allow_html=True
)

st.markdown(
    """
    <div style="font-size: 1.5em; text-align: right; font-weight: bold;">
    your beloved ˵ •̀ ᴗ - ˵ )
    </div>
    """, unsafe_allow_html=True
)
