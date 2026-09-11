<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>เกมทายคำศัพท์หมวดอาหาร 🍜</title>

<style>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: Arial, Tahoma, sans-serif;
}

body {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
  background: linear-gradient(135deg, #fff3cd, #ffccbc);
  color: #4e342e;
}

.container {
  width: 100%;
  max-width: 700px;
  background: white;
  padding: 30px;
  border-radius: 25px;
  box-shadow: 0 15px 40px rgba(0,0,0,0.15);
}

h1 {
  text-align: center;
  color: #e65100;
  margin-bottom: 10px;
}

.subtitle {
  text-align: center;
  margin-bottom: 25px;
  color: #795548;
}

.score-box {
  display: flex;
  justify-content: space-between;
  background: #fff8e1;
  padding: 15px;
  border-radius: 15px;
  margin-bottom: 15px;
  font-weight: bold;
}

.progress {
  width: 100%;
  height: 10px;
  background: #eee;
  border-radius: 10px;
  overflow: hidden;
  margin-bottom: 25px;
}

.progress-bar {
  height: 100%;
  width: 0%;
  background: linear-gradient(90deg, #ff9800, #f44336);
  transition: 0.3s;
}

.question {
  background: #fffaf5;
  border: 2px solid #ffcc80;
  border-radius: 20px;
  padding: 25px;
}

.question h2 {
  text-align: center;
  color: #bf360c;
  margin-bottom: 15px;
}

.hint {
  text-align: center;
  font-size: 25px;
  line-height: 1.7;
  margin-bottom: 20px;
}

input {
  width: 100%;
  padding: 15px;
  border: 2px solid #ffcc80;
  border-radius: 12px;
  font-size: 18px;
  text-align: center;
  outline: none;
  margin-bottom: 15px;
}

input:focus {
  border-color: #ff9800;
}

button {
  width: 100%;
  padding: 14px;
  border: none;
  border-radius: 12px;
  color: white;
  font-size: 18px;
  font-weight: bold;
  cursor: pointer;
}

.check {
  background: #ff9800;
}

.next {
  background: #43a047;
  display: none;
  margin-top: 10px;
}

.result {
  text-align: center;
  font-size: 19px;
  font-weight: bold;
  margin-top: 15px;
  min-height: 25px;
}

.correct {
  color: #2e7d32;
}

.wrong {
  color: #d32f2f;
}

.final {
  display: none;
  text-align: center;
  background: #fff8e1;
  padding: 25px;
  border-radius: 20px;
}

.final h2 {
  color: #e65100;
  margin-bottom: 15px;
}

.final-score {
  font-size: 50px;
  font-weight: bold;
  color: #2e7d32;
  margin: 15px;
}

.level {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
}

.restart {
  background: #e91e63;
}

.answers {
  text-align: left;
  background: white;
  padding: 15px;
  border-radius: 12px;
  margin-bottom: 20px;
}

.answers p {
  margin: 8px 0;
}

@media (max-width: 600px) {
  .container {
    padding: 20px;
  }

  h1 {
    font-size: 26px;
  }

  .hint {
    font-size: 21px;
  }
}
</style>
</head>

<body>

<div class="container">

  <div id="game">

    <h1>🍜 เกมทายคำศัพท์หมวดอาหาร 🍛</h1>
    <p class="subtitle">อ่านคำใบ้ แล้วทายชื่ออาหารให้ถูกต้อง!</p>

    <div class="score-box">
      <span>ข้อ <span id="number">1</span> / 12</span>
      <span>คะแนน: <span id="score">0</span></span>
    </div>

    <div class="progress">
      <div class="progress-bar" id="progress"></div>
    </div>

    <div class="question">

      <h2>💡 คำใบ้</h2>

      <div class="hint" id="hint"></div>

      <input
        type="text"
        id="answer"
        placeholder="พิมพ์คำตอบ..."
        autocomplete="off"
      >

      <button class="check" id="check" onclick="checkAnswer()">
        ตรวจคำตอบ ✅
      </button>

      <div class="result" id="result"></div>

      <button class="next" id="next" onclick="nextQuestion()">
        ข้อถัดไป ➡️
      </button>

    </div>

  </div>


  <div class="final" id="final">

    <h2>🎉 จบเกม!</h2>

    <p>คุณได้คะแนน</p>

    <div class="final-score">
      <span id="finalScore">0</span> / 12
    </div>

    <div class="level" id="level"></div>

    <div class="answers">
      <h3>🍽️ เฉลย</h3>
      <div id="answerList"></div>
    </div>

    <button class="restart" onclick="restart()">
      🔄 เล่นอีกครั้ง
    </button>

  </div>

</div>


<script>

const questions = [

  {
    hint: "🐷🌿🔥 หมู + ใบเขียว + พริก + กระทะไฟแรง = ?",
    answer: "ผัดกะเพรา"
  },

  {
    hint: "🍜🥜🦐🍋 เส้น + ถั่ว + กุ้ง + มะนาว = ?",
    answer: "ผัดไทย"
  },

  {
    hint: "🦐🌶️🍋🔥 กุ้ง + พริก + มะนาว + น้ำซุปร้อนๆ = ?",
    answer: "ต้มยำกุ้ง"
  },

  {
    hint: "🥒🌶️🥜🦀 ผักกรอบๆ + พริก + ถั่ว + ของทะเล = ?",
    answer: "ส้มตำ"
  },

  {
    hint: "🍗🥥🌿🌶️ ไก่ + กะทิ + เครื่องแกง + ใบหอมๆ = ?",
    answer: "แกงเขียวหวาน"
  },

  {
    hint: "🍖🥔🥥🧅 เนื้อนุ่ม + มันฝรั่ง + กะทิ + หอมใหญ่ + เครื่องเทศ = ?",
    answer: "มัสมั่นไก่/เนื้อ"
  },

  {
    hint: "🍗🧂🔥 ไก่ + น้ำปลา + ทอดจนกรอบ = ?",
    answer: "ไก่ทอด"
  },

  {
    hint: "🍚🐔🥒🥣 ข้าวมันๆ + ไก่นุ่ม + แตงกวา + น้ำจิ้ม = ?",
    answer: "ข้าวมันไก่"
  },

  {
    hint: "🐷🔥🥩🌶️ หมูส่วนมันๆ + ย่างไฟ + น้ำจิ้มแจ่ว = ?",
    answer: "คอหมูย่าง"
  },

  {
    hint: "🦐🧄🌶️🧂 กุ้ง + กระเทียมเยอะๆ + พริก + รสเค็มๆ = ?",
    answer: "กุ้งผัดพริกเกลือ"
  },

  {
    hint: "🥚🐷🧂🍳 ไข่ฟูๆ + หมูสับ + ทอดในน้ำมัน = ?",
    answer: "ไข่เจียวหมูสับ"
  },

  {
    hint: "🐷🥚🍚🥬 หมูตุ๋นนุ่มๆ + ไข่ + ข้าวสวย + ผักดอง = ?",
    answer: "ข้าวขาหมู"
  }

];


let current = 0;
let score = 0;
let answered = false;


function loadQuestion() {

  document.getElementById("number").textContent = current + 1;

  document.getElementById("hint").textContent =
    questions[current].hint;

  document.getElementById("answer").value = "";

  document.getElementById("answer").disabled = false;

  document.getElementById("check").style.display = "block";

  document.getElementById("next").style.display = "none";

  document.getElementById("result").textContent = "";

  document.getElementById("result").className = "result";

  document.getElementById("progress").style.width =
    ((current + 1) / questions.length * 100) + "%";

  answered = false;

  document.getElementById("answer").focus();
}


function checkAnswer() {

  if (answered) return;

  const input = document
    .getElementById("answer")
    .value
    .trim()
    .replace(/\s/g, "");

  const correct = questions[current]
    .answer
    .replace(/\s/g, "");

  const result = document.getElementById("result");

  if (input === "") {

    result.textContent = "⚠️ กรุณาพิมพ์คำตอบก่อน";

    result.className = "result wrong";

    return;
  }


  answered = true;

  document.getElementById("answer").disabled = true;

  document.getElementById("check").style.display = "none";

  document.getElementById("next").style.display = "block";


  if (
    input === correct ||
    (current === 5 &&
      (input === "มัสมั่นไก่" ||
       input === "มัสมั่นเนื้อ" ||
       input === "แกงมัสมั่น")) ||
    (current === 6 &&
      input.includes("ไก่ทอด")) ||
    (current === 0 &&
      input === "ผัดกระเพรา")
  ) {

    score++;

    document.getElementById("score").textContent = score;

    result.textContent = "🎉 ถูกต้อง! +1 คะแนน";

    result.className = "result correct";

  } else {

    result.textContent =
      "❌ ไม่ถูกต้อง คำตอบคือ " + questions[current].answer;

    result.className = "result wrong";
  }
}


function nextQuestion() {

  current++;

  if (current < questions.length) {

    loadQuestion();

  } else {

    showFinal();
  }
}


function showFinal() {

  document.getElementById("game").style.display = "none";

  document.getElementById("final").style.display = "block";

  document.getElementById("finalScore").textContent = score;


  let level = document.getElementById("level");


  if (score === 12) {

    level.textContent = "🏆 ระดับยอดเยี่ยม";
    level.style.color = "#2e7d32";

  } else if (score >= 6) {

    level.textContent = "👍 ระดับดี";
    level.style.color = "#1976d2";

  } else if (score >= 1) {

    level.textContent = "💪 พยายามอีกนิด";
    level.style.color = "#f57c00";

  } else {

    level.textContent = "😢 แพ้";
    level.style.color = "#d32f2f";
  }


  const list = document.getElementById("answerList");

  list.innerHTML = "";

  questions.forEach((q, i) => {

    list.innerHTML +=
      `<p><strong>${i + 1}.</strong> ${q.answer}</p>`;

  });
}


function restart() {

  current = 0;

  score = 0;

  document.getElementById("score").textContent = "0";

  document.getElementById("game").style.display = "block";

  document.getElementById("final").style.display = "none";

  loadQuestion();
}


document.getElementById("answer")
.addEventListener("keydown", function(event) {

  if (event.key === "Enter") {

    if (!answered) {

      checkAnswer();

    } else {

      nextQuestion();

    }

  }

});


loadQuestion();

</script>

</body>
</html>
