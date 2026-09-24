# gen_hard_test4.py
# High-Difficulty 2026 Digital SAT Practice Test 4 Generator
import json
import os

DOMAINS = {
    "RW": {
        "CRAFT": "Craft and Structure",
        "INFO": "Information and Ideas",
        "CONV": "Standard English Conventions",
        "EXPR": "Expression of Ideas"
    },
    "MATH": {
        "ALG": "Algebra",
        "ADV": "Advanced Math",
        "PSDA": "Problem-Solving and Data Analysis",
        "GEOM": "Geometry and Trigonometry"
    }
}

RW_TARGETS = ['D', 'B', 'A', 'C', 'B', 'D', 'C', 'A', 'B', 'A', 'D', 'C', 'A', 'C', 'B', 'D', 'A', 'B', 'D', 'C', 'B', 'A', 'C', 'D', 'C', 'A', 'B']
MATH_TARGETS = ['A', 'C', 'B', 'D', 'B', 'D', 'A', 'C', 'D', 'B', 'A', 'C', 'B', 'D', 'C', 'A', 'C', 'A', 'D', 'B', 'D', 'B']

def make_hard_mcq(qid, domain, subdomain, diff, stimulus, prompt, correct_text, distractors, target_letter, explanation):
    target_idx = ord(target_letter) - ord('A')
    choices_texts = list(distractors[:3])
    choices_texts.insert(target_idx, correct_text)
    choices = [{"letter": chr(65 + i), "text": t} for i, t in enumerate(choices_texts)]
    full_explanation = f"Choice {target_letter} is correct. {explanation}"
    return {
        "id": qid,
        "type": "mcq",
        "domain": domain,
        "subdomain": subdomain,
        "difficulty": diff,
        "stimulus": stimulus,
        "prompt": prompt,
        "choices": choices,
        "correctAnswer": target_letter,
        "explanation": full_explanation
    }

def make_spr(qid, domain, subdomain, diff, stimulus, prompt, correct_answers, explanation):
    ans_list = correct_answers if isinstance(correct_answers, list) else [str(correct_answers)]
    return {
        "id": qid,
        "type": "spr",
        "domain": domain,
        "subdomain": subdomain,
        "difficulty": diff,
        "stimulus": stimulus,
        "prompt": prompt,
        "correctAnswer": ans_list,
        "explanation": f"The correct answer is {ans_list[0]}. {explanation}"
    }
