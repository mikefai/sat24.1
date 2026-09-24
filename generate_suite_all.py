# generate_suite_all.py
# Complete 432 SAT Question Dataset Generator for Digital SAT 2026
import json
import os

print("Starting generation of 4 full SAT 2026 mock exams...")

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

def make_mcq(qid, domain, subdomain, diff, stimulus, prompt, choices, correct_letter, explanation):
    return {
        "id": qid,
        "type": "mcq",
        "domain": domain,
        "subdomain": subdomain,
        "difficulty": diff,
        "stimulus": stimulus,
        "prompt": prompt,
        "choices": [{"letter": chr(65 + i), "text": c} for i, c in enumerate(choices)],
        "correctAnswer": correct_letter,
        "explanation": explanation
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
        "explanation": explanation
    }

def make_bullet_notes(notes):
    bullets = "".join([f"<li style='margin-bottom: 4px;'>{n}</li>" for n in notes])
    return f"While researching a topic, a student has taken the following notes:<br><ul style='margin: 8px 0; padding-left: 20px; list-style-type: disc;'>{bullets}</ul>"

def make_dual_passage(text1, text2):
    return f"<strong>Text 1</strong><br>{text1}<br><br><strong>Text 2</strong><br>{text2}"

def make_table(headers, rows):
    th_cells = "".join([f"<th style='padding: 6px; text-align: left; border-bottom: 2px solid #cbd5e1;'>{h}</th>" for h in headers])
    tr_rows = ""
    for r in rows:
        td_cells = "".join([f"<td style='padding: 5px; border-bottom: 1px solid #e2e8f0;'>{cell}</td>" for cell in r])
        tr_rows += f"<tr>{td_cells}</tr>"
    return f"<table style='width: 100%; border-collapse: collapse; margin: 10px 0; font-size: 13px; background: #fff;'><thead><tr style='background: #f8fafc;'>{th_cells}</tr></thead><tbody>{tr_rows}</tbody></table>"

print("Helper functions initialized.")
