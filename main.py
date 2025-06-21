import streamlit as st

# --- 페이지 설정 ---
st.set_page_config(page_title="MBTI 진로 추천", page_icon="🌟", layout="wide")

# --- CSS 스타일링 추가 ---
st.markdown("""
    <style>
    .title {
        font-size: 48px;
        font-weight: bold;
        color: #5D3FD3;
        text-align: center;
    }
    .subtitle {
        font-size: 24px;
        color: #FF69B4;
        text-align: center;
        margin-bottom: 30px;
    }
    .mbti-box {
        font-size: 20px;
        padding: 1.2em;
        background: #ffffffaa;
        border-radius: 20px;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.1);
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 제목 ---
st.markdown('<div class="title">🌈 MBTI 기반 진로 추천 웹앱 🚀</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">당신의 성격에 딱 맞는 직업을 추천해드립니다! 💼✨</div>', unsafe_allow_html=True)

# --- MBTI 선택 ---
mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

selected_mbti = st.selectbox("당신의 MBTI를 선택하세요 🔍", mbti_types)

# --- 추천 진로 데이터 (직업 + 설명) ---
mbti_recommendations = {
    "IS
