// Digital SAT 2026 Test Suite Registry
import { test1 } from './test1.js';
import { test2 } from './test2.js';
import { test3 } from './test3.js';
import { test4 } from './test4.js';

export const TESTS_DATABASE = [test1, test2, test3, test4];

export function getTestById(id) {
  return TESTS_DATABASE.find(t => t.id === id) || null;
}

export function getAllTestsMetadata() {
  return TESTS_DATABASE.map(t => ({
    id: t.id,
    title: t.title,
    description: t.description,
    totalQuestions: t.totalQuestions,
    sections: [
      { name: "Reading and Writing", modules: 2, totalQuestions: 54, time: "64 min" },
      { name: "Math", modules: 2, totalQuestions: 54, time: "70 min" }
    ]
  }));
}
