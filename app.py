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
audio_url = "https://raw.githubusercontent.com/auliaslsblc/Adzkal-Birthday/5f9c598805b3d77fe5ddfb66cdf48c13c8d4d006/lagu_ulang_tahun.mp3"
play_audio_from_url(audio_url)

# --- Pengaturan Halaman dan Judul ---
st.set_page_config(
    page_title="Happy 22nd Birthday, Askal!",
    page_icon="🎂",
    layout="wide"
)

# --- Kode CSS untuk Video Background ---
video_url_background = "https://raw.githubusercontent.com/auliaslsblc/Adzkal-Birthday/84c131c30bdb06552690625b3daa7d52e3b552eb/video_background.mp4" # URL VIDEO BACKGROUND KAMU
st.markdown(
    f"""
    <style>
    .stApp {{
        position: relative;
    }}
    .video-background {{
        position: fixed;
        right: 0;
        bottom: 0;
        min-width: 100%;
        min-height: 100%;
        width: auto;
        height: auto;
        z-index: -100;
        background-color: #89CFF0; /* Warna fallback jika video gagal */
        opacity: 0.8; /* Opsional: Atur transparansi video agar teks lebih jelas */
    }}
    /* Pastikan konten Streamlit berada di atas video */
    .stApp > header, .stApp > div {{
        z-index: 0;
        position: relative;
    }}
    </style>
    <video playsinline autoplay muted loop class="video-background">
        <source src="{video_url_background}" type="video/mp4">
        Your browser does not support the video tag.
    </video>
    """, unsafe_allow_html=True
    )
# --- Header Foto di Atas Halaman ---
st.image("https://raw.githubusercontent.com/auliaslsblc/Adzkal-Birthday/main/header_foto.jpg", use_container_width=True)
# --- Judul dan Efek Visual ---
st.title("🎂 Happy 22nd Birthday Askalierrr! 🎉")
st.balloons()
st.subheader("It's so amazing to see you grow and become an even better person everyday. Hope this year brings you so much joy and happiness.")
st.write("---")

# --- Bagian Pesan Pertama ---
st.markdown(
    """
    <div style="font-size: 1.15em; line-height: 1.5; text-align: justify;">
    Life has been tough, but you never gave up.
    <br><br>
    Terima kasih ya sudah berjuang sampai sejauh ini. Thank you for being such an amazing person and for all the little things you do.
    <br><br>
    Semangat yaa sekolah sama kerjanya pasti itu cape banget kan tapi coba deh liat diri kamu yang sekarang, kamu keren! keep up the good work and never stop chasing your dreams ya kal so excited to see all the great things you'll accomplish to the next step hihi&gt;⩊&lt;
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
    Semoga Allah selalu melindungi kamu dari hal-hal yang buruk dan semoga hidup kamu selalu penuh dengan berkah ya. May God bless you and keep you safe, always.
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
    aku tahu belakangan ini kamu pasti lagi banyak masalah. mungkin ada saat-saat kamu pengen nyerah but I want you to know how proud I am of you. Aku liat semua perjuangan kamu dari awal sampai sekarang dan semua kerja keras kamu.
    <br><br>
    Remember that it's okay to not be okay. Take a break, breathe, and know that you are not alone. Kamu adalah orang yang luar biasa tau kal, dan aku percaya kamu bisa melewati ini semua. Keep your head up, everything will be okay. I'm here for you, always kal♡
    semoga aku selalu bisa nemenin step by step dalam hidup kamu ya!>ᴗ<
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
    semoga kamu suka sama kado yang aku berikan dan love letter website ini ya!
    </div>
    """, unsafe_allow_html=True
)
st.write("---")

# --- Galeri Foto Kenangan ---
st.subheader("our memories ꉂ(˵˃ ᗜ ˂˵)")
st.caption("semoga kita bisa berjumpa di real life ya jangan virtual mulu hahah ૮₍ ˶ᵔ ᵕ ᵔ˶ ₎ა")

col1, col2, col3 = st.columns(3)
with col1:
    st.image("https://raw.githubusercontent.com/auliaslsblc/Adzkal-Birthday/main/foto_kita_1.jpg")
with col2:
    st.image("https://raw.githubusercontent.com/auliaslsblc/Adzkal-Birthday/main/foto_kita_2.jpg")
with col3:
    st.image("https://raw.githubusercontent.com/auliaslsblc/Adzkal-Birthday/main/foto_kita_3.jpg")
    
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
    aulia,
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
