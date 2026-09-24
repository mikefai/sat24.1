# build_full_suite.py
# Generates 4 full-length SAT 2026 mock exams:
# 4 tests * 108 questions = 432 authentic SAT questions
import json
import os

print("Building 4 Full-Length SAT 2026 Mock Exams...")

# Helper to write JS module file
def write_test_module(filename, var_name, test_data):
    filepath = os.path.join("src", "data", filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"// Digital SAT 2026 Practice Test: {test_data['title']}\n")
        f.write(f"export const {var_name} = ")
        json.dump(test_data, f, indent=2, ensure_ascii=False)
        f.write(";\n")
    print(f"Wrote {filepath} with {test_data['totalQuestions']} questions.")

