// examEngine.js - Digital SAT 2026 Test Engine & Interactive Bluebook State Machine
import { calculateSectionScore, analyzePerformance } from '../data/scoring.js';
import { Storage } from './storage.js';
import { Calculator } from './calculator.js';
import { ReferenceSheet } from './referenceSheet.js';

export const ExamEngine = {
  test: null,
  sectionId: "rw", // "rw" or "math"
  moduleIndex: 0, // 0 for Module 1, 1 for Module 2
  questionIndex: 0, // 0 to 26
  mode: "timed", // "timed" or "practice"

  userAnswers: {},
  flagged: new Set(),
  eliminated: new Set(), // set of `${qId}_${letter}`

  timerSeconds: 0,
  timerInterval: null,
  timerHidden: false,
  hasWarned5Min: false,

  isEliminatorActive: false,

  init(testData, mode = "timed") {
    this.test = testData;
    this.mode = mode;
    this.sectionId = "rw";
    this.moduleIndex = 0;
    this.questionIndex = 0;
    this.userAnswers = {};
    this.flagged = new Set();
    this.eliminated = new Set();
    this.hasWarned5Min = false;

    this.startModuleTimer();
    this.renderCurrentQuestion();
  },

  getCurrentModule() {
    return this.test.sections[this.sectionId].modules[this.moduleIndex];
  },

  getCurrentQuestion() {
    return this.getCurrentModule().questions[this.questionIndex];
  },

  startModuleTimer() {
    if (this.timerInterval) clearInterval(this.timerInterval);
    const mod = this.getCurrentModule();
    this.timerSeconds = mod.timeLimitSeconds;
    this.hasWarned5Min = false;

    this.updateTimerDisplay();

    this.timerInterval = setInterval(() => {
      this.timerSeconds--;
      this.updateTimerDisplay();

      // 5-minute warning
      if (this.timerSeconds === 300 && !this.hasWarned5Min) {
        this.hasWarned5Min = true;
        this.showToastWarning("5 minutes remaining in this module.");
      }

      if (this.timerSeconds <= 0) {
        clearInterval(this.timerInterval);
        this.handleTimeExpired();
      }
    }, 1000);
  },

  updateTimerDisplay() {
    const timerText = document.getElementById("timer-display-text");
    if (!timerText) return;

    if (this.timerHidden) {
      timerText.textContent = "Timer";
      return;
    }

    const mins = Math.floor(this.timerSeconds / 60);
    const secs = this.timerSeconds % 60;
    timerText.textContent = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
  },

  toggleTimerVisibility() {
    this.timerHidden = !this.timerHidden;
    const btn = document.getElementById("btn-toggle-timer");
    if (btn) btn.textContent = this.timerHidden ? "Show" : "Hide";
    this.updateTimerDisplay();
  },

  renderCurrentQuestion() {
    const q = this.getCurrentQuestion();
    const mod = this.getCurrentModule();
    const totalInMod = mod.questions.length;
    const currentNum = this.questionIndex + 1;
    const qKey = `${this.sectionId}_${q.id}`;

    // Update Header
    const sectionTitle = document.getElementById("exam-header-section-title");
    if (sectionTitle) {
      const secName = this.sectionId === "rw" ? "Reading and Writing" : "Math";
      sectionTitle.textContent = `Section ${this.sectionId === "rw" ? "1" : "2"}: ${secName} — Module ${this.moduleIndex + 1}`;
    }

    // Toggle Math Tools
    const btnCalc = document.getElementById("btn-header-calc");
    const btnRef = document.getElementById("btn-header-ref");
    if (btnCalc) btnCalc.style.display = "inline-flex"; // Always available or primarily in math
    if (btnRef) btnRef.style.display = this.sectionId === "math" ? "inline-flex" : "none";

    // Mark for Review Checkbox
    const flagBtn = document.getElementById("btn-mark-review");
    const isFlagged = this.flagged.has(qKey);
    if (flagBtn) {
      flagBtn.classList.toggle("flagged", isFlagged);
      flagBtn.innerHTML = `
        <svg width="16" height="16" viewBox="0 0 24 24" fill="${isFlagged ? '#e11d48' : 'none'}" stroke="currentColor" stroke-width="2">
          <path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"/>
          <line x1="4" y1="22" x2="4" y2="15"/>
        </svg>
        <span>${isFlagged ? "Flagged for Review" : "Mark for Review"}</span>
      `;
    }

    // Update Bottom Navigation text
    const qCountBadge = document.getElementById("footer-question-count");
    if (qCountBadge) {
      qCountBadge.textContent = `Question ${currentNum} of ${totalInMod}`;
    }

    const btnBack = document.getElementById("btn-nav-back");
    if (btnBack) {
      btnBack.disabled = this.questionIndex === 0;
    }

    const btnNext = document.getElementById("btn-nav-next");
    if (btnNext) {
      btnNext.textContent = this.questionIndex === totalInMod - 1 ? "Review Module" : "Next";
    }

    // Render Question Content
    const examBody = document.getElementById("exam-body-content");
    if (!examBody) return;

    const isRW = this.sectionId === "rw";
    const selectedAnswer = this.userAnswers[qKey];

    let contentHtml = "";

    if (isRW) {
      // Split Layout for Reading and Writing
      contentHtml = `
      <div class="exam-split-layout">
        <!-- Left Pane: Stimulus -->
        <div class="exam-pane exam-left-pane">
          <div class="pane-header">
            <span class="pane-tag">${q.subdomain || "Passage"}</span>
            <span class="pane-difficulty badge-${(q.difficulty || 'Medium').toLowerCase()}">${q.difficulty || 'Medium'}</span>
          </div>
          <div class="pane-body stimulus-text" id="stimulus-container">
            ${q.stimulus}
          </div>
        </div>

        <!-- Right Pane: Prompt and Options -->
        <div class="exam-pane exam-right-pane">
          <div class="question-number-header">
            <span class="q-badge">${currentNum}</span>
            ${q.domain ? `<span class="q-domain-label">${q.domain}</span>` : ""}
          </div>
          <div class="question-prompt-text">
            ${q.prompt}
          </div>

          <div class="question-choices-list">
            ${q.choices.map(c => {
              const isSelected = selectedAnswer === c.letter;
              const isEliminated = this.eliminated.has(`${q.id}_${c.letter}`);
              return `
              <div class="choice-row ${isSelected ? 'selected' : ''} ${isEliminated ? 'eliminated' : ''}" data-letter="${c.letter}">
                <button class="choice-letter-btn" aria-label="Select option ${c.letter}">${c.letter}</button>
                <div class="choice-text-content">${c.text}</div>
                <button class="choice-eliminate-btn" title="Eliminate option ${c.letter}" data-eliminate="${c.letter}" aria-label="Eliminate option ${c.letter}">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <line x1="18" y1="6" x2="6" y2="18"/>
                    <line x1="6" y1="6" x2="18" y2="18"/>
                  </svg>
                </button>
              </div>
              `;
            }).join("")}
          </div>

          ${this.mode === "practice" ? this.renderPracticeExplanation(q) : ""}
        </div>
      </div>
      `;
    } else {
      // Centered or Clean Split Layout for Math
      contentHtml = `
      <div class="exam-math-layout ${q.stimulus ? 'has-stimulus' : ''}">
        ${q.stimulus ? `
          <div class="math-stimulus-pane">
            <div class="pane-header">
              <span class="pane-tag">${q.subdomain || "Problem Context"}</span>
              <span class="pane-difficulty badge-${(q.difficulty || 'Medium').toLowerCase()}">${q.difficulty || 'Medium'}</span>
            </div>
            <div class="stimulus-text">${q.stimulus}</div>
          </div>
        ` : ""}

        <div class="math-question-pane">
          <div class="question-number-header">
            <span class="q-badge">${currentNum}</span>
            ${q.domain ? `<span class="q-domain-label">${q.domain}</span>` : ""}
            ${!q.stimulus ? `<span class="pane-difficulty badge-${(q.difficulty || 'Medium').toLowerCase()}">${q.difficulty || 'Medium'}</span>` : ""}
          </div>
          <div class="question-prompt-text math-prompt">
            ${q.prompt}
          </div>

          ${q.type === "mcq" ? `
            <div class="question-choices-list">
              ${q.choices.map(c => {
                const isSelected = selectedAnswer === c.letter;
                const isEliminated = this.eliminated.has(`${q.id}_${c.letter}`);
                return `
                <div class="choice-row ${isSelected ? 'selected' : ''} ${isEliminated ? 'eliminated' : ''}" data-letter="${c.letter}">
                  <button class="choice-letter-btn" aria-label="Select option ${c.letter}">${c.letter}</button>
                  <div class="choice-text-content">${c.text}</div>
                  <button class="choice-eliminate-btn" title="Eliminate option ${c.letter}" data-eliminate="${c.letter}" aria-label="Eliminate option ${c.letter}">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                      <line x1="18" y1="6" x2="6" y2="18"/>
                      <line x1="6" y1="6" x2="18" y2="18"/>
                    </svg>
                  </button>
                </div>
                `;
              }).join("")}
            </div>
          ` : `
            <!-- Student-Produced Response (SPR) Input -->
            <div class="spr-container">
              <div class="spr-input-label">Student-Produced Response (enter fraction, decimal, or integer):</div>
              <div class="spr-input-box-wrap">
                <input type="text" id="spr-user-input" class="spr-input-field" placeholder="e.g. 7/4 or 1.75" value="${selectedAnswer || ''}" maxlength="7" autofocus>
                <button id="btn-spr-clear" class="sat-btn sat-btn-secondary sat-btn-sm">Clear</button>
              </div>
              <div class="spr-guidelines">
                <ul>
                  <li>For negative numbers, enter a minus sign <code>-</code> first.</li>
                  <li>Fractions such as <code>3/4</code> or decimals such as <code>0.75</code> are accepted.</li>
                  <li>Do not enter mixed numbers like <code>3 1/2</code> (enter <code>7/2</code> or <code>3.5</code>).</li>
                </ul>
              </div>
            </div>
          `}

          ${this.mode === "practice" ? this.renderPracticeExplanation(q) : ""}
        </div>
      </div>
      `;
    }

    examBody.innerHTML = contentHtml;

    // Attach choice and input event listeners
    this.attachQuestionEventListeners(q);

    // Typeset KaTeX Math
    if (window.renderMathInElement) {
      window.renderMathInElement(examBody, {
        delimiters: [
          { left: "$$", right: "$$", display: true },
          { left: "$", right: "$", display: false },
          { left: "\\(", right: "\\)", display: false },
          { left: "\\[", right: "\\]", display: true }
        ],
        throwOnError: false
      });
    }

    // Save auto-progress in local storage
    this.saveProgress();
  },

  renderPracticeExplanation(q) {
    return `
    <div class="practice-explanation-box">
      <button class="btn-toggle-explanation" onclick="this.nextElementSibling.classList.toggle('hidden')">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>
        <span>Toggle Answer Explanation (Practice Mode)</span>
      </button>
      <div class="explanation-details hidden">
        <div class="exp-correct"><strong>Correct Answer:</strong> ${Array.isArray(q.correctAnswer) ? q.correctAnswer.join(" or ") : q.correctAnswer}</div>
        <div class="exp-body">${q.explanation}</div>
      </div>
    </div>
    `;
  },

  attachQuestionEventListeners(q) {
    const qKey = `${this.sectionId}_${q.id}`;

    // Choice Rows
    document.querySelectorAll(".choice-row").forEach(row => {
      const letter = row.getAttribute("data-letter");
      const elimBtn = row.querySelector(".choice-eliminate-btn");

      // Handle Option Selection
      row.onclick = (e) => {
        if (e.target.closest(".choice-eliminate-btn")) return;
        if (row.classList.contains("eliminated")) return;

        this.userAnswers[qKey] = letter;
        document.querySelectorAll(".choice-row").forEach(r => r.classList.remove("selected"));
        row.classList.add("selected");
        this.saveProgress();
      };

      // Handle Option Elimination
      if (elimBtn) {
        elimBtn.onclick = (e) => {
          e.stopPropagation();
          const elimKey = `${q.id}_${letter}`;
          if (this.eliminated.has(elimKey)) {
            this.eliminated.delete(elimKey);
            row.classList.remove("eliminated");
          } else {
            this.eliminated.add(elimKey);
            row.classList.add("eliminated");
            // If eliminated was selected, unselect it
            if (this.userAnswers[qKey] === letter) {
              delete this.userAnswers[qKey];
              row.classList.remove("selected");
            }
          }
          this.saveProgress();
        };
      }
    });

    // SPR Input
    const sprInput = document.getElementById("spr-user-input");
    const sprClear = document.getElementById("btn-spr-clear");

    if (sprInput) {
      sprInput.oninput = () => {
        const val = sprInput.value.trim();
        if (val) {
          this.userAnswers[qKey] = val;
        } else {
          delete this.userAnswers[qKey];
        }
        this.saveProgress();
      };
    }
    if (sprClear) {
      sprClear.onclick = () => {
        if (sprInput) sprInput.value = "";
        delete this.userAnswers[qKey];
        this.saveProgress();
      };
    }
  },

  toggleFlagCurrent() {
    const q = this.getCurrentQuestion();
    const qKey = `${this.sectionId}_${q.id}`;
    if (this.flagged.has(qKey)) {
      this.flagged.delete(qKey);
    } else {
      this.flagged.add(qKey);
    }
    this.renderCurrentQuestion();
  },

  nextQuestion() {
    const mod = this.getCurrentModule();
    if (this.questionIndex < mod.questions.length - 1) {
      this.questionIndex++;
      this.renderCurrentQuestion();
    } else {
      // Reached end of module questions -> open Module Review Screen
      this.openReviewScreen();
    }
  },

  prevQuestion() {
    if (this.questionIndex > 0) {
      this.questionIndex--;
      this.renderCurrentQuestion();
    }
  },

  jumpToQuestion(index) {
    const mod = this.getCurrentModule();
    if (index >= 0 && index < mod.questions.length) {
      this.questionIndex = index;
      this.closeReviewModal();
      this.renderCurrentQuestion();
    }
  },

  openReviewScreen() {
    const modal = document.getElementById("module-review-modal");
    if (!modal) return;

    const mod = this.getCurrentModule();
    const total = mod.questions.length;
    let answeredCount = 0;
    let flaggedCount = 0;

    const gridHtml = mod.questions.map((q, idx) => {
      const qKey = `${this.sectionId}_${q.id}`;
      const isAnswered = this.userAnswers[qKey] !== undefined && this.userAnswers[qKey] !== "";
      const isFlag = this.flagged.has(qKey);
      const isCurrent = idx === this.questionIndex;

      if (isAnswered) answeredCount++;
      if (isFlag) flaggedCount++;

      let statusClass = isAnswered ? "answered" : "unanswered";
      if (isCurrent) statusClass += " current";

      return `
      <button class="review-grid-cell ${statusClass}" onclick="window.ExamEngine.jumpToQuestion(${idx})" aria-label="Question ${idx + 1}">
        <span class="cell-num">${idx + 1}</span>
        ${isFlag ? `<span class="cell-flag-icon">★</span>` : ""}
      </button>
      `;
    }).join("");

    const summaryHtml = `
      <div class="review-summary-bar">
        <div class="review-stat"><strong>Answered:</strong> ${answeredCount} / ${total}</div>
        <div class="review-stat"><strong>Unanswered:</strong> ${total - answeredCount}</div>
        <div class="review-stat"><strong>Marked for Review:</strong> ${flaggedCount}</div>
      </div>
    `;

    document.getElementById("review-grid-container").innerHTML = gridHtml;
    document.getElementById("review-summary-container").innerHTML = summaryHtml;
    modal.classList.remove("hidden");
  },

  closeReviewModal() {
    const modal = document.getElementById("module-review-modal");
    if (modal) modal.classList.add("hidden");
  },

  confirmSubmitModule() {
    const confirmModal = document.getElementById("confirm-submit-modal");
    if (confirmModal) confirmModal.classList.remove("hidden");
  },

  closeConfirmModal() {
    const confirmModal = document.getElementById("confirm-submit-modal");
    if (confirmModal) confirmModal.classList.add("hidden");
  },

  executeModuleSubmit() {
    this.closeConfirmModal();
    this.closeReviewModal();

    if (this.sectionId === "rw") {
      if (this.moduleIndex === 0) {
        // RW Module 1 -> RW Module 2
        this.moduleIndex = 1;
        this.questionIndex = 0;
        this.startModuleTimer();
        this.renderCurrentQuestion();
        this.showToastWarning("Beginning Reading and Writing — Module 2");
      } else {
        // Finished RW Section -> 10-Minute Break Screen
        this.openBreakScreen();
      }
    } else if (this.sectionId === "math") {
      if (this.moduleIndex === 0) {
        // Math Module 1 -> Math Module 2
        this.moduleIndex = 1;
        this.questionIndex = 0;
        this.startModuleTimer();
        this.renderCurrentQuestion();
        this.showToastWarning("Beginning Math — Module 2");
      } else {
        // Finished Math Section -> Final Exam Submission & Score Generation!
        this.finalizeExam();
      }
    }
  },

  breakTimerSeconds: 600, // 10 minutes
  breakInterval: null,

  openBreakScreen() {
    if (this.timerInterval) clearInterval(this.timerInterval);
    const breakModal = document.getElementById("break-screen-modal");
    if (!breakModal) return;

    this.breakTimerSeconds = 600;
    breakModal.classList.remove("hidden");

    const timerElem = document.getElementById("break-timer-display");
    const updateBreakTimer = () => {
      const mins = Math.floor(this.breakTimerSeconds / 60);
      const secs = this.breakTimerSeconds % 60;
      if (timerElem) {
        timerElem.textContent = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
      }
    };
    updateBreakTimer();

    this.breakInterval = setInterval(() => {
      this.breakTimerSeconds--;
      updateBreakTimer();
      if (this.breakTimerSeconds <= 0) {
        clearInterval(this.breakInterval);
        this.resumeFromBreak();
      }
    }, 1000);
  },

  resumeFromBreak() {
    if (this.breakInterval) clearInterval(this.breakInterval);
    const breakModal = document.getElementById("break-screen-modal");
    if (breakModal) breakModal.classList.add("hidden");

    // Transition to Math Section Module 1
    this.sectionId = "math";
    this.moduleIndex = 0;
    this.questionIndex = 0;
    this.startModuleTimer();
    this.renderCurrentQuestion();
    this.showToastWarning("Section 2: Math — Module 1 has begun");
  },

  handleTimeExpired() {
    this.showToastWarning("Time has expired for this module!");
    setTimeout(() => {
      this.executeModuleSubmit();
    }, 1200);
  },

  finalizeExam() {
    if (this.timerInterval) clearInterval(this.timerInterval);
    Storage.clearSession();

    // Calculate official scaled scores and diagnostics
    const report = analyzePerformance(this.test, this.userAnswers);
    report.testId = this.test.id;
    report.testTitle = this.test.title;

    // Save to test history
    Storage.saveCompletedTest(report);

    // Switch to Score Report View
    if (window.App) {
      window.App.renderScoreReport(report);
    }
  },

  saveProgress() {
    Storage.saveSession({
      testId: this.test.id,
      mode: this.mode,
      sectionId: this.sectionId,
      moduleIndex: this.moduleIndex,
      questionIndex: this.questionIndex,
      userAnswers: this.userAnswers,
      flagged: Array.from(this.flagged),
      eliminated: Array.from(this.eliminated),
      timerSeconds: this.timerSeconds
    });
  },

  showToastWarning(msg) {
    const toast = document.getElementById("sat-toast");
    if (toast) {
      toast.textContent = msg;
      toast.classList.remove("hidden");
      setTimeout(() => toast.classList.add("hidden"), 3500);
    }
  }
};
