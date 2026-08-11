import steamlit as st

#ส่วนที่ 1 หัวข้อหน้าเว็บ (title สีเเดง)
st.markdown("# :red[🏋️ คำนวณค่าดัชนีมวลกาย   BMI]")
st.write("กรอกข้อมูลน้ำหนักเเละส่วนสูงของคุณ เพื่อเช็คสุขภาพเบื้องต้น")

#ส่วนที่2สร้างช่องรับค่าน้ำหนัก เเละ ส่วนสูง
weight = st.number_input("กรอกน้ำหนักของคุณ (กิโลกรัม):",min_value=1.0, value=1.0)
height_cm = st.number_input("กรอกส่วนสูงของคุณ (เซนติเมตร):", min_value=1.0, value=1.0)

#ส่วนที่ 3 สร้างปุ่มกดคำนวณ
if st.button("คำนวณค่าBMI 🎯"):
    # เเปลงส่วนสูง cm เป็น เมตร เเล้วคำนวณ BMI
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)

      
