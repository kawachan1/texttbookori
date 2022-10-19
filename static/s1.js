"use strict";

// クリックかタップか判定
const eventType = window.ontouchstart !== null ? "click" : "touchstart";
const numbersArr = [
  1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
];
const number = document.querySelectorAll(".number");
const startBtn = document.querySelector(".startBtn");
startBtn.addEventListener(eventType, start);
const endBtn = document.getElementById("endBtn");
endBtn.addEventListener(eventType, () => {
  location.reload();
});
const time = document.getElementById("time");

let count = 1;

let startTime;
let timeoutId;

// 数字をシャッフル
function shuffle(array) {
  // Fisher–Yates shuffleアルゴリズムでシャッフル
  let a = array.length;
  while (a) {
    let j = Math.floor(Math.random() * a);
    let t = array[--a];
    array[a] = array[j];
    array[j] = t;
  }
  return array;
}

// ストップウォッチ
function timer() {
  const d = new Date(Date.now() - startTime);
  const s = String(d.getSeconds()).padStart(3, "0");
  const ms = String(d.getMilliseconds()).padStart(3, "0");
  time.textContent = `${s}.${ms}`;
  timeoutId = setTimeout(() => {
    timer();
  }, 10);
}

// スタートボタンが押された時の処理
function start() {
  count = 1;
  number.forEach((value) => {
    value.className = "number";
  });
  startBtn.removeEventListener(eventType, start);
  startBtn.className = "next";
  startBtn.textContent = `Next ${count}`;
  startTime = Date.now();
  timer();
  const shuffleNumber = shuffle(numbersArr);
  number.forEach((value, index) => {
    value.textContent = shuffleNumber[index];
    value.addEventListener(eventType, clickNumber);
  });
}

// 数字がタッチされた時の処理
function clickNumber() {
  if (Number(this.textContent) === count) {
    number.forEach((value) => {
      value.className = "number";
    });
    this.className = "touched";
    count++;
    startBtn.textContent = `Next ${count}`;
    if (count > 20) {
      end();
      return;
    }
  }
}

// ゲーム終了
function end() {
  startBtn.textContent = `測定開始`;
  startBtn.className = "startBtn";
  startBtn.addEventListener(eventType, start);
  clearTimeout(timeoutId);
}
