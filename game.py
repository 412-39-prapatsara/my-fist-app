import streamlit as st

st.set_page_config(page_title="เกมทายคำศัพท์หมวดอาหารไทย", page_icon="🥘")

# ข้อมูลคำถาม
QUESTIONS = [
    {
        "hint": "🐷🌿🔥 หมู + ใบเขียว + พริก + กระทะไฟแรง = ?",
        "answers": ["ผัดกะเพรา", "กะเพรา"],
        "display": "ผัดกะเพรา",
    },
    {
        "hint": "🍜🥜🦐🍋 เส้น + ถั่ว + กุ้ง + มะนาว = ?",
        "answers": ["ผัดไทย"],
        "display": "ผัดไทย",
    },
    {
        "hint": "🦐🌶️🍋🔥 กุ้ง + พริก + มะนาว + น้ำซุปร้อนๆ = ?",
        "answers": ["ต้มยำกุ้ง"],
        "display": "ต้มยำกุ้ง",
    },
    {
        "hint": "🥒🌶️🥜🦀 ผักกรอบๆ + พริก + ถั่ว + ของทะเล = ?",
        "answers": ["ส้มตำ"],
        "display": "ส้มตำ",
    },
    {
        "hint": "🍗🥥🌿🌶️ ไก่ + กะทิ + เครื่องแกง + ใบหอมๆ = ?",
        "answers": ["แกงเขียวหวาน", "แกงเขียวหวานไก่"],
        "display": "แกงเขียวหวาน",
    },
    {
        "hint": "🍖🥔🥥🧅 เนื้อนุ่ม + มันฝรั่ง + กะทิ + หอมใหญ่ + เครื่องเทศ = ?",
        "answers": ["มัสมั่นไก่", "มัสมั่นเนื้อ", "มัสมั่น"],
        "display": "มัสมั่นไก่/เนื้อ",
    },
    {
        "hint": "🍗🧂🔥 ไก่ + น้ำปลา + ทอดจนกรอบ = ?",
        "answers": ["ไก่ทอด"],
        "display": "ไก่ทอด",
    },
    {
        "hint": "🍚🐔🥒🥣 ข้าวมันๆ + ไก่นุ่ม + แตงกวา + น้ำจิ้ม = ?",
        "answers": ["ข้าวมันไก่"],
        "display": "ข้าวมันไก่",
    },
    {
        "hint": "🐷🔥🥩🌶️ หมูส่วนมันๆ + ย่างไฟ + น้ำจิ้มแจ่ว = ?",
        "answers": ["คอหมูย่าง"],
        "display": "คอหมูย่าง",
    },
    {
        "hint": "🦐🧄🌶️🧂 กุ้ง + กระเทียมเยอะๆ + พริก + รสเค็มๆ = ?",
        "answers": ["กุ้งผัดพริกเกลือ"],
        "display": "กุ้งผัดพริกเกลือ",
    },
    {
        "hint": "🥚🐷🧂🍳 ไข่ฟูๆ + หมูสับ + ทอดในน้ำมัน = ?",
        "answers": ["ไข่เจียวหมูสับ"],
        "display": "ไข่เจียวหมูสับ",
    },
    {
        "hint": "🐷🥚🍚🥬 หมูตุ๋นนุ่มๆ + ไข่ + ข้าวสวย + ผักดอง = ?",
        "answers": ["ข้าวขาหมู"],
        "display": "ข้าวขาหมู",
    },
]

# กำหนด Session State สำหรับบันทึกสถานะเกม
if "current_q" not in st.session_state:
    st.session_state.current_q = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "finished" not in st.session_state:
    st.session_state.finished = False

st.title("🎉 เกมทายคำศัพท์หมวดอาหารไทย 🥘")

# เมื่อจบเกมแล้ว
if st.session_state.finished:
    score = st.session_state.score
    st.subheader(f"🎯 คะแนนรวม: {score}/{len(QUESTIONS)} คะแนน")

    if score == 12:
        st.balloons()
        st.success("🏆 ระดับยอดเยี่ยม!")
    elif 6 <= score <= 11:
        st.info("👍 ระดับดี")
    elif 1 <= score <= 5:
        st.warning("✌️ พยายามอีกนิด")
    else:
        st.error("💀 แพ้")

    if st.button("🔄 เล่นใหม่อีกครั้ง"):
        st.session_state.current_q = 0
        st.session_state.score = 0
        st.session_state.finished = False
        st.rerun()

# ขณะกำลังเล่นเกม
else:
    q_idx = st.session_state.current_q
    q_data = QUESTIONS[q_idx]

    st.write(f"### ข้อที่ {q_idx + 1} / {len(QUESTIONS)}")
    st.info(f"คำใบ้: {q_data['hint']}")

    user_ans = st.text_input(
        "พิมพ์คำตอบของคุณ:", key=f"input_{q_idx}"
    ).strip()

    if st.button("ส่งคำตอบ"):
        clean_user_ans = user_ans.replace(" ", "")
        valid_answers = [a.replace(" ", "") for a in q_data["answers"]]

        if clean_user_ans in valid_answers:
            st.success("✅ ถูกต้องครับ/ค่ะ!")
            st.session_state.score += 1
        else:
            st.error(f"❌ ผิดครับ/ค่ะ! คำตอบคือ: {q_data['display']}")

        # ไปยังข้อถัดไป
        if q_idx + 1 < len(QUESTIONS):
            st.session_state.current_q += 1
        else:
            st.session_state.finished = True

        st.rerun()
