// Digital SAT Equating and Scoring System
// Section scores: 200 - 800 for Reading & Writing, 200 - 800 for Math
// Total Score: 400 - 1600

export const DOMAINS = {
  RW: {
    CRAFT_STRUCTURE: "Craft and Structure",
    INFO_IDEAS: "Information and Ideas",
    CONVENTIONS: "Standard English Conventions",
    EXPRESSION: "Expression of Ideas"
  },
  MATH: {
    ALGEBRA: "Algebra",
    ADVANCED_MATH: "Advanced Math",
    PROBLEM_SOLVING: "Problem-Solving and Data Analysis",
    GEOMETRY_TRIG: "Geometry and Trigonometry"
  }
};

/**
 * Converts raw correct answers (out of 54) to scaled score (200 - 800)
 * Digital SAT scoring follows a non-linear equating curve where:
 * 54/54 -> 800
 * 53/54 -> 790-800
 * 50/54 -> 750
 * 45/54 -> 690
 * 40/54 -> 640
 * 35/54 -> 590
 * 30/54 -> 540
 * 25/54 -> 490
 * 20/54 -> 440
 * 15/54 -> 390
 * 10/54 -> 330
 * 0/54  -> 200
 */
export function calculateSectionScore(correctCount, totalQuestions = 54) {
  if (correctCount <= 0) return 200;
  if (correctCount >= totalQuestions) return 800;

  const ratio = correctCount / totalQuestions;
  
  // Non-linear scaled curve modeled after official Digital SAT scoring table
  let rawScaled;
  if (ratio >= 0.95) {
    // 51 to 54: 760 to 800
    rawScaled = 760 + ((ratio - 0.95) / 0.05) * 40;
  } else if (ratio >= 0.85) {
    // 46 to 50: 680 to 750
    rawScaled = 680 + ((ratio - 0.85) / 0.10) * 80;
  } else if (ratio >= 0.70) {
    // 38 to 45: 580 to 670
    rawScaled = 580 + ((ratio - 0.70) / 0.15) * 100;
  } else if (ratio >= 0.50) {
    // 27 to 37: 460 to 570
    rawScaled = 460 + ((ratio - 0.50) / 0.20) * 120;
  } else if (ratio >= 0.30) {
    // 16 to 26: 340 to 450
    rawScaled = 340 + ((ratio - 0.30) / 0.20) * 120;
  } else {
    // 1 to 15: 200 to 330
    rawScaled = 200 + (ratio / 0.30) * 140;
  }

  // Round to nearest 10 as in real SAT
  const rounded = Math.round(rawScaled / 10) * 10;
  return Math.min(800, Math.max(200, rounded));
}

/**
 * Calculates national percentile estimate based on total composite score
 */
export function calculatePercentile(totalScore) {
  if (totalScore >= 1550) return "99th+";
  if (totalScore >= 1500) return "98th";
  if (totalScore >= 1450) return "96th";
  if (totalScore >= 1400) return "93rd";
  if (totalScore >= 1350) return "89th";
  if (totalScore >= 1300) return "84th";
  if (totalScore >= 1250) return "78th";
  if (totalScore >= 1200) return "71st";
  if (totalScore >= 1150) return "64th";
  if (totalScore >= 1100) return "56th";
  if (totalScore >= 1050) return "48th";
  if (totalScore >= 1000) return "40th";
  if (totalScore >= 950) return "32nd";
  if (totalScore >= 900) return "24th";
  if (totalScore >= 800) return "13th";
  return "<10th";
}

/**
 * Diagnostic analysis across domains
 */
export function analyzePerformance(testData, userAnswers) {
  const result = {
    rw: {
      total: 54,
      correct: 0,
      incorrect: 0,
      omitted: 0,
      score: 200,
      domains: {}
    },
    math: {
      total: 54,
      correct: 0,
      incorrect: 0,
      omitted: 0,
      score: 200,
      domains: {}
    },
    totalScore: 400,
    percentile: "<10th",
    questionAnalysis: []
  };

  // Initialize domain metrics
  Object.values(DOMAINS.RW).forEach(dom => {
    result.rw.domains[dom] = { correct: 0, total: 0 };
  });
  Object.values(DOMAINS.MATH).forEach(dom => {
    result.math.domains[dom] = { correct: 0, total: 0 };
  });

  // Evaluate Reading & Writing (Module 1 + Module 2)
  const rwQuestions = [...testData.sections.rw.modules[0].questions, ...testData.sections.rw.modules[1].questions];
  rwQuestions.forEach((q, index) => {
    const userAns = userAnswers[`rw_${q.id}`];
    const isCorrect = checkAnswer(q, userAns);
    const isOmitted = userAns === undefined || userAns === null || userAns === "";

    if (isCorrect) result.rw.correct++;
    else if (isOmitted) result.rw.omitted++;
    else result.rw.incorrect++;

    if (q.domain && result.rw.domains[q.domain]) {
      result.rw.domains[q.domain].total++;
      if (isCorrect) result.rw.domains[q.domain].correct++;
    }

    result.questionAnalysis.push({
      section: "Reading and Writing",
      module: index < 27 ? 1 : 2,
      displayNumber: (index % 27) + 1,
      id: q.id,
      key: `rw_${q.id}`,
      question: q,
      userAnswer: userAns,
      isCorrect,
      isOmitted,
      correctAnswer: q.correctAnswer,
      explanation: q.explanation,
      domain: q.domain,
      difficulty: q.difficulty
    });
  });

  // Evaluate Math (Module 1 + Module 2)
  const mathQuestions = [...testData.sections.math.modules[0].questions, ...testData.sections.math.modules[1].questions];
  mathQuestions.forEach((q, index) => {
    const userAns = userAnswers[`math_${q.id}`];
    const isCorrect = checkAnswer(q, userAns);
    const isOmitted = userAns === undefined || userAns === null || userAns === "";

    if (isCorrect) result.math.correct++;
    else if (isOmitted) result.math.omitted++;
    else result.math.incorrect++;

    if (q.domain && result.math.domains[q.domain]) {
      result.math.domains[q.domain].total++;
      if (isCorrect) result.math.domains[q.domain].correct++;
    }

    result.questionAnalysis.push({
      section: "Math",
      module: index < 27 ? 1 : 2,
      displayNumber: (index % 27) + 1,
      id: q.id,
      key: `math_${q.id}`,
      question: q,
      userAnswer: userAns,
      isCorrect,
      isOmitted,
      correctAnswer: q.correctAnswer,
      explanation: q.explanation,
      domain: q.domain,
      difficulty: q.difficulty
    });
  });

  result.rw.score = calculateSectionScore(result.rw.correct, 54);
  result.math.score = calculateSectionScore(result.math.correct, 54);
  result.totalScore = result.rw.score + result.math.score;
  result.percentile = calculatePercentile(result.totalScore);

  return result;
}

/**
 * Checks if user answer matches correct answer
 * Supports multiple choice (A, B, C, D) and Student Produced Response (SPR) fractions/decimals
 */
export function checkAnswer(question, userAnswer) {
  if (userAnswer === undefined || userAnswer === null || userAnswer === "") {
    return false;
  }

  const cleanUser = String(userAnswer).trim().toLowerCase();
  
  if (Array.isArray(question.correctAnswer)) {
    return question.correctAnswer.some(ans => matchSingleAnswer(cleanUser, ans));
  }
  
  return matchSingleAnswer(cleanUser, question.correctAnswer);
}

function matchSingleAnswer(user, target) {
  const cleanTarget = String(target).trim().toLowerCase();
  if (user === cleanTarget) return true;

  // Fraction vs Decimal comparison for Math SPR
  const userNum = parseNumeric(user);
  const targetNum = parseNumeric(cleanTarget);
  if (userNum !== null && targetNum !== null) {
    return Math.abs(userNum - targetNum) < 0.0001;
  }
  return false;
}

function parseNumeric(str) {
  if (/^-?\d+\/\d+$/.test(str)) {
    const [num, den] = str.split("/").map(Number);
    if (den === 0) return null;
    return num / den;
  }
  const parsed = Number(str);
  return isNaN(parsed) ? null : parsed;
}
