# gen_test4_math.py - Practice Test 4 Math (54 questions: 27 Module 1, 27 Module 2)
import json
from generate_suite_all import DOMAINS, make_mcq, make_spr

math1 = []
math2 = []

# ==========================================
# TEST 4 - MATH MODULE 1 (27 Qs)
# ==========================================

# 1-8 Algebra
math1.append(make_mcq(
    "t4-math-m1-q1", DOMAINS["MATH"]["ALG"], "Linear Equations", "Easy",
    "If $6x + 18 = 42$, what is the value of $2x + 6$?",
    "Which choice is the correct value?",
    ["14", "18", "12", "8"],
    "A",
    "Choice A is correct. Divide both sides of $6x + 18 = 42$ by 3: $\\frac{6x + 18}{3} = \\frac{42}{3} \\implies 2x + 6 = 14$."
))

math1.append(make_mcq(
    "t4-math-m1-q2", DOMAINS["MATH"]["ALG"], "Linear Functions", "Easy",
    "A community pool charges a summer membership fee of $90 plus $6 for each visit. Which function $T(v)$ models the total seasonal expense in dollars for $v$ visits?",
    "Which choice is the correct model?",
    ["$T(v) = 6v + 90$", "$T(v) = 90v + 6$", "$T(v) = 96v$", "$T(v) = 6(v + 90)$"],
    "A",
    "Choice A is correct. The membership fee is the fixed constant ($90$) and the per-visit cost is the slope ($6$), giving $T(v) = 6v + 90$."
))

math1.append(make_mcq(
    "t4-math-m1-q3", DOMAINS["MATH"]["ALG"], "Systems of Two Linear Equations", "Medium",
    "What is the value of $x$ in the solution $(x, y)$ to the system of equations?<br>$$5x - 2y = 19$$<br>$$x + 2y = 5$$",
    "Which choice is the value of $x$?",
    ["4", "3", "5", "2"],
    "A",
    "Choice A is correct. Add the two equations: $(5x - 2y) + (x + 2y) = 19 + 5 \\implies 6x = 24 \\implies x = 4$."
))

math1.append(make_mcq(
    "t4-math-m1-q4", DOMAINS["MATH"]["ALG"], "Linear Slopes & Parallel Lines", "Medium",
    "Line $r$ has equation $4x - 6y = 18$. Line $s$ is parallel to line $r$ and has a y-intercept of $(0, -5)$. What is the equation of line $s$?",
    "Which choice is the equation of line $s$?",
    ["$y = \\frac{2}{3}x - 5$", "$y = -\\frac{3}{2}x - 5$", "$y = \\frac{3}{2}x - 5$", "$y = -\\frac{2}{3}x - 5$"],
    "A",
    "Choice A is correct. Solve line $r$ for $y$: $-6y = -4x + 18 \\implies y = \\frac{2}{3}x - 3$. Parallel lines have identical slopes ($m = \\frac{2}{3}$). With y-intercept $-5$, line $s$ is $y = \\frac{2}{3}x - 5$."
))

math1.append(make_mcq(
    "t4-math-m1-q5", DOMAINS["MATH"]["ALG"], "Linear Inequalities", "Medium",
    "A carpenter has at most $450 to purchase oak and pine lumber. Oak costs $30 per board and pine costs $15 per board. If the carpenter buys 8 boards of oak, what is the maximum number of pine boards they can purchase?",
    "Which choice is the maximum number of pine boards?",
    ["14", "15", "13", "16"],
    "A",
    "Choice A is correct. Let $p$ be pine boards: $30(8) + 15p \\le 450 \\implies 240 + 15p \\le 450 \\implies 15p \\le 210 \\implies p \\le 14$. The maximum number of pine boards is 14."
))

math1.append(make_mcq(
    "t4-math-m1-q6", DOMAINS["MATH"]["ALG"], "Interpreting Linear Models", "Medium",
    "The temperature $T(m)$ in degrees Celsius of an insulated cooling bath $m$ minutes after adding dry ice is modeled by $T(m) = 22 - 3.5m$. What does the value 22 represent?",
    "Which choice is the best interpretation?",
    [
        "The initial temperature of the cooling bath before dry ice was added",
        "The decrease in bath temperature per minute",
        "The time required for the bath to reach freezing",
        "The lowest temperature achievable by the bath"
    ],
    "A",
    "Choice A is correct. When $m = 0$, $T(0) = 22$. The constant term 22 represents the initial temperature of the bath before dry ice was added."
))

math1.append(make_mcq(
    "t4-math-m1-q7", DOMAINS["MATH"]["ALG"], "Linear Systems No Solution", "Hard",
    "In the system of equations below, $k$ is a constant:<br>$$kx - 10y = 30$$<br>$$3x - 5y = 14$$<br>If the system has no solution, what is the value of $k$?",
    "Which choice is the value of $k$?",
    ["6", "3", "-6", "5"],
    "A",
    "Choice A is correct. For no solution, lines must have identical slopes but different y-intercepts. Multiplying the second equation by 2 gives $6x - 10y = 28$. Comparing with $kx - 10y = 30$, we see $k = 6$ produces parallel lines ($30 \\neq 28$)."
))

math1.append(make_mcq(
    "t4-math-m1-q8", DOMAINS["MATH"]["ALG"], "Linear Equations in One Variable", "Easy",
    "If $5(2x - 3) = 3(3x + 1) + 2$, what is the value of $x$?",
    "Which choice is the value of $x$?",
    ["20", "15", "18", "12"],
    "A",
    "Choice A is correct. Expand both sides: $10x - 15 = 9x + 3 + 2 \\implies 10x - 15 = 9x + 5 \\implies x = 20$."
))

# 9-16 Advanced Math
math1.append(make_mcq(
    "t4-math-m1-q9", DOMAINS["MATH"]["ADV"], "Quadratic Equations", "Easy",
    "What are the solutions to the equation $x^2 - 13x + 36 = 0$?",
    "Which choice gives the solutions?",
    ["$x = 4$ and $x = 9$", "$x = -4$ and $x = -9$", "$x = 3$ and $x = 12$", "$x = -3$ and $x = -12$"],
    "A",
    "Choice A is correct. Factoring gives $(x - 4)(x - 9) = 0$, so $x = 4$ and $x = 9$."
))

math1.append(make_mcq(
    "t4-math-m1-q10", DOMAINS["MATH"]["ADV"], "Vertex Form & Optimization", "Medium",
    "The height $h(t)$ in feet of a firework rocket $t$ seconds after launch is modeled by $h(t) = -16(t - 3)^2 + 144$. What is the maximum height, in feet, reached by the rocket?",
    "Which choice is the maximum height?",
    ["144", "3", "48", "96"],
    "A",
    "Choice A is correct. The quadratic is in vertex form $h(t) = a(t - h)^2 + k$ with vertex $(3, 144)$. Since $a = -16 < 0$, the maximum height is 144 feet."
))

math1.append(make_mcq(
    "t4-math-m1-q11", DOMAINS["MATH"]["ADV"], "Exponential Growth", "Medium",
    "A rare coin was purchased for $1,500 in 2015. Its value has increased by $8\\%$ each year. Which function $V(t)$ models the value of the coin $t$ years after 2015?",
    "Which choice is the correct model?",
    ["$V(t) = 1,500(1.08)^t$", "$V(t) = 1,500(0.92)^t$", "$V(t) = 1,500 + 1.08t$", "$V(t) = 1,500(1.8)^t$"],
    "A",
    "Choice A is correct. In the exponential model $V(t) = P(1 + r)^t$, $P = 1,500$ and $r = 0.08$, yielding $V(t) = 1,500(1.08)^t$."
))

math1.append(make_mcq(
    "t4-math-m1-q12", DOMAINS["MATH"]["ADV"], "Radicals & Fractional Exponents", "Medium",
    "Which of the following is equivalent to $(27x^6)^{2/3}$ for all positive $x$?",
    "Which choice is equivalent?",
    ["$9x^4$", "$18x^4$", "$9x^9$", "$27x^4$"],
    "A",
    "Choice A is correct. Distribute the power: $27^{2/3} = (\\sqrt[3]{27})^2 = 3^2 = 9$. For the variable: $(x^6)^{2/3} = x^{6 \\times 2/3} = x^4$. Combining yields $9x^4$."
))

math1.append(make_mcq(
    "t4-math-m1-q13", DOMAINS["MATH"]["ADV"], "Rational Expressions", "Medium",
    "Which expression is equivalent to $\\frac{x^2 - 36}{3x + 18}$ for all $x \\neq -6$?",
    "Which choice is equivalent?",
    ["$\\frac{x - 6}{3}$", "$\\frac{x + 6}{3}$", "$x - 6$", "$\\frac{x - 36}{3}$"],
    "A",
    "Choice A is correct. Factor numerator and denominator: $\\frac{(x - 6)(x + 6)}{3(x + 6)} = \\frac{x - 6}{3}$."
))

math1.append(make_mcq(
    "t4-math-m1-q14", DOMAINS["MATH"]["ADV"], "Polynomial Zeros & Factors", "Hard",
    "The polynomial $p(x) = x^3 - 5x^2 - 2x + 24$ has a known zero at $x = -2$. What is the product of the other two zeros?",
    "Which choice is the product of the other two zeros?",
    ["-12", "12", "-6", "8"],
    "A",
    "Choice A is correct. By Vieta's formulas, the product of all three roots of a monic cubic $x^3 + bx^2 + cx + d = 0$ is $-d = -24$. Since one root is $-2$, the product of the remaining two roots is $\\frac{-24}{-2} = 12$ wait! Let's check roots: if $p(x) = (x + 2)(x^2 - 7x + 12) = (x + 2)(x - 3)(x - 4)$. Roots are $-2, 3, 4$. Product of the other two is $3 \\times 4 = 12$! Let's update choices to [\"12\", \"-12\", \"-6\", \"8\"]."
))
math1[-1]["choices"] = [{"letter": "A", "text": "12"}, {"letter": "B", "text": "-12"}, {"letter": "C", "text": "-6"}, {"letter": "D", "text": "8"}]
math1[-1]["explanation"] = "Choice A is correct. Factoring $p(x)$ gives $(x + 2)(x^2 - 7x + 12) = (x + 2)(x - 3)(x - 4)$. The zeros are $-2, 3$, and $4$. The product of the other two zeros is $3 \\times 4 = 12$."

math1.append(make_mcq(
    "t4-math-m1-q15", DOMAINS["MATH"]["ADV"], "Nonlinear Systems", "Hard",
    "What is the positive x-coordinate of the intersection point of the system:<br>$$y = x^2 - 4$$<br>$$y = 5x + 10$$",
    "Which choice is the positive x-coordinate?",
    ["7", "5", "2", "6"],
    "A",
    "Choice A is correct. Set equal: $x^2 - 4 = 5x + 10 \\implies x^2 - 5x - 14 = 0 \\implies (x - 7)(x + 2) = 0$. The positive x-coordinate is 7."
))

math1.append(make_mcq(
    "t4-math-m1-q16", DOMAINS["MATH"]["ADV"], "Radical Equations", "Hard",
    "What is the solution set of $\\sqrt{5x + 24} = x + 2$?",
    "Which choice is the valid solution set?",
    ["{4}", "{-5, 4}", "{-5}", "{6}"],
    "A",
    "Choice A is correct. Square both sides: $5x + 24 = (x + 2)^2 = x^2 + 4x + 4 \\implies x^2 - x - 20 = 0 \\implies (x - 5)(x + 4) = 0$ wait: $(x - 5)(x + 4) = x^2 - x - 20 = 0$. If $x = 5$, $\\sqrt{49} = 7 = 5 + 2$ (valid). If $x = -4$, $\\sqrt{4} = 2 \\neq -2$ (extraneous). Let's update choices to [\"5\", \"-4\", \"5 and -4\", \"6\"]."
))
math1[-1]["choices"] = [{"letter": "A", "text": "{5}"}, {"letter": "B", "text": "{-4, 5}"}, {"letter": "C", "text": "{-4}"}, {"letter": "D", "text": "{6}"}]
math1[-1]["explanation"] = "Choice A is correct. Squaring both sides yields $5x + 24 = x^2 + 4x + 4 \\implies x^2 - x - 20 = 0 \\implies (x - 5)(x + 4) = 0$. Testing $x = 5$ gives $\\sqrt{49} = 7 = 5 + 2$ (valid). Testing $x = -4$ gives $\\sqrt{4} = 2 \\neq -2$ (extraneous). The solution set is {5}."

# 17-22 Problem-Solving and Data Analysis
math1.append(make_mcq(
    "t4-math-m1-q17", DOMAINS["MATH"]["PSDA"], "Percentages & Margins", "Easy",
    "A retail store purchases a jacket for $60 wholesale and marks up the price by $60\\%$. During an end-of-season sale, the jacket is discounted by $25\\%$ from the marked-up price. What is the sale price of the jacket?",
    "Which choice is the sale price?",
    ["$72", "$75", "$68", "$80"],
    "A",
    "Choice A is correct. Marked up price: $60 \\times 1.60 = $96. After 25% discount: $96 \\times 0.75 = $72."
))

math1.append(make_mcq(
    "t4-math-m1-q18", DOMAINS["MATH"]["PSDA"], "Ratios and Proportions", "Easy",
    "A recipe for artisan bread requires 3 cups of flour for every 1.25 cups of water. If a bakery uses 15 cups of flour, how many cups of water are required?",
    "Which choice is the number of cups of water?",
    ["6.25", "5.00", "7.50", "6.00"],
    "A",
    "Choice A is correct. Proportion: $\\frac{3\\text{ flour}}{1.25\\text{ water}} = \\frac{15\\text{ flour}}{w\\text{ water}}$. Cross-multiplying: $3w = 15 \\times 1.25 = 18.75 \\implies w = 6.25$ cups."
))

table_t4_q19 = "<table style='width: 80%; border-collapse: collapse; margin: 10px auto; font-size: 13px;'><thead><tr style='background: #f1f5f9;'><th style='padding: 6px; border: 1px solid #cbd5e1;'>Vehicle Type</th><th style='padding: 6px; border: 1px solid #cbd5e1;'>Electric</th><th style='padding: 6px; border: 1px solid #cbd5e1;'>Gasoline</th><th style='padding: 6px; border: 1px solid #cbd5e1;'>Total</th></tr></thead><tbody><tr><td style='padding: 6px; border: 1px solid #cbd5e1;'>Sedan</td><td style='padding: 6px; border: 1px solid #cbd5e1; text-align: center;'>64</td><td style='padding: 6px; border: 1px solid #cbd5e1; text-align: center;'>56</td><td style='padding: 6px; border: 1px solid #cbd5e1; text-align: center;'>120</td></tr><tr><td style='padding: 6px; border: 1px solid #cbd5e1;'>SUV</td><td style='padding: 6px; border: 1px solid #cbd5e1; text-align: center;'>36</td><td style='padding: 6px; border: 1px solid #cbd5e1; text-align: center;'>84</td><td style='padding: 6px; border: 1px solid #cbd5e1; text-align: center;'>120</td></tr><tr><td style='padding: 6px; border: 1px solid #cbd5e1;'>Total</td><td style='padding: 6px; border: 1px solid #cbd5e1; text-align: center;'>100</td><td style='padding: 6px; border: 1px solid #cbd5e1; text-align: center;'>140</td><td style='padding: 6px; border: 1px solid #cbd5e1; text-align: center;'>240</td></tr></tbody></table>"
math1.append(make_mcq(
    "t4-math-m1-q19", DOMAINS["MATH"]["PSDA"], "Two-Way Frequency Tables", "Medium",
    table_t4_q19 + "<br>The table shows fleet data for 240 commercial vehicles.",
    "If a vehicle selected at random from the fleet is an electric vehicle, what is the probability that it is an SUV?",
    ["$\\frac{36}{100}$", "$\\frac{36}{120}$", "$\\frac{36}{240}$", "$\\frac{64}{100}$"],
    "A",
    "Choice A is correct. The given condition restricts the sample space to electric vehicles (total = 100). Among those 100 vehicles, 36 are SUVs. The probability is $\\frac{36}{100}$ (or $0.36$)."
))

math1.append(make_mcq(
    "t4-math-m1-q20", DOMAINS["MATH"]["PSDA"], "Scatterplots & Lines of Best Fit", "Medium",
    "A regression line estimating battery life in hours ($y$) based on screen brightness setting in percentage ($x$) is given by $\\hat{y} = -0.08x + 14$. For a device operated at $50\\%$ brightness, the actual battery life was 10.5 hours. What is the residual in hours?",
    "Which choice is the residual?",
    ["0.5", "-0.5", "1.0", "-1.0"],
    "A",
    "Choice A is correct. Predicted battery life: $\\hat{y} = -0.08(50) + 14 = -4 + 14 = 10.0$ hours. Residual $= \\text{Actual} - \\text{Predicted} = 10.5 - 10.0 = 0.5$ hours."
))

math1.append(make_mcq(
    "t4-math-m1-q21", DOMAINS["MATH"]["PSDA"], "Margin of Error & Poll Results", "Hard",
    "A randomized survey of 800 hospital patients found that $72\\%$ were satisfied with dietary options, with a margin of error of $\\pm 3.1\\%$ at a $95\\%$ confidence level. Which of the following is a plausible value for the true percentage of all hospital patients who are satisfied?",
    "Which choice is plausible?",
    ["$73.5\\%$", "$68.2\\%$", "$76.0\\%$", "$75.4\\%$"],
    "A",
    "Choice A is correct. The confidence interval is $72\\% \\pm 3.1\\% = [68.9\\%, 75.1\\%]$. Only $73.5\\%$ falls inside this interval."
))

math1.append(make_mcq(
    "t4-math-m1-q22", DOMAINS["MATH"]["PSDA"], "Arithmetic Mean", "Medium",
    "A data set consists of six numbers: 14, 18, 22, 26, 30, and $y$. If the mean of the data set is 24, what is the value of $y$?",
    "Which choice is the value of $y$?",
    ["34", "30", "36", "32"],
    "A",
    "Choice A is correct. The sum of 6 numbers with mean 24 is $6 \\times 24 = 144$. The sum of the first five numbers is $14 + 18 + 22 + 26 + 30 = 110$. Thus $y = 144 - 110 = 34$."
))

# 23-27 Geometry & Trig (SPR Grid-Ins for 23-27)
math1.append(make_spr(
    "t4-math-m1-q23", DOMAINS["MATH"]["GEOM"], "Right Triangle Trigonometry", "Medium",
    "In right triangle $PQR$ with right angle at $Q$, side $PQ = 20$ and side $QR = 21$. What is the value of $\\tan(P)$?",
    "Enter the exact fractional or decimal value of $\\tan(P)$:",
    ["21/20", "1.05"],
    "The answer is 21/20 (or 1.05). In right triangle $PQR$, $\\tan(P) = \\frac{\\text{opp}}{\\text{adj}} = \\frac{QR}{PQ} = \\frac{21}{20} = 1.05$."
))

math1.append(make_spr(
    "t4-math-m1-q24", DOMAINS["MATH"]["GEOM"], "Circle Equations", "Medium",
    "A circle in the xy-plane is given by $(x + 9)^2 + (y - 5)^2 = 121$. What is the diameter of the circle?",
    "Enter the diameter:",
    ["22"],
    "The answer is 22. In the equation $(x - h)^2 + (y - k)^2 = r^2$, $r^2 = 121 \\implies r = 11$. The diameter is $2r = 2(11) = 22$."
))

math1.append(make_spr(
    "t4-math-m1-q25", DOMAINS["MATH"]["GEOM"], "Radian Sector Area", "Hard",
    "A circle has a radius of 10 cm. A sector of the circle is formed by a central angle of $\\frac{3\\pi}{5}$ radians. The area of the sector is $k\\pi$ square centimeters. What is the value of $k$?",
    "Enter the value of $k$:",
    ["30"],
    "The answer is 30. Sector area $A = \\frac{1}{2}r^2\\theta = \\frac{1}{2}(10^2)\\left(\\frac{3\\pi}{5}\\right) = \\frac{1}{2}(100)\\left(\\frac{3\\pi}{5}\\right) = 50 \\times \\frac{3\\pi}{5} = 30\\pi$. Thus $k = 30$."
))

math1.append(make_spr(
    "t4-math-m1-q26", DOMAINS["MATH"]["ALG"], "Linear Equations", "Easy",
    "If $8x + 12 = 52$, what is the value of $4x + 6$?",
    "Enter the value:",
    ["26"],
    "The answer is 26. Notice that $4x + 6 = \\frac{8x + 12}{2} = \\frac{52}{2} = 26$."
))

math1.append(make_spr(
    "t4-math-m1-q27", DOMAINS["MATH"]["GEOM"], "Sphere Volume", "Medium",
    "A sphere has a radius of 3 cm. The volume of the sphere is $k\\pi$ cubic centimeters. What is the value of $k$?",
    "Enter the value of $k$:",
    ["36"],
    "The answer is 36. Sphere volume $V = \\frac{4}{3}\\pi r^3 = \\frac{4}{3}\\pi (3^3) = \\frac{4}{3}\\pi (27) = 36\\pi$. Therefore $k = 36$."
))

# ==========================================
# TEST 4 - MATH MODULE 2 (27 Qs)
# ==========================================

# 1-8 Algebra
math2.append(make_mcq(
    "t4-math-m2-q1", DOMAINS["MATH"]["ALG"], "Linear Systems No Solution", "Hard",
    "In the system of equations below, $p$ is a constant:<br>$$px - 9y = 21$$<br>$$4x - 6y = 15$$<br>If the system has no solution, what is the value of $p$?",
    "Which choice is the value of $p$?",
    ["6", "-6", "4", "9"],
    "A",
    "Choice A is correct. Parallel lines have equal slopes: $\\frac{p}{9} = \\frac{4}{6} \\implies \\frac{p}{9} = \\frac{2}{3} \\implies p = 9 \\times \\frac{2}{3} = 6$."
))

math2.append(make_mcq(
    "t4-math-m2-q2", DOMAINS["MATH"]["ALG"], "Absolute Value Inequalities", "Hard",
    "What is the number of integers that satisfy $|3x - 6| \\le 9$?",
    "Which choice is the number of integers?",
    ["7", "6", "5", "8"],
    "A",
    "Choice A is correct. $-9 \\le 3x - 6 \\le 9 \\implies -3 \\le 3x \\le 15 \\implies -1 \\le x \\le 5$. The integers in this closed interval are {-1, 0, 1, 2, 3, 4, 5}, which totals 7 integers."
))

math2.append(make_mcq(
    "t4-math-m2-q3", DOMAINS["MATH"]["ALG"], "Multi-Variable Systems", "Hard",
    "If $4x - 3y = 18$ and $2x + y = 4$, what is the value of $x - y$?",
    "Which choice is the value of $x - y$?",
    ["5", "3", "7", "1"],
    "A",
    "Choice A is correct. Multiply second equation by 3: $6x + 3y = 12$. Add to first: $10x = 30 \\implies x = 3$. Substitute into second: $2(3) + y = 4 \\implies y = -2$. Then $x - y = 3 - (-2) = 5$."
))

math2.append(make_mcq(
    "t4-math-m2-q4", DOMAINS["MATH"]["ALG"], "Compound Inequalities", "Medium",
    "Which of the following represents all solutions to $-7 < 2x - 3 \\le 11$?",
    "Which choice represents all solutions?",
    ["$-2 < x \\le 7$", "$-2 \\le x < 7$", "$-5 < x \\le 7$", "$-2 < x \\le 14$"],
    "A",
    "Choice A is correct. Add 3: $-4 < 2x \\le 14$. Divide by 2: $-2 < x \\le 7$."
))

math2.append(make_mcq(
    "t4-math-m2-q5", DOMAINS["MATH"]["ALG"], "Function Notation", "Medium",
    "For the function $f(x) = 6x - 11$, if $f(2k) = 37$, what is the value of $k$?",
    "Which choice is the value of $k$?",
    ["4", "8", "2", "6"],
    "A",
    "Choice A is correct. $f(2k) = 6(2k) - 11 = 12k - 11$. Setting $12k - 11 = 37 \\implies 12k = 48 \\implies k = 4$."
))

math2.append(make_mcq(
    "t4-math-m2-q6", DOMAINS["MATH"]["ALG"], "Linear Modeling Rate Problem", "Hard",
    "Company X rents equipment for a flat fee of $250 plus $35 per day. Company Y rents the same equipment for $100 plus $60 per day. For what number of rental days would the total cost be identical for both companies?",
    "Which choice is the number of days?",
    ["6", "5", "8", "4"],
    "A",
    "Choice A is correct. Set costs equal: $250 + 35d = 100 + 60d \\implies 150 = 25d \\implies d = 6$ days."
))

math2.append(make_mcq(
    "t4-math-m2-q7", DOMAINS["MATH"]["ALG"], "Perpendicular Line Equations", "Hard",
    "Line $g$ has equation $2x + 5y = 15$. Line $h$ is perpendicular to line $g$ and passes through $(4, 3)$. What is the y-intercept of line $h$?",
    "Which choice is the y-intercept?",
    ["-7", "7", "-5", "3"],
    "A",
    "Choice A is correct. Slope of $g$ is $-\\frac{2}{5}$. Perpendicular slope is $\\frac{5}{2}$. Using point $(4, 3)$: $y - 3 = \\frac{5}{2}(x - 4) \\implies y - 3 = \\frac{5}{2}x - 10 \\implies y = \\frac{5}{2}x - 7$. The y-intercept is $-7$."
))

math2.append(make_mcq(
    "t4-math-m2-q8", DOMAINS["MATH"]["ALG"], "Formula Rearrangement", "Medium",
    "The centripetal force formula is $F = \\frac{mv^2}{r}$. Which equation correctly expresses the radius $r$ in terms of $F, m$, and $v$?",
    "Which choice expresses $r$?",
    ["$r = \\frac{mv^2}{F}$", "$r = \\frac{F}{mv^2}$", "$r = \\frac{Fv^2}{m}$", "$r = \\sqrt{\\frac{mv^2}{F}}$"],
    "A",
    "Choice A is correct. Multiply by $r$: $Fr = mv^2$. Divide by $F$: $r = \\frac{mv^2}{F}$."
))

# 9-17 Advanced Math
math2.append(make_mcq(
    "t4-math-m2-q9", DOMAINS["MATH"]["ADV"], "Discriminant Analysis", "Hard",
    "In the quadratic equation $5x^2 - 20x + c = 0$, $c$ is a constant. If the equation has exactly one distinct real solution, what is the value of $c$?",
    "Which choice is the value of $c$?",
    ["20", "100", "4", "25"],
    "A",
    "Choice A is correct. Exactly one real solution requires $b^2 - 4ac = 0$. $(-20)^2 - 4(5)(c) = 0 \\implies 400 - 20c = 0 \\implies 20c = 400 \\implies c = 20$."
))

math2.append(make_mcq(
    "t4-math-m2-q10", DOMAINS["MATH"]["ADV"], "Completing the Square Minimum", "Hard",
    "What is the minimum value of $f(x) = x^2 - 16x + 75$?",
    "Which choice is the minimum value?",
    ["11", "8", "-11", "64"],
    "A",
    "Choice A is correct. Complete the square: $f(x) = (x^2 - 16x + 64) + 75 - 64 = (x - 8)^2 + 11$. Since $(x - 8)^2 \\ge 0$, the minimum value is 11 (at $x = 8$)."
))

math2.append(make_mcq(
    "t4-math-m2-q11", DOMAINS["MATH"]["ADV"], "Exponential Growth Doubling Time", "Hard",
    "An investment grows according to $A(t) = 5,000(2)^{t/12}$, where $t$ is measured in years. How many years will it take for the investment to reach $40,000$?",
    "Which choice is the number of years?",
    ["36", "24", "48", "12"],
    "A",
    "Choice A is correct. Set $5,000(2)^{t/12} = 40,000 \\implies 2^{t/12} = 8 = 2^3$. Equating exponents: $\\frac{t}{12} = 3 \\implies t = 36$ years."
))

math2.append(make_mcq(
    "t4-math-m2-q12", DOMAINS["MATH"]["ADV"], "Polynomial Remainder Theorem", "Hard",
    "When the polynomial $f(x) = 3x^3 - 4x^2 + kx - 5$ is divided by $x - 2$, the remainder is 15. What is the value of $k$?",
    "Which choice is the value of $k$?",
    ["6", "4", "8", "5"],
    "A",
    "Choice A is correct. By the Remainder Theorem, $f(2) = 15$. Evaluating: $f(2) = 3(2^3) - 4(2^2) + k(2) - 5 = 24 - 16 + 2k - 5 = 2k + 3$. Setting $2k + 3 = 15 \\implies 2k = 12 \\implies k = 6$."
))

math2.append(make_mcq(
    "t4-math-m2-q13", DOMAINS["MATH"]["ADV"], "Complex Number Simplification", "Hard",
    "What is the value of $\\frac{7 + 4i}{2 - i}$, where $i = \\sqrt{-1}$?",
    "Which choice is the simplified form?",
    ["$2 + 3i$", "$2 - 3i$", "$3 + 2i$", "$1 + 4i$"],
    "A",
    "Choice A is correct. Multiply by conjugate $2 + i$: $\\frac{(7 + 4i)(2 + i)}{2^2 - i^2} = \\frac{14 + 7i + 8i + 4i^2}{4 - (-1)} = \\frac{14 + 15i - 4}{5} = \\frac{10 + 15i}{5} = 2 + 3i$."
))

math2.append(make_mcq(
    "t4-math-m2-q14", DOMAINS["MATH"]["ADV"], "Rational Equations", "Hard",
    "What is the sum of the solutions to $\\frac{5}{x - 1} + \\frac{2}{x + 3} = 1$?",
    "Which choice is the sum of the solutions?",
    ["5", "4", "7", "-5"],
    "A",
    "Choice A is correct. Multiply by $(x - 1)(x + 3)$: $5(x + 3) + 2(x - 1) = (x - 1)(x + 3) \\implies 5x + 15 + 2x - 2 = x^2 + 2x - 3 \\implies 7x + 13 = x^2 + 2x - 3 \\implies x^2 - 5x - 16 = 0$. By Vieta's formulas, the sum of roots is $-(-5)/1 = 5$."
))

math2.append(make_mcq(
    "t4-math-m2-q15", DOMAINS["MATH"]["ADV"], "Nonlinear Graphs Intersections", "Hard",
    "The parabola $y = x^2 - 6x + 5$ intersects the line $y = -2x + 17$ at points $A$ and $B$. What is the midpoint of segment $AB$?",
    "Which choice is the midpoint?",
    ["(2, 13)", "(2, 17)", "(3, 11)", "(4, 9)"],
    "A",
    "Choice A is correct. Equate: $x^2 - 6x + 5 = -2x + 17 \\implies x^2 - 4x - 12 = 0 \\implies (x - 6)(x + 2) = 0$. Points of intersection: $x = 6 \\implies y = -2(6) + 17 = 5$; $x = -2 \\implies y = -2(-2) + 17 = 21$. Midpoint: $(\\frac{6 + (-2)}{2}, \\frac{5 + 21}{2}) = (2, 13)$."
))

math2.append(make_mcq(
    "t4-math-m2-q16", DOMAINS["MATH"]["ADV"], "Exponential Equations", "Medium",
    "If $3^{2x + 1} = 243$, what is the value of $x$?",
    "Which choice is the value of $x$?",
    ["2", "3", "1", "4"],
    "A",
    "Choice A is correct. Since $243 = 3^5$, we have $3^{2x + 1} = 3^5 \\implies 2x + 1 = 5 \\implies 2x = 4 \\implies x = 2$."
))

math2.append(make_mcq(
    "t4-math-m2-q17", DOMAINS["MATH"]["ADV"], "Rational Exponents Equivalence", "Hard",
    "For $x > 0$, if $\\frac{(x^{3/4})^2}{\\sqrt[4]{x^2}} = x^p$, what is the value of $p$?",
    "Which choice is the value of $p$?",
    ["1", "$\\frac{1}{2}$", "$\\frac{3}{2}$", "2"],
    "A",
    "Choice A is correct. Numerator is $x^{6/4} = x^{3/2}$. Denominator is $x^{2/4} = x^{1/2}$. Dividing gives $x^{3/2 - 1/2} = x^1 = x$. Thus $p = 1$."
))

# 18-22 Problem-Solving and Data Analysis
math2.append(make_mcq(
    "t4-math-m2-q18", DOMAINS["MATH"]["PSDA"], "Standard Deviation Comparison", "Hard",
    "Group 1 scores are {80, 80, 80, 80}. Group 2 scores are {60, 70, 90, 100}. Both groups have a mean score of 80. Which statement is true?",
    "Which choice is true?",
    [
        "Group 2 has a greater standard deviation than Group 1.",
        "Group 1 has a greater standard deviation than Group 2.",
        "Both groups have identical standard deviations.",
        "The standard deviations cannot be determined from the given values."
    ],
    "A",
    "Choice A is correct. Group 1 has zero deviation from the mean (standard deviation = 0). Group 2 scores are dispersed away from the mean, so Group 2 has a greater standard deviation."
))

math2.append(make_mcq(
    "t4-math-m2-q19", DOMAINS["MATH"]["PSDA"], "Margin of Error Sample Size", "Hard",
    "A nationwide survey of 900 consumers had a margin of error of $\\pm 3.2\\%$. If the researchers want to reduce the margin of error to $\\pm 1.6\\%$ at the same confidence level, how many consumers must they survey?",
    "Which choice is the required sample size?",
    ["3,600", "1,800", "2,700", "7,200"],
    "A",
    "Choice A is correct. The margin of error is inversely proportional to the square root of sample size ($ME \\propto \\frac{1}{\\sqrt{n}}$). Halving the margin of error requires multiplying the sample size by $2^2 = 4$. Thus $900 \\times 4 = 3,600$."
))

math2.append(make_mcq(
    "t4-math-m2-q20", DOMAINS["MATH"]["PSDA"], "Conditional Probability", "Hard",
    "In a high school, $40\\%$ of students are in the arts program and $60\\%$ are in the STEM program. Of the arts students, $30\\%$ play an instrument. Of the STEM students, $15\\%$ play an instrument. What fraction of all instrument players are arts students?",
    "Which choice is the fraction?",
    ["$\\frac{12}{21}$", "$\\frac{9}{21}$", "$\\frac{12}{40}$", "$\\frac{30}{45}$"],
    "A",
    "Choice A is correct. Arts instrument players: $0.40 \\times 0.30 = 0.12$. STEM instrument players: $0.60 \\times 0.15 = 0.09$. Total instrument players $= 0.12 + 0.09 = 0.21$. The fraction who are arts students is $\\frac{0.12}{0.21} = \\frac{12}{21}$ (or $\\frac{4}{7}$)."
))

math2.append(make_mcq(
    "t4-math-m2-q21", DOMAINS["MATH"]["PSDA"], "Interquartile Range Comparison", "Medium",
    "Dataset A has $Q_1 = 40$ and $Q_3 = 65$. Dataset B has $Q_1 = 30$ and $Q_3 = 70$. Which dataset has a greater interquartile range (IQR)?",
    "Which choice is correct?",
    [
        "Dataset B has a greater IQR by 15.",
        "Dataset A has a greater IQR by 10.",
        "Both datasets have identical IQRs.",
        "Dataset B has a greater IQR by 5."
    ],
    "A",
    "Choice A is correct. For Dataset A, $IQR = 65 - 40 = 25$. For Dataset B, $IQR = 70 - 30 = 40$. Dataset B's IQR is $40 - 25 = 15$ greater."
))

math2.append(make_mcq(
    "t4-math-m2-q22", DOMAINS["MATH"]["PSDA"], "Unit Conversions Multi-Step", "Medium",
    "A commercial water filter processes 360 gallons of water per hour. Given that 1 gallon is approximately 3.785 liters and 1 hour is 60 minutes, what is the filtration rate in liters per minute? (Round to the nearest whole liter)",
    "Which choice is the rate?",
    ["23 L/min", "15 L/min", "38 L/min", "28 L/min"],
    "A",
    "Choice A is correct. $\\frac{360 \\times 3.785}{60} = 6 \\times 3.785 = 22.71 \\approx 23$ liters per minute."
))

# 23-27 Geometry & Trig (SPR Grid-Ins for 23-27)
math2.append(make_spr(
    "t4-math-m2-q23", DOMAINS["MATH"]["GEOM"], "Circle Completing the Square", "Hard",
    "A circle in the xy-plane is defined by $x^2 + y^2 - 14x + 8y - 16 = 0$. What is the radius of the circle?",
    "Enter the radius:",
    ["9"],
    "The answer is 9. Group and complete squares: $(x^2 - 14x + 49) + (y^2 + 8y + 16) = 16 + 49 + 16 \\implies (x - 7)^2 + (y + 4)^2 = 81$. Radius $r = \\sqrt{81} = 9$."
))

math2.append(make_spr(
    "t4-math-m2-q24", DOMAINS["MATH"]["GEOM"], "Similar Triangles & Scale Factor", "Hard",
    "Triangle $XYZ$ is similar to triangle $UVW$, where the length of each side of triangle $UVW$ is $1.8$ times the length of the corresponding side of triangle $XYZ$. If the perimeter of triangle $XYZ$ is 30, what is the perimeter of triangle $UVW$?",
    "Enter the perimeter:",
    ["54"],
    "The answer is 54. The perimeter scales linearly by the side length scale factor: $\\text{Perimeter}(UVW) = 1.8 \\times \\text{Perimeter}(XYZ) = 1.8 \\times 30 = 54$."
))

math2.append(make_spr(
    "t4-math-m2-q25", DOMAINS["MATH"]["GEOM"], "Cofunction Identity", "Medium",
    "In a right triangle with acute angles $A$ and $B$, $\\sin(A) = \\frac{9}{41}$. What is the value of $\\cos(B)$?",
    "Enter the exact fractional or decimal value of $\\cos(B)$:",
    ["9/41", "0.22"],
    "The answer is 9/41 (or approx 0.22). For complementary acute angles $A$ and $B$, $\\cos(B) = \\sin(A) = \\frac{9}{41}$."
))

math2.append(make_spr(
    "t4-math-m2-q26", DOMAINS["MATH"]["ADV"], "Parabola Vertex Y-Value", "Hard",
    "What is the minimum value of $f(x) = 3x^2 - 18x + 35$?",
    "Enter the minimum value:",
    ["8"],
    "The answer is 8. The vertex x-coordinate is $x = -\\frac{-18}{2(3)} = 3$. Evaluating at $x = 3$: $f(3) = 3(3^2) - 18(3) + 35 = 27 - 54 + 35 = 8$."
))

math2.append(make_spr(
    "t4-math-m2-q27", DOMAINS["MATH"]["GEOM"], "Radian Conversion", "Easy",
    "An angle measures $240^\\circ$. In radians, the angle is $\\frac{k\\pi}{3}$. What is the value of the integer $k$?",
    "Enter the value of $k$:",
    ["4"],
    "The answer is 4. Convert degrees to radians: $240^\\circ \\times \\frac{\\pi}{180^\\circ} = \\frac{4\\pi}{3}$. Therefore $k = 4$."
))

print(f"Test 4 Math Module 1 ready: {len(math1)} questions.")
print(f"Test 4 Math Module 2 ready: {len(math2)} questions.")
