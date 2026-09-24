# assemble_test4.py
# Assembles Test 4 data and writes src/data/test4.js
import json
import os
from build_t4_rw1 import get_rw_m1_questions
from build_t4_rw2 import get_rw_m2_questions
from build_t4_m1 import get_math_m1_questions
from build_t4_m2 import get_math_m2_questions

def assemble_and_write():
    rw_m1 = get_rw_m1_questions()
    rw_m2 = get_rw_m2_questions()
    math_m1 = get_math_m1_questions()
    math_m2 = get_math_m2_questions()

    print(f"Loaded: RW M1={len(rw_m1)}, RW M2={len(rw_m2)}, Math M1={len(math_m1)}, Math M2={len(math_m2)}")

    test4_data = {
        "id": "test-4",
        "title": "Practice Test 4 (2026 Advanced Edition)",
        "description": "Full-length 2026 Digital SAT practice test featuring rigorous adaptive Module 2 questions, multi-step math problems, and academic vocabulary.",
        "totalQuestions": len(rw_m1) + len(rw_m2) + len(math_m1) + len(math_m2),
        "sections": {
            "rw": {
                "id": "rw",
                "title": "Reading and Writing",
                "timeMinutes": 64,
                "modules": [
                    {
                        "id": "test-4-rw-m1",
                        "moduleNumber": 1,
                        "title": "Reading and Writing - Module 1",
                        "timeLimitSeconds": 1920,
                        "questions": rw_m1
                    },
                    {
                        "id": "test-4-rw-m2",
                        "moduleNumber": 2,
                        "title": "Reading and Writing - Module 2",
                        "timeLimitSeconds": 1920,
                        "questions": rw_m2
                    }
                ]
            },
            "math": {
                "id": "math",
                "title": "Math",
                "timeMinutes": 70,
                "modules": [
                    {
                        "id": "test-4-math-m1",
                        "moduleNumber": 1,
                        "title": "Math - Module 1",
                        "timeLimitSeconds": 2100,
                        "questions": math_m1
                    },
                    {
                        "id": "test-4-math-m2",
                        "moduleNumber": 2,
                        "title": "Math - Module 2",
                        "timeLimitSeconds": 2100,
                        "questions": math_m2
                    }
                ]
            }
        }
    }

    output_path = os.path.join("src", "data", "test4.js")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("// Digital SAT 2026 Practice Test 4 (High-Difficulty Edition)\n")
        f.write("export const test4 = " + json.dumps(test4_data, indent=2) + ";\n")
    print(f"Test 4 successfully written to {output_path} with {test4_data['totalQuestions']} questions.")

if __name__ == "__main__":
    assemble_and_write()
