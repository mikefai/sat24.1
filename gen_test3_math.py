# gen_test3_math.py - Practice Test 3 Math (54 questions: 27 Module 1, 27 Module 2)
import json
from generate_suite_all import DOMAINS, make_mcq, make_spr

math1 = []
math2 = []

# ==========================================
# TEST 3 - MATH MODULE 1 (27 Qs)
# ==========================================

# 1-8 Algebra
math1.append(make_mcq(
    "t3-math-m1-q1", DOMAINS["MATH"]["ALG"], "Linear Equations", "Easy",
    "If $5x - 15 = 45$, what is the value of $x - 3$?",
    "Which choice is the correct value?",
    ["9", "12", "6", "15"],
    "A",
    "Choice A is correct. Divide both sides of $5x - 15 = 45$ by 5: $\\frac{5(x - 3)}{5} = \\frac{45}{5} \\implies x - 3 = 9$."
))

math1.append(make_mcq(
    "t3-math-m1-q2", DOMAINS["MATH"]["ALG"], "Linear Functions", "Easy",
    "A bike rental shop charges an initial base fee of $12 plus $4.50 per hour of usage. Which function $C(h)$ gives the total rental cost in dollars for $h$ hours?",
    "Which choice is the correct function?",
    ["$C(h) = 4.50h + 12$", "$C(h) = 12h + 4.50$", "$C(h) = 16.50h$", "$C(h) = 4.50(h + 12)$"],
    "A",
    "Choice A is correct. The base fee is the y-intercept (12) and the hourly rate is the slope (4.50), yielding $C(h) = 4.50h + 12$."
))

math1.append(make_mcq(
    "t3-math-m1-q3", DOMAINS["MATH"]["ALG"], "Systems of Two Linear Equations", "Medium",
    "What is the value of $y$ in the solution $(x, y)$ to the system of equations?<br>$$4x + y = 25$$<br>$$2x - 3y = 9$$",
    "Which choice is the value of $y$?",
    ["1", "3", "6", "-1"],
    "A",
    "Choice A is correct. Multiply the second equation by 2: $4x - 6y = 18$. Subtract this from the first equation: $(4x + y) - (4x - 6y) = 25 - 18 \\implies 7y = 7 \\implies y = 1$."
))

math1.append(make_mcq(
    "t3-math-m1-q4", DOMAINS["MATH"]["ALG"], "Linear Slopes & Perpendicular Lines", "Medium",
    "Line $j$ passes through the points $(1, 4)$ and $(5, 12)$. Line $k$ is perpendicular to line $j$. What is the slope of line $k$?",
    "Which choice is the slope of line $k$?",
    ["$-\\frac{1}{2}$", "$\\frac{1}{2}$", "$-2$", "$2$"],
    "A",
    "Choice A is correct. The slope of line $j$ is $m_j = \\frac{12 - 4}{5 - 1} = \\frac{8}{4} = 2$. Perpendicular lines have negative reciprocal slopes, so $m_k = -\\frac{1}{2}$."
))

math1.append(make_mcq(
    "t3-math-m1-q5", DOMAINS["MATH"]["ALG"], "Linear Inequalities", "Medium",
    "A baker has at most 50 pounds of flour available. Each batch of cookies requires 2.5 pounds of flour, and each loaf of bread requires 4 pounds of flour. If the baker makes 6 loaves of bread, what is the maximum number of batches of cookies they can bake?",
    "Which choice is the maximum number of batches?",
    ["10", "11", "9", "12"],
    "A",
    "Choice A is correct. Let $c$ be batches of cookies: $2.5c + 4(6) \\le 50 \\implies 2.5c + 24 \\le 50 \\implies 2.5c \\le 26 \\implies c \\le 10.4$. The maximum number of whole batches is 10."
))

math1.append(make_mcq(
    "t3-math-m1-q6", DOMAINS["MATH"]["ALG"], "Linear Modeling Interpretation", "Medium",
    "A water reservoir's volume $V(d)$ in thousands of gallons $d$ days after the start of a dry season is modeled by $V(d) = 850 - 14.5d$. What does the number 14.5 represent in this context?",
    "Which choice is the best interpretation?",
    [
        "The reservoir loses approximately 14.5 thousand gallons of water each day.",
        "The initial capacity of the reservoir was 14.5 thousand gallons.",
        "The reservoir will be completely empty in 14.5 days.",
        "The maximum daily evaporation rate is 14.5 percent."
    ],
    "A",
    "Choice A is correct. The slope $-14.5$ indicates the rate of change: a decrease of 14.5 thousand gallons of water per day."
))

math1.append(make_mcq(
    "t3-math-m1-q7", DOMAINS["MATH"]["ALG"], "Linear Systems No Solution", "Hard",
    "In the system of equations below, $b$ is a constant:<br>$$6x - 9y = 24$$<br>$$2x - 3y = b$$<br>If the system has infinitely many solutions, what is the value of $b$?",
    "Which choice is the value of $b$?",
    ["8", "12", "24", "4"],
    "A",
    "Choice A is correct. Divide the first equation by 3: $2x - 3y = 8$. For infinitely many solutions, the two equations must be identical, so $b = 8$."
))

math1.append(make_mcq(
    "t3-math-m1-q8", DOMAINS["MATH"]["ALG"], "Linear Equations in One Variable", "Easy",
    "If $2(4x + 3) - 5 = 3(2x + 5)$, what is the value of $x$?",
    "Which choice is the value of $x$?",
    ["7", "5", "8", "6"],
    "A",
    "Choice A is correct. Expand both sides: $8x + 6 - 5 = 6x + 15 \\implies 8x + 1 = 6x + 15 \\implies 2x = 14 \\implies x = 7$."
))

# 9-16 Advanced Math
math1.append(make_mcq(
    "t3-math-m1-q9", DOMAINS["MATH"]["ADV"], "Quadratic Equations", "Easy",
    "What are the solutions to the quadratic equation $x^2 - 14x + 48 = 0$?",
    "Which choice gives the solutions?",
    ["$x = 6$ and $x = 8$", "$x = -6$ and $x = -8$", "$x = 4$ and $x = 12$", "$x = -4$ and $x = -12$"],
    "A",
    "Choice A is correct. Factoring gives $(x - 6)(x - 8) = 0$, so $x = 6$ and $x = 8$."
))

math1.append(make_mcq(
    "t3-math-m1-q10", DOMAINS["MATH"]["ADV"], "Vertex Form & Optimization", "Medium",
    "The function $f(x) = -3(x - 5)^2 + 45$ models the revenue in thousands of dollars for a new product priced at $x$ dollars. What product price maximizes revenue?",
    "Which choice is the price that maximizes revenue?",
    ["$5", "$45", "$15", "$3"],
    "A",
    "Choice A is correct. The vertex form $f(x) = a(x - h)^2 + k$ has its vertex at $(h, k) = (5, 45)$. Since $a = -3 < 0$, the maximum occurs at the x-coordinate of the vertex, which is $x = 5$."
))

math1.append(make_mcq(
    "t3-math-m1-q11", DOMAINS["MATH"]["ADV"], "Exponential Growth", "Medium",
    "An investment fund of $8,000 earns an annual interest rate of $7.5\\%$ compounded annually. Which function $A(t)$ gives the account balance after $t$ years?",
    "Which choice is the correct function?",
    ["$A(t) = 8,000(1.075)^t$", "$A(t) = 8,000(0.925)^t$", "$A(t) = 8,000 + 1.075t$", "$A(t) = 8,000(1.75)^t$"],
    "A",
    "Choice A is correct. The compound growth formula is $A(t) = P(1 + r)^t$. Here $P = 8,000$ and $r = 0.075$, giving $A(t) = 8,000(1.075)^t$."
))

math1.append(make_mcq(
    "t3-math-m1-q12", DOMAINS["MATH"]["ADV"], "Radicals & Fractional Exponents", "Medium",
    "Which of the following expressions is equivalent to $\\sqrt[4]{x^7}$ for all positive values of $x$?",
    "Which choice is equivalent?",
    ["$x^{7/4}$", "$x^{4/7}$", "$x^{28}$", "$x^3$"],
    "A",
    "Choice A is correct. By index exponent rules, $\\sqrt[n]{x^m} = x^{m/n}$. Thus $\\sqrt[4]{x^7} = x^{7/4}$."
))

math1.append(make_mcq(
    "t3-math-m1-q13", DOMAINS["MATH"]["ADV"], "Rational Expressions", "Medium",
    "Which expression is equivalent to $\\frac{x^2 - 25}{2x + 10}$ for all $x \\neq -5$?",
    "Which choice is equivalent?",
    ["$\\frac{x - 5}{2}$", "$\\frac{x + 5}{2}$", "$x - 5$", "$\\frac{x - 25}{2}$"],
    "A",
    "Choice A is correct. Factor numerator and denominator: $\\frac{(x - 5)(x + 5)}{2(x + 5)} = \\frac{x - 5}{2}$."
))

math1.append(make_mcq(
    "t3-math-m1-q14", DOMAINS["MATH"]["ADV"], "Polynomial Zeros & Factors", "Hard",
    "If $f(x) = 2x^3 - 3x^2 - 11x + 6$ has a zero at $x = 3$, what is the sum of the other two zeros?",
    "Which choice is the sum of the other two zeros?",
    ["$-1.5$", "$1.5$", "$-3$", "$0.5$"],
    "A",
    "Choice A is correct. In a cubic $ax^3 + bx^2 + cx + d = 0$, the sum of all three roots is $-b/a = -(-3)/2 = 1.5$. Since one root is $3$, the sum of the other two roots is $1.5 - 3 = -1.5$."
))

math1.append(make_mcq(
    "t3-math-m1-q15", DOMAINS["MATH"]["ADV"], "Nonlinear Systems", "Hard",
    "What is the positive y-value of the intersection of $y = x^2 - 7$ and $y = 3x + 3$?",
    "Which choice is the positive y-value?",
    ["18", "5", "12", "15"],
    "A",
    "Choice A is correct. Set equal: $x^2 - 7 = 3x + 3 \\implies x^2 - 3x - 10 = 0 \\implies (x - 5)(x + 2) = 0$. For $x = 5$, $y = 3(5) + 3 = 18$. For $x = -2$, $y = 3(-2) + 3 = -3$. The positive y-value is 18."
))

math1.append(make_mcq(
    "t3-math-m1-q16", DOMAINS["MATH"]["ADV"], "Radical Equations", "Hard",
    "What is the solution set of $\\sqrt{3x + 16} = x + 2$?",
    "Which choice is the valid solution set?",
    ["{3}", "{-4, 3}", "{-4}", "{5}"],
    "A",
    "Choice A is correct. Square both sides: $3x + 16 = x^2 + 4x + 4 \\implies x^2 + x - 12 = 0 \\implies (x + 4)(x - 3) = 0$. For $x = -4$, $\\sqrt{4} = 2 \\neq -2$ (extraneous). For $x = 3$, $\\sqrt{25} = 5 = 3 + 2$ (valid). Solution set is {3}."
))

# 17-22 Problem-Solving and Data Analysis
math1.append(make_mcq(
    "t3-math-m1-q17", DOMAINS["MATH"]["PSDA"], "Percentages & Consecutive Discounts", "Easy",
    "A laptop listed at $800 is discounted by $15\\%$. An additional employee discount of $5\\%$ is applied to the discounted price. What is the final price of the laptop?",
    "Which choice is the final price?",
    ["$646", "$640", "$650", "$660"],
    "A",
    "Choice A is correct. After 15% discount: $800 \\times 0.85 = $680. After additional 5% discount: $680 \\times 0.95 = $646."
))

math1.append(make_mcq(
    "t3-math-m1-q18", DOMAINS["MATH"]["PSDA"], "Ratios and Rates", "Easy",
    "A factory machine produces 180 plastic components in 45 minutes. At this constant rate, how many components will the machine produce in 2.5 hours?",
    "Which choice is the number of components?",
    ["600", "540", "450", "720"],
    "A",
    "Choice A is correct. Rate $= \\frac{180 \\text{ components}}{45 \\text{ min}} = 4 \\text{ components/min}$. In 2.5 hours ($2.5 \\times 60 = 150 \\text{ minutes}$): $4 \\times 150 = 600$ components."
))

table_t3_q19 = "<table style='width: 80%; border-collapse: collapse; margin: 10px auto; font-size: 13px;'><thead><tr style='background: #f1f5f9;'><th style='padding: 6px; border: 1px solid #cbd5e1;'>Subscription</th><th style='padding: 6px; border: 1px solid #cbd5e1;'>Under 30</th><th style='padding: 6px; border: 1px solid #cbd5e1;'>30 and Older</th><th style='padding: 6px; border: 1px solid #cbd5e1;'>Total</th></tr></thead><tbody><tr><td style='padding: 6px; border: 1px solid #cbd5e1;'>Basic Tier</td><td style='padding: 6px; border: 1px solid #cbd5e1; text-align: center;'>50</td><td style='padding: 6px; border: 1px solid #cbd5e1; text-align: center;'>70</td><td style='padding: 6px; border: 1px solid #cbd5e1; text-align: center;'>120</td></tr><tr><td style='padding: 6px; border: 1px solid #cbd5e1;'>Premium Tier</td><td style='padding: 6px; border: 1px solid #cbd5e1; text-align: center;'>80</td><td style='padding: 6px; border: 1px solid #cbd5e1; text-align: center;'>40</td><td style='padding: 6px; border: 1px solid #cbd5e1; text-align: center;'>120</td></tr><tr><td style='padding: 6px; border: 1px solid #cbd5e1;'>Total</td><td style='padding: 6px; border: 1px solid #cbd5e1; text-align: center;'>130</td><td style='padding: 6px; border: 1px solid #cbd5e1; text-align: center;'>110</td><td style='padding: 6px; border: 1px solid #cbd5e1; text-align: center;'>240</td></tr></tbody></table>"
math1.append(make_mcq(
    "t3-math-m1-q19", DOMAINS["MATH"]["PSDA"], "Two-Way Frequency Tables", "Medium",
    table_t3_q19 + "<br>The table summarizes subscription tiers for 240 streaming service users.",
    "If a subscriber selected at random is under 30 years old, what is the probability that the subscriber is on the Premium Tier?",
    ["$\\frac{80}{130}$", "$\\frac{80}{120}$", "$\\frac{80}{240}$", "$\\frac{50}{130}$"],
    "A",
    "Choice A is correct. The given condition restricts the sample space to subscribers under 30 (total = 130). Among those 130 users, 80 are on the Premium Tier. Thus the probability is $\\frac{80}{130}$ (or $\\frac{8}{13}$)."
))

math1.append(make_mcq(
    "t3-math-m1-q20", DOMAINS["MATH"]["PSDA"], "Linear Regression Residuals", "Medium",
    "A linear model predicts house price $\\hat{y}$ in thousands of dollars from square footage $x$: $\\hat{y} = 0.15x + 80$. A house with 2,000 square feet was sold for $395,000 ($395 thousand). What is the residual of this prediction in thousands of dollars?",
    "Which choice is the residual?",
    ["15", "-15", "20", "-20"],
    "A",
    "Choice A is correct. Predicted price: $\\hat{y} = 0.15(2,000) + 80 = 300 + 80 = 380$ thousand dollars. Residual $= \\text{Actual} - \\text{Predicted} = 395 - 380 = 15$ thousand dollars."
))

math1.append(make_mcq(
    "t3-math-m1-q21", DOMAINS["MATH"]["PSDA"], "Margin of Error & Sample Size", "Hard",
    "A survey of 625 registered voters found that $58\\%$ favor a new municipal conservation referendum, with a margin of error of $\\pm 3.9\\%$ at a $95\\%$ confidence level. Which of the following is the most appropriate conclusion?",
    "Which choice is the most appropriate conclusion?",
    [
        "It is likely that between $54.1\\%$ and $61.9\\%$ of all registered voters in the municipality favor the referendum.",
        "Exactly $58\\%$ of all registered voters favor the referendum.",
        "If 625 different voters were surveyed, the percentage favoring the referendum would definitely remain $58\\%$.",
        "The referendum is guaranteed to pass with at least $60\\%$ of the vote."
    ],
    "A",
    "Choice A is correct. The confidence interval is $58\\% \\pm 3.9\\% = [54.1\\%, 61.9\\%]$, indicating that the true population proportion likely falls within this range."
))

math1.append(make_mcq(
    "t3-math-m1-q22", DOMAINS["MATH"]["PSDA"], "Weighted Average", "Medium",
    "A course grade is calculated from three components: homework ($20\\%$, score 90), midterm ($30\\%$, score 80), and final exam ($50\\%$, score 92). What is the student's final weighted course score?",
    "Which choice is the weighted score?",
    ["88", "86", "90", "87"],
    "A",
    "Choice A is correct. Weighted score $= 0.20(90) + 0.30(80) + 0.50(92) = 18 + 24 + 46 = 88$."
))

# 23-27 Geometry & Trig (SPR Grid-Ins for 23-27)
math1.append(make_spr(
    "t3-math-m1-q23", DOMAINS["MATH"]["GEOM"], "Right Triangle Trigonometry", "Medium",
    "In right triangle $DEF$ with right angle at $E$, side $DE = 12$ and side $EF = 5$. What is the value of $\\cos(D)$?",
    "Enter the exact fractional or decimal value of $\\cos(D)$:",
    ["12/13", "0.923"],
    "The answer is 12/13 (or approx 0.923). In right triangle $DEF$, the hypotenuse is $DF = \\sqrt{12^2 + 5^2} = \\sqrt{169} = 13$. The adjacent side to angle $D$ is $DE = 12$. Thus $\\cos(D) = \\frac{\\text{adj}}{\\text{hyp}} = \\frac{12}{13}$."
))

math1.append(make_spr(
    "t3-math-m1-q24", DOMAINS["MATH"]["GEOM"], "Circle Equations", "Medium",
    "A circle in the xy-plane has equation $(x - 7)^2 + (y + 4)^2 = 144$. What is the radius of the circle?",
    "Enter the radius:",
    ["12"],
    "The answer is 12. In the equation $(x - h)^2 + (y - k)^2 = r^2$, $r^2 = 144 \\implies r = 12$."
))

math1.append(make_spr(
    "t3-math-m1-q25", DOMAINS["MATH"]["GEOM"], "Arc Length", "Hard",
    "A circle has a radius of 15 cm. A central angle of $\\frac{4\\pi}{5}$ radians intercepts an arc of length $k\\pi$ cm. What is the value of $k$?",
    "Enter the value of $k$:",
    ["12"],
    "The answer is 12. Arc length $s = r\\theta = 15 \\times \\frac{4\\pi}{5} = 3 \\times 4\\pi = 12\\pi$. Thus $k = 12$."
))

math1.append(make_spr(
    "t3-math-m1-q26", DOMAINS["MATH"]["ALG"], "Linear Equations", "Easy",
    "If $7x - 8 = 48$, what is the value of $14x - 16$?",
    "Enter the value:",
    ["96"],
    "The answer is 96. Notice that $14x - 16 = 2(7x - 8) = 2(48) = 96$."
))

math1.append(make_spr(
    "t3-math-m1-q27", DOMAINS["MATH"]["GEOM"], "Cone Volume", "Medium",
    "A right circular cone has a base radius of 6 cm and a height of 10 cm. The volume of the cone is $k\\pi$ cubic centimeters. What is the value of $k$?",
    "Enter the value of $k$:",
    ["120"],
    "The answer is 120. Volume of cone $V = \\frac{1}{3}\\pi r^2 h = \\frac{1}{3}\\pi (6^2)(10) = \\frac{1}{3}\\pi (36)(10) = 120\\pi$. Thus $k = 120$."
))

# ==========================================
# TEST 3 - MATH MODULE 2 (27 Qs)
# ==========================================

# 1-8 Algebra
math2.append(make_mcq(
    "t3-math-m2-q1", DOMAINS["MATH"]["ALG"], "Linear Systems No Solution", "Hard",
    "In the system of equations below, $c$ is a constant:<br>$$cx - 8y = 15$$<br>$$3x - 12y = 20$$<br>If the system has no solution, what is the value of $c$?",
    "Which choice is the value of $c$?",
    ["2", "-2", "4", "6"],
    "A",
    "Choice A is correct. A system has no solution when the slopes are equal but intercepts differ. Slope of the second line is $\\frac{3}{12} = \\frac{1}{4}$. Slope of the first line is $\\frac{c}{8}$. Setting $\\frac{c}{8} = \\frac{1}{4} \\implies c = 2$."
))

math2.append(make_mcq(
    "t3-math-m2-q2", DOMAINS["MATH"]["ALG"], "Absolute Value Equations", "Medium",
    "What is the positive difference between the two solutions to $|4x - 8| = 24$?",
    "Which choice is the difference?",
    ["12", "8", "16", "6"],
    "A",
    "Choice A is correct. Case 1: $4x - 8 = 24 \\implies 4x = 32 \\implies x = 8$. Case 2: $4x - 8 = -24 \\implies 4x = -16 \\implies x = -4$. The difference between the solutions is $8 - (-4) = 12$."
))

math2.append(make_mcq(
    "t3-math-m2-q3", DOMAINS["MATH"]["ALG"], "Multi-Variable Systems", "Hard",
    "If $5x - 3y = 21$ and $2x + y = 4$, what is the value of $x + y$?",
    "Which choice is the value of $x + y$?",
    ["1", "3", "-1", "5"],
    "A",
    "Choice A is correct. From second eq, $y = 4 - 2x$. Substitute into first: $5x - 3(4 - 2x) = 21 \\implies 5x - 12 + 6x = 21 \\implies 11x = 33 \\implies x = 3$. Then $y = 4 - 2(3) = -2$. Thus $x + y = 3 + (-2) = 1$."
))

math2.append(make_mcq(
    "t3-math-m2-q4", DOMAINS["MATH"]["ALG"], "System of Linear Inequalities", "Hard",
    "Which point $(x, y)$ is in the solution region of the system of inequalities?<br>$$y \\ge 3x - 4$$<br>$$y < -2x + 8$$",
    "Which choice is in the solution region?",
    ["(1, 2)", "(3, 10)", "(0, 10)", "(4, 2)"],
    "A",
    "Choice A is correct. Test $(1, 2)$: $2 \\ge 3(1) - 4 = -1$ (True). And $2 < -2(1) + 8 = 6$ (True). Both inequalities are satisfied."
))

math2.append(make_mcq(
    "t3-math-m2-q5", DOMAINS["MATH"]["ALG"], "Function Notation & Evaluation", "Medium",
    "For the function $h(x) = 5x + 9$, if $h(3a) = 54$, what is the value of $a$?",
    "Which choice is the value of $a$?",
    ["3", "5", "2", "6"],
    "A",
    "Choice A is correct. $h(3a) = 5(3a) + 9 = 15a + 9$. Setting $15a + 9 = 54 \\implies 15a = 45 \\implies a = 3$."
))

math2.append(make_mcq(
    "t3-math-m2-q6", DOMAINS["MATH"]["ALG"], "Linear Modeling Rate Comparison", "Hard",
    "Tank A has 400 gallons of water and drains at a rate of 15 gallons per minute. Tank B has 150 gallons of water and fills at a rate of 10 gallons per minute. After how many minutes will both tanks contain the exact same amount of water?",
    "Which choice is the number of minutes?",
    ["10", "12", "15", "8"],
    "A",
    "Choice A is correct. Set the two volume expressions equal: $400 - 15m = 150 + 10m \\implies 250 = 25m \\implies m = 10$ minutes."
))

math2.append(make_mcq(
    "t3-math-m2-q7", DOMAINS["MATH"]["ALG"], "Rearranging Scientific Formulas", "Medium",
    "The kinetic energy formula is $K = \\frac{1}{2}mv^2$. Which equation correctly expresses the velocity $v$ in terms of $K$ and $m$ for positive $v$?",
    "Which choice expresses $v$?",
    ["$v = \\sqrt{\\frac{2K}{m}}$", "$v = \\frac{2K}{m}$", "$v = \\sqrt{\\frac{K}{2m}}$", "$v = \\frac{\\sqrt{K}}{2m}$"],
    "A",
    "Choice A is correct. Multiply both sides by 2: $2K = mv^2$. Divide by $m$: $\\frac{2K}{m} = v^2$. Take the square root: $v = \\sqrt{\\frac{2K}{m}}$."
))

math2.append(make_mcq(
    "t3-math-m2-q8", DOMAINS["MATH"]["ALG"], "Perpendicular Lines", "Medium",
    "Line $u$ has equation $5x + 2y = 12$. Line $w$ is perpendicular to line $u$ and passes through the point $(5, -1)$. What is the y-intercept of line $w$?",
    "Which choice is the y-intercept of line $w$?",
    ["-3", "3", "-1", "5"],
    "A",
    "Choice A is correct. Slope of line $u$ is $-\\frac{5}{2}$. Perpendicular slope $m = \\frac{2}{5}$. Using point $(5, -1)$: $y - (-1) = \\frac{2}{5}(x - 5) \\implies y + 1 = \\frac{2}{5}x - 2 \\implies y = \\frac{2}{5}x - 3$. The y-intercept is $-3$."
))

# 9-17 Advanced Math
math2.append(make_mcq(
    "t3-math-m2-q9", DOMAINS["MATH"]["ADV"], "Discriminant Analysis", "Hard",
    "For what value of $c$ will the quadratic equation $4x^2 - 12x + c = 0$ have exactly one distinct real solution?",
    "Which choice is the value of $c$?",
    ["9", "36", "6", "12"],
    "A",
    "Choice A is correct. Exactly one real solution requires discriminant $b^2 - 4ac = 0$. Here $(-12)^2 - 4(4)(c) = 0 \\implies 144 - 16c = 0 \\implies 16c = 144 \\implies c = 9$."
))

math2.append(make_mcq(
    "t3-math-m2-q10", DOMAINS["MATH"]["ADV"], "Completing the Square & Minimum", "Hard",
    "What is the minimum value of the function $g(x) = x^2 - 10x + 31$?",
    "Which choice is the minimum value?",
    ["6", "5", "11", "31"],
    "A",
    "Choice A is correct. Complete the square: $g(x) = (x^2 - 10x + 25) + 31 - 25 = (x - 5)^2 + 6$. Since $(x - 5)^2 \\ge 0$, the minimum value is 6 (at $x = 5$)."
))

math2.append(make_mcq(
    "t3-math-m2-q11", DOMAINS["MATH"]["ADV"], "Exponential Decay Half-Life", "Hard",
    "A radioactive substance decays according to $N(t) = 400(0.5)^{t/15}$, where $t$ is measured in hours. How many hours will it take for the substance to decay to 25 grams?",
    "Which choice is the number of hours?",
    ["60", "45", "75", "30"],
    "A",
    "Choice A is correct. Set $400(0.5)^{t/15} = 25 \\implies (0.5)^{t/15} = \\frac{25}{400} = \\frac{1}{16} = (0.5)^4$. Equating exponents: $\\frac{t}{15} = 4 \\implies t = 60$ hours."
))

math2.append(make_mcq(
    "t3-math-m2-q12", DOMAINS["MATH"]["ADV"], "Polynomial Factor Theorem", "Hard",
    "If $x - 4$ is a factor of the polynomial $P(x) = x^3 - 6x^2 + kx - 8$, what is the value of $k$?",
    "Which choice is the value of $k$?",
    ["10", "-10", "8", "12"],
    "A",
    "Choice A is correct. By the Factor Theorem, $P(4) = 0$. $4^3 - 6(4^2) + k(4) - 8 = 0 \\implies 64 - 96 + 4k - 8 = 0 \\implies -40 + 4k = 0 \\implies 4k = 40 \\implies k = 10$."
))

math2.append(make_mcq(
    "t3-math-m2-q13", DOMAINS["MATH"]["ADV"], "Complex Number Division", "Hard",
    "What is the equivalent simplified form of $\\frac{8 + 6i}{1 + i}$, where $i = \\sqrt{-1}$?",
    "Which choice is the simplified form?",
    ["$7 - i$", "$7 + i$", "$1 + 7i$", "$8 + 6i$"],
    "A",
    "Choice A is correct. Multiply by conjugate $1 - i$: $\\frac{(8 + 6i)(1 - i)}{1^2 - i^2} = \\frac{8 - 8i + 6i - 6i^2}{1 - (-1)} = \\frac{8 - 2i + 6}{2} = \\frac{14 - 2i}{2} = 7 - i$."
))

math2.append(make_mcq(
    "t3-math-m2-q14", DOMAINS["MATH"]["ADV"], "Rational Expressions Simplification", "Hard",
    "Which expression is equivalent to $\\frac{3}{x - 3} - \\frac{2}{x + 2}$ for all valid $x$?",
    "Which choice is equivalent?",
    ["$\\frac{x + 12}{(x - 3)(x + 2)}$", "$\\frac{x}{(x - 3)(x + 2)}$", "$\\frac{1}{x - 5}$", "$\\frac{x - 12}{(x - 3)(x + 2)}$"],
    "A",
    "Choice A is correct. Find common denominator: $\\frac{3(x + 2) - 2(x - 3)}{(x - 3)(x + 2)} = \\frac{3x + 6 - 2x + 6}{(x - 3)(x + 2)} = \\frac{x + 12}{(x - 3)(x + 2)}$."
))

math2.append(make_mcq(
    "t3-math-m2-q15", DOMAINS["MATH"]["ADV"], "Nonlinear Systems of Equations", "Hard",
    "What is the x-coordinate of the intersection point of $y = 2x^2 - 4x + 1$ and $y = 4x - 7$?",
    "Which choice is the x-coordinate?",
    ["2", "4", "1", "3"],
    "A",
    "Choice A is correct. Equate the two equations: $2x^2 - 4x + 1 = 4x - 7 \\implies 2x^2 - 8x + 8 = 0 \\implies 2(x^2 - 4x + 4) = 0 \\implies 2(x - 2)^2 = 0 \\implies x = 2$."
))

math2.append(make_mcq(
    "t3-math-m2-q16", DOMAINS["MATH"]["ADV"], "Exponential Function Behavior", "Medium",
    "The value of a vehicle depreciates according to $V(t) = 32,000(0.85)^t$, where $t$ is years after purchase. What percentage of its value does the vehicle lose each year?",
    "Which choice is the annual percentage loss?",
    ["$15\\%$", "$85\\%$", "$32\\%$", "$1.5\\%$"],
    "A",
    "Choice A is correct. The decay factor is $0.85 = 1 - 0.15$, which corresponds to an annual loss of $15\\%$."
))

math2.append(make_mcq(
    "t3-math-m2-q17", DOMAINS["MATH"]["ADV"], "Rational Exponents Rules", "Hard",
    "If $x > 0$, what is the value of $n$ if $\\frac{\\sqrt[3]{x^5}}{\\sqrt{x^3}} = x^n$?",
    "Which choice is the value of $n$?",
    ["$\\frac{1}{6}$", "$-\\frac{1}{6}$", "$\\frac{2}{3}$", "$1$"],
    "A",
    "Choice A is correct. In exponent notation: $\\frac{x^{5/3}}{x^{3/2}} = x^{5/3 - 3/2} = x^{10/6 - 9/6} = x^{1/6}$. Thus $n = \\frac{1}{6}$."
))

# 18-22 Problem-Solving and Data Analysis
math2.append(make_mcq(
    "t3-math-m2-q18", DOMAINS["MATH"]["PSDA"], "Standard Deviation Comparison", "Hard",
    "Set X contains the integers {50, 50, 50, 50}. Set Y contains the integers {40, 45, 55, 60}. Which statement is correct?",
    "Which choice is correct?",
    [
        "Both sets have the same mean, but Set Y has a greater standard deviation.",
        "Set X has a greater mean and a greater standard deviation than Set Y.",
        "Both sets have the same standard deviation, but Set Y has a greater mean.",
        "Set Y has a smaller standard deviation than Set X."
    ],
    "A",
    "Choice A is correct. Both sets have a mean of 50. In Set X, all numbers equal 50 (standard deviation = 0). Set Y numbers deviate from 50, so Set Y has a strictly greater standard deviation."
))

math2.append(make_mcq(
    "t3-math-m2-q19", DOMAINS["MATH"]["PSDA"], "Margin of Error Interpretation", "Hard",
    "A poll of 1,000 citizens estimated that $62\\%$ favor clean energy subsidies with a margin of error of $\\pm 3.1\\%$ at $95\\%$ confidence. Which statement is the most valid conclusion?",
    "Which choice is the most valid conclusion?",
    [
        "It is plausible that between $58.9\\%$ and $65.1\\%$ of all citizens favor the subsidies.",
        "Exactly $62\\%$ of all citizens favor the subsidies.",
        "Every sample of 1,000 citizens will yield exactly $62\\%$ support.",
        "Support among citizens is guaranteed never to fall below $60\\%$."
    ],
    "A",
    "Choice A is correct. The $95\\%$ confidence interval is $62\\% \\pm 3.1\\% = [58.9\\%, 65.1\\%]$, so it is plausible that the true proportion lies in this range."
))

math2.append(make_mcq(
    "t3-math-m2-q20", DOMAINS["MATH"]["PSDA"], "Conditional Probability", "Hard",
    "In a manufacturing facility, Machine A produces $60\\%$ of all components and Machine B produces $40\\%$. Machine A has a $2\\%$ defect rate, while Machine B has a $5\\%$ defect rate. If a randomly chosen component is defective, what is the probability that it was produced by Machine A?",
    "Which choice is the probability?",
    ["$\\frac{12}{32}$", "$\\frac{20}{32}$", "$\\frac{2}{7}$", "$\\frac{6}{10}$"],
    "A",
    "Choice A is correct. Defective from A: $0.60 \\times 0.02 = 0.012$. Defective from B: $0.40 \\times 0.05 = 0.020$. Total defectives $= 0.012 + 0.020 = 0.032$. Probability produced by A $= \\frac{0.012}{0.032} = \\frac{12}{32} = \\frac{3}{8}$."
))

math2.append(make_mcq(
    "t3-math-m2-q21", DOMAINS["MATH"]["PSDA"], "Box Plot Analysis", "Medium",
    "The median score on an exam was 75, with an interquartile range (IQR) of 18. If the first quartile ($Q_1$) was 66, what was the third quartile ($Q_3$)?",
    "Which choice is $Q_3$?",
    ["84", "80", "93", "75"],
    "A",
    "Choice A is correct. By definition, $IQR = Q_3 - Q_1 \\implies 18 = Q_3 - 66 \\implies Q_3 = 66 + 18 = 84$."
))

math2.append(make_mcq(
    "t3-math-m2-q22", DOMAINS["MATH"]["PSDA"], "Unit Conversions", "Medium",
    "A high-speed train travels at 300 kilometers per hour. Given that 1 kilometer is 1,000 meters and 1 hour is 3,600 seconds, what is the train's speed in meters per second? (Round to the nearest whole number)",
    "Which choice is the speed?",
    ["83 m/s", "100 m/s", "75 m/s", "120 m/s"],
    "A",
    "Choice A is correct. $\\frac{300 \\times 1000}{3600} = \\frac{300,000}{3,600} \\approx 83.33$ meters per second."
))

# 23-27 Geometry & Trig (SPR Grid-Ins for 23-27)
math2.append(make_spr(
    "t3-math-m2-q23", DOMAINS["MATH"]["GEOM"], "Circle Completing the Square", "Hard",
    "A circle in the xy-plane has equation $x^2 + y^2 - 12x + 4y - 9 = 0$. What is the radius of the circle?",
    "Enter the radius:",
    ["7"],
    "The answer is 7. Complete squares: $(x^2 - 12x + 36) + (y^2 + 4y + 4) = 9 + 36 + 4 \\implies (x - 6)^2 + (y + 2)^2 = 49$. Since $r^2 = 49$, the radius is $r = 7$."
))

math2.append(make_spr(
    "t3-math-m2-q24", DOMAINS["MATH"]["GEOM"], "Similar Triangles & Area Ratio", "Hard",
    "Triangle $ABC$ is similar to triangle $XYZ$, with corresponding sides in the ratio $3:5$. If the area of triangle $ABC$ is 36 square centimeters, what is the area of triangle $XYZ$, in square centimeters?",
    "Enter the area:",
    ["100"],
    "The answer is 100. The area ratio of similar figures is the square of the side ratio: $\\frac{\\text{Area}(XYZ)}{\\text{Area}(ABC)} = \\left(\\frac{5}{3}\\right)^2 = \\frac{25}{9}$. Thus $\\text{Area}(XYZ) = 36 \\times \\frac{25}{9} = 4 \\times 25 = 100$."
))

math2.append(make_spr(
    "t3-math-m2-q25", DOMAINS["MATH"]["GEOM"], "Cofunction Trigonometric Identity", "Medium",
    "In a right triangle with acute angles $x^\\circ$ and $y^\\circ$, $\\sin(x^\\circ) = \\cos(48^\\circ)$. What is the value of $x$?",
    "Enter the degree value of $x$:",
    ["42"],
    "The answer is 42. Since $\\sin(x^\\circ) = \\cos(90^\\circ - x^\\circ)$, we have $90 - x = 48 \\implies x = 42$."
))

math2.append(make_spr(
    "t3-math-m2-q26", DOMAINS["MATH"]["ADV"], "Parabola Vertex Y-Value", "Hard",
    "What is the maximum value of the function $f(x) = -4x^2 + 16x - 7$?",
    "Enter the maximum value:",
    ["9"],
    "The answer is 9. The vertex x-coordinate is $x = -\\frac{16}{2(-4)} = 2$. Evaluating at $x = 2$: $f(2) = -4(2^2) + 16(2) - 7 = -16 + 32 - 7 = 9$."
))

math2.append(make_spr(
    "t3-math-m2-q27", DOMAINS["MATH"]["GEOM"], "Radian Conversion", "Easy",
    "An angle measures $135^\\circ$. In radians, the angle is $\\frac{k\\pi}{4}$. What is the value of the integer $k$?",
    "Enter the value of $k$:",
    ["3"],
    "The answer is 3. Convert degrees to radians: $135^\\circ \\times \\frac{\\pi}{180^\\circ} = \\frac{3\\pi}{4}$. Therefore $k = 3$."
))

print(f"Test 3 Math Module 1 ready: {len(math1)} questions.")
print(f"Test 3 Math Module 2 ready: {len(math2)} questions.")
