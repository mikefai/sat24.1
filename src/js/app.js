// app.js - Main Application Coordinator for Digital SAT 2026 Platform
import { TESTS_DATABASE, getTestById, getAllTestsMetadata } from '../data/tests.js';
import { Storage } from './storage.js';
import { ExamEngine } from './examEngine.js';
import { Calculator } from './calculator.js';
import { ReferenceSheet } from './referenceSheet.js';

window.ExamEngine = ExamEngine;
window.Calculator = Calculator;
window.ReferenceSheet = ReferenceSheet;

export const App = {
  currentView: "hub", // "hub", "exam", "report"
  activeReport: null,
  reviewFilter: "all", // "all", "incorrect", "omitted", "flagged"
  reviewSectionFilter: "all", // "all", "rw", "math"

  init() {
    this.renderHeader();
    this.renderModals();
    this.attachGlobalEvents();

    // Check for saved session or render Hub
    const session = Storage.getSession();
    if (session && session.testId) {
      this.renderHub(true);
    } else {
      this.renderHub(false);
    }
  },

  renderHeader() {
    // Header rendered dynamically depending on view
  },

  renderModals() {
    const modalContainer = document.getElementById("modals-container");
    if (!modalContainer) return;

    modalContainer.innerHTML = `
      ${Calculator.renderModal()}
      ${ReferenceSheet.renderModal()}

      <!-- Directions Modal -->
      <div id="directions-modal" class="sat-modal-overlay hidden" role="dialog">
        <div class="sat-modal-content directions-modal">
          <div class="sat-modal-header">
            <h2>Exam Directions</h2>
            <button id="close-directions-modal" class="sat-modal-close">&times;</button>
          </div>
          <div class="sat-modal-body">
            <h3>Section 1: Reading and Writing</h3>
            <p>The Reading and Writing section consists of two 32-minute modules, each with 27 questions. Questions address craft and structure, information and ideas, standard English conventions, and expression of ideas. All questions are multiple-choice with four options.</p>
            <h3>Section 2: Math</h3>
            <p>The Math section consists of two 35-minute modules, each with 27 questions. Questions cover algebra, advanced math, problem-solving and data analysis, and geometry and trigonometry. Approximately 75% are multiple choice and 25% are Student-Produced Responses. An embedded graphing calculator and geometry formula reference sheet are available at all times during the Math section.</p>
            <h3>Timing and Navigation</h3>
            <p>You may move back and forth among questions within the current module. You cannot return to a module once you have submitted it. A 10-minute break is provided between the Reading and Writing section and the Math section.</p>
          </div>
          <div class="sat-modal-footer">
            <button class="sat-btn sat-btn-primary" onclick="document.getElementById('directions-modal').classList.add('hidden')">Close Directions</button>
          </div>
        </div>
      </div>

      <!-- Module Review Modal -->
      <div id="module-review-modal" class="sat-modal-overlay hidden" role="dialog">
        <div class="sat-modal-content review-screen-modal">
          <div class="sat-modal-header">
            <h2>Module Review Screen</h2>
            <button class="sat-modal-close" onclick="ExamEngine.closeReviewModal()">&times;</button>
          </div>
          <div class="sat-modal-body">
            <p class="review-instructions">Review your answers before submitting this module. Click any question number to return to that question.</p>
            <div id="review-summary-container"></div>
            <div id="review-grid-container" class="review-grid"></div>
          </div>
          <div class="sat-modal-footer">
            <button class="sat-btn sat-btn-secondary" onclick="ExamEngine.closeReviewModal()">Return to Current Question</button>
            <button class="sat-btn sat-btn-primary" onclick="ExamEngine.confirmSubmitModule()">Submit Module</button>
          </div>
        </div>
      </div>

      <!-- Submit Confirmation Modal -->
      <div id="confirm-submit-modal" class="sat-modal-overlay hidden" role="dialog">
        <div class="sat-modal-content confirm-modal">
          <div class="sat-modal-header">
            <h2>Confirm Module Submission</h2>
            <button class="sat-modal-close" onclick="ExamEngine.closeConfirmModal()">&times;</button>
          </div>
          <div class="sat-modal-body">
            <p><strong>Are you sure you want to submit this module?</strong></p>
            <p style="color: #64748b; font-size: 14px; margin-top: 8px;">Once you submit, you will not be able to return to or review your answers for this module.</p>
          </div>
          <div class="sat-modal-footer">
            <button class="sat-btn sat-btn-secondary" onclick="ExamEngine.closeConfirmModal()">Keep Reviewing</button>
            <button class="sat-btn sat-btn-danger" onclick="ExamEngine.executeModuleSubmit()">Yes, Submit Module</button>
          </div>
        </div>
      </div>

      <!-- 10-Minute Break Modal -->
      <div id="break-screen-modal" class="sat-modal-overlay hidden" role="dialog">
        <div class="sat-modal-content break-modal">
          <div class="break-header-icon">
            <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#2563eb" stroke-width="2">
              <circle cx="12" cy="12" r="10"/>
              <polyline points="12 6 12 12 16 14"/>
            </svg>
          </div>
          <h2>Scheduled 10-Minute Break</h2>
          <p>You have completed Section 1 (Reading and Writing). Take a moment to relax, stretch, and hydrate before beginning Section 2 (Math).</p>
          <div class="break-timer-box">
            <span class="break-timer-label">Break Remaining:</span>
            <div id="break-timer-display" class="break-timer-digits">10:00</div>
          </div>
          <div class="break-actions">
            <button class="sat-btn sat-btn-primary sat-btn-lg" onclick="ExamEngine.resumeFromBreak()">Resume Exam Now (Start Math)</button>
          </div>
        </div>
      </div>
    `;

    Calculator.initEvents();
    ReferenceSheet.initEvents();

    const dirModal = document.getElementById("directions-modal");
    const closeDirBtn = document.getElementById("close-directions-modal");
    if (closeDirBtn && dirModal) {
      closeDirBtn.onclick = () => dirModal.classList.add("hidden");
    }
  },

  attachGlobalEvents() {
    // Navigation controls
    const btnBack = document.getElementById("btn-nav-back");
    const btnNext = document.getElementById("btn-nav-next");
    const btnReview = document.getElementById("btn-nav-review");
    const btnFlag = document.getElementById("btn-mark-review");
    const btnTimer = document.getElementById("btn-toggle-timer");

    if (btnBack) btnBack.onclick = () => ExamEngine.prevQuestion();
    if (btnNext) btnNext.onclick = () => ExamEngine.nextQuestion();
    if (btnReview) btnReview.onclick = () => ExamEngine.openReviewScreen();
    if (btnFlag) btnFlag.onclick = () => ExamEngine.toggleFlagCurrent();
    if (btnTimer) btnTimer.onclick = () => ExamEngine.toggleTimerVisibility();

    // Header Tool buttons
    const btnCalc = document.getElementById("btn-header-calc");
    const btnRef = document.getElementById("btn-header-ref");
    const btnDir = document.getElementById("btn-header-directions");

    if (btnCalc) btnCalc.onclick = () => Calculator.open();
    if (btnRef) btnRef.onclick = () => ReferenceSheet.open();
    if (btnDir) {
      btnDir.onclick = () => {
        const d = document.getElementById("directions-modal");
        if (d) d.classList.remove("hidden");
      };
    }
  },

  renderHub(hasSavedSession = false) {
    this.currentView = "hub";
    document.getElementById("exam-header").classList.add("hidden");
    document.getElementById("exam-footer").classList.add("hidden");
    document.getElementById("app-main").className = "app-hub-view";

    const tests = getAllTestsMetadata();
    const history = Storage.getHistory();

    const hubHtml = `
      <div class="hub-container">
        <!-- Hero Section -->
        <header class="hub-hero">
          <div class="hub-badge">College Board Bluebook™ 2026 Standard</div>
          <h1 class="hub-title">Digital SAT® 2026 Complete Mock Examination Suite</h1>
          <p class="hub-subtitle">
            4 full-length authentic practice examinations conforming to the 2026 Digital SAT testing specifications.
            Each exam includes <strong>54 Reading & Writing questions</strong> and <strong>54 Math questions</strong> (108 questions per exam, 432 total), complete with embedded graphing calculator, formula reference sheet, and step-by-step answer explanations.
          </p>
        </header>

        <!-- Mode & Actions bar -->
        <div class="hub-settings-bar">
          <div class="hub-mode-selector">
            <span class="mode-label">Testing Mode:</span>
            <label class="mode-radio-label">
              <input type="radio" name="test-mode" value="timed" checked>
              <span><strong>Timed Real Exam Mode</strong> (Official 64m RW + 70m Math timing with 10m break)</span>
            </label>
            <label class="mode-radio-label">
              <input type="radio" name="test-mode" value="practice">
              <span><strong>Practice Study Mode</strong> (Instant explanation toggles on every question)</span>
            </label>
          </div>
        </div>

        ${hasSavedSession ? `
          <div class="resume-session-banner">
            <div class="resume-text">
              <strong>Exam In Progress:</strong> You have an unfinished test session saved in your browser.
            </div>
            <div class="resume-buttons">
              <button class="sat-btn sat-btn-primary" onclick="App.resumeSession()">Resume Active Exam</button>
              <button class="sat-btn sat-btn-secondary" onclick="App.discardSession()">Discard</button>
            </div>
          </div>
        ` : ""}

        <!-- 4 Test Cards Grid -->
        <section class="tests-grid">
          ${tests.map((t, idx) => {
            const record = history.find(h => h.testId === t.id);
            return `
            <div class="test-card">
              <div class="test-card-header">
                <div class="test-number-pill">Practice Test ${idx + 1}</div>
                ${record ? `<span class="score-pill">Score: ${record.totalScore}</span>` : `<span class="new-pill">Ready</span>`}
              </div>
              <h2 class="test-card-title">${t.title}</h2>
              <p class="test-card-desc">${t.description}</p>

              <div class="test-card-specs">
                <div class="spec-item">
                  <strong>Section 1:</strong> 54 Reading & Writing (2 modules × 27 Qs)
                </div>
                <div class="spec-item">
                  <strong>Section 2:</strong> 54 Math (2 modules × 27 Qs with Calculator)
                </div>
                <div class="spec-item">
                  <strong>Total:</strong> 108 Questions | 134 Minutes + 10m Break
                </div>
              </div>

              <div class="test-card-footer">
                <button class="sat-btn sat-btn-primary test-start-btn" onclick="App.startTest('${t.id}')">
                  ${record ? "Retake Exam" : "Start Full Exam"}
                </button>
                ${record ? `
                  <button class="sat-btn sat-btn-secondary" onclick="App.viewPastReport('${t.id}')">View Score Report</button>
                ` : ""}
              </div>
            </div>
            `;
          }).join("")}
        </section>

        <!-- Past Test Performance History -->
        ${history.length > 0 ? `
          <section class="history-section">
            <div class="section-title-wrap">
              <h2>Your Exam History & Diagnostic Track Record</h2>
              <button class="sat-btn sat-btn-sm sat-btn-secondary" onclick="App.clearHistory()">Clear History</button>
            </div>
            <div class="history-table-wrap">
              <table class="history-table">
                <thead>
                  <tr>
                    <th>Test Name</th>
                    <th>Date</th>
                    <th>RW Score</th>
                    <th>Math Score</th>
                    <th>Composite Score</th>
                    <th>Percentile</th>
                    <th>Actions</th>
                  </tr>
                </thead>
                <tbody>
                  ${history.map(h => `
                    <tr>
                      <td><strong>${h.testTitle}</strong></td>
                      <td>${new Date(h.date).toLocaleDateString()}</td>
                      <td>${h.rwScore} / 800</td>
                      <td>${h.mathScore} / 800</td>
                      <td><span class="score-badge-highlight">${h.totalScore} / 1600</span></td>
                      <td>${h.percentile}</td>
                      <td>
                        <button class="sat-btn sat-btn-sm sat-btn-primary" onclick="App.viewPastReport('${h.testId}')">View Report</button>
                      </td>
                    </tr>
                  `).join("")}
                </tbody>
              </table>
            </div>
          </section>
        ` : ""}
      </div>
    `;

    document.getElementById("app-main").innerHTML = hubHtml;
  },

  startTest(testId) {
    const testData = getTestById(testId);
    if (!testData) return;

    const modeRadio = document.querySelector('input[name="test-mode"]:checked');
    const mode = modeRadio ? modeRadio.value : "timed";

    this.currentView = "exam";
    document.getElementById("exam-header").classList.remove("hidden");
    document.getElementById("exam-footer").classList.remove("hidden");
    document.getElementById("app-main").className = "app-exam-view";
    document.getElementById("app-main").innerHTML = `<div id="exam-body-content"></div>`;

    ExamEngine.init(testData, mode);
  },

  resumeSession() {
    const session = Storage.getSession();
    if (!session) return;

    const testData = getTestById(session.testId);
    if (!testData) return;

    this.currentView = "exam";
    document.getElementById("exam-header").classList.remove("hidden");
    document.getElementById("exam-footer").classList.remove("hidden");
    document.getElementById("app-main").className = "app-exam-view";
    document.getElementById("app-main").innerHTML = `<div id="exam-body-content"></div>`;

    ExamEngine.test = testData;
    ExamEngine.mode = session.mode || "timed";
    ExamEngine.sectionId = session.sectionId || "rw";
    ExamEngine.moduleIndex = session.moduleIndex || 0;
    ExamEngine.questionIndex = session.questionIndex || 0;
    ExamEngine.userAnswers = session.userAnswers || {};
    ExamEngine.flagged = new Set(session.flagged || []);
    ExamEngine.eliminated = new Set(session.eliminated || []);
    ExamEngine.timerSeconds = session.timerSeconds || 1920;

    ExamEngine.startModuleTimer();
    ExamEngine.renderCurrentQuestion();
  },

  discardSession() {
    if (confirm("Are you sure you want to discard your saved session? Progress will be lost.")) {
      Storage.clearSession();
      this.renderHub(false);
    }
  },

  clearHistory() {
    if (confirm("Are you sure you want to clear your test history?")) {
      Storage.clearAllData();
      this.renderHub(false);
    }
  },

  viewPastReport(testId) {
    const record = Storage.getTestRecord(testId);
    if (record && record.reportData) {
      this.renderScoreReport(record.reportData);
    }
  },

  renderScoreReport(report) {
    this.currentView = "report";
    this.activeReport = report;
    document.getElementById("exam-header").classList.add("hidden");
    document.getElementById("exam-footer").classList.add("hidden");
    document.getElementById("app-main").className = "app-report-view";

    const reportHtml = `
      <div class="report-container">
        <!-- Top Nav / Return -->
        <div class="report-top-nav">
          <button class="sat-btn sat-btn-secondary" onclick="App.renderHub(false)">
            ← Return to Exam Hub
          </button>
          <div class="report-actions">
            <button class="sat-btn sat-btn-secondary" onclick="window.print()">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/></svg>
              Print / Save PDF
            </button>
            <button class="sat-btn sat-btn-primary" onclick="App.startTest('${report.testId}')">
              Retake This Exam
            </button>
          </div>
        </div>

        <!-- Score Banner -->
        <div class="report-banner">
          <div class="report-title-area">
            <span class="report-pill">Official 2026 Equating Standard</span>
            <h1>Diagnostic Score Report</h1>
            <p>${report.testTitle}</p>
          </div>

          <div class="report-score-cards-grid">
            <!-- Total Composite -->
            <div class="score-card total-card">
              <div class="score-card-label">Total Composite Score</div>
              <div class="score-big-number">${report.totalScore}</div>
              <div class="score-scale">Scale: 400 – 1600</div>
              <div class="percentile-tag">National Percentile: <strong>${report.percentile}</strong></div>
            </div>

            <!-- Section 1: Reading and Writing -->
            <div class="score-card section-card">
              <div class="score-card-label">Reading and Writing</div>
              <div class="score-med-number">${report.rw.score}</div>
              <div class="score-scale">Scale: 200 – 800</div>
              <div class="score-stat-line">
                <span>Correct: <strong>${report.rw.correct}</strong> / 54</span>
                <span>Incorrect: <strong>${report.rw.incorrect}</strong></span>
                <span>Omitted: <strong>${report.rw.omitted}</strong></span>
              </div>
            </div>

            <!-- Section 2: Math -->
            <div class="score-card section-card">
              <div class="score-card-label">Math</div>
              <div class="score-med-number">${report.math.score}</div>
              <div class="score-scale">Scale: 200 – 800</div>
              <div class="score-stat-line">
                <span>Correct: <strong>${report.math.correct}</strong> / 54</span>
                <span>Incorrect: <strong>${report.math.incorrect}</strong></span>
                <span>Omitted: <strong>${report.math.omitted}</strong></span>
              </div>
            </div>
          </div>
        </div>

        <!-- Domain Mastery Breakdown -->
        <div class="report-section">
          <h2>Content Domain Mastery Analysis</h2>
          <div class="domains-two-col">
            <!-- RW Domains -->
            <div class="domain-box">
              <h3>Reading and Writing Domains</h3>
              ${Object.entries(report.rw.domains).map(([dom, stat]) => {
                const pct = stat.total > 0 ? Math.round((stat.correct / stat.total) * 100) : 0;
                return `
                <div class="domain-bar-row">
                  <div class="domain-label-group">
                    <span class="dom-title">${dom}</span>
                    <span class="dom-stat">${stat.correct} / ${stat.total} (${pct}%)</span>
                  </div>
                  <div class="progress-track">
                    <div class="progress-fill ${pct >= 75 ? 'high' : pct >= 50 ? 'med' : 'low'}" style="width: ${pct}%;"></div>
                  </div>
                </div>
                `;
              }).join("")}
            </div>

            <!-- Math Domains -->
            <div class="domain-box">
              <h3>Math Domains</h3>
              ${Object.entries(report.math.domains).map(([dom, stat]) => {
                const pct = stat.total > 0 ? Math.round((stat.correct / stat.total) * 100) : 0;
                return `
                <div class="domain-bar-row">
                  <div class="domain-label-group">
                    <span class="dom-title">${dom}</span>
                    <span class="dom-stat">${stat.correct} / ${stat.total} (${pct}%)</span>
                  </div>
                  <div class="progress-track">
                    <div class="progress-fill ${pct >= 75 ? 'high' : pct >= 50 ? 'med' : 'low'}" style="width: ${pct}%;"></div>
                  </div>
                </div>
                `;
              }).join("")}
            </div>
          </div>
        </div>

        <!-- Question-by-Question Review with Explanations -->
        <div class="report-section">
          <div class="review-header-controls">
            <h2>Detailed Question-by-Question Review (108 Questions)</h2>
            <div class="filter-controls-group">
              <div class="filter-btn-group">
                <span class="filter-label">Filter:</span>
                <button class="filter-chip active" onclick="App.setReviewFilter('all', this)">All (108)</button>
                <button class="filter-chip" onclick="App.setReviewFilter('incorrect', this)">Incorrect (${report.rw.incorrect + report.math.incorrect})</button>
                <button class="filter-chip" onclick="App.setReviewFilter('omitted', this)">Omitted (${report.rw.omitted + report.math.omitted})</button>
              </div>

              <div class="filter-btn-group">
                <span class="filter-label">Section:</span>
                <button class="filter-chip active" onclick="App.setSectionFilter('all', this)">All</button>
                <button class="filter-chip" onclick="App.setSectionFilter('rw', this)">Reading & Writing (54)</button>
                <button class="filter-chip" onclick="App.setSectionFilter('math', this)">Math (54)</button>
              </div>
            </div>
          </div>

          <div id="report-questions-list" class="questions-review-list">
            ${this.renderQuestionReviewCards(report)}
          </div>
        </div>
      </div>
    `;

    document.getElementById("app-main").innerHTML = reportHtml;

    // Render KaTeX Math in review
    if (window.renderMathInElement) {
      window.renderMathInElement(document.getElementById("app-main"), {
        delimiters: [
          { left: "$$", right: "$$", display: true },
          { left: "$", right: "$", display: false },
          { left: "\\(", right: "\\)", display: false }
        ]
      });
    }
  },

  setReviewFilter(filter, el) {
    this.reviewFilter = filter;
    el.parentElement.querySelectorAll(".filter-chip").forEach(c => c.classList.remove("active"));
    el.classList.add("active");
    this.updateQuestionListDisplay();
  },

  setSectionFilter(sec, el) {
    this.reviewSectionFilter = sec;
    el.parentElement.querySelectorAll(".filter-chip").forEach(c => c.classList.remove("active"));
    el.classList.add("active");
    this.updateQuestionListDisplay();
  },

  updateQuestionListDisplay() {
    const container = document.getElementById("report-questions-list");
    if (!container || !this.activeReport) return;
    container.innerHTML = this.renderQuestionReviewCards(this.activeReport);

    if (window.renderMathInElement) {
      window.renderMathInElement(container, {
        delimiters: [
          { left: "$$", right: "$$", display: true },
          { left: "$", right: "$", display: false },
          { left: "\\(", right: "\\)", display: false }
        ]
      });
    }
  },

  renderQuestionReviewCards(report) {
    let filtered = report.questionAnalysis;

    // Apply correctness filter
    if (this.reviewFilter === "incorrect") {
      filtered = filtered.filter(q => !q.isCorrect && !q.isOmitted);
    } else if (this.reviewFilter === "omitted") {
      filtered = filtered.filter(q => q.isOmitted);
    }

    // Apply section filter
    if (this.reviewSectionFilter === "rw") {
      filtered = filtered.filter(q => q.section === "Reading and Writing");
    } else if (this.reviewSectionFilter === "math") {
      filtered = filtered.filter(q => q.section === "Math");
    }

    if (filtered.length === 0) {
      return `<div class="empty-filter-state">No questions match the selected filter.</div>`;
    }

    return filtered.map(item => {
      const q = item.question;
      const statusClass = item.isCorrect ? "correct" : item.isOmitted ? "omitted" : "incorrect";
      const statusText = item.isCorrect ? "Correct" : item.isOmitted ? "Omitted" : "Incorrect";

      return `
      <div class="review-card ${statusClass}">
        <div class="review-card-top">
          <div class="top-left">
            <span class="review-status-badge ${statusClass}">${statusText}</span>
            <span class="q-full-title">${item.section} — Module ${item.module}, Question ${item.displayNumber}</span>
          </div>
          <div class="top-right">
            <span class="domain-pill">${item.domain}</span>
            <span class="badge-${(item.difficulty || 'Medium').toLowerCase()}">${item.difficulty}</span>
          </div>
        </div>

        <div class="review-card-body">
          ${q.stimulus ? `<div class="review-stimulus">${q.stimulus}</div>` : ""}
          <div class="review-prompt"><strong>Prompt:</strong> ${q.prompt}</div>

          ${q.type === "mcq" ? `
            <div class="review-choices-grid">
              ${q.choices.map(c => {
                const isUser = item.userAnswer === c.letter;
                const isTarget = q.correctAnswer === c.letter;
                let cClass = "";
                if (isTarget) cClass = "target-choice";
                if (isUser && !isTarget) cClass = "user-wrong-choice";

                return `
                <div class="review-choice ${cClass}">
                  <span class="c-letter">${c.letter}</span>
                  <span class="c-text">${c.text}</span>
                  ${isTarget ? `<span class="c-badge correct">Correct Answer</span>` : ""}
                  ${isUser && !isTarget ? `<span class="c-badge user">Your Answer</span>` : ""}
                </div>
                `;
              }).join("")}
            </div>
          ` : `
            <div class="review-spr-answers">
              <div class="ans-block"><strong>Your Answer:</strong> <span class="${item.isCorrect ? 'text-green' : 'text-red'}">${item.userAnswer || "Omitted"}</span></div>
              <div class="ans-block"><strong>Correct Answer:</strong> <span class="text-green">${Array.isArray(q.correctAnswer) ? q.correctAnswer.join(" or ") : q.correctAnswer}</span></div>
            </div>
          `}

          <!-- Comprehensive Step-by-Step Explanation -->
          <div class="review-explanation-box">
            <div class="exp-title">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
              Step-by-Step Educational Explanation
            </div>
            <div class="exp-content">${item.explanation}</div>
          </div>
        </div>
      </div>
      `;
    }).join("");
  }
};

window.App = App;

// Bootstrap on DOM ready
document.addEventListener("DOMContentLoaded", () => {
  App.init();
});
