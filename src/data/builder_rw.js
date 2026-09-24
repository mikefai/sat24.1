// Reading & Writing Question Builder with rich, authentic SAT question structures
import { DOMAINS } from './scoring.js';

export function makeVocabQuestion(id, passage, targetBlank, choices, correctLetter, explanation, difficulty = "Medium") {
  return {
    id,
    type: "mcq",
    domain: DOMAINS.RW.CRAFT_STRUCTURE,
    subdomain: "Words in Context",
    difficulty,
    stimulus: passage,
    prompt: "Which choice completes the text with the most logical and precise word or phrase?",
    choices: choices.map((c, i) => ({
      letter: String.fromCharCode(65 + i),
      text: c
    })),
    correctAnswer: correctLetter,
    explanation
  };
}

export function makeStructureQuestion(id, passage, prompt, choices, correctLetter, explanation, difficulty = "Medium") {
  return {
    id,
    type: "mcq",
    domain: DOMAINS.RW.CRAFT_STRUCTURE,
    subdomain: "Text Structure and Purpose",
    difficulty,
    stimulus: passage,
    prompt,
    choices: choices.map((c, i) => ({
      letter: String.fromCharCode(65 + i),
      text: c
    })),
    correctAnswer: correctLetter,
    explanation
  };
}

export function makeDualPassageQuestion(id, text1, text2, prompt, choices, correctLetter, explanation, difficulty = "Hard") {
  return {
    id,
    type: "mcq",
    domain: DOMAINS.RW.CRAFT_STRUCTURE,
    subdomain: "Cross-Text Connections",
    difficulty,
    stimulus: `<strong>Text 1</strong><br>${text1}<br><br><strong>Text 2</strong><br>${text2}`,
    prompt,
    choices: choices.map((c, i) => ({
      letter: String.fromCharCode(65 + i),
      text: c
    })),
    correctAnswer: correctLetter,
    explanation
  };
}

export function makeCentralIdeaQuestion(id, passage, prompt, choices, correctLetter, explanation, difficulty = "Medium") {
  return {
    id,
    type: "mcq",
    domain: DOMAINS.RW.INFO_IDEAS,
    subdomain: "Central Ideas and Details",
    difficulty,
    stimulus: passage,
    prompt,
    choices: choices.map((c, i) => ({
      letter: String.fromCharCode(65 + i),
      text: c
    })),
    correctAnswer: correctLetter,
    explanation
  };
}

export function makeInferenceQuestion(id, passage, prompt, choices, correctLetter, explanation, difficulty = "Hard") {
  return {
    id,
    type: "mcq",
    domain: DOMAINS.RW.INFO_IDEAS,
    subdomain: "Inferences",
    difficulty,
    stimulus: passage,
    prompt: prompt || "Which choice most logically completes the text?",
    choices: choices.map((c, i) => ({
      letter: String.fromCharCode(65 + i),
      text: c
    })),
    correctAnswer: correctLetter,
    explanation
  };
}

export function makeQuantitativeEvidenceQuestion(id, tableHtml, passage, prompt, choices, correctLetter, explanation, difficulty = "Medium") {
  return {
    id,
    type: "mcq",
    domain: DOMAINS.RW.INFO_IDEAS,
    subdomain: "Command of Evidence: Quantitative",
    difficulty,
    stimulus: `${tableHtml}<br>${passage}`,
    prompt,
    choices: choices.map((c, i) => ({
      letter: String.fromCharCode(65 + i),
      text: c
    })),
    correctAnswer: correctLetter,
    explanation
  };
}

export function makeTextualEvidenceQuestion(id, passage, prompt, choices, correctLetter, explanation, difficulty = "Medium") {
  return {
    id,
    type: "mcq",
    domain: DOMAINS.RW.INFO_IDEAS,
    subdomain: "Command of Evidence: Textual",
    difficulty,
    stimulus: passage,
    prompt,
    choices: choices.map((c, i) => ({
      letter: String.fromCharCode(65 + i),
      text: c
    })),
    correctAnswer: correctLetter,
    explanation
  };
}

export function makeGrammarQuestion(id, passage, prompt, choices, correctLetter, explanation, difficulty = "Medium") {
  return {
    id,
    type: "mcq",
    domain: DOMAINS.RW.CONVENTIONS,
    subdomain: "Boundaries and Sentence Structure",
    difficulty,
    stimulus: passage,
    prompt: prompt || "Which choice completes the text so that it conforms to the conventions of Standard English?",
    choices: choices.map((c, i) => ({
      letter: String.fromCharCode(65 + i),
      text: c
    })),
    correctAnswer: correctLetter,
    explanation
  };
}

export function makeTransitionQuestion(id, passage, choices, correctLetter, explanation, difficulty = "Medium") {
  return {
    id,
    type: "mcq",
    domain: DOMAINS.RW.EXPRESSION,
    subdomain: "Transitions",
    difficulty,
    stimulus: passage,
    prompt: "Which choice completes the text with the most logical transition?",
    choices: choices.map((c, i) => ({
      letter: String.fromCharCode(65 + i),
      text: c
    })),
    correctAnswer: correctLetter,
    explanation
  };
}

export function makeRhetoricalSynthesisQuestion(id, notesBullets, prompt, choices, correctLetter, explanation, difficulty = "Medium") {
  const formattedNotes = `While researching a topic, a student has taken the following notes:<br><ul style="margin: 8px 0; padding-left: 20px; list-style-type: disc;">${notesBullets.map(b => `<li style="margin-bottom: 4px;">${b}</li>`).join('')}</ul>`;
  return {
    id,
    type: "mcq",
    domain: DOMAINS.RW.EXPRESSION,
    subdomain: "Rhetorical Synthesis",
    difficulty,
    stimulus: formattedNotes,
    prompt,
    choices: choices.map((c, i) => ({
      letter: String.fromCharCode(65 + i),
      text: c
    })),
    correctAnswer: correctLetter,
    explanation
  };
}
