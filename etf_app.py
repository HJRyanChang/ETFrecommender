import pandas as pd

# 샘플 ETF 데이터
etf_data = pd.DataFrame({
    "ETF 이름": [
        "TIGER 미국나스닥100", "KODEX 2차전지산업", "KBSTAR 글로벌AI",
        "KODEX 배당가치", "TIGER 미국S&P500", "KODEX 미국채10년",
        "KODEX 국채10년", "ARIRANG 고배당주", "TIGER 미국달러단기채"
    ],
    "자산군": [
        "해외주식", "국내주식", "글로벌주식",
        "국내주식", "해외주식", "채권",
        "채권", "국내주식", "채권"
    ],
    "주요 섹터": [
        "IT, 테크", "2차전지", "AI, 테크",
        "고배당, 가치주", "지수추종", "미국 국채",
        "국내 국채", "고배당주", "달러채권"
    ],
    "운용보수 (%)": [0.07, 0.45, 0.3, 0.2, 0.09, 0.15, 0.15, 0.25, 0.2],
    "최근 1년 수익률 (%)": [24.5, 33.1, 18.4, 7.2, 19.8, 3.1, 2.8, 9.7, 5.3]
})

# 고객 유형 정의
customer_profiles = {
    "A. 사회초년생": {
        "설명": "성장 잠재력이 높은 섹터에 투자하고자 하는 초기 투자자",
        "추천 ETF": ["TIGER 미국나스닥100", "KODEX 2차전지산업", "KBSTAR 글로벌AI"]
    },
    "B. 40대 안정 추구형": {
        "설명": "위험과 수익 간 균형을 추구하는 중년 직장인",
        "추천 ETF": ["KODEX 배당가치", "TIGER 미국S&P500", "KODEX 미국채10년"]
    },
    "C. 은퇴 준비 시니어": {
        "설명": "보수적 성향과 안정적 수익을 원하는 은퇴 준비자",
        "추천 ETF": ["KODEX 국채10년", "ARIRANG 고배당주", "TIGER 미국달러단기채"]
    }
}

# Streamlit UI (프로토타입)
def run_etf_app():
    import streamlit as st

    st.title("💹 개인 맞춤형 ETF 추천 프로그램")
    st.markdown("당신의 투자 성향에 맞는 ETF 포트폴리오를 추천해드립니다.")

    user_type = st.selectbox("고객 유형을 선택하세요:", list(customer_profiles.keys()))

    if user_type:
        st.subheader(f"[{user_type}] 추천 포트폴리오")
        selected_etfs = customer_profiles[user_type]["추천 ETF"]
        display_df = etf_data[etf_data["ETF 이름"].isin(selected_etfs)].reset_index(drop=True)
        st.dataframe(display_df)

        st.markdown("### 📘 포트폴리오 설명")
        st.markdown(customer_profiles[user_type]["설명"])

if __name__ == "__main__":
    run_etf_app()
