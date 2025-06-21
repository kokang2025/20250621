import streamlit as st

st.set_page_config(page_title="MBTI 진로 추천", layout="wide")

st.markdown(
    """
    <style>
    .mbti-button {
        display: inline-block;
        margin: 10px;
        padding: 20px 30px;
        font-size: 2.5rem;
        font-weight: bold;
        color: white;
        background: linear-gradient(145deg, #6a11cb, #2575fc);
        border: none;
        border-radius: 12px;
        cursor: pointer;
        text-align: center;
        text-decoration: none;
        transition: transform 0.2s;
    }
    .mbti-button:hover {
        transform: scale(1.05);
        background: linear-gradient(145deg, #8e2de2, #4a00e0);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align:center;'>🌟 MBTI 기반 진로 추천 웹앱 🌟</h1>", unsafe_allow_html=True)

mbti_emojis = {
    "ISTJ": "🧱", "ISFJ": "🛡️", "INFJ": "🔮", "INTJ": "🧠",
    "ISTP": "🔧", "ISFP": "🎨", "INFP": "💖", "INTP": "📘",
    "ESTP": "🏎️", "ESFP": "🎉", "ENFP": "🌈", "ENTP": "🗣️",
    "ESTJ": "📋", "ESFJ": "🤝", "ENFJ": "💡", "ENTJ": "🏆"
}

mbti_recommendations = {
    "ISTJ": [("회계사", "정확성과 책임감이 요구되는 직업"),
             ("공무원", "안정적인 환경과 절차 중심의 업무")],
    "ISFJ": [("간호사", "사람을 돕고 헌신하는 직업"),
             ("초등교사", "배려심 깊고 세심한 교육")],
    "INFJ": [("상담가", "깊은 통찰력과 공감 능력"),
             ("작가", "내면의 세계를 글로 표현")],
    "INTJ": [("전략기획가", "장기적인 계획과 분석력"),
             ("연구원", "논리적 사고와 독립적인 탐구")],
    "ISTP": [("기계공학자", "손재주와 문제 해결 능력"),
             ("파일럿", "위기 대응과 집중력")],
    "ISFP": [("디자이너", "감각적이고 예술적인 표현"),
             ("플로리스트", "자연과 감성의 조화")],
    "INFP": [("작가", "창의적이고 감성적인 이야기 전달"),
             ("심리학자", "사람의 마음을 이해하는 직업")],
    "INTP": [("프로그래머", "논리적 문제 해결과 분석"),
             ("철학자", "깊은 사고와 이론 탐구")],
    "ESTP": [("기업가", "모험심과 추진력 있는 창업"),
             ("스턴트맨", "액션과 도전을 즐기는 직업")],
    "ESFP": [("방송인", "사람들과 어울리고 표현하는 직업"),
             ("이벤트 플래너", "즐거운 경험을 만드는 일")],
    "ENFP": [("광고기획자", "아이디어와 창의력의 조화"),
             ("강연가", "열정적으로 사람들에게 영감을")],
    "ENTP": [("발명가", "혁신적 사고와 도전 정신"),
             ("스타트업 CEO", "빠른 결정과 실행력")],
    "ESTJ": [("경영 관리자", "조직을 이끄는 리더십"),
             ("군인", "질서와 체계 중심의 조직생활")],
    "ESFJ": [("사회복지사", "타인을 돕고 공감하는 직업"),
             ("HR매니저", "사람들과의 협력 중심 업무")],
    "ENFJ": [("교사", "타인을 돕고 이끄는 역할"),
             ("리더십 트레이너", "동기를 부여하고 지도")],
    "ENTJ": [("CEO", "목표 달성에 집착하는 리더"),
             ("정치가", "큰 그림을 보고 이끄는 힘")]
}

selected_mbti = None
clicked = st.session_state.get("clicked", None)

for mbti, emoji in mbti_emojis.items():
    col = st.columns(4)[0]  # 한 줄에 1개씩 크게 배치하려면 이 부분 조정
    if st.markdown(
        f"""
        <a href="?mbti={mbti}" class="mbti-button">{emoji} {mbti}</a>
        """, unsafe_allow_html=True):
        clicked = mbti
        st.session_state.clicked = clicked

query_params = st.experimental_get_query_params()
selected_mbti = query_params.get("mbti", [None])[0]

if selected_mbti:
    st.markdown(f"<h2>{mbti_emojis[selected_mbti]} {selected_mbti} 추천 직업</h2>", unsafe_allow_html=True)
    for job, desc in mbti_recommendations[selected_mbti]:
        with st.expander(f"💼 {job}"):
            st.markdown(f"- 설명: {desc}")
