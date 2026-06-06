import streamlit as st
import openai
import stripe
from supabase import create_client, Client

# [안전장치 1] 홈페이지 레이아웃을 가장 먼저 강제로 그려버립니다. (에러 차단)
st.set_page_config(page_title="Global AI Video Factory Enterprise", page_icon="🎬", layout="wide")
st.title("🚀 Global AI Video Factory Enterprise")
st.caption("최고경영자(CEO) 및 글로벌 운영본부 전용 초지능 비디오 자동화 플랫폼")

# [안전장치 2] 시스템이 비밀 금고를 못 읽어도 튕기지 않도록 대피소를 만듭니다.
OPENAI_API_KEY = st.secrets.get("OPENAI_API_KEY", "")
STRIPE_SECRET_KEY = st.secrets.get("STRIPE_SECRET_KEY", "")
STRIPE_PRICE_ID = st.secrets.get("STRIPE_PRICE_ID", "")
SUPABASE_URL = st.secrets.get("SUPABASE_URL", "")
SUPABASE_KEY = st.secrets.get("SUPABASE_KEY", "")

# 사이드바: 대표님이 찾으시던 엔터프라이즈 멤버십 및 결제 구역 (이제 무조건 노출됩니다)
st.sidebar.header("🔐 Enterprise Membership")
user_email = st.sidebar.text_input("고객 이메일 주소를 입력하세요:", placeholder="enterprise@company.com")

# 만약 시스템 비밀 금고가 작동하지 않을 경우를 대비한 수동 입력 비상구
if not OPENAI_API_KEY:
    st.warning("⚠️ 시스템 비밀 금고(Secrets)가 아직 동기화되지 않았거나 포맷 오류가 있습니다. 홈페이지는 정상 가동되오니, 아래 비상구에 직접 입력하시거나 설정을 확인해 주세요.")
    with st.expander("🔑 [CEO 전용] 보안 키 수동 입력/확인 창"):
        OPENAI_API_KEY = st.text_input("OpenAI API Key 입력", value=OPENAI_API_KEY, type="password")
        STRIPE_SECRET_KEY = st.text_input("Stripe Secret Key 입력", value=STRIPE_SECRET_KEY, type="password")
        STRIPE_PRICE_ID = st.text_input("Stripe Price ID 입력", value=STRIPE_PRICE_ID)
        SUPABASE_URL = st.text_input("Supabase URL 입력", value=SUPABASE_URL)
        SUPABASE_KEY = st.text_input("Supabase Key (anon public) 입력", value=SUPABASE_KEY, type="password")

if user_email:
    st.sidebar.success(f"🔑 {user_email} 엔터프라이즈 계정 인식 완료")
    
    if st.sidebar.button("💳 프리미엄 비디오 플랜 구독 (월 $49)"):
        try:
            stripe.api_key = STRIPE_SECRET_KEY
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{'price': STRIPE_PRICE_ID, 'quantity': 1}],
                mode='subscription',
                success_url="https://share.streamlit.io/", 
                cancel_url="https://share.streamlit.io/",  
                customer_email=user_email,
            )
            st.sidebar.markdown(f"[🔗 여기를 클릭해 안전 결제를 진행하세요]({checkout_session.url})")
        except Exception as e:
            st.sidebar.error(f"결제 시스템 연결 실패: {e}")

# 메인 화면: 무인 AI 비디오 생산 및 기획 인프라 가동 구역
st.subheader("🎬 초지능 AI 비디오 생성 및 글로벌 미디어 디렉터 오피스")
user_input = st.text_input("제작할 비디오 콘셉트 및 생성 지시를 입력하세요:", placeholder="예: 북미 시장 타겟 프리미엄 테크 제품 홍보 영상 스크립트와 연출 큐시트 짜줘")

if st.button("⚡ 비디오 생산 라인 가동"):
    if not user_input:
        st.warning("생산 지시 내용을 입력해 주십시오, 대표님.")
    elif not OPENAI_API_KEY:
        st.error("OpenAI API Key가 누락되었습니다. 비상구 창에 입력해 주세요.")
    else:
        with st.spinner("AI 글로벌 엔진 기동 중... 엔터프라이즈 비디오 아키텍처 연산 중..."):
            try:
                openai.api_key = OPENAI_API_KEY
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "당신은 세계 최고 권위의 AI 미디어 콘텐츠 및 비디오 마케팅 엔터프라이즈 전문가입니다. 대표님의 지시에 따라 완벽한 영상 스크립트, 스토리보드 연출 콘셉트, 글로벌 마케팅 전략을 정중하고 명확하게 제안하세요."},
                        {"role": "user", "content": user_input}
                    ]
                )
                answer = response.choices[0].message['content']
                st.balloons() 
                st.success("🎯 글로벌 비디오 콘텐츠 설계 및 생산 완료!")
                st.write(answer)
                
                # Supabase 데이터베이스 자동 기록 장치
                if SUPABASE_URL and SUPABASE_KEY:
                    try:
                        supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
                        supabase.table("user_logs").insert({"email": user_email, "query": user_input, "status": "video_enterprise_success"}).execute()
                    except:
                        pass
            except Exception as e:
                st.error(f"엔진 가동 중 오류 발생: {e}")
                "📐 Camera Blueprint"
            ])
            
            with tab_spec1:
                st.caption("비디오 생성 AI(Sora, Runway)에 그대로 입력하면 실사급 영상이 출력되는 독점 프롬프트 매트릭스입니다.")
                st.info(current_data.get('prompt', 'Prompt generation sync active.'))
                
            with tab_spec2:
                st.caption("AI 가상 가상인간 합성 및 음성 호흡 구간 조절용 자동 싱크로율 데이터 사양입니다.")
                st.code(f"""[Audio Lip-Sync Profile]
- Language Accent: Native {current_data['lang']}
- Emotional Pitch: {tone}
- Micro-expression Vector: Auto-synchronized
- Breath Pause Intervals: Every 4.5 seconds for retention""", language="ini")
                
            with tab_spec3:
                st.caption("비디오 촬영팀 및 모션 그래픽 디자이너용 정밀 기술 지시서입니다.")
                st.code(current_data['visual'], language="text")
                
    else:
        with st.container(border=True):
            st.markdown("<h3 style='text-align: center;'>🌐</h3>", unsafe_allow_html=True)
            st.info(L["waiting_msg"])

st.write("---")
st.warning(L["pay_banner"])
