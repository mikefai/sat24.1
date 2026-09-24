# build_t4_m2.py
# Generates 27 Math Module 2 questions for Test 4 (100% Adaptive Hard Module: 22 MCQ + 5 SPR)

DOMAINS = {
    "ALG": "Algebra",
    "ADV": "Advanced Math",
    "PSDA": "Problem-Solving and Data Analysis",
    "GEOM": "Geometry and Trigonometry"
}

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

def get_math_m2_questions():
    mcq_specs = [
        # Q1: Nonlinear Systems with Tangent Line (ADV) - Target A
        (DOMAINS["ADV"], "Nonlinear systems", "Hard",
         "In the xy-plane, the line y = mx - 5 is tangent to the parabola y = 2x^2 + 8x + 3, where m is a negative constant.",
         "What is the value of m?",
         "-8",
         ["-4", "-12", "-16"],
         "Set the equations equal: 2x^2 + 8x + 3 = mx - 5 => 2x^2 + (8 - m)x + 8 = 0. For the line to be tangent to the parabola, the quadratic must have exactly one real solution, so its discriminant must equal zero: Delta = (8 - m)^2 - 4(2)(8) = 0 => (8 - m)^2 - 64 = 0 => (8 - m)^2 = 64. Thus 8 - m = 8 or 8 - m = -8. If 8 - m = 8, m = 0. If 8 - m = -8, m = 16. Wait! Let's check: (8 - m)^2 = 64 => m = 0 or m = 16? Neither is negative! Let's adjust constants: y = mx + 1 and y = 2x^2 + 6x + 9:\n2x^2 + (6 - m)x + 8 = 0 => (6 - m)^2 - 4(2)(8) = 0 => (6 - m)^2 = 64 => 6 - m = 8 => m = -2, or 6 - m = -8 => m = 14. If m is negative, m = -2.\nLet's use: y = mx + 1 is tangent to y = 2x^2 + 6x + 9, where m is a negative constant. Then m = -2."),

        # Q2: Circles and Distance to Line (GEOM) - Target C
        (DOMAINS["GEOM"], "Circles", "Hard",
         "A circle in the xy-plane is defined by x^2 + y^2 - 6x - 10y + 9 = 0. What is the minimum distance from the origin (0, 0) to a point on the circle?",
         "sqrt(34) - 5",
         ["sqrt(34)", "5", "sqrt(34) + 5"],
         "Complete the square: (x - 3)^2 + (y - 5)^2 = -9 + 9 + 25 = 25. The center is C(3, 5) and the radius is r = 5. The distance from the origin to the center is d = sqrt(3^2 + 5^2) = sqrt(9 + 25) = sqrt(34). The minimum distance from the origin to the circle is d - r = sqrt(34) - 5."),

        # Q3: Exponentials with Time Unit Conversions (ADV) - Target B
        (DOMAINS["ADV"], "Nonlinear functions", "Hard",
         "The active mass A(t), in milligrams, of a therapeutic radioactive isotope decreases according to the equation A(t) = 360 * (1/2)^(t / 18), where t is the elapsed time in hours.",
         "Which of the following equivalent expressions displays the daily decay factor of the isotope as a base?",
         "A(t) = 360 * (2^(-4/3))^(t / 24)",
         ["A(t) = 360 * (2^(-3/4))^(t / 24)", "A(t) = 360 * (2^(-1/18))^(24t)", "A(t) = 360 * (2^(-4/3))^(24t)"],
         "To express the decay in terms of days (intervals of 24 hours), write the exponent t / 18 as (24 / 18) * (t / 24) = (4/3) * (t / 24). Then A(t) = 360 * [(1/2)^(4/3)]^(t / 24) = 360 * [2^(-4/3)]^(t / 24)."),

        # Q4: Trigonometric Identities and Cofunctions (GEOM) - Target D
        (DOMAINS["GEOM"], "Right triangles and trigonometry", "Hard",
         "In right triangle PQR, angle Q is 90 degrees. If sin(P) = 4k - 0.3 and cos(R) = 2k + 0.5, what is the value of k?",
         "0.4",
         ["0.1", "0.2", "0.3"],
         "In any right triangle with right angle at Q, acute angles P and R are complementary (P + R = 90 degrees). By the cofunction identity, sin(P) = cos(90 - P) = cos(R). Therefore: 4k - 0.3 = 2k + 0.5 => 2k = 0.8 => k = 0.4."),

        # Q5: Polynomials - Sum of Zeros (ADV) - Target B
        (DOMAINS["ADV"], "Equivalent expressions and polynomials", "Hard",
         "The polynomial function g(x) = 4x^3 - 24x^2 + 11x + 66 can be written in factored form as (2x + 3)(2x - k)(x - 2).",
         "What is the value of k?",
         "11",
         ["6", "9", "14"],
         "Expand the product: (2x + 3)(2x - k) = 4x^2 + (6 - 2k)x - 3k. Multiply by (x - 2): [4x^2 + (6 - 2k)x - 3k](x - 2) = 4x^3 - 8x^2 + (6 - 2k)x^2 - 2(6 - 2k)x - 3kx + 6k = 4x^3 + (-2 - 2k)x^2 + (-12 + k)x + 6k. Compare constant term with g(x): 6k = 66 => k = 11. Check x^2 coefficient: -2 - 2(11) = -24 (Matches -24x^2). Check x coefficient: -12 + 11 = -1? In g(x) we have +11x. Wait, (-12 - 3k + 4k) = -12 + k = -12 + 11 = -1 != 11. Let's make it match exactly:\nLet (2x - 3)(2x + 1)(x - 4):\n(4x^2 - 4x - 3)(x - 4) = 4x^3 - 16x^2 - 4x^2 + 16x - 3x + 12 = 4x^3 - 20x^2 + 13x + 12.\nWritten as (2x - 3)(2x + 1)(x - k) => k = 4.\nOr (2x + 1)(2x - k)(x - 3) = (4x^2 + (2-2k)x - k)(x - 3) = 4x^3 - 12x^2 + (2-2k)x^2 - 3(2-2k)x - kx + 3k = 4x^3 + (-10-2k)x^2 + (-6+5k)x + 3k.\nFor k = 7: 4x^3 - 24x^2 + 29x + 21.\nLet's use: g(x) = 4x^3 - 24x^2 + 29x + 21 = (2x + 1)(2x - k)(x - 3). Then k = -... wait, if k = 7: (2x - 7)(2x + 1) = 4x^2 - 12x - 7. Multiplied by (x - 3): 4x^3 - 12x^2 - 12x^2 + 36x - 7x + 21 = 4x^3 - 24x^2 + 29x + 21. Constant is 3k? (2x - 7)(2x + 1) has constant -7, times -3 gives +21! So (2x + 1)(2x - k)(x - 3) with k = 7 gives exactly 4x^3 - 24x^2 + 29x + 21. Then k = 7!"),

        # Q6: Boxplots and Standard Deviation (PSDA) - Target D
        (DOMAINS["PSDA"], "One-variable data: distributions and measures of center", "Hard",
         "Dataset A consists of 50 values with a mean of 100 and a range of 20, with all values clustered tightly between 90 and 110. Dataset B consists of 50 values with a mean of 100, where 25 values are equal to 60 and 25 values are equal to 140.",
         "Which statement comparing the standard deviation of Dataset A (s_A) and Dataset B (s_B) must be true?",
         "s_A < s_B",
         ["s_A > s_B", "s_A = s_B", "There is not enough information to compare s_A and s_B."],
         "Standard deviation measures the average dispersion or distance of data points from the mean. In Dataset A, all points are within 10 units of the mean of 100 (so s_A < 10). In Dataset B, every single point is exactly 40 units away from the mean (so s_B = 40). Therefore, s_A < s_B."),

        # Q7: Quadratic Vertices with Free Parameters (ADV) - Target A
        (DOMAINS["ADV"], "Nonlinear functions", "Hard",
         "The quadratic function h is defined by h(x) = x^2 - 2px + (p^2 + 3p - 15), where p is a constant. If the minimum value of h(x) is 9, what is the value of p?",
         "8",
         ["4", "6", "10"],
         "Complete the square for h(x): h(x) = (x^2 - 2px + p^2) + 3p - 15 = (x - p)^2 + (3p - 15). Since the leading coefficient is 1 > 0, the parabola opens upward, and its minimum value is the vertex y-coordinate, which is 3p - 15. Setting this equal to 9: 3p - 15 = 9 => 3p = 24 => p = 8."),

        # Q8: Rational Functions and Slant Asymptotes (ADV) - Target C
        (DOMAINS["ADV"], "Nonlinear functions", "Hard",
         "For which of the following equations does the line y = 2x - 3 serve as an asymptote to the graph of y = f(x)?",
         "f(x) = (2x^2 - 3x + 5) / x",
         ["f(x) = (2x^2 + 3x - 5) / x", "f(x) = (4x^2 - 6x + 1) / (2x)", "f(x) = (2x - 3) / (x^2 + 1)"],
         "A rational function has a slant asymptote y = mx + b if dividing the numerator by the denominator produces a quotient of mx + b and a remainder that approaches 0 as x approaches infinity. Dividing (2x^2 - 3x + 5) by x gives 2x - 3 + 5/x. As x -> infinity, 5/x -> 0, so y = 2x - 3 is the slant asymptote."),

        # Q9: Linear Programming / Constraint Word Problems (ALG) - Target D
        (DOMAINS["ALG"], "Linear inequalities", "Hard",
         "A pharmaceutical lab produces two formulations, X and Y. Each liter of X requires 3 hours of synthesis and 2 hours of purification. Each liter of Y requires 4 hours of synthesis and 5 hours of purification. The lab has at most 180 hours of synthesis and at most 160 hours of purification available per week.",
         "Which system of inequalities models the possible number of liters of X, x, and Y, y, that can be produced per week?",
         "3x + 4y <= 180 and 2x + 5y <= 160",
         ["4x + 3y <= 180 and 5x + 2y <= 160", "3x + 2y <= 180 and 4x + 5y <= 160", "3x + 4y >= 180 and 2x + 5y >= 160"],
         "Total synthesis time is 3x + 4y, which cannot exceed 180 hours: 3x + 4y <= 180. Total purification time is 2x + 5y, which cannot exceed 160 hours: 2x + 5y <= 160."),

        # Q10: Circle Secant and Tangent Theorem (GEOM) - Target B
        (DOMAINS["GEOM"], "Circles", "Hard",
         "In a circle, a tangent segment PT from an external point P touches the circle at T. A secant line from P intersects the circle at points A and B, such that P, A, and B are collinear with A between P and B. If PA = 4 and AB = 12, what is the length of PT?",
         "8",
         ["6", "4*sqrt(3)", "10"],
         "By the Tangent-Secant Theorem, PT^2 = PA * PB. Here PA = 4, and PB = PA + AB = 4 + 12 = 16. Thus PT^2 = 4 * 16 = 64, which gives PT = sqrt(64) = 8."),

        # Q11: Inverting Exponential and Logarithmic Models (ADV) - Target A
        (DOMAINS["ADV"], "Nonlinear functions", "Hard",
         "A sound engineer measures the acoustic intensity level L, in decibels (dB), using the formula L = 10 * log_10(I / I_0), where I is the sound intensity in watts per square meter and I_0 is the threshold of hearing. If the intensity of sound 1 is 10,000 times the intensity of sound 2, by how many decibels does sound 1 exceed sound 2?",
         "40 dB",
         ["10 dB", "20 dB", "100 dB"],
         "The difference in decibels is L_1 - L_2 = 10 * log_10(I_1 / I_0) - 10 * log_10(I_2 / I_0) = 10 * log_10(I_1 / I_2). Given I_1 / I_2 = 10,000 = 10^4, we have L_1 - L_2 = 10 * log_10(10^4) = 10 * 4 = 40 dB."),

        # Q12: Quadratic Formula with Surds (ADV) - Target C
        (DOMAINS["ADV"], "Quadratic and exponential equations", "Hard",
         "The solutions to the equation 3x^2 - 12x + 5 = 0 can be written in the form (a +/- sqrt(b)) / c, where a, b, and c are positive integers with no common factor greater than 1.",
         "What is the value of a + b + c?",
         "30",
         ["26", "28", "34"],
         "Using the quadratic formula for ax^2 + bx + c = 0: x = [-(-12) +/- sqrt((-12)^2 - 4(3)(5))] / (2*3) = [12 +/- sqrt(144 - 60)] / 6 = [12 +/- sqrt(84)] / 6 = [12 +/- 2*sqrt(21)] / 6. Dividing numerator and denominator by 2 gives (6 +/- sqrt(21)) / 3. Here a = 6, b = 21, and c = 3. Since gcd(6, 21, 3) = 3? Wait! 21 is inside the square root! In the expression (a +/- sqrt(b)) / c, gcd(a, c) = gcd(6, 3) = 3! So 6 and 3 share a common factor of 3! If we divide by 3: 2 +/- sqrt(21)/3 = 2 +/- sqrt(21/9) = 2 +/- sqrt(7/3). The standard form requires a, b, c to have no common factor among a and c, which means we can't simplify further unless b is adjusted. But notice gcd(a, c) = gcd(6, 3) = 3. Let's make an equation where a, b, c have gcd(a, b, c) = 1 or a and c are coprime:\nConsider 2x^2 - 6x + 1 = 0: x = (6 +/- sqrt(36 - 8))/4 = (6 +/- sqrt(28))/4 = (6 +/- 2*sqrt(7))/4 = (3 +/- sqrt(7))/2.\nHere a = 3, b = 7, c = 2. gcd(3, 2) = 1. a + b + c = 3 + 7 + 2 = 12.\nLet's check target letter: Target C! We can set correct answer to 12 at Choice C!"),

        # Q13: Scatterplots and Line of Best Fit Residuals (PSDA) - Target B
        (DOMAINS["PSDA"], "Two-variable data: models and scatterplots", "Hard",
         "In a linear regression analysis relating engine displacement x (in liters) to fuel efficiency y (in miles per gallon), the line of best fit is given by y_hat = -4.2x + 38.5. For an engine with a displacement of 3.0 liters, the actual measured fuel efficiency was 27.4 miles per gallon.",
         "What is the residual, in miles per gallon, for this data point?",
         "1.5",
         ["-1.5", "2.1", "-2.1"],
         "The residual is defined as Actual y - Predicted y (y - y_hat). For x = 3.0: y_hat = -4.2(3.0) + 38.5 = -12.6 + 38.5 = 25.9. The actual value is y = 27.4. Therefore, residual = 27.4 - 25.9 = +1.5."),

        # Q14: Volume of Frustum / Composite Solid (GEOM) - Target D
        (DOMAINS["GEOM"], "Area and volume", "Hard",
         "A right circular cone with height 18 cm and base radius 6 cm is sliced by a plane parallel to its base at a height of 12 cm from the apex, removing the top smaller cone to form a frustum.",
         "What is the volume, in cm^3, of the resulting frustum?",
         "152pi",
         ["144pi", "168pi", "196pi"],
         "The original cone has radius R = 6 and height H = 18. Its total volume is V_total = (1/3)*pi*R^2*H = (1/3)*pi*(36)*(18) = 216pi. The removed top cone has height h = 12. By similar triangles, its radius is r = R * (h / H) = 6 * (12 / 18) = 4 cm. The volume of the removed top cone is V_top = (1/3)*pi*r^2*h = (1/3)*pi*(16)*(12) = 64pi. The volume of the frustum is V_total - V_top = 216pi - 64pi = 152pi."),

        # Q15: Complex Numbers in Quadratic Expressions (ADV) - Target C
        (DOMAINS["ADV"], "Equivalent expressions and polynomials", "Hard",
         "If i = sqrt(-1), which of the following is equivalent to the expression (5 + 3i) / (2 - i)?",
         "(7 + 11i) / 5",
         ["(13 + 11i) / 5", "(7 + 11i) / 3", "(1 + i) / 5"],
         "Multiply numerator and denominator by the complex conjugate of the denominator, (2 + i):\nNumerator: (5 + 3i)(2 + i) = 10 + 5i + 6i + 3i^2 = 10 + 11i - 3 = 7 + 11i.\nDenominator: (2 - i)(2 + i) = 4 - i^2 = 4 - (-1) = 5.\nThus the expression simplifies to (7 + 11i) / 5."),

        # Q16: Systems of Linear Equations with No Solution (ALG) - Target A
        (DOMAINS["ALG"], "Linear systems", "Hard",
         "In the system of equations below, c is a constant:\n(c - 2)x + 4y = 9\n6x + (c + 3)y = 15\nFor which positive value of c does the system have no solution?",
         "5",
         ["6", "4", "3"],
         "The system has no solution when the lines are parallel and distinct, meaning their slopes are equal: (c - 2) / 6 = 4 / (c + 3) => (c - 2)(c + 3) = 24 => c^2 + c - 6 = 24 => c^2 + c - 30 = 0 => (c + 6)(c - 5) = 0. The positive solution is c = 5. Checking the constants: for c = 5, 3x + 4y = 9 and 6x + 8y = 15. Doubling the first gives 6x + 8y = 18 != 15, confirming the lines are parallel and distinct (no solution)."),

        # Q17: Absolute Value Equations and Inequalities (ALG) - Target C
        (DOMAINS["ALG"], "Linear equations in one variable", "Hard",
         "What is the sum of all solutions to the equation |3x - 7| = 2x + 9?",
         "14",
         ["16", "-2/5", "15.6"],
         "Case 1: 3x - 7 = 2x + 9 => x = 16. Check: |3(16) - 7| = |41| = 41; 2(16) + 9 = 41 (Valid).\nCase 2: 3x - 7 = -(2x + 9) = -2x - 9 => 5x = -2 => x = -2/5 = -0.4. Check: |3(-0.4) - 7| = |-8.2| = 8.2; 2(-0.4) + 9 = -0.8 + 9 = 8.2 (Valid).\nWait, both solutions are valid! The sum is 16 + (-0.4) = 15.6. Wait, if prompt says sum of all integer solutions? Or let's choose |2x - 5| = x + 4:\nCase 1: 2x - 5 = x + 4 => x = 9. Check: |13| = 13.\nCase 2: 2x - 5 = -x - 4 => 3x = 1 => x = 1/3. Check: |2/3 - 5| = 13/3; 1/3 + 4 = 13/3. Both valid!\nWhat if |x - 4| = 3x - 8:\nCase 1: x - 4 = 3x - 8 => 2x = 4 => x = 2. Check: |2-4|=2; 3(2)-8=-2 (Extraneous!).\nCase 2: x - 4 = -3x + 8 => 4x = 12 => x = 3. Check: |3-4|=1; 3(3)-8=1 (Valid). Only one solution x = 3.\nLet's design a case with two integer solutions:\n|x^2 - 16|? Or |2x - 8| = 6:\n2x - 8 = 6 => 2x = 14 => x = 7.\n2x - 8 = -6 => 2x = 2 => x = 1. Sum = 8.\nLet's use: |3x - 12| = 15:\n3x - 12 = 15 => 3x = 27 => x = 9.\n3x - 12 = -15 => 3x = -3 => x = -1.\nSum of solutions = 9 + (-1) = 8. Target C can have '8'!"),

        # Q18: Exponential vs Linear Growth Rate (PSDA) - Target A
        (DOMAINS["PSDA"], "Percentages", "Hard",
         "Model A predicts that an investment grows by $4,500 every year. Model B predicts that the same investment grows by 6% compounded annually. Both models start with an initial investment of $50,000.",
         "In which year t will Model B's annual dollar gain first exceed Model A's annual dollar gain?",
         "Year 8",
         ["Year 6", "Year 10", "Year 12"],
         "Model A's annual gain is fixed at $4,500. Model B's value at year t is 50,000 * (1.06)^t. The gain during year t+1 is 50,000 * (1.06)^t * 0.06 = 3,000 * (1.06)^t. We want 3,000 * (1.06)^t > 4,500 => (1.06)^t > 1.5. Taking logs: t * ln(1.06) > ln(1.5) => t > 0.40546 / 0.05827 = 6.958. Thus, after 7 full years (at year 8), Model B's annual gain first exceeds $4,500."),

        # Q19: Circle Intersected by a Line (GEOM) - Target D
        (DOMAINS["GEOM"], "Circles", "Hard",
         "In the xy-plane, the circle (x - 4)^2 + (y - 3)^2 = 25 intersects the x-axis at points A and B.",
         "What is the distance between points A and B?",
         "8",
         ["6", "10", "4*sqrt(3)"],
         "The x-axis corresponds to y = 0. Substituting y = 0 into the circle equation: (x - 4)^2 + (0 - 3)^2 = 25 => (x - 4)^2 + 9 = 25 => (x - 4)^2 = 16. Taking the square root gives x - 4 = 4 or x - 4 = -4, so x = 8 or x = 0. The points of intersection are A(0, 0) and B(8, 0). The distance between them is 8 - 0 = 8."),

        # Q20: Radian Measure and Polygon Trigonometry (GEOM) - Target B
        (DOMAINS["GEOM"], "Right triangles and trigonometry", "Hard",
         "A regular hexagon is inscribed in a circle with radius 10 cm. What is the exact area, in cm^2, of the hexagon?",
         "150*sqrt(3)",
         ["300", "75*sqrt(3)", "200*sqrt(3)"],
         "A regular hexagon inscribed in a circle of radius r consists of 6 equilateral triangles, each with side length equal to r = 10 cm. The area of an equilateral triangle with side s is (sqrt(3)/4)*s^2. For s = 10, the area is (sqrt(3)/4)*(100) = 25*sqrt(3). The total area of the regular hexagon is 6 * 25*sqrt(3) = 150*sqrt(3) cm^2."),

        # Q21: Higher Degree Polynomial Zeros and Graph Intercepts (ADV) - Target D
        (DOMAINS["ADV"], "Equivalent expressions and polynomials", "Hard",
         "The graph of y = (x^2 - 9)(x^2 - 4x - 5) intersects the x-axis at k distinct points.",
         "What is the value of k?",
         "4",
         ["2", "3", "5"],
         "Factor each quadratic: x^2 - 9 = (x - 3)(x + 3), giving zeros x = 3 and x = -3. x^2 - 4x - 5 = (x - 5)(x + 1), giving zeros x = 5 and x = -1. All four zeros (-3, -1, 3, 5) are distinct real numbers. Therefore, the graph intersects the x-axis at exactly 4 distinct points."),

        # Q22: Non-linear System with Tangency Condition (ADV) - Target B
        (DOMAINS["ADV"], "Nonlinear systems", "Hard",
         "For what value of c will the system of equations below have exactly one real solution?\ny = 3x^2 - 12x + 7\ny = 6x + c",
         "-20",
         ["-13", "-26", "-14"],
         "Set the two equations equal: 3x^2 - 12x + 7 = 6x + c => 3x^2 - 18x + (7 - c) = 0. For the system to have exactly one real solution, the discriminant must be zero: Delta = (-18)^2 - 4(3)(7 - c) = 0 => 324 - 12(7 - c) = 0 => 324 - 84 + 12c = 0 => 240 + 12c = 0 => 12c = -240 => c = -20.")
    ]

    # Adjust Q1, Q5, Q12, Q17 specs to ensure 100% exact numerical and target letter consistency:
    mcq_specs[0] = (
        DOMAINS["ADV"], "Nonlinear systems", "Hard",
        "In the xy-plane, the line y = mx + 1 is tangent to the parabola y = 2x^2 + 6x + 9, where m is a negative constant.",
        "What is the value of m?",
        "-2",
        ["-4", "-6", "-8"],
        "Set the equations equal: 2x^2 + 6x + 9 = mx + 1 => 2x^2 + (6 - m)x + 8 = 0. For tangency, the discriminant must be zero: (6 - m)^2 - 4(2)(8) = 0 => (6 - m)^2 - 64 = 0 => (6 - m)^2 = 64. Thus 6 - m = 8 or 6 - m = -8. If 6 - m = 8, m = -2. If 6 - m = -8, m = 14. Since m < 0, m = -2."
    )
    mcq_specs[4] = (
        DOMAINS["ADV"], "Equivalent expressions and polynomials", "Hard",
        "The polynomial function g(x) = 4x^3 - 24x^2 + 29x + 21 can be written in factored form as (2x + 1)(2x - k)(x - 3), where k is a positive constant.",
        "What is the value of k?",
        "7",
        ["5", "9", "11"],
        "Expanding (2x + 1)(2x - k)(x - 3): the constant term is (1)(-k)(-3) = 3k. Setting this equal to the constant term of g(x), 21, gives 3k = 21 => k = 7. Checking the other coefficients with k = 7: (2x + 1)(2x - 7)(x - 3) = (4x^2 - 12x - 7)(x - 3) = 4x^3 - 24x^2 + 29x + 21, which matches perfectly."
    )
    mcq_specs[11] = (
        DOMAINS["ADV"], "Quadratic and exponential equations", "Hard",
        "The solutions to the equation 2x^2 - 6x + 1 = 0 can be written in the form (a +/- sqrt(b)) / c, where a, b, and c are positive integers and gcd(a, c) = 1.",
        "What is the value of a + b + c?",
        "12",
        ["10", "14", "16"],
        "Using the quadratic formula: x = [-(-6) +/- sqrt((-6)^2 - 4(2)(1))] / (2*2) = [6 +/- sqrt(36 - 8)] / 4 = [6 +/- sqrt(28)] / 4 = [6 +/- 2*sqrt(7)] / 4 = (3 +/- sqrt(7)) / 2. Here a = 3, b = 7, and c = 2. Since gcd(3, 2) = 1, this form satisfies the conditions. Thus a + b + c = 3 + 7 + 2 = 12."
    )
    mcq_specs[16] = (
        DOMAINS["ALG"], "Linear equations in one variable", "Hard",
        "What is the sum of all distinct solutions to the equation |3x - 12| = 15?",
        "What is the sum of all distinct solutions to the equation?",
        "8",
        ["6", "10", "12"],
        "The equation splits into two cases: Case 1: 3x - 12 = 15 => 3x = 27 => x = 9. Case 2: 3x - 12 = -15 => 3x = -3 => x = -1. The sum of the solutions is 9 + (-1) = 8."
    )

    questions = []
    for i, spec in enumerate(mcq_specs):
        qid = f"t4-m2-q{i+1}"
        if len(spec) == 7:
            domain, subdomain, diff, stim, corr, dists, expl = spec
            prompt = stim
        else:
            domain, subdomain, diff, stim, prompt, corr, dists, expl = spec
        target_letter = MATH_TARGETS[i]
        questions.append(make_hard_mcq(qid, domain, subdomain, diff, stim, prompt, corr, dists, target_letter, expl))

    # SPR Questions (Q23 - Q27)
    spr_specs = [
        # Q23: Quadratic Roots and Vieta's Formula (ADV)
        (DOMAINS["ADV"], "Quadratic and exponential equations", "Hard",
         "The quadratic equation x^2 - 16x + 55 = 0 has roots p and q. What is the value of 1/p + 1/q?",
         "What is the value of 1/p + 1/q?",
         "16/55",
         "By Vieta's formulas, the sum of roots is p + q = 16 and the product of roots is pq = 55. The sum of the reciprocals is 1/p + 1/q = (p + q) / (pq) = 16/55."),

        # Q24: Perpendicular Lines and Intercepts (ALG)
        (DOMAINS["ALG"], "Linear equations in two variables", "Hard",
         "Line L_1 passes through the points (-3, 8) and (5, -4). Line L_2 is perpendicular to Line L_1 and passes through the point (6, 11).",
         "What is the y-intercept of Line L_2?",
         "3",
         "The slope of Line L_1 is m_1 = (-4 - 8) / (5 - (-3)) = -12 / 8 = -3/2. Since Line L_2 is perpendicular to L_1, its slope is the negative reciprocal: m_2 = 2/3. Using point-slope form with (6, 11): y - 11 = (2/3)(x - 6) => y - 11 = (2/3)x - 4 => y = (2/3)x + 7? Wait! 11 - 4 = 7! Let's check: y = (2/3)(0) + 7 = 7! So the y-intercept is 7!"),

        # Q25: Circle Tangent and Radius (GEOM)
        (DOMAINS["GEOM"], "Circles", "Hard",
         "A circle in the xy-plane is tangent to the line y = 9 and has its center at (5, -3).",
         "What is the radius of the circle?",
         "12",
         "Since the circle is tangent to the horizontal line y = 9, the radius is the vertical distance between the line y = 9 and the center's y-coordinate, y = -3. Thus, r = |9 - (-3)| = 12."),

        # Q26: Trigonometry and Radian Values (GEOM)
        (DOMAINS["GEOM"], "Right triangles and trigonometry", "Hard",
         "In right triangle XYZ with right angle at Y, sin(X) = 5/13. What is the value of tan(X) + tan(Z)?",
         "What is the value of tan(X) + tan(Z)?",
         "169/60",
         "In right triangle XYZ with right angle at Y, the hypotenuse is 13. Since sin(X) = opposite/hypotenuse = 5/13, the side opposite to X is 5 and the adjacent side is sqrt(13^2 - 5^2) = 12. Therefore, tan(X) = 5/12. For angle Z, the opposite side is 12 and the adjacent side is 5, so tan(Z) = 12/5. The sum is tan(X) + tan(Z) = 5/12 + 12/5 = (25 + 144) / 60 = 169/60."),

        # Q27: Remainder Theorem / Polynomial Division (ADV)
        (DOMAINS["ADV"], "Equivalent expressions and polynomials", "Hard",
         "When the polynomial P(x) = 3x^4 - 2x^3 + 5x^2 - kx + 14 is divided by (x - 2), the remainder is 64.",
         "What is the value of k?",
         "9",
         "By the Polynomial Remainder Theorem, the remainder when P(x) is divided by (x - 2) is P(2). Therefore:\nP(2) = 3(2)^4 - 2(2)^3 + 5(2)^2 - k(2) + 14 = 64\n3(16) - 2(8) + 5(4) - 2k + 14 = 64\n48 - 16 + 20 - 2k + 14 = 64\n66 - 2k = 64 => 2k = 2 => k = 1! Wait! 48 - 16 = 32. 32 + 20 = 52. 52 + 14 = 66. 66 - 2k = 64 => 2k = 2 => k = 1!")
    ]

    # Adjust Q24 and Q27 for clarity:
    spr_specs[1] = (
        DOMAINS["ALG"], "Linear equations in two variables", "Hard",
        "Line L_1 passes through the points (-3, 8) and (5, -4). Line L_2 is perpendicular to Line L_1 and passes through the point (6, 11).",
        "What is the y-intercept of Line L_2?",
        "7",
        "The slope of Line L_1 is m_1 = (-4 - 8) / (5 - (-3)) = -12 / 8 = -3/2. Line L_2 is perpendicular, so its slope is m_2 = 2/3. Using point-slope form with (6, 11): y - 11 = (2/3)(x - 6) => y - 11 = (2/3)x - 4 => y = (2/3)x + 7. The y-intercept is 7."
    )
    spr_specs[4] = (
        DOMAINS["ADV"], "Equivalent expressions and polynomials", "Hard",
        "When the polynomial P(x) = 3x^4 - 2x^3 + 5x^2 - kx + 14 is divided by (x - 2), the remainder is 64.",
        "What is the value of k?",
        "1",
        "By the Remainder Theorem, P(2) = 64: 3(2^4) - 2(2^3) + 5(2^2) - 2k + 14 = 64 => 48 - 16 + 20 - 2k + 14 = 64 => 66 - 2k = 64 => 2k = 2 => k = 1."
    )

    for i, spec in enumerate(spr_specs):
        qid = f"t4-m2-q{23+i}"
        if len(spec) == 6:
            domain, subdomain, diff, stim, corr, expl = spec
            prompt = stim.split("?")[-2].split(".")[-1] + "?" if "?" in stim else stim
        else:
            domain, subdomain, diff, stim, prompt, corr, expl = spec
        questions.append(make_spr(qid, domain, subdomain, diff, stim, prompt, corr, expl))

    return questions
