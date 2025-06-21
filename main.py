import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI 진로 추천 💼", page_icon="🧠", layout="wide")

st.markdown(
    "<h1 style='text-align: center; color: #6c5ce7;'>💫 MBTI 성격유형별 진로 추천 💫</h1>",
    unsafe_allow_html=True,
)
st.markdown("<hr>", unsafe_allow_html=True)

# MBTI 이모지 매핑
mbti_emojis = {
    "ISTJ": "🧱", "ISFJ": "🛡️", "INFJ": "🔮", "INTJ": "🧠",
    "ISTP": "🔧", "ISFP": "🎨", "INFP": "💖", "INTP": "📘",
    "ESTP": "🏎️", "ESFP": "🎉", "ENFP": "🌈", "ENTP": "🗣️",
    "ESTJ": "📋", "ESFJ": "🤝", "ENFJ": "💡", "ENTJ": "🏆"
}

# 추천 작업과 설명
mbti_jobs = {
    "ISTJ": [("데이터 분석가", "정확하고 신중한 ISTJ는 데이터의 논리적 해석에 강합니다."),
             ("회계사", "정확성과 신뢰를 요하는 회계 업무에 탁월합니다.")],
    "ISFJ": [("간호사", "타인을 돌보는 데 헌신적인 성향이 강합니다."),
             ("사회복지사", "공감능력과 책임감으로 공동체에 기여합니다.")],
    "INFJ": [("상담사", "깊은 통찰력과 직관으로 사람을 이해하고 도울 수 있습니다."),
             ("작가", "풍부한 감성으로 의미 있는 이야기를 창조합니다.")],
    "INTJ": [("AI 엔지니어", "논리적이며 미래지향적인 사고력으로 기술을 이끌 수 있습니다."),
             ("전략기획가", "복잡한 문제 해결에 강한 능력을 발휘합니다.")],
    "ISTP": [("기계 엔지니어", "도구와 시스템을 다루는 데 강한 능력이 있습니다."),
             ("응급구조사", "위기 상황에 침착하고 신속하게 대처합니다.")],
    "ISFP": [("플로리스트", "감각적이고 자연 친화적인 작업에 적합합니다."),
             ("디자이너", "섬세한 미적 감각으로 창의력을 발휘합니다.")],
    "INFP": [("시인", "깊은 감성을 시와 글로 표현할 수 있습니다."),
             ("아동문학가", "아이들의 마음을 따뜻하게 울릴 수 있습니다.")],
    "INTP": [("연구원", "새로운 지식을 탐구하는 데 탁월한 집중력을 발휘합니다."),
             ("이론물리학자", "복잡한 개념을 창의적으로 연결하고 분석합니다.")],
    "ESTP": [("세일즈 전문가", "에너지 넘치고 사람을 설득하는 능력이 뛰어납니다."),
             ("이벤트 플래너", "즉흥적인 대응과 실행력이 요구되는 직무에 적합합니다.")],
    "ESFP": [("MC / 엔터테이너", "주목받는 걸 좋아하고 감정을 잘 표현합니다."),
             ("여행가이드", "활동적이며 사교적이라 여행을 즐겁게 만듭니다.")],
    "ENFP": [("크리에이터", "무한한 아이디어로 대중과 소통합니다."),
             ("광고기획자", "창의적 캠페인과 사람을 연결짓는 능력이 탁월합니다.")],
    "ENTP": [("스타트업 창업가", "도전을 즐기며 변화를 선도하는 성격입니다."),
             ("정치 컨설턴트", "말과 전략으로 판을 바꾸는 데 능숙합니다.")],
    "ESTJ": [("공무원", "정확하고 조직적인 일 처리에 능숙합니다."),
             ("프로젝트 매니저", "실행 중심적이며 효율적인 계획을 세웁니다.")],
    "ESFJ": [("교사", "사람을 좋아하고 공동체 중심의 활동에 잘 어울립니다."),
             ("간호 행정가", "타인 배려와 조직 운영을 동시에 잘 합니다.")],
    "ENFJ": [("리더십 코치", "사람을 동기부여하고 성장하게 합니다."),
             ("사회운동가", "타인을 위한 정의로운 삶을 추구합니다.")],
    "ENTJ": [("CEO", "강한 추진력과 목표지향적 사고로 조직을 이끕니다."),
             ("전략 컨설턴트", "문제 해결과 분석에 강한 전문가입니다.")]
}

# 버튼 색상 스타일 (컬러풀하게!)
button_styles = [
    "background-color: #fd79a8;", "background-color: #a29bfe;", "background-color: #55efc4;",
    "background-color: #ffeaa7;", "background-color: #74b9ff;", "background-color: #fab1a0;",
    "background-color: #81ecec;", "background-color: #e17055;", "background-color: #dfe6e9;",
    "background-color: #6c5ce7;", "background-color: #fdcb6e;", "background-color: #00cec9;",
    "background-color: #e84393;", "background-color: #2d3436;", "background-color: #00b894;",
    "background-color: #636e72;"
]

# MBTI 버튼 그리기
st.markdown("### 👇 아래에서 당신의 MBTI를 선택하세요!")
mbti_list = list(mbti_emojis.keys())
selected_mbti = None

rows = [mbti_list[i:i+4] for i in range(0, len(mbti_list), 4)]

for row in rows:
    cols = st.columns(len(row))
    for i, mbti in enumerate(row):
        style = f"{button_styles[mbti_list.index(mbti)]} color: white; border-radius: 10px; padding: 10px; font-weight: bold;"
        button_label = f"{mbti_emojis[mbti]} {mbti}"
        if cols[i].button(button_label, key=mbti):
            selected_mbti = mbti

# 결과 출력
if selected_mbti:
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align: center; color: #0984e3;'>{mbti_emojis[selected_mbti]} {selected_mbti} 추천 진로</h2>", unsafe_allow_html=True)
    
    for job, description in mbti_jobs[selected_mbti]:
        with st.expander(f"💼 {job}"):
            st.write(description)
