import streamlit as st
import pandas as pd
import altair as alt
import os

# 앱 제목
st.title("🌍 국가별 MBTI 유형 분포 Top 10")

# 데이터 불러오기 함수
@st.cache_data
def load_data(uploaded_file=None):
    file_path = "countriesMBTI_16types.csv"
    
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
    elif uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
    else:
        df = None
    return df

# 파일 확인 및 업로드 옵션
uploaded_file = None
if not os.path.exists("countriesMBTI_16types.csv"):
    uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type="csv")

df = load_data(uploaded_file)

# 데이터가 로드된 경우만 실행
if df is not None:
    # MBTI 유형 목록 (Country 컬럼 제외)
    mbti_types = [col for col in df.columns if col != "Country"]

    # 사용자 선택
    selected_type = st.selectbox("MBTI 유형을 선택하세요:", mbti_types)

    # Top 10 국가 추출
    top10 = df[["Country", selected_type]].sort_values(
        by=selected_type, ascending=False
    ).head(10)

    # Altair 그래프 생성
    chart = (
        alt.Chart(top10)
        .mark_bar()
        .encode(
            x=alt.X(selected_type, title="비율"),
            y=alt.Y("Country", sort="-x", title="국가"),
            tooltip=["Country", selected_type]
        )
        .properties(
            width=600,
            height=400,
            title=f"{selected_type} 비율이 높은 국가 Top 10"
        )
    )

    # 그래프 표시
    st.altair_chart(chart, use_container_width=True)

else:
    st.warning("데이터 파일이 없습니다. CSV 파일을 업로드해주세요.")
