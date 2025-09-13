import streamlit as st
import random
import time

# 페이지 기본 설정
st.set_page_config(page_title="MBTI 공부법 추천기", page_icon="📚", layout="centered")

st.title("🌟 MBTI 유형별 완벽 공부법 추천기 ✨")
st.write("당신의 MBTI를 선택하면, 딱 맞는 공부 비법을 알려드릴게요! 🚀")

# MBTI 유형 리스트
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# MBTI별 공부법 추천 딕셔너리
study_tips = {
    "INTJ": "📑 계획부터 세워야 마음이 편안해요! 체계적인 스케줄러를 만들어 두세요.",
    "INTP": "🤯 아이디어 폭발! 개념을 연결하는 마인드맵으로 공부하면 좋아요.",
    "ENTJ": "💼 목표가 분명해야 동기부여 UP! 큰 그림을 세우고 달려가세요.",
    "ENTP": "🎤 토론이 곧 공부! 친구랑 문제를 두고 논쟁하면 머리에 쏙 들어와요.",
    "INFJ": "🧘‍♀️ 조용하고 깊이 있는 환경에서 몰입하는 공부가 잘 맞아요.",
    "INFP": "🎨 감성 자극 필수! 예쁜 필기, 음악과 함께 공부하면 집중도 UP.",
    "ENFJ": "👥 함께할 때 빛나요! 스터디 그룹 리더가 되어보세요.",
    "ENFP": "🔥 지루하면 금방 포기! 다양한 방식으로 공부 분위기를 바꿔주세요.",
    "ISTJ": "📊 철저한 반복학습! 플래너와 체크리스트는 최고의 무기.",
    "ISFJ": "🤝 친절한 설명가! 남에게 가르쳐주며 공부하면 기억에 오래 남아요.",
    "ESTJ": "📋 규칙적인 루틴으로! 정해진 시간에 맞춰 학습하면 안정감.",
    "ESFJ": "💡 서로 칭찬하며 함께 공부하는 환경에서 실력이 쑥쑥.",
    "ISTP": "🛠️ 직접 손으로 풀고, 문제를 적용하면서 배워야 효과적!",
    "ISFP": "🌿 편안하고 자유로운 공간에서 느긋하게 공부해야 잘 들어와요.",
    "ESTP": "⚡ 스피드 러닝! 짧고 굵게, 현실적인 문제 풀이가 제격.",
    "ESFP": "🎶 음악과 함께, 즐거운 분위기 속에서 해야 집중이 잘 돼요!"
}

# MBTI 선택
user_mbti = st.selectbox("👉 당신의 MBTI를 선택하세요:", mbti_types)

if st.button("✨ 공부법 추천받기 ✨"):
    with st.spinner("당신의 공부 성향을 분석 중... 🔍"):
        time.sleep(1.5)
    st.success("분석 완료! 🎉")
    st.balloons()
    st.markdown(f"### 🧩 {user_mbti}에게 딱 맞는 공부법은?")
    st.info(study_tips[user_mbti])

    # 랜덤 보너스 메시지
    bonus = [
        "🚀 오늘도 성장하는 당신, 멋져요!",
        "💡 작은 습관이 큰 변화를 만듭니다.",
        "🔥 열정은 이미 충분해요, 이제 실천만 남았네요!"
    ]
    st.write(random.choice(bonus))
