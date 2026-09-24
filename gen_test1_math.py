# gen_test1_math.py - Test 1 Math (54 questions: 27 Module 1, 27 Module 2)
import json
from generate_suite_all import DOMAINS, make_mcq, make_spr

math1 = []
math2 = []

# ==========================================
# TEST 1 - MATH MODULE 1 (27 Qs)
# ==========================================

# 1-8 Algebra
math1.append(make_mcq(
    "t1-math-m1-q1", DOMAINS["MATH"]["ALG"], "Linear Equations", "Easy",
    "If $4x + 12 = 36$, what is the value of $x + 3$?",
    "Which choice is the correct value?",
    ["9", "6", "12", "3"],
    "A",
    "Choice A is correct. Divide both sides of $4x + 12 = 36$ by 4: $\\frac{4(x + 3)}{4} = \\frac{36}{4} \\implies x + 3 = 9$."
))

math1.append(make_mcq(
    "t1-math-m1-q2", DOMAINS["MATH"]["ALG"], "Linear Functions", "Easy",
    "A catering company charges a flat equipment rental fee of $150 plus $28 per guest. Which function $C(g)$ models the total cost, in dollars, for $g$ guests?",
    "Which choice is the correct model?",
    ["$C(g) = 28g + 150$", "$C(g) = 150g + 28$", "$C(g) = 178g$", "$C(g) = 28(g + 150)$"],
    "A",
    "Choice A is correct. The flat fee is the y-intercept (150) and the per-guest rate is the slope (28), yielding $C(g) = 28g + 150$."
))

math1.append(make_mcq(
    "t1-math-m1-q3", DOMAINS["MATH"]["ALG"], "Systems of Two Linear Equations", "Medium",
    "Consider the system of equations:<br>$$2x + 3y = 19$$<br>$$x - y = 2$$",
    "What is the value of $x$?",
    ["5", "3", "7", "4"],
    "A",
    "Choice A is correct. From the second equation, $y = x - 2$. Substitute into the first: $2x + 3(x - 2) = 19 \\implies 2x + 3x - 6 = 19 \\implies 5x = 25 \\implies x = 5$."
))

math1.append(make_mcq(
    "t1-math-m1-q4", DOMAINS["MATH"]["ALG"], "Linear Graphs & Slopes", "Medium",
    "Line $k$ in the xy-plane passes through the points $(2, 7)$ and $(6, -1)$. Line $p$ is perpendicular to line $k$. What is the slope of line $p$?",
    "Which choice is the slope of line $p$?",
    ["$\\frac{1}{2}$", "$-\\frac{1}{2}$", "$-2$", "$2$"],
    "A",
    "Choice A is correct. The slope of line $k$ is $m_k = \\frac{-1 - 7}{6 - 2} = \\frac{-8}{4} = -2$. Perpendicular lines have negative reciprocal slopes, so $m_p = -\\frac{1}{-2} = \\frac{1}{2}$."
))

math1.append(make_mcq(
    "t1-math-m1-q5", DOMAINS["MATH"]["ALG"], "Linear Inequalities", "Medium",
    "A landscaper has a budget of at most $600 to purchase mulch and sod. Mulch costs $25 per cubic yard and sod costs $40 per roll. If the landscaper purchases 8 rolls of sod, what is the maximum number of cubic yards of mulch they can purchase?",
    "Which choice is the maximum number?",
    ["11", "12", "14", "10"],
    "A",
    "Choice A is correct. Let $m$ be cubic yards of mulch. $25m + 40(8) \\le 600 \\implies 25m + 320 \\le 600 \\implies 25m \\le 280 \\implies m \\le 11.2$. Since mulch is purchased in whole cubic yards, the maximum is 11."
))

math1.append(make_mcq(
    "t1-math-m1-q6", DOMAINS["MATH"]["ALG"], "Linear Equations in One Variable", "Medium",
    "If $3(2x - 5) + 4 = 5(x - 1) + 7$, what is the value of $x$?",
    "Which choice is the value of $x$?",
    ["18", "12", "15", "9"],
    "A",
    "Choice A is correct. Expand both sides: $6x - 15 + 4 = 5x - 5 + 7 \\implies 6x - 11 = 5x + 2 \\implies x = 13 + 0$ wait: $6x - 5x = 2 + 11 = 13$. Let's check: $3(2(13)-5) + 4 = 3(21) + 4 = 67$; $5(12) + 7 = 67$. So $x = 13$! Let's update choices to [\"13\", \"11\", \"15\", \"9\"]."
))
# Fix choice for q6
math1[-1]["choices"] = [{"letter": "A", "text": "13"}, {"letter": "B", "text": "11"}, {"letter": "C", "text": "15"}, {"letter": "D", "text": "9"}]
math1[-1]["explanation"] = "Choice A is correct. Expanding both sides gives $6x - 15 + 4 = 5x - 5 + 7$, which simplifies to $6x - 11 = 5x + 2$. Subtracting $5x$ and adding 11 yields $x = 13$."

math1.append(make_mcq(
    "t1-math-m1-q7", DOMAINS["MATH"]["ALG"], "Linear Systems", "Medium",
    "In the system of equations below, $c$ is a constant:<br>$$3x - 6y = 12$$<br>$$x - 2y = c$$<br>If the system has infinitely many solutions, what is the value of $c$?",
    "Which choice is the value of $c$?",
    ["4", "12", "2", "6"],
    "A",
    "Choice A is correct. Dividing the first equation $3x - 6y = 12$ by 3 gives $x - 2y = 4$. For the system to have infinitely many solutions, the two equations must be identical, so $c = 4$."
))

math1.append(make_mcq(
    "t1-math-m1-q8", DOMAINS["MATH"]["ALG"], "Interpreting Linear Models", "Medium",
    "The height $h(t)$, in feet, of a weather balloon $t$ minutes after release is given by $h(t) = 450 + 85t$. What does the number 85 represent in this context?",
    "Which choice is the best interpretation?",
    [
        "The balloon rises at an average rate of 85 feet per minute.",
        "The initial altitude of the balloon was 85 feet above sea level.",
        "The balloon will reach maximum altitude in 85 minutes.",
        "The total altitude gained by the balloon is 85 feet."
    ],
    "A",
    "Choice A is correct. The coefficient of $t$ (85) represents the rate of change of height per unit of time, which is 85 feet per minute."
))

# 9-16 Advanced Math
math1.append(make_mcq(
    "t1-math-m1-q9", DOMAINS["MATH"]["ADV"], "Quadratic Equations", "Easy",
    "What are the solutions to the equation $x^2 - 9x + 20 = 0$?",
    "Which choice gives the solutions?",
    ["$x = 4$ and $x = 5$", "$x = -4$ and $x = -5$", "$x = 2$ and $x = 10$", "$x = -2$ and $x = -10$"],
    "A",
    "Choice A is correct. Factoring the quadratic yields $(x - 4)(x - 5) = 0$, so $x = 4$ or $x = 5$."
))

math1.append(make_mcq(
    "t1-math-m1-q10", DOMAINS["MATH"]["ADV"], "Parabolas & Vertex Form", "Medium",
    "The function $f(x) = -2(x - 3)^2 + 18$ models the trajectory of a projectile. What is the maximum value of $f(x)$?",
    "Which choice is the maximum value?",
    ["18", "3", "-2", "36"],
    "A",
    "Choice A is correct. The quadratic function is in vertex form $f(x) = a(x - h)^2 + k$ with $a = -2 < 0$. The vertex is at $(3, 18)$, so the maximum value is 18."
))

math1.append(make_mcq(
    "t1-math-m1-q11", DOMAINS["MATH"]["ADV"], "Exponential Growth", "Medium",
    "An antique violin purchased in 2010 for $12,000 has increased in value by $6\\%$ each year. Which function $V(t)$ gives the value of the violin $t$ years after 2010?",
    "Which choice is the correct function?",
    ["$V(t) = 12,000(1.06)^t$", "$V(t) = 12,000(0.94)^t$", "$V(t) = 12,000 + 1.06t$", "$V(t) = 12,000(1.6)^t$"],
    "A",
    "Choice A is correct. The exponential growth model is $V(t) = P(1 + r)^t$. Here $P = 12,000$ and $r = 0.06$, giving $V(t) = 12,000(1.06)^t$."
))

math1.append(make_mcq(
    "t1-math-m1-q12", DOMAINS["MATH"]["ADV"], "Radicals & Fractional Exponents", "Medium",
    "Which expression is equivalent to $\\sqrt[3]{x^5}$ for all positive values of $x$?",
    "Which choice is equivalent?",
    ["$x^{5/3}$", "$x^{3/5}$", "$x^{15}$", "$x^2$"],
    "A",
    "Choice A is correct. By the definition of rational exponents, $\\sqrt[n]{x^m} = x^{m/n}$. Thus $\\sqrt[3]{x^5} = x^{5/3}$."
))

math1.append(make_mcq(
    "t1-math-m1-q13", DOMAINS["MATH"]["ADV"], "Rational Expressions", "Medium",
    "Which of the following is equivalent to $\\frac{x^2 - 16}{x + 4}$ for all $x \\neq -4$?",
    "Which choice is equivalent?",
    ["$x - 4$", "$x + 4$", "$x - 16$", "$-4$"],
    "A",
    "Choice A is correct. Factoring the numerator as a difference of squares: $x^2 - 16 = (x - 4)(x + 4)$. Dividing by $(x + 4)$ gives $x - 4$."
))

math1.append(make_mcq(
    "t1-math-m1-q14", DOMAINS["MATH"]["ADV"], "Polynomial Factors & Zeros", "Hard",
    "If $p(x) = x^3 - 4x^2 + kx - 12$ and $x - 3$ is a factor of $p(x)$, what is the value of $k$?",
    "Which choice is the value of $k$?",
    ["7", "-7", "3", "5"],
    "A",
    "Choice A is correct. By the Factor Theorem, if $x - 3$ is a factor, then $p(3) = 0$. So $3^3 - 4(3^2) + k(3) - 12 = 0 \\implies 27 - 36 + 3k - 12 = 0 \\implies -21 + 3k = 0 \\implies 3k = 21 \\implies k = 7$."
))

math1.append(make_mcq(
    "t1-math-m1-q15", DOMAINS["MATH"]["ADV"], "Nonlinear Systems", "Hard",
    "What is the positive y-coordinate of the intersection point of the system:<br>$$y = x^2 - 5$$<br>$$y = 2x + 3$$",
    "Which choice is the positive y-coordinate?",
    ["11", "4", "7", "9"],
    "A",
    "Choice A is correct. Equate the two expressions: $x^2 - 5 = 2x + 3 \\implies x^2 - 2x - 8 = 0 \\implies (x - 4)(x + 2) = 0$. For $x = 4$, $y = 2(4) + 3 = 11$. For $x = -2$, $y = 2(-2) + 3 = -1$. The positive y-coordinate is 11."
))

math1.append(make_mcq(
    "t1-math-m1-q16", DOMAINS["MATH"]["ADV"], "Radical Equations", "Hard",
    "What is the solution to $\\sqrt{2x + 15} = x$?",
    "Which choice is the valid solution?",
    ["5", "-3", "5 and -3", "15"],
    "A",
    "Choice A is correct. Square both sides: $2x + 15 = x^2 \\implies x^2 - 2x - 15 = 0 \\implies (x - 5)(x + 3) = 0$. Since $\\sqrt{2x + 15}$ must be non-negative, $x = -3$ is extraneous ($\\sqrt{9} \\neq -3$). Thus $x = 5$ is the only valid solution."
))

# 17-22 Problem-Solving and Data Analysis
math1.append(make_mcq(
    "t1-math-m1-q17", DOMAINS["MATH"]["PSDA"], "Percentages", "Easy",
    "A tablet was originally priced at $400. During a holiday sale, its price was reduced by $20\\%$. An additional member coupon provided an extra $10\\%$ discount off the sale price. What was the final purchase price?",
    "Which choice is the final price?",
    ["$288", "$280", "$300", "$312"],
    "A",
    "Choice A is correct. After the 20% discount, the price is $400 \\times 0.80 = $320. The additional 10% discount off $320 gives $320 \\times 0.90 = $288."
))

math1.append(make_mcq(
    "t1-math-m1-q18", DOMAINS["MATH"]["PSDA"], "Ratios and Proportions", "Easy",
    "A blueprint uses a scale where 0.5 inches represents 12 feet. If a conference room measures 2.5 inches on the blueprint, what is the actual length of the room in feet?",
    "Which choice is the actual length?",
    ["60 feet", "48 feet", "72 feet", "50 feet"],
    "A",
    "Choice A is correct. Setting up the proportion: $\\frac{0.5\\text{ in}}{12\\text{ ft}} = \\frac{2.5\\text{ in}}{x\\text{ ft}}$. Cross-multiplying: $0.5x = 2.5 \\times 12 = 30 \\implies x = 60$ feet."
))

table_q19 = "<table style='width: 80%; border-collapse: collapse; margin: 10px auto; font-size: 13px;'><thead><tr style='background: #f1f5f9;'><th style='padding: 6px; border: 1px solid #cbd5e1;'>Grade</th><th style='padding: 6px; border: 1px solid #cbd5e1;'>Plays Sport</th><th style='padding: 6px; border: 1px solid #cbd5e1;'>Does Not Play</th><th style='padding: 6px; border: 1px solid #cbd5e1;'>Total</th></tr></thead><tbody><tr><td style='padding: 6px; border: 1px solid #cbd5e1;'>10th</td><td style='padding: 6px; border: 1px solid #cbd5e1; text-align: center;'>45</td><td style='padding: 6px; border: 1px solid #cbd5e1; text-align: center;'>55</td><td style='padding: 6px; border: 1px solid #cbd5e1; text-align: center;'>100</td></tr><tr><td style='padding: 6px; border: 1px solid #cbd5e1;'>11th</td><td style='padding: 6px; border: 1px solid #cbd5e1; text-align: center;'>60</td><td style='padding: 6px; border: 1px solid #cbd5e1; text-align: center;'>40</td><td style='padding: 6px; border: 1px solid #cbd5e1; text-align: center;'>100</td></tr><tr><td style='padding: 6px; border: 1px solid #cbd5e1;'>Total</td><td style='padding: 6px; border: 1px solid #cbd5e1; text-align: center;'>105</td><td style='padding: 6px; border: 1px solid #cbd5e1; text-align: center;'>95</td><td style='padding: 6px; border: 1px solid #cbd5e1; text-align: center;'>200</td></tr></tbody></table>"
math1.append(make_mcq(
    "t1-math-m1-q19", DOMAINS["MATH"]["PSDA"], "Two-Way Tables & Probability", "Medium",
    table_q19 + "<br>The table shows the distribution of sports participation among 200 high school students.",
    "If a student who plays a sport is selected at random, what is the probability that the student is in the 11th grade?",
    ["$\\frac{60}{105}$", "$\\frac{60}{200}$", "$\\frac{60}{100}$", "$\\frac{45}{105}$"],
    "A",
    "Choice A is correct. The condition restricts the sample space to students who play a sport (total = 105). Among those 105 students, 60 are in the 11th grade. Thus the probability is $\\frac{60}{105}$ (or $\\frac{4}{7}$)."
))

math1.append(make_mcq(
    "t1-math-m1-q20", DOMAINS["MATH"]["PSDA"], "Scatterplots & Lines of Best Fit", "Medium",
    "A line of best fit for a dataset of study hours ($x$) and exam scores ($y$) is given by $\\hat{y} = 6.5x + 48$. For a student who studied for 6 hours, their actual exam score was 91. What is the residual for this student?",
    "Which choice is the residual?",
    ["4", "-4", "3", "-3"],
    "A",
    "Choice A is correct. The predicted score is $\\hat{y} = 6.5(6) + 48 = 39 + 48 = 87$. The residual is $\\text{Actual} - \\text{Predicted} = 91 - 87 = 4$."
))

math1.append(make_mcq(
    "t1-math-m1-q21", DOMAINS["MATH"]["PSDA"], "Margin of Error & Inferences", "Hard",
    "A representative random sample of 1,200 voters in a city found that $54\\%$ support a proposed park bond, with a margin of error of $\\pm 2.8\\%$ at a $95\\%$ confidence level. Which of the following is a plausible value for the true percentage of all city voters who support the bond?",
    "Which choice is plausible?",
    ["$53.5\\%$", "$57.2\\%$", "$50.5\\%$", "$58.0\\%$"],
    "A",
    "Choice A is correct. The confidence interval is $54\\% \\pm 2.8\\%$, which corresponds to the range $[51.2\\%, 56.8\\%]$. Only $53.5\\%$ lies inside this interval."
))

math1.append(make_mcq(
    "t1-math-m1-q22", DOMAINS["MATH"]["PSDA"], "Data Distributions & Mean", "Medium",
    "A dataset consists of 5 integers: 12, 15, 18, 22, and $x$. If the mean of the dataset is 19, what is the value of $x$?",
    "Which choice is the value of $x$?",
    ["28", "25", "30", "22"],
    "A",
    "Choice A is correct. The sum of 5 numbers with a mean of 19 is $5 \\times 19 = 95$. The sum of the four given numbers is $12 + 15 + 18 + 22 = 67$. Thus $x = 95 - 67 = 28$."
))

# 23-27 Geometry & Trig (SPR Grid-Ins for 23-27)
math1.append(make_spr(
    "t1-math-m1-q23", DOMAINS["MATH"]["GEOM"], "Right Triangle Trigonometry", "Medium",
    "In a right triangle $ABC$ with right angle at $C$, the length of side $AC = 8$ and the length of side $BC = 15$. What is the value of $\\tan(A)$?",
    "Enter the exact fractional or decimal value of $\\tan(A)$:",
    ["15/8", "1.875"],
    "The answer is 15/8 (or 1.875). In right triangle $ABC$, $\\tan(A) = \\frac{\\text{opposite}}{\\text{adjacent}} = \\frac{BC}{AC} = \\frac{15}{8} = 1.875$."
))

math1.append(make_spr(
    "t1-math-m1-q24", DOMAINS["MATH"]["GEOM"], "Circle Equations", "Medium",
    "A circle in the xy-plane is given by the equation $(x - 5)^2 + (y + 3)^2 = 64$. What is the diameter of this circle?",
    "Enter the diameter:",
    ["16"],
    "The answer is 16. The circle equation $(x - h)^2 + (y - k)^2 = r^2$ gives $r^2 = 64$, so the radius $r = 8$. The diameter is $2r = 2(8) = 16$."
))

math1.append(make_spr(
    "t1-math-m1-q25", DOMAINS["MATH"]["GEOM"], "Arc Length & Radians", "Hard",
    "A circle has a radius of 12 cm. An arc subtended by a central angle of $\\frac{\\pi}{3}$ radians has length $k\\pi$ cm. What is the value of $k$?",
    "Enter the value of $k$:",
    ["4"],
    "The answer is 4. Arc length is $s = r\\theta = 12 \\times \\frac{\\pi}{3} = 4\\pi$. Therefore $k = 4$."
))

math1.append(make_spr(
    "t1-math-m1-q26", DOMAINS["MATH"]["ALG"], "Linear Equations", "Easy",
    "If $5x + 7 = 32$, what is the value of $10x + 14$?",
    "Enter the value:",
    ["64"],
    "The answer is 64. Notice that $10x + 14 = 2(5x + 7) = 2(32) = 64$."
))

math1.append(make_spr(
    "t1-math-m1-q27", DOMAINS["MATH"]["GEOM"], "Volume of 3D Solids", "Medium",
    "A rectangular prism has a length of 6 cm, a width of 4 cm, and a height of 9 cm. What is the total volume of the prism, in cubic centimeters?",
    "Enter the volume:",
    ["216"],
    "The answer is 216. Volume $V = l \\times w \\times h = 6 \\times 4 \\times 9 = 216$ cubic centimeters."
))

# ==========================================
# TEST 1 - MATH MODULE 2 (27 Qs)
# ==========================================

# 1-8 Algebra
math2.append(make_mcq(
    "t1-math-m2-q1", DOMAINS["MATH"]["ALG"], "Linear Systems No Solution", "Hard",
    "In the system of equations below, $k$ is a constant:<br>$$kx - 6y = 14$$<br>$$4x - 8y = 19$$<br>If the system has no solution, what is the value of $k$?",
    "Which choice is the value of $k$?",
    ["3", "-3", "4", "6"],
    "A",
    "Choice A is correct. A linear system has no solution when the lines are parallel (identical slopes, different y-intercepts). The slope of the second line is $\\frac{4}{8} = \\frac{1}{2}$. The slope of the first line is $\\frac{k}{6}$. Setting $\\frac{k}{6} = \\frac{1}{2} \\implies k = 3$."
))

math2.append(make_mcq(
    "t1-math-m2-q2", DOMAINS["MATH"]["ALG"], "Absolute Value Equations", "Medium",
    "What is the sum of the solutions to the equation $|3x - 12| = 18$?",
    "Which choice is the sum?",
    ["8", "12", "6", "10"],
    "A",
    "Choice A is correct. Case 1: $3x - 12 = 18 \\implies 3x = 30 \\implies x = 10$. Case 2: $3x - 12 = -18 \\implies 3x = -6 \\implies x = -2$. The sum of the solutions is $10 + (-2) = 8$."
))

math2.append(make_mcq(
    "t1-math-m2-q3", DOMAINS["MATH"]["ALG"], "Multi-Variable Linear Systems", "Hard",
    "If $2a + 3b = 17$ and $4a + b = 9$, what is the value of $a + b$?",
    "Which choice is the value of $a + b$?",
    ["6", "5", "7", "8"],
    "A",
    "Choice A is correct. Adding the two equations: $(2a + 3b) + (4a + b) = 17 + 9 \\implies 6a + 4b = 26$. Let's solve: from second eq, $b = 9 - 4a$. Substitute into first: $2a + 3(9 - 4a) = 17 \\implies 2a + 27 - 12a = 17 \\implies -10a = -10 \\implies a = 1$. Then $b = 9 - 4(1) = 5$. Thus $a + b = 1 + 5 = 6$."
))

math2.append(make_mcq(
    "t1-math-m2-q4", DOMAINS["MATH"]["ALG"], "Linear Inequalities", "Hard",
    "Which point $(x, y)$ satisfies the system of inequalities?<br>$$y > 2x + 1$$<br>$$y \\le -x + 6$$",
    "Which choice is a valid point?",
    ["(1, 4)", "(2, 1)", "(0, 0)", "(3, 8)"],
    "A",
    "Choice A is correct. Test $(1, 4)$: $4 > 2(1) + 1 \\implies 4 > 3$ (True). And $4 \\le -(1) + 6 \\implies 4 \\le 5$ (True). Both inequalities are satisfied."
))

math2.append(make_mcq(
    "t1-math-m2-q5", DOMAINS["MATH"]["ALG"], "Function Notation", "Medium",
    "For the function $g(x) = 4x - 7$, if $g(2k) = 25$, what is the value of $k$?",
    "Which choice is the value of $k$?",
    ["4", "8", "2", "6"],
    "A",
    "Choice A is correct. $g(2k) = 4(2k) - 7 = 8k - 7$. Setting $8k - 7 = 25 \\implies 8k = 32 \\implies k = 4$."
))

math2.append(make_mcq(
    "t1-math-m2-q6", DOMAINS["MATH"]["ALG"], "Linear Modeling", "Hard",
    "A freight company charges a base shipping cost plus an additional rate per pound. For an 8-pound crate, the cost is $34. For a 20-pound crate, the cost is $70. What would be the cost to ship a 32-pound crate?",
    "Which choice is the cost?",
    ["$106", "$98", "$112", "$102"],
    "A",
    "Choice A is correct. The rate per pound is $m = \\frac{70 - 34}{20 - 8} = \\frac{36}{12} = 3$ dollars per pound. Base fee: $34 - 3(8) = $10. For 32 pounds: Cost $= 10 + 3(32) = 10 + 96 = $106."
))

math2.append(make_mcq(
    "t1-math-m2-q7", DOMAINS["MATH"]["ALG"], "Rearranging Formulas", "Medium",
    "The formula for the period of a simple pendulum is $T = 2\\pi\\sqrt{\\frac{L}{g}}$. Which equation correctly expresses the length $L$ in terms of $T, \\pi$, and $g$?",
    "Which choice expresses $L$?",
    ["$L = \\frac{g T^2}{4\\pi^2}$", "$L = \\frac{4\\pi^2 g}{T^2}$", "$L = \\frac{T^2}{2\\pi g}$", "$L = \\frac{2\\pi g}{T^2}$"],
    "A",
    "Choice A is correct. Divide by $2\\pi$: $\\frac{T}{2\\pi} = \\sqrt{\\frac{L}{g}}$. Square both sides: $\\frac{T^2}{4\\pi^2} = \\frac{L}{g}$. Multiply by $g$: $L = \\frac{g T^2}{4\\pi^2}$."
))

math2.append(make_mcq(
    "t1-math-m2-q8", DOMAINS["MATH"]["ALG"], "Perpendicular Lines", "Medium",
    "Line $m$ has the equation $3x - 4y = 8$. Line $n$ is perpendicular to line $m$ and passes through the point $(6, 2)$. What is the y-intercept of line $n$?",
    "Which choice is the y-intercept?",
    ["10", "-6", "8", "6"],
    "A",
    "Choice A is correct. Line $m$ has slope $\\frac{3}{4}$. Line $n$ has perpendicular slope $-\\frac{4}{3}$. Using point-slope form with $(6, 2)$: $y - 2 = -\\frac{4}{3}(x - 6) \\implies y - 2 = -\\frac{4}{3}x + 8 \\implies y = -\\frac{4}{3}x + 10$. The y-intercept is 10."
))

# 9-17 Advanced Math
math2.append(make_mcq(
    "t1-math-m2-q9", DOMAINS["MATH"]["ADV"], "Discriminant Analysis", "Hard",
    "In the quadratic equation $2x^2 - 8x + c = 0$, $c$ is a constant. If the equation has exactly one real solution, what is the value of $c$?",
    "Which choice is the value of $c$?",
    ["8", "16", "4", "32"],
    "A",
    "Choice A is correct. A quadratic equation has exactly one real solution when its discriminant is zero: $b^2 - 4ac = 0$. Here $(-8)^2 - 4(2)(c) = 0 \\implies 64 - 8c = 0 \\implies 8c = 64 \\implies c = 8$."
))

math2.append(make_mcq(
    "t1-math-m2-q10", DOMAINS["MATH"]["ADV"], "Vertex Form & Optimization", "Hard",
    "What is the minimum value of the quadratic function $f(x) = x^2 - 14x + 60$?",
    "Which choice is the minimum value?",
    ["11", "7", "-11", "25"],
    "A",
    "Choice A is correct. Complete the square: $f(x) = (x^2 - 14x + 49) + 60 - 49 = (x - 7)^2 + 11$. Since $(x - 7)^2 \\ge 0$, the minimum value is 11, occurring at $x = 7$."
))

math2.append(make_mcq(
    "t1-math-m2-q11", DOMAINS["MATH"]["ADV"], "Exponential Decay & Half-Life", "Hard",
    "A radioactive isotope has an initial mass of 120 grams and a half-life of 8 days. Which equation models the remaining mass $M(t)$, in grams, after $t$ days?",
    "Which choice is the correct model?",
    ["$M(t) = 120\\left(\\frac{1}{2}\\right)^{t/8}$", "$M(t) = 120\\left(\\frac{1}{2}\\right)^{8t}$", "$M(t) = 120 - 8\\left(\\frac{1}{2}\\right)^t$", "$M(t) = 60(8)^t$"],
    "A",
    "Choice A is correct. The half-life decay formula is $M(t) = M_0\\left(\\frac{1}{2}\\right)^{t/h}$. With $M_0 = 120$ and half-life $h = 8$, the function is $M(t) = 120(1/2)^{t/8}$."
))

math2.append(make_mcq(
    "t1-math-m2-q12", DOMAINS["MATH"]["ADV"], "Polynomial Remainder Theorem", "Hard",
    "When the polynomial $P(x) = 2x^3 - 5x^2 + ax - 8$ is divided by $x - 2$, the remainder is 6. What is the value of $a$?",
    "Which choice is the value of $a$?",
    ["9", "5", "7", "11"],
    "A",
    "Choice A is correct. By the Remainder Theorem, $P(2) = 6$. Evaluating $P(2) = 2(2^3) - 5(2^2) + a(2) - 8 = 16 - 20 + 2a - 8 = 2a - 12$. Setting $2a - 12 = 6 \\implies 2a = 18 \\implies a = 9$."
))

math2.append(make_mcq(
    "t1-math-m2-q13", DOMAINS["MATH"]["ADV"], "Rational Equations", "Hard",
    "What is the sum of all values of $x$ that satisfy the equation $\\frac{6}{x - 2} + \\frac{x}{x + 2} = 2$?",
    "Which choice is the sum?",
    ["6", "4", "8", "2"],
    "A",
    "Choice A is correct. Multiply by $(x - 2)(x + 2)$: $6(x + 2) + x(x - 2) = 2(x^2 - 4) \\implies 6x + 12 + x^2 - 2x = 2x^2 - 8 \\implies x^2 + 4x + 12 = 2x^2 - 8 \\implies x^2 - 4x - 20 = 0$. By Vieta's formulas, the sum of roots is $-(-4)/1 = 4$ wait: let's recheck roots! $x^2 - 4x - 20 = 0$, both roots are real since $(-4)^2 - 4(1)(-20) = 96 > 0$ and neither is $\\pm 2$. Thus sum is 4! Let's update choices to [\"4\", \"6\", \"-4\", \"8\"]."
))
math2[-1]["choices"] = [{"letter": "A", "text": "4"}, {"letter": "B", "text": "6"}, {"letter": "C", "text": "-4"}, {"letter": "D", "text": "8"}]
math2[-1]["explanation"] = "Choice A is correct. Clearing denominators gives $6(x + 2) + x(x - 2) = 2(x^2 - 4)$, simplifying to $x^2 + 4x + 12 = 2x^2 - 8$, or $x^2 - 4x - 20 = 0$. By Vieta's formulas, the sum of roots $-b/a = -(-4)/1 = 4$."

math2.append(make_mcq(
    "t1-math-m2-q14", DOMAINS["MATH"]["ADV"], "Equivalent Radical Expressions", "Medium",
    "If $x > 0$, which expression is equivalent to $\\frac{\\sqrt{x^7}}{\\sqrt[4]{x^6}}$?",
    "Which choice is equivalent?",
    ["$x^2$", "$x^{5/2}$", "$x^{3/4}$", "$x$"],
    "A",
    "Choice A is correct. In exponent notation: $\\frac{x^{7/2}}{x^{6/4}} = \\frac{x^{7/2}}{x^{3/2}} = x^{7/2 - 3/2} = x^{4/2} = x^2$."
))

math2.append(make_mcq(
    "t1-math-m2-q15", DOMAINS["MATH"]["ADV"], "Nonlinear Graphs", "Hard",
    "The graph of $y = f(x)$ has x-intercepts at $(-4, 0)$, $(1, 0)$, and $(5, 0)$, and a y-intercept at $(0, -40)$. Which equation could define $f(x)$?",
    "Which choice defines $f(x)$?",
    ["$f(x) = 2(x + 4)(x - 1)(x - 5)$", "$f(x) = -2(x - 4)(x + 1)(x + 5)$", "$f(x) = (x + 4)(x - 1)(x - 5)$", "$f(x) = 4(x + 4)(x - 1)(x - 5)$"],
    "A",
    "Choice A is correct. The zeros give factors $(x + 4)(x - 1)(x - 5)$. For $f(0) = a(4)(-1)(-5) = 20a$. Setting $20a = -40 \\implies a = -2$ wait: $a(4)(-1)(-5) = +20a$. If $20a = -40$, then $a = -2$. But let's check choice A: if $a = 2$, $f(0) = 2(4)(-1)(-5) = +40$. If y-intercept is $(0, 40)$, then $a = 2$. Let's set y-intercept to $(0, 40)$!"
))
math2[-1]["stimulus"] = "The graph of $y = f(x)$ has x-intercepts at $(-4, 0)$, $(1, 0)$, and $(5, 0)$, and a y-intercept at $(0, 40)$. Which equation could define $f(x)$?"
math2[-1]["explanation"] = "Choice A is correct. With zeros at $-4, 1, 5$, the function has the form $f(x) = a(x + 4)(x - 1)(x - 5)$. Evaluating at $x = 0$: $f(0) = a(4)(-1)(-5) = 20a = 40 \\implies a = 2$."

math2.append(make_mcq(
    "t1-math-m2-q16", DOMAINS["MATH"]["ADV"], "Exponential Transformations", "Medium",
    "The function $g(x) = 3^{x + 2} - 5$ is a transformation of the parent function $f(x) = 3^x$. Which statement accurately describes the transformation?",
    "Which choice describes the transformation?",
    [
        "Shifted 2 units left and 5 units down",
        "Shifted 2 units right and 5 units down",
        "Shifted 2 units left and 5 units up",
        "Shifted 2 units right and 5 units up"
    ],
    "A",
    "Choice A is correct. In $f(x + c) - d$, adding 2 inside the exponent shifts the graph 2 units left, and subtracting 5 outside shifts it 5 units down."
))

math2.append(make_mcq(
    "t1-math-m2-q17", DOMAINS["MATH"]["ADV"], "Complex Numbers", "Hard",
    "What is the result of the expression $\\frac{5 + 2i}{3 - 4i}$, where $i = \\sqrt{-1}$?",
    "Which choice is the simplified result?",
    ["$\\frac{7}{25} + \\frac{26}{25}i$", "$\\frac{7}{25} - \\frac{26}{25}i$", "$\\frac{23}{7} + \\frac{14}{7}i$", "$\\frac{1}{5} + \\frac{2}{5}i$"],
    "A",
    "Choice A is correct. Multiply numerator and denominator by conjugate $3 + 4i$: $\\frac{(5 + 2i)(3 + 4i)}{3^2 - (4i)^2} = \\frac{15 + 20i + 6i + 8i^2}{9 - (-16)} = \\frac{15 + 26i - 8}{25} = \\frac{7 + 26i}{25} = \\frac{7}{25} + \\frac{26}{25}i$."
))

# 18-22 Problem-Solving and Data Analysis
math2.append(make_mcq(
    "t1-math-m2-q18", DOMAINS["MATH"]["PSDA"], "Standard Deviation Comparison", "Hard",
    "Dataset A consists of the values {20, 20, 20, 20, 20}. Dataset B consists of the values {10, 15, 20, 25, 30}. Which statement comparing the two datasets is true?",
    "Which choice is true?",
    [
        "Both datasets have the same mean, but Dataset B has a greater standard deviation.",
        "Both datasets have the same standard deviation, but Dataset B has a greater mean.",
        "Dataset A has a greater mean and a greater standard deviation than Dataset B.",
        "Dataset B has a smaller standard deviation than Dataset A."
    ],
    "A",
    "Choice A is correct. Both datasets have a mean of 20. In Dataset A, all values equal the mean, so standard deviation is 0. Dataset B has spread away from the mean, so its standard deviation is positive and thus greater than Dataset A's."
))

math2.append(make_mcq(
    "t1-math-m2-q19", DOMAINS["MATH"]["PSDA"], "Sample Validity", "Medium",
    "A high school principal wants to determine student satisfaction with the cafeteria menu. Which sampling method will provide the most representative, unbiased sample?",
    "Which choice is the best method?",
    [
        "Selecting 100 students at random from a complete alphabetical roster of all enrolled students.",
        "Surveying the first 100 students who enter the cafeteria on Monday morning.",
        "Asking members of the varsity athletics teams during their practice.",
        "Posting an online survey on the school social media page and collecting voluntary responses."
    ],
    "A",
    "Choice A is correct. Simple random sampling from the complete enrolled student roster gives every student an equal chance of selection, eliminating systematic bias."
))

math2.append(make_mcq(
    "t1-math-m2-q20", DOMAINS["MATH"]["PSDA"], "Exponential vs Linear Growth", "Medium",
    "Option A earns simple interest of $50 per year on an initial $1,000 deposit. Option B earns $4\\%$ annual compound interest on an initial $1,000 deposit. Which statement best describes their long-term growth?",
    "Which choice is correct?",
    [
        "Option B will eventually exceed Option A because compound interest grows exponentially while simple interest grows linearly.",
        "Option A will always remain greater than Option B because $50 > $40.",
        "Both options grow at identical constant rates indefinitely.",
        "Option A grows exponentially while Option B grows linearly."
    ],
    "A",
    "Choice A is correct. Simple interest is linear ($1000 + 50t$), whereas compound interest is exponential ($1000(1.04)^t$). Any exponential growth with base $> 1$ will eventually surpass any linear growth."
))

math2.append(make_mcq(
    "t1-math-m2-q21", DOMAINS["MATH"]["PSDA"], "Conditional Probability", "Hard",
    "In a medical study, $10\\%$ of patients have Condition X. A test correctly identifies the condition $90\\%$ of the time (true positive) and has a $5\\%$ false positive rate for healthy patients. Out of 1,000 patients, approximately how many who test positive actually have Condition X?",
    "Which choice is the closest approximation?",
    ["90 out of 135", "90 out of 100", "90 out of 900", "50 out of 100"],
    "A",
    "Choice A is correct. Out of 1,000 patients: 100 have Condition X; $90\\%$ test positive $= 90$. 900 are healthy; $5\\%$ false positive $= 45$. Total positive tests $= 90 + 45 = 135$. The fraction who actually have the condition is 90 out of 135 (about $66.7\\%$)."
))

math2.append(make_mcq(
    "t1-math-m2-q22", DOMAINS["MATH"]["PSDA"], "Unit Conversions", "Medium",
    "A pipeline transports fluid at a rate of 180 gallons per hour. Given that 1 gallon is approximately 3.785 liters, what is the flow rate in milliliters per second? (Round to the nearest whole number)",
    "Which choice is the rate?",
    ["189", "378", "681", "1,135"],
    "A",
    "Choice A is correct. $\\frac{180\\text{ gal}}{1\\text{ hr}} \\times \\frac{3.785\\text{ L}}{1\\text{ gal}} \\times \\frac{1000\\text{ mL}}{1\\text{ L}} \\times \\frac{1\\text{ hr}}{3600\\text{ s}} = \\frac{180 \\times 3785}{3600} = \\frac{681300}{3600} \\approx 189.25$ mL/s."
))

# 23-27 Geometry & Trig (SPR Grid-Ins for 23-27)
math2.append(make_spr(
    "t1-math-m2-q23", DOMAINS["MATH"]["GEOM"], "Circle Completing the Square", "Hard",
    "A circle in the xy-plane is given by the equation $x^2 + y^2 - 8x + 6y - 11 = 0$. What is the radius of the circle?",
    "Enter the radius:",
    ["6"],
    "The answer is 6. Group and complete squares: $(x^2 - 8x + 16) + (y^2 + 6y + 9) = 11 + 16 + 9 \\implies (x - 4)^2 + (y + 3)^2 = 36$. Since $r^2 = 36$, radius $r = 6$."
))

math2.append(make_spr(
    "t1-math-m2-q24", DOMAINS["MATH"]["GEOM"], "Similar Triangles & Area Ratio", "Hard",
    "Triangle $DEF$ is similar to triangle $ABC$, where each side of triangle $DEF$ is $2.5$ times the length of the corresponding side of triangle $ABC$. If the area of triangle $ABC$ is 16 square units, what is the area of triangle $DEF$?",
    "Enter the area:",
    ["100"],
    "The answer is 100. When lengths are scaled by a factor of $k = 2.5$, areas scale by $k^2 = (2.5)^2 = 6.25$. Area of $DEF = 16 \\times 6.25 = 100$."
))

math2.append(make_spr(
    "t1-math-m2-q25", DOMAINS["MATH"]["GEOM"], "Cofunction Trigonometric Identity", "Medium",
    "In a right triangle, acute angle $x$ satisfies $\\sin(x^\\circ) = \\cos(54^\\circ)$. What is the value of $x$?",
    "Enter the degree measure of $x$:",
    ["36"],
    "The answer is 36. For complementary acute angles in a right triangle, $\\sin(x^\\circ) = \\cos(90^\\circ - x^\\circ)$. Thus $90 - x = 54 \\implies x = 36$."
))

math2.append(make_spr(
    "t1-math-m2-q26", DOMAINS["MATH"]["ADV"], "Vertex of Parabola", "Medium",
    "What is the x-coordinate of the vertex of the parabola $y = 3x^2 - 24x + 55$?",
    "Enter the x-coordinate:",
    ["4"],
    "The answer is 4. The vertex x-coordinate is $x = -\\frac{b}{2a} = -\\frac{-24}{2(3)} = \\frac{24}{6} = 4$."
))

math2.append(make_spr(
    "t1-math-m2-q27", DOMAINS["MATH"]["GEOM"], "Radian Measure Conversion", "Easy",
    "An angle measures $\\frac{5\\pi}{6}$ radians. What is the measure of the angle in degrees?",
    "Enter the degree measure:",
    ["150"],
    "The answer is 150. Converting radians to degrees: $\\frac{5\\pi}{6} \\times \\frac{180^\\circ}{\\pi} = 5 \\times 30^\\circ = 150^\\circ$."
))

print(f"Test 1 Math Module 1 ready: {len(math1)} questions.")
print(f"Test 1 Math Module 2 ready: {len(math2)} questions.")
