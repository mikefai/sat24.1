// Generator script for 4 Full-Length SAT 2026 Mock Exams
// Total: 4 tests * 108 questions = 432 authentic SAT questions
import fs from 'fs';
import path from 'path';

console.log("Generating 4 Full-Length Digital SAT 2026 Mock Exams...");

// Helper to create test structure
function createTestObject(testNum, title, rwM1, rwM2, mathM1, mathM2) {
  return {
    id: `test-${testNum}`,
    title: title,
    description: `Full-length Digital SAT 2026 practice examination matching official College Board Bluebook specifications. Contains 54 Reading & Writing questions and 54 Math questions with detailed step-by-step explanations.`,
    totalQuestions: 108,
    sections: {
      rw: {
        id: "rw",
        title: "Reading and Writing",
        timeMinutes: 64, // 32 per module
        modules: [
          {
            id: `test-${testNum}-rw-m1`,
            moduleNumber: 1,
            title: "Reading and Writing - Module 1",
            timeLimitSeconds: 32 * 60,
            questions: rwM1
          },
          {
            id: `test-${testNum}-rw-m2`,
            moduleNumber: 2,
            title: "Reading and Writing - Module 2",
            timeLimitSeconds: 32 * 60,
            questions: rwM2
          }
        ]
      },
      math: {
        id: "math",
        title: "Math",
        timeMinutes: 70, // 35 per module
        modules: [
          {
            id: `test-${testNum}-math-m1`,
            moduleNumber: 1,
            title: "Math - Module 1",
            timeLimitSeconds: 35 * 60,
            questions: mathM1
          },
          {
            id: `test-${testNum}-math-m2`,
            moduleNumber: 2,
            title: "Math - Module 2",
            timeLimitSeconds: 35 * 60,
            questions: mathM2
          }
        ]
      }
    }
  };
}

// We will write modular generator code for Test 1, Test 2, Test 3, Test 4
