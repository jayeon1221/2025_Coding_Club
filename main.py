import streamlit as st
import time
import base64
from PIL import Image

# ===== 초기 세팅 =====
st.set_page_config(page_title="코딩 동아리: 랜섬웨어를 뚫어라", page_icon="🧩", layout="wide")

# ===== 세션 상태 초기화 =====
if 'start_time' not in st.session_state:
st.session_state.start_time = time.time()
if 'unlocked' not in st.session_state:
st.session_state.unlocked = False

# ===== 타이머 =====
elapsed = time.time() - st.session_state.start_time
remaining = max(0, 300 - int(elapsed)) # 5분 제한

# ===== 우상단에 작게 시간 표시 =====
st.markdown(f"<div style='position:fixed; top:10px; right:20px; color:gray; font-size:14px;'>⏳ {remaining}초 남음</div>", unsafe_allow_html=True)

# ===== 헤더 =====
st.title("🖥️ 코딩 동아리: 랜섬웨어를 뚫어라")
st.markdown("""
- **사건**: 동아리의 컴퓨터가 **랜섬웨어**에 걸렸다! 누군가 해킹해 시스템을 잠궜다.
- **목표**: 퍼즐을 풀어 암호를 복구하고 시스템을 되찾아라.
- 제한 시간은 **5분**!
""")

# ===== 게임 종료 처리 =====
if remaining <= 0:
st.error("⏰ 시간 초과! 시스템은 완전히 잠겼습니다...")
st.stop()

# ===== 방 위치 선택 =====
location = st.selectbox("어디를 조사할까요?", ["노트북", "화이트보드", "책상 서랍", "책장", "쓰레기통"])

# ===== 각 위치 별 오브젝트 반응 =====
if location == "노트북":
st.subheader("💻 노트북")
st.write("노트북에는 최근의 git 커밋 로그가 보인다. 비밀번호에 필요한 숫자가 숨어있다!")
st.code("""
feat: 로그인 기능 추가
fix: 오류 수정
feat: 암호 3
chore: README 업데이트
feat: 암호 9
refactor: UI 개선
feat: 암호 4
feat: 암호 2
""")

elif location == "화이트보드":
st.subheader("🧾 화이트보드")
st.write("화이트보드에 무언가 암호처럼 적혀 있다. base64 형식이다!")
encoded = "U3RyZWFtbGl0IGlzIGZ1bg=="
decoded = base64.b64decode(encoded).decode("utf-8")
with st.expander("👀 디코딩 결과 보기"):
st.code(decoded)

elif location == "책장":
st.subheader("📚 책장")
st.write("책장에 이상한 메모가 꽂혀 있다. 세로로 읽어야 의미가 있는 듯 하다.")
st.code("""
암 디 힌
호 코 트
는 드 는
: : !
""")
st.info("세로로 읽으면...?")

elif location == "책상 서랍":
st.subheader("🔒 책상 서랍")
st.write("자물쇠가 달린 서랍이다. 마지막 4자리 숫자 비밀번호를 입력해야 열 수 있다.")
code_input = st.text_input("비밀번호 입력 (숫자 4자리)", max_chars=4)

if code_input:
if code_input == "3942":
st.success("🎉 정답! 시스템이 복구되었습니다!")
st.balloons()
st.session_state.unlocked = True
else:
st.error("❌ 틀렸습니다. 다시 시도해보세요.")

elif location == "쓰레기통":
st.subheader("🗑️ 쓰레기통")
st.write("버려진 종이조각 안쪽에 QR 코드가 발견되었다!")
try:
image = Image.open("qr_code.png")
st.image(image, caption="QR 코드: 힌트를 담고 있다")
except:
st.warning("⚠️ 'qr_code.png' 파일이 폴더에 없어요. 파일을 추가해 주세요.")
with st.expander("📎 QR 코드 내용 확인"):
st.write("QR 코드에는 '커밋 메시지를 암호 순서대로 조합하라'고 적혀 있다.")

# ===== 성공 시 추가 메시지 =====
if st.session_state.unlocked:
st.markdown("""
### ✅ 복구 완료!
- 랜섬웨어에 감염된 시스템이 복구되었습니다.
- 범인은 아직 밝혀지지 않았지만, 당신의 추리력 덕분에 프로젝트가 살아났습니다.
- 👑 당신은 동아리의 진정한 해커입니다.
""")
