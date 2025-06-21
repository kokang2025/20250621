import streamlit as st

st.set_page_config(page_title="MBTI 직업 추천", layout="wide")

st.markdown("<h1 style='text-align: center; color: #FF69B4;'>🌟 MBTI 기반 진로 추천 사이트 🌈</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>당신의 MBTI를 선택하면, 찰떡같은 직업을 추천해줄게요! 👀✨</h4>", unsafe_allow_html=True)
st.markdown("---")

mbti_emojis = {
    "ISTJ": "🧱",
    "ISFJ": "🛡️",
    "INFJ": "🔮",
    "INTJ": "🧠",
    "ISTP": "🔧",
    "ISFP": "🎨",
    "INFP": "💖",
    "INTP": "📘",
    "ESTP": "🏎️",
    "ESFP": "🎉",
    "ENFP": "🌈",
    "ENTP": "🗣️",
    "ESTJ": "📋",
    "ESFJ": "🤝",
    "ENFJ": "💡",
    "ENTJ": "🏆"
}

mbti_jobs = {
    "ISTJ": ["회계사", "공무원", "데이터 분석가"],
    "ISFJ": ["간호사", "교사", "사회복지사"],
    "INFJ": ["상담가", "심리학자", "작가"],
    "INTJ": ["전략기획가", "공학자", "정책분석가"],
    "ISTP": ["기술자", "파일럿", "응급구조사"],
    "ISFP": ["예술가", "디자이너", "요리사"],
    "INFP": ["시인", "사회운동가", "상담사"],
    "INTP": ["이론 물리학자", "연구원", "프로그래머"],
    "ESTP": ["기업가", "스턴트맨", "판매 전문가"],
    "ESFP": ["연예인", "이벤트 플래너", "헤어디자이너"],
    "ENFP": ["마케팅 전문가", "작가", "기획자"],
    "ENTP": ["발명가", "변호사", "기업가"],
    "ESTJ": ["경영 관리자", "군인", "감독관"],
    "ESFJ": ["간호사", "초등교사", "HR 담당자"],
    "ENFJ": ["리더십 코치", "강사", "정치인"],
    "ENTJ": ["CEO", "변호사", "전략 컨설턴트"]
}

mbti_descriptions = {
    "ISTJ": "신중하고 책임감 있는 성격으로, 명확한 규칙과 질서를 선호해요.",
    "ISFJ": "배려심이 많고 조용한 헌신형, 실용적이고 꼼꼼한 성격이에요.",
    "INFJ": "통찰력 있고 깊이 있는 사고를 지닌 이상주의자예요.",
    "INTJ": "전략적이고 독립적인 사고를 가진 분석가예요.",
    "ISTP": "논리적이고 유연한 문제 해결 능력을 가진 기술자예요.",
    "ISFP": "감성적이고 예술적 재능이 많은 자유로운 영혼이에요.",
    "INFP": "감성적이고 이상주의적이며 공감 능력이 뛰어나요.",
    "INTP": "호기심 많고 아이디어를 탐구하는 사색가예요.",
    "ESTP": "에너지 넘치고 실용적이며 현실적인 성격이에요.",
    "ESFP": "사교적이고 밝은 분위기를 좋아하는 엔터테이너예요.",
    "ENFP": "열정적이고 창의적인 아이디어 뱅크예요.",
    "ENTP": "재치 있고 논쟁을 즐기는 혁신가예요.",
    "ESTJ": "체계적이고 리더십이 뛰어난 관리자예요.",
    "ESFJ": "사람들을 돌보는 것을 즐기는 따뜻한 리더예요.",
    "ENFJ": "사람들에게 영감을 주고자 하는 카리스마 있는 인도자예요.",
    "ENTJ": "결단력 있고 실행력이 강한 리더형이에요."
}

colors = [
    "#FFDAB9", "#E6E6FA", "#FFFACD", "#D1F2EB",
    "#FADBD8", "#D6EAF8", "#F9E79F", "#E8DAEF",
    "#D5F5E3", "#FDEDEC", "#EBDEF0", "#F6DDCC",
    "#AED6F1", "#F5CBA7", "#F1948A", "#A3E4D7"
]

selected_mbti = None
rows = [list(mbti_emojis.keys())[i:i+4] for i in range(0, 16, 4)]

for r, row in enumerate(rows):
    cols = st.columns(4)
    for i, mbti in enumerate(row):
        button_label = f"<span style='font-size: 28px;'>{mbti_emojis[mbti]} <b>{mbti}</b></span>"
        if cols[i].button(mbti, key=f"{mbti}_button"):
            selected_mbti = mbti
        cols[i].markdown(button_label, unsafe_allow_html=True)

st.markdown("---")

if selected_mbti:
    st.markdown(f"<h2 style='color: #FF1493;'>{mbti_emojis[selected_mbti]} {selected_mbti} 추천 직업 ✨</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:18px;'>{mbti_descriptions[selected_mbti]}</p>", unsafe_allow_html=True)

    for job in mbti_jobs[selected_mbti]:
        with st.expander(f"💼 {job}"):
            st.write(f"{job}에 대한 자세한 설명을 여기에 적을 수 있어요. 직업의 성격, 환경, 필요한 역량 등을 추가하세요.")
