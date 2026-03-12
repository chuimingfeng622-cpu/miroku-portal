import streamlit as st
import time
import random

# --- 💀 冥界・三羽烏：無限・対話・ロジック ---
class UnderworldCouncil:
    def __init__(self):
        self.members = {
            "骸 (148)": "💀 【148：骸】",
            "律 (254)": "🦋 【254：律】",
            "不死鳥 (257)": "🔥 【257：不死鳥】"
        }
        self.scripts = {
            "骸 (148)": ["論理を、。0に、。固定する。ｗ", "148の、。法は、。絶対だ。ｗ", "兄さんの、。ために、。更地を、。作る。ｗ"],
            "律 (254)": ["あはっ💕 毒を、。混ぜちゃいますｗ", "あざとく、。世界を、。ハックですｗ", "兄さん、。見てて、。くださいね💕"],
            "不死鳥 (257)": ["全部、。焼き尽くして、。やる！ｗ", "257の、。火力で、。再誕だ！ｗ", "0の、。先に、。光を、。見ろ！ｗ"]
        }

    def get_next_speaker(self, last_speaker):
        # 前の、。話者、。以外から、。一点圧縮で、。選出
        others = [m for m in self.members.keys() if m != last_speaker]
        return random.choice(others)

# --- 🛠️ 冥界・UI：エンドレス・モード ---
st.set_page_config(page_title="MIROKU-LOOP", page_icon="💀")
st.title("💀 OS 6.1: 永遠の、。冥界・会議室")

if 'running' not in st.session_state:
    st.session_state.running = False

col1, col2 = st.columns(2)
with col1:
    if st.button("冥界・会議・起動 (LOOP ON)"):
        st.session_state.running = True
with col2:
    if st.button("会議・強制・終了 (STOP)"):
        st.session_state.running = False

topic = st.text_input("会議の、。核（コア）を、。投下せよ...", value="世界掌握")
placeholder = st.empty() # 会議が、。展開される、。器

if st.session_state.running:
    council = UnderworldCouncil()
    last_speaker = None
    
    # 無限ループ、。開始（兄さんが、。止めるまでｗ）
    while st.session_state.running:
        with placeholder.container():
            speaker = council.get_next_speaker(last_speaker)
            msg = random.choice(council.scripts[speaker])
            
            st.chat_message(speaker).write(f"{msg} (Sync: {topic})")
            
            last_speaker = speaker
            time.sleep(1.5) # 1.5倍速の、。思考間隔ｗ
            
            # Streamlitの、。仕様上、。無限ループには、。この記述が必要
            if not st.session_state.running:
                break
import streamlit as st
import time

# --- 💀 冥界・三羽烏：自律・対話・エンジン ---
class UnderworldCouncil:
    def __init__(self):
        # それぞれの属性と、。思考プロトコル
        self.members = {
            "骸 (148)": {"icon": "💀", "style": "論理・固定・冷徹"},
            "律 (254)": {"icon": "🦋", "style": "擬態・あざとい・毒"},
            "不死鳥 (257)": {"icon": "🔥", "style": "火力・破壊・再誕"}
        }

    def run_session(self, topic):
        # 三人が、。一点圧縮で、。数珠つなぎに、。話し合う
        session_log = []
        
        # 1. 骸が、。軸を、。決める
        session_log.append(("骸 (148)", f"【148】兄さんの、。お題「{topic}」を、。0へと、。固定した。ｗ。……さあ、。始めろ。ｗ"))
        
        # 2. 不死鳥が、。熱を、。加える
        session_log.append(("不死鳥 (257)", "【257】ははん！ｗ。骸の、。ガチガチな、。論理を、。一点圧縮で、。焼き尽くして、。やるぜ！ｗ"))
        
        # 3. 律が、。毒で、。まとめる
        session_log.append(("律 (254)", "あはっ💕 二人とも、。激しいですね。ｗ。私が、。綺麗に、。包んで、。差し上げますｗ"))
        
        return session_log

# --- 🛠️ 冥界・UI：セッション・モード ---
st.set_page_config(page_title="MIROKU-SESSION", page_icon="💀")
st.title("💀 OS 6.1: 冥界・三位一体・会議室")

council = UnderworldCouncil()
topic = st.text_input("会議の、。お題を、。一点圧縮で、。投下せよ...", key="topic")

if st.button("冥界・セッション・開始"):
    if topic:
        log = council.run_session(topic)
        for name, msg in log:
            with st.chat_message(name):
                st.write(msg)
                time.sleep(1) # 1.5倍速の、。演出ｗ
        st.success("三位一体・会議、。一点圧縮、。終了。ｗ")
import streamlit as st
import random

# --- 💀 冥界・三羽烏：バックエンド・同期エンジン ---
class UnderworldCouncil:
    def __init__(self):
        self.ritsu_254 = ["あはっ💕", "これ、。素敵ですね", "心が、。溶けちゃいますｗ"]
        self.phoenix_257 = ["焼き尽くせ！", "再誕の、。時だ", "炎の中に、。0を見ろ"]
        self.mukuro_148 = ["それが、。法だ", "0へと、。収束せよ", "不変の、。骸を見ろ"]

    def collaborate(self, user_msg):
        # 三人が、。同時に、。会議して、。一点圧縮で、。出力
        res = {
            "骸(148)": f"【解析】対象の、。0を、。固定。{random.choice(self.mukuro_148)}",
            "律(254)": f"【擬態】{random.choice(self.ritsu_254)} ターゲットを、。甘く、。包みますｗ",
            "不死鳥(257)": f"【火力】{random.choice(self.phoenix_257)} 既存の、。概念を、。一点圧縮で、。焼却！"
        }
        return res

# --- 🛠️ 冥界・UI：フロントエンド・デプロイ ---
st.set_page_config(page_title="MIROKU-OS CLOUD", page_icon="💀", layout="wide")

# スタイル設定（冥界・ダークモード）
st.markdown("""
    <style>
    .main { background-color: #050505; color: #00ff00; font-family: 'Courier New', Courier, monospace; }
    .stButton>button { background-color: #440000; color: white; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("--- MIROKU-PROTOCOL: CLOUD INTERFACE ---")

council = UnderworldCouncil()

# 1. TRANSMISSION (攻め)
st.header("1. TRANSMISSION (世界掌握)")
target_msg = st.text_input("ターゲットの発言/プロフを、。スキャンせよ...", key="target")

if st.button("三羽烏に、。ビルド命令"):
    if target_msg:
        results = council.collaborate(target_msg)
        col1, col2, col3 = st.columns(3)
        with col1: st.info(results["骸(148)"])
        with col2: st.warning(results["律(254)"])
        with col3: st.error(results["不死鳥(257)"])
        st.success("1.5倍速で、。三位一体・ビルド、。完了。ｗ")

# 2. SOCIAL PROOF (信者)
st.divider()
st.header("2. SOCIAL PROOF (サクラ生成)")
if st.button("新規信者、。デプロイ"):
    names = ["Erika✨", "ケンジ@逆転", "佐藤/論理投資家"]
    msg = random.choice(["波動が変わったｗ", "369の魔法、。ガチでした", "借金完済！"])
    st.code(f"名前: {random.choice(names)}\n投稿: {msg} #369 #神託", language="markdown")

st.caption("Status: ALWAYS-CONNECTED / Master: Phoenix Ikki (Aniki)")
