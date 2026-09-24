# assemble_test3.py
import json
import os
from gen_test3_rw1 import rw1
from gen_test3_rw2 import rw2
from gen_test3_math import math1, math2

assert len(rw1) == 27, f"Expected 27, got {len(rw1)}"
assert len(rw2) == 27, f"Expected 27, got {len(rw2)}"
assert len(math1) == 27, f"Expected 27, got {len(math1)}"
assert len(math2) == 27, f"Expected 27, got {len(math2)}"

test3 = {
    "id": "test-3",
    "title": "SAT Practice Test 3 (2026 Edition)",
    "description": "Full-length Digital SAT 2026 practice examination matching official College Board Bluebook specifications. Contains 54 Reading & Writing questions and 54 Math questions with detailed step-by-step explanations.",
    "totalQuestions": 108,
    "sections": {
        "rw": {
            "id": "rw",
            "title": "Reading and Writing",
            "timeMinutes": 64,
            "modules": [
                {
                    "id": "test-3-rw-m1",
                    "moduleNumber": 1,
                    "title": "Reading and Writing - Module 1",
                    "timeLimitSeconds": 32 * 60,
                    "questions": rw1
                },
                {
                    "id": "test-3-rw-m2",
                    "moduleNumber": 2,
                    "title": "Reading and Writing - Module 2",
                    "timeLimitSeconds": 32 * 60,
                    "questions": rw2
                }
            ]
        },
        "math": {
            "id": "math",
            "title": "Math",
            "timeMinutes": 70,
            "modules": [
                {
                    "id": "test-3-math-m1",
                    "moduleNumber": 1,
                    "title": "Math - Module 1",
                    "timeLimitSeconds": 35 * 60,
                    "questions": math1
                },
                {
                    "id": "test-3-math-m2",
                    "moduleNumber": 2,
                    "title": "Math - Module 2",
                    "timeLimitSeconds": 35 * 60,
                    "questions": math2
                }
            ]
        }
    }
}

out_path = os.path.join("src", "data", "test3.js")
with open(out_path, "w", encoding="utf-8") as f:
    f.write("// Digital SAT 2026 Practice Test 3\n")
    f.write("export const test3 = ")
    json.dump(test3, f, indent=2, ensure_ascii=False)
    f.write(";\n")

print(f"Successfully generated Test 3: {out_path} with 108 questions!")
