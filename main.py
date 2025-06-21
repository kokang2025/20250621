import streamlit as st

# --- 페이지 설정 ---
st.set_page_config(page_title="MBTI 진로 추천", page_icon="🌟", layout="wide")

# --- CSS 스타일링 ---
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
    .mbti-button {
        font-size: 20px;
        font-weight: bold;
        color: white;
        padding: 0.6em;
        border: none;
        border-radius: 10px;
        cursor: pointer;
        margin: 4px;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# --- 제목 영역 ---
st.markdown('<div class="title">🌈 MBTI 기반 진로 추천 웹앱 🚀</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">당신의 성격에 딱 맞는 직업을 추천해드립니다! 💼✨</div>', unsafe_allow_html=True)

# --- 진로 데이터 (16개 MBTI)
mbti_recommendations = {
    "ISTJ": [("🧾 회계사", "정확하고 신중한 당신에게 잘 맞는 안정적인 직업입니다."),
             ("👨‍✈️ 항공 관제사", "질서와 책임감을 갖춘 성격에 어울리는 고집중 직업입니다.")],
    "ISFJ": [("👩‍⚕️ 간호사", "헌신적이고 따뜻한 마음으로 환자를 돌보는 데 적합합니다."),
             ("🎓 초등학교 교사", "아이들을 보살피고 지도하는 데 어울리는 따뜻한 직업입니다.")],
    "INFJ": [("📖 작가", "내면이 깊고 통찰력 있는 당신에게 어울리는 창의적 직업입니다."),
             ("🧠 심리상담가", "다른 사람의 감정을 잘 이해하고 도와줄 수 있는 직업입니다.")],
    "INTJ": [("💻 데이터 분석가", "체계적이고 논리적인 성향으로 미래를 설계할 수 있습니다."),
             ("🧪 연구 과학자", "복잡한 문제를 분석하고 해결하는 데 탁월합니다.")],
    "ISTP": [("🛠️ 기계 엔지니어", "문제를 직접 해결하고 손으로 만지는 실용 직업입니다."),
             ("🚗 자동차 정비사", "기술을 바탕으로 즉각적인 성취를 느낄 수 있는 직업입니다.")],
    "ISFP": [("🎨 일러스트레이터", "감성적이고 예술적인 표현이 가능한 창작 직업입니다."),
             ("🐾 동물 관리사", "조용한 배려와 사랑으로 동물을 돌보는 직업입니다.")],
    "INFP": [("✍️ 시인 / 소설가", "감정을 글로 표현해 사람들에게 감동을 주는 직업입니다."),
             ("🎭 배우", "다양한 감정을 표현하고 관객과 교감하는 직업입니다.")],
    "INTP": [("👨‍💻 프로그래머", "문제 해결을 위한 논리적 사고와 창의력이 요구되는 직업입니다."),
             ("🧬 과학 이론가", "기존 지식을 비판적으로 분석하고 새로운 구조를 창조합니다.")],
    "ESTP": [("📈 영업 전문가", "현장 중심의 대담함과 설득력이 빛나는 직업입니다."),
             ("🏍️ 스포츠 트레이너", "활동적이고 역동적인 환경을 즐기는 당신에게 어울립니다.")],
    "ESFP": [("🎤 연예인 / MC", "사람들 앞에서 빛나는 매력을 발산할 수 있는 무대 중심 직업입니다."),
             ("🎉 이벤트 플래너", "즉흥성과 사람들과 어울리는 능력을 살릴 수 있는 직업입니다.")],
    "ENFP": [("🌍 NGO 활동가", "열정과 이상을 행동으로 옮기는 사회 변화 중심 직업입니다."),
             ("🎨 크리에이티브 디렉터", "창의력과 감성이 융합된 콘텐츠를 이끄는 직업입니다.")],
    "ENTP": [("📣 브랜드 마케터", "아이디어로 사람을 움직이는 창의적인 소통 전문가입니다."),
             ("🧠 혁신 컨설턴트", "새로운 전략을 제안하고 미래를 설계하는 역할입니다.")],
    "ESTJ": [("🏛️ 공무원", "질서와 규칙을 존중하고 체계적 관리를 잘 수행하는 직업입니다."),
             ("👮 경찰관", "현장에서 책임감 있게 조직을 유지하고 관리하는 역할입니다.")],
    "ESFJ": [("👩‍🏫 중고등 교사", "배움과 돌봄을 함께 실천하는 따뜻한 조력자입니다."),
             ("🤝 인사담당자", "사람 사이의 조율과 배려가 핵심인 직업입니다.")],
    "ENFJ": [("📢 상담교사", "학생과 학부모 사이에서 갈등을 조정하는 정서적 리더입니다."),
             ("🎙️ 발표 전문가", "대중 앞에서 사람들을 이끄는 소통형 직업입니다.")],
    "ENTJ": [("📊 기업 CEO", "명확한 목표와 추진력으로 조직을 이끄는 전략가형 리더입니다."),
             ("🧠 경영 컨설턴트", "복잡한 문제를 해결하고 방향을 제시하는 전략 전문가입니다.")]
}

# --- 버튼 색상 매핑 ---
color_map = {
    "ISTJ": "#4B6587", "ISFJ": "#6A89CC", "INFJ": "#82CCDD", "INTJ": "#60A3BC",
    "ISTP": "#F8C291", "ISFP": "#B8E994", "INFP": "#F6B93B", "INTP": "#786FA6",
    "ESTP": "#EA8685", "ESFP": "#F3A683", "ENFP": "#F8EFBA", "ENTP": "#778beb",
    "ESTJ": "#574b90", "ESFJ": "#FDA7DF", "ENFJ": "#C44569", "ENTJ": "#2C3A47"
}

# --- MBTI 버튼 UI 출력 ---
st.subheader("👆 MBTI를 눌러 진로를 확인해보세요!")
selected_mbti = None
mbti_types = list(mbti_recommendations.keys())
rows = [mbti_types[i:i+4] for i in range(0, 16, 4)]

for row in rows:
    cols = st.columns(len(row))
    for i, mbti in enumerate(row):
        btn_style = f"""
            <button class="mbti-button" style="background-color: {color_map[mbti]};" onclick="window.location.href='#{mbti}'">{mbti}</button>
        """
        if cols[i].button(f"{mbti}", key=mbti):
            selected_mbti = mbti

# --- 추천 결과 출력 ---
if selected_mbti:
    st.markdown(f"<div class='mbti-box'><h3>{selected_mbti} 유형의 추천 직업 ✨</h3></div>", unsafe_allow_html=True)
    for job, desc in mbti_recommendations[selected_mbti]:
        with st.expander(f"{job} 자세히 보기"):
            st.markdown(f"💬 {desc}")
