const questions = [
    {
        question:"1. Night. You can't sleep and You go to Your kitchen. What drink will You take?",
        a:'1. Coffee. Black and strong.',
        b:'2. Milk. White and cold.',
        c:'3. Tea. Green and fragrant.'
    },
    {
        question:'2. Remember yourself as a child, what kind of fruit would You pick?',
        a:'1. Cherry.',
        b:'2. Banana.',
        c:'3. Orange.'
    },
    {
        question:'3. What color is best for a volkswagen golf car?',
        a:'1. Dark blue.',
        b:'2. Pearl-pink or yellow.',
        c:'3. Bright emerald'
    },
    {
        question:'4. Which book will You take for reading before sleeping?',
        a:'1. Sleepy Hollow. Washington Irving.',
        b:'2. Planet of Apes. Pierre Boulle.',
        c:"3. Herbalist's Encyclopedia."
    },
    {
        question: '5. Which film do You like?',
        a:"1. 'Captain'. Based on the book 'Captain Alatriste'.",
        b:"2. 'John Carter'. Based on the book 'Princess of Mars'.",
        c:"3. 'Apocalypse'. By Mel Gibson."
    },
    {
        question:'6. What is a resort of Your dream?',
        a:'1. Mountains, pine trees, cool snow.',
        b:'2. Sun, see, warm sand.',
        c:'3. Jungle, flowers, exotic birds.'
    },
    {
        question:'7. What is Your favorite pet?',
        a:'1. Dog.',
        b:'2. Cat.',
        c:'3. Parrot.'
    }
];
const results = [
    text = [
        `<div id="quiz-end" class="quiz-end">Prague Cake, Black Forest Cake, Sparta Cake, Chocolate Ice Cream.</div>`,
        `<div id="quiz-end" class="quiz-end">Pigeon Milk Cake, Honey Cake, Cappuccino Cake, Creme Brulee Ice Cream.</div>`,
        `<div id="quiz-end" class="quiz-end">Kyiv Cake, Apples Biscuit, Baklava, Sorbet.</div>`,
    ],
    image = [
        `<div id="quiz-img"><img id="result-img1" src="https://raw.githubusercontent.com/SonirAster/Sweet-Recipes-Book/41a20f04a0f86958b3a03afbfbd79bc6b9f2df8f/quiz1.jpg" /></div>`,
        `<div id="quiz-img"><img id="result-img1" src="https://raw.githubusercontent.com/SonirAster/Sweet-Recipes-Book/41a20f04a0f86958b3a03afbfbd79bc6b9f2df8f/quiz2.jpg"/></div>`,
        `<div id="quiz-img"><img id="result-img1" src="https://raw.githubusercontent.com/SonirAster/Sweet-Recipes-Book/41a20f04a0f86958b3a03afbfbd79bc6b9f2df8f/quiz3.jpg" /></div>`,
    ],
];

const quizBtn = document.getElementById('quiz-btn');
const endBtn = document.getElementById('endQuiz');
const currentQuestion = document.getElementById('question');
const current_a_text = document.getElementById('a_text');
const current_b_text = document.getElementById('b_text');
const current_c_text = document.getElementById('c_text');

quizBtn.addEventListener('click', startQuiz);
endBtn.addEventListener('click', finishQuiz);
current_a_text.addEventListener('click', selectOption);
current_b_text.addEventListener('click', selectOption);
current_c_text.addEventListener('click', selectOption);

let score = 0;
let questionIndex = 0;
let question = questions[questionIndex]['question'];
let option_a = questions[questionIndex]['a'];
let option_b = questions[questionIndex]['b'];
let option_c = questions[questionIndex]['c'];
let result = document.getElementById('quiz-end');
let resultImg = document.getElementById('quiz-img');


function finishQuiz () {
    document.getElementById('dd').style.display = 'block';
    document.getElementById('quiz-result').style.display = 'none';
    document.getElementById('quiz').style.display = 'none';
}
function startQuiz() {
    document.getElementById('dd').style.display = 'none';
    document.getElementById('quiz-result').style.display = 'none';
    document.getElementById('quiz').style.display = 'block';
    loadQuiz(question, option_a, option_b, option_c);
    questionIndex++;
}
function loadQuiz (question, option_a, option_b, option_c) {
    currentQuestion.innerHTML = `<div id='question'>${question}</div>`;
    current_a_text.innerHTML = `<li id='a_text'>${option_a}</li>`
    current_b_text.innerHTML = `<li id='b_text'>${option_b}</li>`
    current_c_text.innerHTML = `<li id='c_text'>${option_c}</li>`
}
function selectOption (optn) {
    if (questionIndex < 6 ){
        option_a = questions[questionIndex]['a'];
        option_b = questions[questionIndex]['b'];
        option_c = questions[questionIndex]['c'];
        question = questions[questionIndex]['question'];
        loadQuiz (question, option_a, option_b, option_c);
        countResult(optn.target);
        questionIndex++;
    } else if (questionIndex = 6) {
        option_a = questions[questionIndex]['a'];
        option_b = questions[questionIndex]['b'];
        option_c = questions[questionIndex]['c'];
        question = questions[questionIndex]['question'];
        loadQuiz (question, option_a, option_b, option_c);
        countResult(optn.target);
        showResult(score);
    }
}
function countResult(el) {
    if (el.innerText.includes('1')) {
        score = score + 1;
    } else if (el.innerText.includes('2')) {
        score = score + 2;
    } else {
        score = score + 3;
    }
}
function showResult (score) {
    document.getElementById('quiz').style.display = 'none';
    document.getElementById('quiz-result').style.display = 'block';
    if (score <= 11) {
        result.innerHTML = results[0][0];
        resultImg.innerHTML = results[1][0];
    } else if (score >= 12 && score <= 16) {
        result.innerHTML =  results[0][1];
        resultImg.innerHTML = results[1][1];
    } else {
        result.innerHTML = results[0][2];
        resultImg.innerHTML = results[1][2];
    }
}