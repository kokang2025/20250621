import streamlit as st

# --- 페이지 설정 ---
st.set_page_config(page_title="MBTI 진로 추천", page_icon="🌟", layout="wide")

# --- CSS 스타일링 추가 ---
st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #f5f7fa, #c3cfe2);
    }
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

# --- 추천 진로 데이터 ---
mbti_recommendations = {
    "ISTJ": ("🧾 회계사, 👨‍✈️ 항공 관제사", "정확성과 책임감이 중요한 분야가 딱 어울려요!"),
    "ISFJ": ("👩‍⚕️ 간호사, 🎓 교사", "배려심 깊고 성실한 당신에게 딱!"),
    "INFJ": ("📖 작가, 🧠 심리학자", "깊이 있는 통찰력과 이상주의자가 빛나는 분야예요."),
    "INTJ": ("💻 데이터 분석가, 🧪 과학자", "논리적인 분석력과 미래지향적인 분야에서 활약할 수 있어요."),
    "ISTP": ("🛠️ 기술자, 🚗 자동차 정비사", "도전과 해결이 중심이 되는 실용적인 일에 어울려요."),
    "ISFP": ("🎨 예술가, 🐶 동물관리사", "감성적이고 조용한 창의력을 펼칠 수 있어요."),
    "INFP": ("✍️ 시인, 🎭 배우", "세상에 감동을 전할 수 있는 감성 직업이 잘 어울려요."),
    "INTP": ("🧬 연구원, 👨‍💻 프로그래머", "논리와 분석이 중요한 지식 중심 분야가 좋아요."),
    "ESTP": ("📈 세일즈, 🏍️ 스포츠선수", "에너지 넘치고 실전에서 활약하는 일을 잘해요!"),
    "ESFP": ("🎤 엔터테이너, 🎉 이벤트기획자", "사람들과의 만남과 무대가 어울리는 당신!"),
    "ENFP": ("🌍 NGO활동가, 🎨 디자이너", "창의적이고 자유로운 환경에서 빛나요!"),
    "ENTP": ("📣 마케터, 🧠 발명가", "아이디어 폭발! 새로운 걸 만드는 데 적합해요."),
    "ESTJ": ("🏛️ 관리자, 👮 경찰", "체계적이고 리더십이 필요한 역할에 강해요."),
    "ESFJ": ("👩‍🏫 교사, 🤝 인사담당자", "협력과 지원이 필요한 조직에서 빛나요."),
    "ENFJ": ("📢 상담사, 🎙️ 발표자", "사람들을 이끌고 돕는 일에 탁월해요."),
    "ENTJ": ("📊 CEO, 🧠 전략가", "비전을 세우고 이끄는 최고의 리더형!")
}

# --- 추천 출력 ---
if selected_mbti:
    job, comment = mbti_recommendations[selected_mbti]
    st.markdown(f"""
    <div class="mbti-box">
        <h3>{selected_mbti} 유형에게 추천되는 진로는? 🎯</h3>
        <p>💡 <strong>{job}</strong></p>
        <p>💬 <em>{comment}</em></p>
    </div>
    """, unsafe_allow_html=True)
