# gen_test2_math.py - Practice Test 2 Math (54 questions: 27 Module 1, 27 Module 2)
import json
from generate_suite_all import DOMAINS, make_mcq, make_spr

math1 = []
math2 = []

# ==========================================
# TEST 2 - MATH MODULE 1 (27 Qs)
# ==========================================

# 1-8 Algebra
math1.append(make_mcq(
    "t2-math-m1-q1", DOMAINS["MATH"]["ALG"], "Linear Equations", "Easy",
    "If $7x - 14 = 35$, what is the value of $2x - 4$?",
    "Which choice is the correct value?",
    ["10", "14", "7", "5"],
    "A",
    "Choice A is correct. Divide both sides of $7x - 14 = 35$ by 7: $x - 2 = 5$. Then multiply by 2: $2(x - 2) = 2(5) \\implies 2x - 4 = 10$."
))

math1.append(make_mcq(
    "t2-math-m1-q2", DOMAINS["MATH"]["ALG"], "Linear Functions", "Easy",
    "A fitness center charges a registration fee of $75 plus $45 per month of membership. Which function $M(t)$ represents the total cost in dollars for $t$ months?",
    "Which choice is the correct function?",
    ["$M(t) = 45t + 75$", "$M(t) = 75t + 45$", "$M(t) = 120t$", "$M(t) = 45(t + 75)$"],
    "A",
    "Choice A is correct. The registration fee is the constant y-intercept (75) and monthly dues are the slope (45), yielding $M(t) = 45t + 75$."
))

math1.append(make_mcq(
    "t2-math-m1-q3", DOMAINS["MATH"]["ALG"], "Systems of Two Linear Equations", "Medium",
    "What is the solution $(x, y)$ to the system of equations?<br>$$3x + 2y = 22$$<br>$$x - 2y = 2$$",
    "Which choice is the solution $(x, y)$?",
    ["(6, 2)", "(4, 5)", "(8, -1)", "(5, 3.5)"],
    "A",
    "Choice A is correct. Add the two equations: $(3x + 2y) + (x - 2y) = 22 + 2 \\implies 4x = 24 \\implies x = 6$. Substitute $x = 6$ into the second equation: $6 - 2y = 2 \\implies 2y = 4 \\implies y = 2$. The solution is $(6, 2)$."
))

math1.append(make_mcq(
    "t2-math-m1-q4", DOMAINS["MATH"]["ALG"], "Linear Slopes & Parallel Lines", "Medium",
    "Line $p$ is defined by the equation $2x - 5y = 15$. Line $q$ is parallel to line $p$ and passes through the origin $(0, 0)$. What is the equation of line $q$?",
    "Which choice is the equation of line $q$?",
    ["$y = \\frac{2}{5}x$", "$y = -\\frac{5}{2}x$", "$y = \\frac{5}{2}x$", "$y = -\\frac{2}{5}x$"],
    "A",
    "Choice A is correct. Solve line $p$ for $y$: $-5y = -2x + 15 \\implies y = \\frac{2}{5}x - 3$. Parallel lines have equal slopes ($m = \\frac{2}{5}$). Passing through the origin gives y-intercept 0, so $y = \\frac{2}{5}x$."
))

math1.append(make_mcq(
    "t2-math-m1-q5", DOMAINS["MATH"]["ALG"], "Linear Inequalities", "Medium",
    "A delivery truck can carry a maximum payload of 3,200 pounds. The truck is currently loaded with 800 pounds of cargo. If each additional crate weighs 150 pounds, what is the maximum number of additional crates the truck can carry?",
    "Which choice is the maximum number of crates?",
    ["16", "17", "15", "18"],
    "A",
    "Choice A is correct. Let $c$ be the number of crates: $150c + 800 \\le 3200 \\implies 150c \\le 2400 \\implies c \\le 16$. The maximum number of additional crates is 16."
))

math1.append(make_mcq(
    "t2-math-m1-q6", DOMAINS["MATH"]["ALG"], "Linear Modeling", "Medium",
    "The total price $P(k)$ in dollars of purchasing $k$ kilograms of organic coffee beans is given by $P(k) = 18.50k + 4.00$, where 4.00 is a fixed packaging fee. What does the value 18.50 represent?",
    "Which choice is the best interpretation?",
    [
        "The cost per kilogram of coffee beans",
        "The fixed packaging fee per order",
        "The minimum number of kilograms that can be purchased",
        "The discount applied to bulk purchases"
    ],
    "A",
    "Choice A is correct. In $P(k) = 18.50k + 4.00$, the slope 18.50 represents the rate of change of price per kilogram of coffee beans."
))

math1.append(make_mcq(
    "t2-math-m1-q7", DOMAINS["MATH"]["ALG"], "Linear Systems No Solution", "Hard",
    "In the system of equations below, $a$ is a constant:<br>$$ax + 6y = 18$$<br>$$2x + 3y = 7$$<br>If the system has no solution, what is the value of $a$?",
    "Which choice is the value of $a$?",
    ["4", "2", "-4", "6"],
    "A",
    "Choice A is correct. For no solution, lines must have identical slopes but different intercepts. Multiplying the second equation by 2 gives $4x + 6y = 14$. Comparing with $ax + 6y = 18$, we see $a = 4$ produces parallel lines ($18 \\neq 14$)."
))

math1.append(make_mcq(
    "t2-math-m1-q8", DOMAINS["MATH"]["ALG"], "Linear Equations in One Variable", "Easy",
    "If $4(3x - 2) = 2(5x + 8)$, what is the value of $x$?",
    "Which choice is the value of $x$?",
    ["12", "8", "6", "10"],
    "A",
    "Choice A is correct. Expand both sides: $12x - 8 = 10x + 16 \\implies 2x = 24 \\implies x = 12$."
))

# 9-16 Advanced Math
math1.append(make_mcq(
    "t2-math-m1-q9", DOMAINS["MATH"]["ADV"], "Quadratic Equations", "Easy",
    "What are the solutions to the equation $x^2 - 12x + 35 = 0$?",
    "Which choice gives the solutions?",
    ["$x = 5$ and $x = 7$", "$x = -5$ and $x = -7$", "$x = 2$ and $x = 10$", "$x = 1$ and $x = 35$"],
    "A",
    "Choice A is correct. Factoring gives $(x - 5)(x - 7) = 0$, so $x = 5$ and $x = 7$."
))

math1.append(make_mcq(
    "t2-math-m1-q10", DOMAINS["MATH"]["ADV"], "Vertex Form & Optimization", "Medium",
    "The height $h(t)$ in meters of a drone $t$ seconds after takeoff is modeled by $h(t) = -5(t - 4)^2 + 80$. What is the maximum height, in meters, reached by the drone?",
    "Which choice is the maximum height?",
    ["80", "4", "20", "64"],
    "A",
    "Choice A is correct. The quadratic function is in vertex form $h(t) = a(t - h)^2 + k$ with vertex at $(4, 80)$. Since $a = -5 < 0$, the maximum height is 80 meters."
))

math1.append(make_mcq(
    "t2-math-m1-q11", DOMAINS["MATH"]["ADV"], "Exponential Growth", "Medium",
    "A bacterial colony begins with 250 cells and triples in population every 4 hours. Which function $N(t)$ models the population after $t$ hours?",
    "Which choice is the correct model?",
    ["$N(t) = 250(3)^{t/4}$", "$N(t) = 250(3)^{4t}$", "$N(t) = 250(4)^{t/3}$", "$N(t) = 750^t$"],
    "A",
    "Choice A is correct. The exponential model with initial count $N_0 = 250$, growth factor 3, and cycle period 4 hours is $N(t) = 250(3)^{t/4}$."
))

math1.append(make_mcq(
    "t2-math-m1-q12", DOMAINS["MATH"]["ADV"], "Radicals & Rational Exponents", "Medium",
    "Which expression is equivalent to $(16x^8)^{3/4}$ for all $x > 0$?",
    "Which choice is equivalent?",
    ["$8x^6$", "$12x^6$", "$8x^8$", "$16x^6$"],
    "A",
    "Choice A is correct. Apply the exponent to both base terms: $16^{3/4} = (\\sqrt[4]{16})^3 = 2^3 = 8$. For the variable: $(x^8)^{3/4} = x^{8 \\times 3/4} = x^6$. Combining yields $8x^6$."
))

math1.append(make_mcq(
    "t2-math-m1-q13", DOMAINS["MATH"]["ADV"], "Rational Expressions", "Medium",
    "Which expression is equivalent to $\\frac{2x^2 + 7x + 3}{x + 3}$ for all $x \\neq -3$?",
    "Which choice is equivalent?",
    ["$2x + 1$", "$2x - 1$", "$x + 1$", "$2x + 3$"],
    "A",
    "Choice A is correct. Factor the numerator: $2x^2 + 7x + 3 = (2x + 1)(x + 3)$. Dividing by $(x + 3)$ gives $2x + 1$."
))

math1.append(make_mcq(
    "t2-math-m1-q14", DOMAINS["MATH"]["ADV"], "Polynomial Zeros & Factors", "Hard",
    "A polynomial $f(x)$ has zeros at $x = -2, 0$, and $3$. Which of the following could be the expression for $f(x)$?",
    "Which choice could be $f(x)$?",
    ["$x(x + 2)(x - 3)$", "$(x - 2)x(x + 3)$", "$(x + 2)^2(x - 3)$", "$x^2(x - 2)(x + 3)$"],
    "A",
    "Choice A is correct. Zeros at $-2, 0$, and $3$ correspond to factors $(x + 2), x$, and $(x - 3)$, which gives $x(x + 2)(x - 3)$."
))

math1.append(make_mcq(
    "t2-math-m1-q15", DOMAINS["MATH"]["ADV"], "Nonlinear Systems", "Hard",
    "What is the sum of the x-coordinates of the intersection points of the system:<br>$$y = x^2 - 3x - 10$$<br>$$y = 2x + 4$$",
    "Which choice is the sum?",
    ["5", "3", "7", "-5"],
    "A",
    "Choice A is correct. Equate the two equations: $x^2 - 3x - 10 = 2x + 4 \\implies x^2 - 5x - 14 = 0$. By Vieta's formulas, the sum of roots is $-(-5)/1 = 5$. (Factoring confirms: $(x - 7)(x + 2) = 0 \\implies 7 + (-2) = 5$)."
))

math1.append(make_mcq(
    "t2-math-m1-q16", DOMAINS["MATH"]["ADV"], "Radical Equations", "Hard",
    "What is the solution set of $\\sqrt{4x + 9} = x - 3$?",
    "Which choice is the valid solution set?",
    ["{10}", "{0, 10}", "{-2, 10}", "{7}"],
    "A",
    "Choice A is correct. Square both sides: $4x + 9 = (x - 3)^2 \\implies 4x + 9 = x^2 - 6x + 9 \\implies x^2 - 10x = 0 \\implies x(x - 10) = 0$. If $x = 0$, $\\sqrt{9} = 3 \\neq -3$ (extraneous). If $x = 10$, $\\sqrt{49} = 7 = 10 - 3$ (valid). Thus {10}."
))

# 17-22 Problem-Solving and Data Analysis
math1.append(make_mcq(
    "t2-math-m1-q17", DOMAINS["MATH"]["PSDA"], "Percentages & Percent Change", "Easy",
    "A tech startup had 80 employees in 2022. By 2024, the number of employees grew to 116. What was the percentage increase in employees from 2022 to 2024?",
    "Which choice is the percentage increase?",
    ["$45\\%$", "$36\\%$", "$40\\%$", "$55\\%$"],
    "A",
    "Choice A is correct. Percent increase $= \\frac{116 - 80}{80} \\times 100\\% = \\frac{36}{80} \\times 100\\% = 0.45 \\times 100\\% = 45\\%$."
))

math1.append(make_mcq(
    "t2-math-m1-q18", DOMAINS["MATH"]["PSDA"], "Unit Conversions", "Easy",
    "An athlete runs at a steady pace of 12 kilometers per hour. Given that 1 kilometer is approximately 0.62 miles, what is the athlete's speed in miles per hour?",
    "Which choice is the speed?",
    ["7.44 mph", "8.12 mph", "6.20 mph", "19.35 mph"],
    "A",
    "Choice A is correct. $12 \\text{ km/hr} \\times 0.62 \\text{ miles/km} = 7.44 \\text{ miles/hr}$."
))

table_t2_q19 = "<table style='width: 80%; border-collapse: collapse; margin: 10px auto; font-size: 13px;'><thead><tr style='background: #f1f5f9;'><th style='padding: 6px; border: 1px solid #cbd5e1;'>Role</th><th style='padding: 6px; border: 1px solid #cbd5e1;'>Prefers Remote</th><th style='padding: 6px; border: 1px solid #cbd5e1;'>Prefers In-Office</th><th style='padding: 6px; border: 1px solid #cbd5e1;'>Total</th></tr></thead><tbody><tr><td style='padding: 6px; border: 1px solid #cbd5e1;'>Engineers</td><td style='padding: 6px; border: 1px solid #cbd5e1; text-align: center;'>72</td><td style='padding: 6px; border: 1px solid #cbd5e1; text-align: center;'>18</td><td style='padding: 6px; border: 1px solid #cbd5e1; text-align: center;'>90</td></tr><tr><td style='padding: 6px; border: 1px solid #cbd5e1;'>Marketers</td><td style='padding: 6px; border: 1px solid #cbd5e1; text-align: center;'>38</td><td style='padding: 6px; border: 1px solid #cbd5e1; text-align: center;'>32</td><td style='padding: 6px; border: 1px solid #cbd5e1; text-align: center;'>70</td></tr><tr><td style='padding: 6px; border: 1px solid #cbd5e1;'>Total</td><td style='padding: 6px; border: 1px solid #cbd5e1; text-align: center;'>110</td><td style='padding: 6px; border: 1px solid #cbd5e1; text-align: center;'>50</td><td style='padding: 6px; border: 1px solid #cbd5e1; text-align: center;'>160</td></tr></tbody></table>"
math1.append(make_mcq(
    "t2-math-m1-q19", DOMAINS["MATH"]["PSDA"], "Two-Way Frequency Tables", "Medium",
    table_t2_q19 + "<br>The table shows workplace preferences for 160 corporate employees.",
    "If an employee who prefers remote work is chosen at random, what is the probability that the employee is an engineer?",
    ["$\\frac{72}{110}$", "$\\frac{72}{90}$", "$\\frac{72}{160}$", "$\\frac{18}{50}$"],
    "A",
    "Choice A is correct. The given condition specifies employees who prefer remote work (total = 110). Of those 110 employees, 72 are engineers. Thus the probability is $\\frac{72}{110}$ (or $\\frac{36}{55}$)."
))

math1.append(make_mcq(
    "t2-math-m1-q20", DOMAINS["MATH"]["PSDA"], "Scatterplots & Residuals", "Medium",
    "A researcher uses the regression model $\\hat{y} = 1.8x + 14$ to predict daily ice cream sales in hundreds of dollars ($y$) based on temperature in degrees Celsius ($x$). On a day with a temperature of $30^\\circ\\text{C}$, actual sales were $70$ hundred dollars. What is the residual?",
    "Which choice is the residual?",
    ["2", "-2", "4", "0"],
    "A",
    "Choice A is correct. Predicted sales: $\\hat{y} = 1.8(30) + 14 = 54 + 14 = 68$. Residual $= \\text{Actual} - \\text{Predicted} = 70 - 68 = 2$."
))

math1.append(make_mcq(
    "t2-math-m1-q21", DOMAINS["MATH"]["PSDA"], "Data Measures: Median & Mean", "Medium",
    "A student scored 82, 86, 90, and 94 on four tests. What score must they achieve on the fifth test so that their overall average (mean) is 90?",
    "Which choice is the required score?",
    ["98", "94", "96", "92"],
    "A",
    "Choice A is correct. For a mean of 90 across 5 tests, total points needed $= 5 \\times 90 = 450$. The sum of the first 4 tests is $82 + 86 + 90 + 94 = 352$. Required score $= 450 - 352 = 98$."
))

math1.append(make_mcq(
    "t2-math-m1-q22", DOMAINS["MATH"]["PSDA"], "Probability Rules", "Medium",
    "A jar contains 8 red marbles, 12 blue marbles, and 10 green marbles. If two marbles are drawn at random without replacement, what is the probability that both marbles are blue?",
    "Which choice is the probability?",
    ["$\\frac{22}{145}$", "$\\frac{16}{75}$", "$\\frac{4}{25}$", "$\\frac{11}{150}$"],
    "A",
    "Choice A is correct. Total marbles = $8 + 12 + 10 = 30$. Probability of first blue $= \\frac{12}{30} = \\frac{2}{5}$. Probability of second blue $= \\frac{11}{29}$. Combined probability $= \\frac{12}{30} \\times \\frac{11}{29} = \\frac{2}{5} \\times \\frac{11}{29} = \\frac{22}{145}$."
))

# 23-27 Geometry & Trig (SPR Grid-Ins for 23-27)
math1.append(make_spr(
    "t2-math-m1-q23", DOMAINS["MATH"]["GEOM"], "Right Triangle Trigonometry", "Medium",
    "In right triangle $XYZ$, the measure of angle $Z$ is $90^\\circ$. If side $XY = 25$ and side $YZ = 24$, what is the value of $\\sin(X)$?",
    "Enter the exact fractional or decimal value of $\\sin(X)$:",
    ["24/25", "0.96"],
    "The answer is 24/25 (or 0.96). In right triangle $XYZ$ with hypotenuse $XY = 25$, side $YZ$ is the opposite side to angle $X$. Therefore, $\\sin(X) = \\frac{\\text{opp}}{\\text{hyp}} = \\frac{24}{25} = 0.96$."
))

math1.append(make_spr(
    "t2-math-m1-q24", DOMAINS["MATH"]["GEOM"], "Circle Equations", "Medium",
    "A circle in the xy-plane has equation $(x + 6)^2 + (y - 8)^2 = 81$. What is the radius of the circle?",
    "Enter the radius:",
    ["9"],
    "The answer is 9. The standard circle equation is $(x - h)^2 + (y - k)^2 = r^2$. Here $r^2 = 81$, so $r = \\sqrt{81} = 9$."
))

math1.append(make_spr(
    "t2-math-m1-q25", DOMAINS["MATH"]["GEOM"], "Radian Sector Area", "Hard",
    "A circle has a radius of 6 cm. A sector of the circle is formed by a central angle of $\\frac{2\\pi}{3}$ radians. The area of the sector is $k\\pi$ square centimeters. What is the value of $k$?",
    "Enter the value of $k$:",
    ["12"],
    "The answer is 12. Area of sector is $A = \\frac{1}{2}r^2\\theta = \\frac{1}{2}(6^2)\\left(\\frac{2\\pi}{3}\\right) = \\frac{1}{2}(36)\\left(\\frac{2\\pi}{3}\\right) = 18 \\times \\frac{2\\pi}{3} = 12\\pi$. Thus $k = 12$."
))

math1.append(make_spr(
    "t2-math-m1-q26", DOMAINS["MATH"]["ALG"], "Linear Equations", "Easy",
    "If $6(x - 3) = 42$, what is the value of $x$?",
    "Enter the value of $x$:",
    ["10"],
    "The answer is 10. Divide by 6: $x - 3 = 7 \\implies x = 10$."
))

math1.append(make_spr(
    "t2-math-m1-q27", DOMAINS["MATH"]["GEOM"], "Cylinder Volume", "Medium",
    "A right circular cylinder has a radius of 4 inches and a height of 10 inches. The volume of the cylinder is $k\\pi$ cubic inches. What is the value of $k$?",
    "Enter the value of $k$:",
    ["160"],
    "The answer is 160. Cylinder volume is $V = \\pi r^2 h = \\pi (4^2)(10) = 160\\pi$. Therefore $k = 160$."
))

# ==========================================
# TEST 2 - MATH MODULE 2 (27 Qs)
# ==========================================

# 1-8 Algebra
math2.append(make_mcq(
    "t2-math-m2-q1", DOMAINS["MATH"]["ALG"], "Linear Systems Infinitely Many Solutions", "Hard",
    "In the system of equations below, $m$ and $p$ are constants:<br>$$mx + 8y = 20$$<br>$$3x + 2y = p$$<br>If the system has infinitely many solutions, what is the value of $m + p$?",
    "Which choice is the value of $m + p$?",
    ["17", "12", "15", "19"],
    "A",
    "Choice A is correct. Multiply the second equation by 4: $12x + 8y = 4p$. For infinitely many solutions, this must be identical to $mx + 8y = 20$. Thus $m = 12$ and $4p = 20 \\implies p = 5$. Therefore $m + p = 12 + 5 = 17$."
))

math2.append(make_mcq(
    "t2-math-m2-q2", DOMAINS["MATH"]["ALG"], "Absolute Value Inequalities", "Hard",
    "What is the set of all integers that satisfy $|2x - 5| \\le 3$?",
    "Which choice is the set of all integers?",
    ["{1, 2, 3, 4}", "{2, 3, 4}", "{1, 2, 3}", "{0, 1, 2, 3, 4}"],
    "A",
    "Choice A is correct. $-3 \\le 2x - 5 \\le 3 \\implies 2 \\le 2x \\le 8 \\implies 1 \\le x \\le 4$. The integers in this interval are 1, 2, 3, and 4."
))

math2.append(make_mcq(
    "t2-math-m2-q3", DOMAINS["MATH"]["ALG"], "Multi-Variable Systems", "Hard",
    "If $3x - 2y = 13$ and $x + 4y = -5$, what is the value of $x - y$?",
    "Which choice is the value of $x - y$?",
    ["5", "3", "7", "1"],
    "A",
    "Choice A is correct. Multiply first eq by 2: $6x - 4y = 26$. Add to second eq: $7x = 21 \\implies x = 3$. Substitute into second: $3 + 4y = -5 \\implies 4y = -8 \\implies y = -2$. Then $x - y = 3 - (-2) = 5$."
))

math2.append(make_mcq(
    "t2-math-m2-q4", DOMAINS["MATH"]["ALG"], "Compound Linear Inequalities", "Medium",
    "Which of the following is equivalent to $-4 < 3x + 5 \\le 14$?",
    "Which choice is equivalent?",
    ["$-3 < x \\le 3$", "$-3 \\le x < 3$", "$-1 < x \\le 3$", "$-9 < x \\le 9$"],
    "A",
    "Choice A is correct. Subtract 5: $-9 < 3x \\le 9$. Divide by 3: $-3 < x \\le 3$."
))

math2.append(make_mcq(
    "t2-math-m2-q5", DOMAINS["MATH"]["ALG"], "Function Transformations", "Medium",
    "The linear function $f(x) = 4x - 6$ is shifted vertically upward by 10 units to create function $g(x)$. What is the x-intercept of $g(x)$?",
    "Which choice is the x-intercept?",
    ["(-1, 0)", "(1, 0)", "(-4, 0)", "(4, 0)"],
    "A",
    "Choice A is correct. $g(x) = f(x) + 10 = 4x - 6 + 10 = 4x + 4$. Setting $g(x) = 0 \\implies 4x + 4 = 0 \\implies x = -1$. The x-intercept is $(-1, 0)$."
))

math2.append(make_mcq(
    "t2-math-m2-q6", DOMAINS["MATH"]["ALG"], "Word Problem Linear Modeling", "Hard",
    "A solar panel installation company offers two financing models. Model A charges $1,200 down and $85 per month. Model B charges $400 down and $125 per month. After how many months will the total payments for both models be equal?",
    "Which choice is the number of months?",
    ["20", "18", "24", "16"],
    "A",
    "Choice A is correct. Set the models equal: $1200 + 85m = 400 + 125m \\implies 800 = 40m \\implies m = 20$ months."
))

math2.append(make_mcq(
    "t2-math-m2-q7", DOMAINS["MATH"]["ALG"], "Perpendicular Bisector Slope", "Hard",
    "Segment $AB$ has endpoints $A(-3, 2)$ and $B(5, 8)$. What is the slope of the perpendicular bisector of segment $AB$?",
    "Which choice is the slope?",
    ["$-\\frac{4}{3}$", "$\\frac{3}{4}$", "$-\\frac{3}{4}$", "$\\frac{4}{3}$"],
    "A",
    "Choice A is correct. Slope of $AB = \\frac{8 - 2}{5 - (-3)} = \\frac{6}{8} = \\frac{3}{4}$. The perpendicular bisector has the negative reciprocal slope, which is $-\\frac{4}{3}$."
))

math2.append(make_mcq(
    "t2-math-m2-q8", DOMAINS["MATH"]["ALG"], "Linear Function Evaluation", "Medium",
    "If $f(x) = mx + b$, $f(3) = 11$, and $f(7) = 23$, what is the value of $f(10)$?",
    "Which choice is the value of $f(10)$?",
    ["32", "29", "35", "30"],
    "A",
    "Choice A is correct. Slope $m = \\frac{23 - 11}{7 - 3} = \\frac{12}{4} = 3$. From $f(3) = 11: 3(3) + b = 11 \\implies b = 2$. Thus $f(x) = 3x + 2$. For $x = 10: f(10) = 3(10) + 2 = 32$."
))

# 9-17 Advanced Math
math2.append(make_mcq(
    "t2-math-m2-q9", DOMAINS["MATH"]["ADV"], "Discriminant Analysis", "Hard",
    "The equation $3x^2 - 12x + k = 0$ has two distinct real solutions. Which inequality represents all possible values of $k$?",
    "Which choice represents $k$?",
    ["$k < 12$", "$k > 12$", "$k < 48$", "$k > 48$"],
    "A",
    "Choice A is correct. For two distinct real solutions, $b^2 - 4ac > 0$. Here $(-12)^2 - 4(3)(k) > 0 \\implies 144 - 12k > 0 \\implies 12k < 144 \\implies k < 12$."
))

math2.append(make_mcq(
    "t2-math-m2-q10", DOMAINS["MATH"]["ADV"], "Completing the Square", "Hard",
    "Which of the following is equivalent to $2x^2 - 16x + 38$?",
    "Which choice is equivalent?",
    ["$2(x - 4)^2 + 6$", "$2(x - 4)^2 + 22$", "$2(x - 8)^2 - 26$", "$(2x - 8)^2 + 6$"],
    "A",
    "Choice A is correct. Factor out 2: $2(x^2 - 8x) + 38 = 2(x^2 - 8x + 16 - 16) + 38 = 2(x - 4)^2 - 32 + 38 = 2(x - 4)^2 + 6$."
))

math2.append(make_mcq(
    "t2-math-m2-q11", DOMAINS["MATH"]["ADV"], "Exponential Growth Rate Comparison", "Hard",
    "Function $f(x) = 40(1.15)^x$ models population growth where $x$ is in years. By what percentage does the population increase every decade (10 years)? (Round to the nearest percent)",
    "Which choice is the percentage increase?",
    ["$305\\%$", "$150\\%$", "$405\\%$", "$15\\%$"],
    "A",
    "Choice A is correct. In 10 years, the growth multiplier is $(1.15)^{10} \\approx 4.0456$. The percentage increase is $(4.0456 - 1) \\times 100\\% \\approx 305\\%$."
))

math2.append(make_mcq(
    "t2-math-m2-q12", DOMAINS["MATH"]["ADV"], "Rational Equations & Extraneous Solutions", "Hard",
    "What is the solution to $\\frac{x}{x - 2} - \\frac{2}{x + 1} = \\frac{6}{x^2 - x - 2}$?",
    "Which choice is the solution?",
    ["-1 is extraneous; no real solution", "$x = 2$", "$x = -1$", "$x = 4$"],
    "A",
    "Choice A is correct. Note that $x^2 - x - 2 = (x - 2)(x + 1)$. Multiplying by $(x - 2)(x + 1)$: $x(x + 1) - 2(x - 2) = 6 \\implies x^2 + x - 2x + 4 = 6 \\implies x^2 - x - 2 = 0 \\implies (x - 2)(x + 1) = 0$. Both $x = 2$ and $x = -1$ make denominators zero, so both are extraneous; there are no real solutions."
))

math2.append(make_mcq(
    "t2-math-m2-q13", DOMAINS["MATH"]["ADV"], "Complex Number Multiplication", "Medium",
    "If $i = \\sqrt{-1}$, what is the value of $(4 - 3i)(2 + 5i)$?",
    "Which choice is the value?",
    ["$23 + 14i$", "$8 - 15i$", "$23 - 14i$", "$7 + 14i$"],
    "A",
    "Choice A is correct. Expand: $4(2) + 4(5i) - 3i(2) - 3i(5i) = 8 + 20i - 6i - 15i^2 = 8 + 14i - 15(-1) = 8 + 14i + 15 = 23 + 14i$."
))

math2.append(make_mcq(
    "t2-math-m2-q14", DOMAINS["MATH"]["ADV"], "Polynomial Long Division", "Hard",
    "What is the quotient and remainder when $3x^2 + 7x + 9$ is divided by $x + 2$?",
    "Which choice is the correct result?",
    ["$3x + 1$ with remainder 7", "$3x + 1$ with remainder 11", "$3x - 1$ with remainder 7", "$3x + 2$ with remainder 5"],
    "A",
    "Choice A is correct. Dividing $3x^2 + 7x + 9$ by $x + 2$: $3x(x + 2) = 3x^2 + 6x$. Subtracting gives remainder $x + 9$. $1(x + 2) = x + 2$. Subtracting gives remainder 7. Quotient is $3x + 1$ with remainder 7."
))

math2.append(make_mcq(
    "t2-math-m2-q15", DOMAINS["MATH"]["ADV"], "Nonlinear Systems of Equations", "Hard",
    "How many real intersection points exist between the circle $x^2 + y^2 = 25$ and the line $y = 2x + 10$?",
    "Which choice is the number of intersection points?",
    ["1", "2", "0", "Infinitely many"],
    "A",
    "Choice A is correct. Substitute $y = 2x + 10$ into circle: $x^2 + (2x + 10)^2 = 25 \\implies x^2 + 4x^2 + 40x + 100 = 25 \\implies 5x^2 + 40x + 75 = 0 \\implies x^2 + 8x + 15 = 0 \\implies (x + 3)(x + 5) = 0$. Wait! That yields TWO real solutions: $x = -3$ and $x = -5$! Let's check: at $x = -3$, $y = 4 \\implies (-3)^2 + 4^2 = 25$. At $x = -5$, $y = 0 \\implies (-5)^2 + 0^2 = 25$. There are 2 intersection points! Let's set the question to ask for 2!"
))
math2[-1]["choices"] = [{"letter": "A", "text": "2"}, {"letter": "B", "text": "1"}, {"letter": "C", "text": "0"}, {"letter": "D", "text": "4"}]
math2[-1]["explanation"] = "Choice A is correct. Substituting $y = 2x + 10$ gives $x^2 + (2x + 10)^2 = 25 \\implies 5x^2 + 40x + 75 = 0 \\implies x^2 + 8x + 15 = 0 \\implies (x + 3)(x + 5) = 0$. This yields two real solutions: $(-3, 4)$ and $(-5, 0)$."

math2.append(make_mcq(
    "t2-math-m2-q16", DOMAINS["MATH"]["ADV"], "Exponential Equations", "Medium",
    "If $2^{3x - 1} = 32$, what is the value of $x$?",
    "Which choice is the value of $x$?",
    ["2", "3", "1", "4"],
    "A",
    "Choice A is correct. Since $32 = 2^5$, we have $2^{3x - 1} = 2^5 \\implies 3x - 1 = 5 \\implies 3x = 6 \\implies x = 2$."
))

math2.append(make_mcq(
    "t2-math-m2-q17", DOMAINS["MATH"]["ADV"], "Rational Exponent Simplification", "Hard",
    "For $x > 0$, if $\\frac{(x^{1/2})^3}{\\sqrt[3]{x^4}} = x^k$, what is the value of $k$?",
    "Which choice is the value of $k$?",
    ["$\\frac{1}{6}$", "$\\frac{5}{6}$", "$\\frac{1}{3}$", "$\\frac{2}{3}$"],
    "A",
    "Choice A is correct. Numerator is $x^{3/2}$. Denominator is $x^{4/3}$. Dividing yields $x^{3/2 - 4/3} = x^{9/6 - 8/6} = x^{1/6}$. Thus $k = 1/6$."
))

# 18-22 Problem-Solving and Data Analysis
math2.append(make_mcq(
    "t2-math-m2-q18", DOMAINS["MATH"]["PSDA"], "Standard Deviation", "Hard",
    "Two classes took the same 100-point physics test. Both classes had an average score of 78. Class 1 scores ranged from 72 to 84. Class 2 scores ranged from 55 to 98. Which statement is true?",
    "Which choice is true?",
    [
        "Class 2 has a greater standard deviation than Class 1.",
        "Class 1 has a greater standard deviation than Class 2.",
        "Both classes have identical standard deviations.",
        "The standard deviation cannot be compared without knowing individual student test scores."
    ],
    "A",
    "Choice A is correct. Standard deviation measures the spread or dispersion of data around the mean. Class 2 has a much wider spread (range of 43 points vs 12 points for Class 1) around the same mean (78), so Class 2 has a greater standard deviation."
))

math2.append(make_mcq(
    "t2-math-m2-q19", DOMAINS["MATH"]["PSDA"], "Margin of Error Sample Size", "Hard",
    "A polling agency surveyed 400 likely voters and found an estimated support of $52\\%$ with a margin of error of $\\pm 4.9\\%$. If the agency wishes to reduce the margin of error to approximately $\\pm 2.45\\%$ at the same confidence level, approximately how many voters must they survey?",
    "Which choice is the required sample size?",
    ["1,600", "800", "2,400", "3,200"],
    "A",
    "Choice A is correct. The margin of error is inversely proportional to the square root of sample size: $ME \\propto \\frac{1}{\\sqrt{n}}$. To halve the margin of error (from 4.9% to 2.45%), the sample size must be multiplied by $2^2 = 4$. Thus $400 \\times 4 = 1,600$."
))

math2.append(make_mcq(
    "t2-math-m2-q20", DOMAINS["MATH"]["PSDA"], "Conditional Probability", "Hard",
    "In a company of 200 employees, 120 work in sales and 80 work in engineering. Among sales staff, $25\\%$ hold an advanced degree. Among engineers, $60\\%$ hold an advanced degree. What percentage of all employees who hold an advanced degree are engineers?",
    "Which choice is the percentage?",
    ["$61.5\\%$", "$40.0\\%$", "$50.0\\%$", "$72.0\\%$"],
    "A",
    "Choice A is correct. Sales with advanced degree: $120 \\times 0.25 = 30$. Engineers with advanced degree: $80 \\times 0.60 = 48$. Total holding advanced degrees $= 30 + 48 = 78$. The percentage who are engineers is $\\frac{48}{78} \\approx 0.6154$ or $61.5\\%$."
))

math2.append(make_mcq(
    "t2-math-m2-q21", DOMAINS["MATH"]["PSDA"], "Box Plots & IQR", "Medium",
    "A dataset has a minimum of 14, first quartile ($Q_1$) of 22, median of 35, third quartile ($Q_3$) of 46, and maximum of 68. What is the interquartile range (IQR) of this dataset?",
    "Which choice is the IQR?",
    ["24", "54", "35", "13"],
    "A",
    "Choice A is correct. The interquartile range is defined as $IQR = Q_3 - Q_1 = 46 - 22 = 24$."
))

math2.append(make_mcq(
    "t2-math-m2-q22", DOMAINS["MATH"]["PSDA"], "Unit Conversions Multi-Step", "Medium",
    "An industrial pump discharges water at a rate of 45 liters per minute. Given that 1 liter is 1,000 cubic centimeters and 1 hour is 60 minutes, how many cubic centimeters does the pump discharge in 3 hours?",
    "Which choice is the total discharge?",
    ["8,100,000", "2,700,000", "135,000", "4,500,000"],
    "A",
    "Choice A is correct. $45 \\text{ L/min} \\times 60 \\text{ min/hr} \\times 3 \\text{ hr} = 8,100 \\text{ liters}$. Converting to cubic centimeters: $8,100 \\times 1,000 = 8,100,000 \\text{ cm}^3$."
))

# 23-27 Geometry & Trig (SPR Grid-Ins for 23-27)
math2.append(make_spr(
    "t2-math-m2-q23", DOMAINS["MATH"]["GEOM"], "Circle Completing the Square", "Hard",
    "A circle in the xy-plane has the equation $x^2 + y^2 + 10x - 4y - 7 = 0$. What is the radius of the circle?",
    "Enter the radius:",
    ["6"],
    "The answer is 6. Group and complete squares: $(x^2 + 10x + 25) + (y^2 - 4y + 4) = 7 + 25 + 4 \\implies (x + 5)^2 + (y - 2)^2 = 36$. Radius $r = \\sqrt{36} = 6$."
))

math2.append(make_spr(
    "t2-math-m2-q24", DOMAINS["MATH"]["GEOM"], "Similar Triangles & Scale Factor", "Hard",
    "Triangle $PQR$ is similar to triangle $STU$, where vertex $P$ corresponds to $S$. If the perimeter of $PQR$ is 24 and the perimeter of $STU$ is 60, and side $PQ = 6$, what is the length of side $ST$?",
    "Enter the length of side $ST$:",
    ["15"],
    "The answer is 15. The ratio of perimeters equals the ratio of corresponding side lengths: $\\frac{\\text{Perimeter}(STU)}{\\text{Perimeter}(PQR)} = \\frac{60}{24} = 2.5$. Therefore, $ST = 2.5 \\times PQ = 2.5 \\times 6 = 15$."
))

math2.append(make_spr(
    "t2-math-m2-q25", DOMAINS["MATH"]["GEOM"], "Cofunction Trigonometric Identity", "Medium",
    "In a right triangle with acute angles $A$ and $B$, $\\cos(A) = \\frac{7}{25}$. What is the value of $\\sin(B)$?",
    "Enter the exact fractional or decimal value of $\\sin(B)$:",
    ["7/25", "0.28"],
    "The answer is 7/25 (or 0.28). In any right triangle, acute angles $A$ and $B$ are complementary ($A + B = 90^\\circ$), so $\\sin(B) = \\cos(A) = \\frac{7}{25} = 0.28$."
))

math2.append(make_spr(
    "t2-math-m2-q26", DOMAINS["MATH"]["ADV"], "Vertex of Parabola Minimum Value", "Hard",
    "What is the minimum y-value of the parabola $y = 2x^2 - 12x + 25$?",
    "Enter the minimum value:",
    ["7"],
    "The answer is 7. The vertex x-coordinate is $x = -\\frac{-12}{2(2)} = 3$. Evaluating at $x = 3$: $y = 2(3^2) - 12(3) + 25 = 18 - 36 + 25 = 7$."
))

math2.append(make_spr(
    "t2-math-m2-q27", DOMAINS["MATH"]["GEOM"], "Radian Angle Measure", "Easy",
    "An angle measures $210^\\circ$. Expressed in radians, the angle is $\\frac{k\\pi}{6}$. What is the value of the integer $k$?",
    "Enter the value of $k$:",
    ["7"],
    "The answer is 7. Convert degrees to radians: $210^\\circ \\times \\frac{\\pi}{180^\\circ} = \\frac{21\\pi}{18} = \\frac{7\\pi}{6}$. Therefore $k = 7$."
))

print(f"Test 2 Math Module 1 ready: {len(math1)} questions.")
print(f"Test 2 Math Module 2 ready: {len(math2)} questions.")
