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

# --- 제목 출력 ---
st.markdown('<div class="title">🌈 MBTI 기반 진로 추천 웹앱 🚀</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">당신의 성격에 딱 맞는 직업을 추천해드립니다! 💼✨</div>', unsafe_allow_html=True)

# --- MBTI 선택 박스 ---
mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

selected_mbti = st.selectbox("당신의 MBTI를 선택하세요 🔍", mbti_types)

# --- 추천 진로 데이터 ---
mbti_recommendations = {
    "ISTJ": [
        ("🧾 회계사", "정확한 숫자와 절차에 강한 당신에게 적합한 안정적 전문 직업입니다."),
        ("👨‍✈️ 항공 관제사", "고도의 집중력과 질서를 중시하는 성격에 잘 맞는 직업입니다.")
    ],
    "ISFJ": [
        ("👩‍⚕️ 간호사", "헌신적이고 섬세한 성격으로 환자 돌봄에 강점을 지닌 직업입니다."),
        ("🎓 초등학교 교사", "아이들의 성장을 돕고 보살피는 데 어울리는 따뜻한 직업입니다.")
    ],
    "INFJ": [
        ("📖 작가", "깊은 내면과 창의성을 글로 표현하는 데 적합한 감성 직업입니다."),
        ("🧠 심리상담가", "사람들의 고민을 듣고 해결을 돕는 공감의 전문가입니다.")
    ],
    "INTJ": [
        ("💻 데이터 분석가", "분석력과 체계적인 사고가 필요한 전략적 직업입니다."),
        ("🧪 연구 과학자", "새로운 이론을 정립하고 문제를 해결하는 탐구 직업입니다.")
    ],
    "ISTP": [
        ("🛠️ 기계 엔지니어", "문제를 직접 해결하고 손으로 만지는 실용 직업입니다."),
        ("🚗 자동차 정비사", "기술을 바탕으로 즉각적인 성취를 느낄 수 있는 현장 직업입니다.")
    ],
    "ISFP": [
        ("🎨 일러스트레이터", "감성적이고 예술적인 표현이 가능한 창작 직업입니다."),
        ("🐾 동물 관리사", "조용한 배려와 사랑으로 동물을 돌보는 직업입니다.")
    ],
    "INFP": [
        ("✍️ 시인 / 소설가", "감정을 글로 표현해 사람들에게 감동을 주는 직업입니다."),
        ("🎭 배우", "감정과 상상을 현실에서 표현하는 직업입니다.")
    ],
    "INTP": [
        ("👨‍💻 프로그래머", "문제 해결을 위한 논리적 사고와 창의력이 요구되는 직업입니다."),
        ("🧬 과학 이론가", "기존 지식을 비판적으로 분석하고 새로운 구조를 창조합니다.")
    ],
    "ESTP": [
        ("📈 영업 전문가", "현장 중심의 대담함과 설득력이 빛나는 직업입니다."),
        ("🏍️ 스포츠 트레이너", "활동적이고 역동적인 환경을 즐기는 당신에게 어울립니다.")
    ],
    "ESFP": [
        ("🎤 연예인 / MC", "사람들 앞에서 빛나는 매력을 발산할 수 있는 무대 중심 직업입니다."),
        ("🎉 이벤트 플래너", "즉흥성과 사람들과 어울리는 능력을 살릴 수 있는 직업입니다.")
    ],
    "ENFP": [
        ("🌍 NGO 활동가", "열정과 이상을 행동으로 옮기는 사회 변화 중심 직업입니다."),
        ("🎨 크리에이티브 디렉터", "창의력과 감성이 융합된 콘텐츠를 이끄는 직업입니다.")
    ],
    "ENTP": [
        ("📣 브랜드 마케터", "아이디어로 사람을 움직이는 창의적인 소통 전문가입니다."),
        ("🧠 혁신 컨설턴트", "새로운 전략을 제안하고 미래를 설계하는 역할입니다.")
    ],
    "ESTJ": [
        ("🏛️ 공무원", "질서와 규칙을 존중하고 체계적 관리를 잘 수행하는 직업입니다."),
        ("👮 경찰관", "현장에서 책임감 있게 조직을 유지하고 관리하는 역할입니다.")
    ],
    "ESFJ": [
        ("👩‍🏫 중고등 교사", "배움과 돌봄을 함께 실천하는 따뜻한 조력자입니다."),
        ("🤝 인사담당자", "사람 사이의 조율과 배려가 핵심인 직업입니다.")
    ],
    "ENFJ": [
        ("📢 상담교사", "학생과 학부모 사이에서 갈등을 조정하는 정서적 리더입니다."),
        ("🎙️ 발표 전문가", "대중 앞에서 사람들을 이끄는 소통형 직업입니다.")
    ],
    "ENTJ": [
        ("📊 기업 CEO", "명확한 목표와 추진력으로 조직을 이끄는 전략가형 리더입니다."),
        ("🧠 경영 컨설턴트", "복잡한 문제를 해결하고 방향을 제시하는 전략 전문가입니다.")
    ]
}

# --- 출력 영역 ---
if selected_mbti:
    st.markdown(f"""
    <div class="mbti-box">
        <h3>{selected_mbti} 유형에게 추천되는 진로는? 🎯</h3>
    </div>
    """, unsafe_allow_html=True)

    # 토글(expander)로 직업 설명 출력
    for job, description in mbti_recommendations.get(selected_mbti, []):
        with st.expander(f"{job} 자세히 보기 🔍"):
            st.markdown(f"💬 {description}")
