# Digital SAT® 2026 Mock Examination Suite

A high-fidelity web application featuring **4 Full-Length Digital SAT 2026 Mock Exams** (432 verified questions) designed according to College Board Bluebook™ specifications, test structures, and equating standards.

---

## 🌟 Key Features

### 1. 4 Full-Length Authentic 2026 Exams (432 Questions)
- **Exam Structure per Test**:
  - **Section 1: Reading and Writing**: Module 1 (27 Qs, 32 min) + Module 2 (27 Qs, 32 min) = 54 Qs
  - **Scheduled 10-Minute Break**: Timed pause screen with countdown and instant resume
  - **Section 2: Math**: Module 1 (27 Qs, 35 min) + Module 2 (27 Qs, 35 min) = 54 Qs (Questions 1–22 Multiple Choice, Questions 23–27 Student-Produced Responses)
  - **Total**: 108 Questions per exam | 134 Minutes testing time + 10m break

### 2. Complete College Board Bluebook™ Interface
- **Split-Screen Layout**: Academic stimulus on the left pane and question prompt/choices on the right pane for Reading & Writing.
- **KaTeX Math Typesetting**: High-fidelity LaTeX math rendering for equations, functions, geometry, and formulas.
- **Student-Produced Response (SPR)**: Free-response input for grid-ins supporting fractions, decimals, integers, and negative values.
- **Question Navigator**: Jump to any question with answered, unanswered, and flagged indicators.
- **Option Elimination**: Cross out answers using the eliminator tool.
- **Section Countdown Timer**: Live timer with Hide/Show toggle and 5-minute warning banner.

### 3. Built-in Math Tools
- **Graphing & Scientific Calculator**: Interactive HTML5 canvas graphing tool with function plotting, zoom, pan, coordinates, and scientific functions ($\sin$, $\cos$, $\tan$, $\log$, $\sqrt{}$, powers, deg/rad).
- **Official Formula Reference Sheet**: Geometry formulas, area/volume references, and 30-60-90 / 45-45-90 special right triangles.

### 4. Official Equating Algorithm & Diagnostic Report
- **Scaled 400–1600 Composite Score**: 200–800 for Reading & Writing, 200–800 for Math.
- **National Percentile Ranking**: Grounded in official Digital SAT performance distributions.
- **Domain Mastery Breakdown**: Progress bars and accuracy stats across all 8 tested domains.
- **Filterable Question Review**: Filter by All, Incorrect, or Omitted, with step-by-step educational explanations for every question.
- **Local Persistence**: Test progress and score history automatically saved to `localStorage`.

---

## 🚀 Quick Start

### Prerequisites
No dependencies or backend required! The application runs in any modern web browser.

### Running Locally

Using Python:
```bash
python -m http.server 8080
```
Then navigate to: `http://localhost:8080/`

Using Node:
```bash
npx serve -l 3000
```
Then navigate to: `http://localhost:3000/`

---

## 🧪 Verification

Run the verification test suite to validate all 432 questions across all 4 exams:
```bash
node verify_suite.js
```

---

## 📁 Project Structure

```
├── index.html              # Main HTML entry point
├── package.json            # Project metadata
├── verify_suite.js         # 432-question database integrity tester
├── public/                 # Static assets & favicon
└── src/
    ├── css/
    │   └── main.css        # Bluebook design system stylesheet
    ├── data/
    │   ├── builder_math.js # Math question constructor helpers
    │   ├── builder_rw.js   # RW question constructor helpers
    │   ├── scoring.js      # 400–1600 equating engine & analytics
    │   ├── test1.js        # Practice Exam 1 (108 Qs)
    │   ├── test2.js        # Practice Exam 2 (108 Qs)
    │   ├── test3.js        # Practice Exam 3 (108 Qs)
    │   ├── test4.js        # Practice Exam 4 (108 Qs)
    │   └── tests.js        # Central test database registry
    └── js/
        ├── app.js          # Main application coordinator
        ├── calculator.js   # Graphing & scientific calculator
        ├── examEngine.js   # Bluebook test runner state machine
        ├── referenceSheet.js # Math formula reference modal
        └── storage.js      # Session & history persistence
```
