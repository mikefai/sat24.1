import { TESTS_DATABASE } from './src/data/tests.js';

console.log('Testing suite verification...');
console.log('Number of tests loaded:', TESTS_DATABASE.length);

let totalQuestions = 0;
const allIds = new Set();

TESTS_DATABASE.forEach((t, i) => {
  const rw1 = t.sections.rw.modules[0].questions.length;
  const rw2 = t.sections.rw.modules[1].questions.length;
  const m1 = t.sections.math.modules[0].questions.length;
  const m2 = t.sections.math.modules[1].questions.length;
  const testTotal = rw1 + rw2 + m1 + m2;

  console.log(`Test ${i + 1} (${t.id}): RW M1=${rw1}, RW M2=${rw2}, Math M1=${m1}, Math M2=${m2} -> Total: ${testTotal}`);

  if (rw1 !== 27 || rw2 !== 27 || m1 !== 27 || m2 !== 27) {
    throw new Error(`Test ${t.id} does not have exactly 27 questions per module!`);
  }

  const allQuestionsInTest = [
    ...t.sections.rw.modules[0].questions,
    ...t.sections.rw.modules[1].questions,
    ...t.sections.math.modules[0].questions,
    ...t.sections.math.modules[1].questions
  ];

  allQuestionsInTest.forEach(q => {
    if (allIds.has(q.id)) {
      throw new Error(`Duplicate question ID detected: ${q.id}`);
    }
    allIds.add(q.id);

    if (!q.prompt || !q.explanation || q.correctAnswer === undefined) {
      throw new Error(`Missing required fields in question ${q.id}`);
    }
    totalQuestions++;
  });
});

console.log('==============================================');
console.log(`GRAND TOTAL VERIFIED QUESTIONS: ${totalQuestions} / 432`);
console.log('ALL INTEGRITY CHECKS PASSED PERFECTLY!');
console.log('==============================================');
