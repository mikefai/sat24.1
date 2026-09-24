// calculator.js - Digital SAT Built-in Graphing & Scientific Calculator

export const Calculator = {
  activeTab: "graphing",
  angleMode: "deg", // 'deg' or 'rad'
  graphScale: 25, // pixels per unit
  originX: 0,
  originY: 0,
  functions: ["x^2 - 4", "2*x + 1"],
  activeColor: ["#2563eb", "#dc2626", "#16a34a"],

  renderModal() {
    return `
    <div id="calc-modal" class="sat-modal-overlay hidden" role="dialog" aria-modal="true" aria-labelledby="calc-title">
      <div class="sat-modal-content calc-modal-content">
        <div class="sat-modal-header">
          <div class="modal-title-wrap">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <rect x="4" y="2" width="16" height="20" rx="2"/>
              <line x1="8" y1="6" x2="16" y2="6"/>
              <line x1="16" y1="14" x2="16" y2="18"/>
              <path d="M8 10h.01M12 10h.01M16 10h.01M8 14h.01M12 14h.01M8 18h.01M12 18h.01"/>
            </svg>
            <h2 id="calc-title">Graphing Calculator</h2>
          </div>
          <div class="calc-tab-group">
            <button id="calc-tab-graph" class="calc-tab-btn active">Graphing</button>
            <button id="calc-tab-sci" class="calc-tab-btn">Scientific</button>
          </div>
          <button id="close-calc-modal" class="sat-modal-close" aria-label="Close Calculator">&times;</button>
        </div>

        <div class="sat-modal-body calc-modal-body">
          <!-- GRAPHING VIEW -->
          <div id="calc-graphing-view" class="calc-view">
            <div class="calc-graph-controls">
              <div class="func-input-wrap">
                <span class="func-label" style="color: #2563eb;">y₁ =</span>
                <input type="text" id="calc-func-1" class="calc-func-input" value="x^2 - 4" placeholder="e.g. x^2 - 4">
              </div>
              <div class="func-input-wrap">
                <span class="func-label" style="color: #dc2626;">y₂ =</span>
                <input type="text" id="calc-func-2" class="calc-func-input" value="2*x + 1" placeholder="e.g. 2*x + 1">
              </div>
              <div class="calc-graph-actions">
                <button id="btn-plot-graph" class="sat-btn sat-btn-primary sat-btn-sm">Plot Graph</button>
                <button id="btn-zoom-in" class="sat-btn sat-btn-secondary sat-btn-sm" title="Zoom In">+</button>
                <button id="btn-zoom-out" class="sat-btn sat-btn-secondary sat-btn-sm" title="Zoom Out">−</button>
                <button id="btn-zoom-reset" class="sat-btn sat-btn-secondary sat-btn-sm" title="Reset View">Reset</button>
              </div>
            </div>
            <div class="canvas-container">
              <canvas id="calc-graph-canvas" width="560" height="340"></canvas>
              <div id="calc-coord-tooltip" class="calc-tooltip hidden"></div>
            </div>
          </div>

          <!-- SCIENTIFIC VIEW -->
          <div id="calc-sci-view" class="calc-view hidden">
            <div class="sci-display-wrap">
              <div id="sci-expr" class="sci-expr-line"></div>
              <div id="sci-result" class="sci-result-line">0</div>
            </div>

            <div class="sci-mode-bar">
              <button id="btn-angle-mode" class="calc-badge-btn">DEG</button>
              <span class="sci-mode-hint">Digital SAT Standard Mode</span>
            </div>

            <div class="sci-keypad">
              <!-- Row 1 -->
              <button class="calc-btn fn-btn" data-val="sin(">sin</button>
              <button class="calc-btn fn-btn" data-val="cos(">cos</button>
              <button class="calc-btn fn-btn" data-val="tan(">tan</button>
              <button class="calc-btn fn-btn" data-val="pi">π</button>
              <button class="calc-btn fn-btn" data-val="e">e</button>
              <button class="calc-btn danger-btn" id="btn-sci-clear">AC</button>
              <button class="calc-btn danger-btn" id="btn-sci-del">DEL</button>

              <!-- Row 2 -->
              <button class="calc-btn fn-btn" data-val="asin(">sin⁻¹</button>
              <button class="calc-btn fn-btn" data-val="acos(">cos⁻¹</button>
              <button class="calc-btn fn-btn" data-val="atan(">tan⁻¹</button>
              <button class="calc-btn fn-btn" data-val="(">(</button>
              <button class="calc-btn fn-btn" data-val=")">)</button>
              <button class="calc-btn op-btn" data-val="/">÷</button>
              <button class="calc-btn op-btn" data-val="*">×</button>

              <!-- Row 3 -->
              <button class="calc-btn fn-btn" data-val="sqrt(">√</button>
              <button class="calc-btn fn-btn" data-val="^2">x²</button>
              <button class="calc-btn fn-btn" data-val="^">xʸ</button>
              <button class="calc-btn num-btn" data-val="7">7</button>
              <button class="calc-btn num-btn" data-val="8">8</button>
              <button class="calc-btn num-btn" data-val="9">9</button>
              <button class="calc-btn op-btn" data-val="-">−</button>

              <!-- Row 4 -->
              <button class="calc-btn fn-btn" data-val="ln(">ln</button>
              <button class="calc-btn fn-btn" data-val="log(">log</button>
              <button class="calc-btn fn-btn" data-val="abs(">|x|</button>
              <button class="calc-btn num-btn" data-val="4">4</button>
              <button class="calc-btn num-btn" data-val="5">5</button>
              <button class="calc-btn num-btn" data-val="6">6</button>
              <button class="calc-btn op-btn" data-val="+">+</button>

              <!-- Row 5 -->
              <button class="calc-btn fn-btn" data-val="10^">10ˣ</button>
              <button class="calc-btn fn-btn" data-val="Ans">Ans</button>
              <button class="calc-btn fn-btn" data-val="%">%</button>
              <button class="calc-btn num-btn" data-val="1">1</button>
              <button class="calc-btn num-btn" data-val="2">2</button>
              <button class="calc-btn num-btn" data-val="3">3</button>
              <button class="calc-btn eq-btn" id="btn-sci-eq" rowspan="2">=</button>

              <!-- Row 6 -->
              <button class="calc-btn num-btn wide-2" data-val="0" style="grid-column: span 2;">0</button>
              <button class="calc-btn num-btn" data-val=".">.</button>
              <button class="calc-btn fn-btn" data-val="(-)">(-)</button>
            </div>
          </div>
        </div>
      </div>
    </div>
    `;
  },

  initEvents() {
    const modal = document.getElementById("calc-modal");
    const closeBtn = document.getElementById("close-calc-modal");
    const tabGraph = document.getElementById("calc-tab-graph");
    const tabSci = document.getElementById("calc-tab-sci");
    const viewGraph = document.getElementById("calc-graphing-view");
    const viewSci = document.getElementById("calc-sci-view");

    if (!modal) return;

    const hide = () => modal.classList.add("hidden");
    if (closeBtn) closeBtn.onclick = hide;

    // Tab switching
    if (tabGraph && tabSci) {
      tabGraph.onclick = () => {
        tabGraph.classList.add("active");
        tabSci.classList.remove("active");
        viewGraph.classList.remove("hidden");
        viewSci.classList.add("hidden");
        this.activeTab = "graphing";
        this.drawGraph();
      };
      tabSci.onclick = () => {
        tabSci.classList.add("active");
        tabGraph.classList.remove("active");
        viewSci.classList.remove("hidden");
        viewGraph.classList.add("hidden");
        this.activeTab = "scientific";
      };
    }

    // Graphing controls
    const btnPlot = document.getElementById("btn-plot-graph");
    const btnZoomIn = document.getElementById("btn-zoom-in");
    const btnZoomOut = document.getElementById("btn-zoom-out");
    const btnReset = document.getElementById("btn-zoom-reset");
    const input1 = document.getElementById("calc-func-1");
    const input2 = document.getElementById("calc-func-2");

    if (btnPlot) {
      btnPlot.onclick = () => {
        this.functions = [input1.value.trim(), input2.value.trim()].filter(Boolean);
        this.drawGraph();
      };
    }
    if (btnZoomIn) {
      btnZoomIn.onclick = () => {
        this.graphScale = Math.min(100, this.graphScale * 1.3);
        this.drawGraph();
      };
    }
    if (btnZoomOut) {
      btnZoomOut.onclick = () => {
        this.graphScale = Math.max(8, this.graphScale / 1.3);
        this.drawGraph();
      };
    }
    if (btnReset) {
      btnReset.onclick = () => {
        this.graphScale = 25;
        const canvas = document.getElementById("calc-graph-canvas");
        if (canvas) {
          this.originX = canvas.width / 2;
          this.originY = canvas.height / 2;
        }
        this.drawGraph();
      };
    }

    // Canvas Mouse interaction
    const canvas = document.getElementById("calc-graph-canvas");
    const tooltip = document.getElementById("calc-coord-tooltip");
    let isDragging = false;
    let startX = 0, startY = 0;

    if (canvas) {
      this.originX = canvas.width / 2;
      this.originY = canvas.height / 2;

      canvas.onmousedown = (e) => {
        isDragging = true;
        startX = e.clientX - this.originX;
        startY = e.clientY - this.originY;
      };
      window.addEventListener("mouseup", () => { isDragging = false; });
      canvas.onmousemove = (e) => {
        const rect = canvas.getBoundingClientRect();
        const mouseX = e.clientX - rect.left;
        const mouseY = e.clientY - rect.top;

        if (isDragging) {
          this.originX = e.clientX - startX;
          this.originY = e.clientY - startY;
          this.drawGraph();
          tooltip.classList.add("hidden");
        } else {
          // Tooltip calculation
          const mathX = (mouseX - this.originX) / this.graphScale;
          const mathY = -(mouseY - this.originY) / this.graphScale;
          tooltip.textContent = `(${mathX.toFixed(2)}, ${mathY.toFixed(2)})`;
          tooltip.style.left = `${mouseX + 12}px`;
          tooltip.style.top = `${mouseY + 12}px`;
          tooltip.classList.remove("hidden");
        }
      };
      canvas.onmouseleave = () => {
        if (!isDragging) tooltip.classList.add("hidden");
      };
    }

    // Scientific Calculator Setup
    this.initScientific();
  },

  sciExpression: "",
  lastAnswer: 0,

  initScientific() {
    const exprDisplay = document.getElementById("sci-expr");
    const resDisplay = document.getElementById("sci-result");
    const modeBtn = document.getElementById("btn-angle-mode");
    const clearBtn = document.getElementById("btn-sci-clear");
    const delBtn = document.getElementById("btn-sci-del");
    const eqBtn = document.getElementById("btn-sci-eq");

    if (modeBtn) {
      modeBtn.onclick = () => {
        this.angleMode = this.angleMode === "deg" ? "rad" : "deg";
        modeBtn.textContent = this.angleMode.toUpperCase();
      };
    }

    const updateDisplay = () => {
      if (exprDisplay) exprDisplay.textContent = this.sciExpression || "";
    };

    if (clearBtn) {
      clearBtn.onclick = () => {
        this.sciExpression = "";
        updateDisplay();
        if (resDisplay) resDisplay.textContent = "0";
      };
    }

    if (delBtn) {
      delBtn.onclick = () => {
        this.sciExpression = this.sciExpression.slice(0, -1);
        updateDisplay();
      };
    }

    document.querySelectorAll(".sci-keypad .calc-btn[data-val]").forEach(btn => {
      btn.onclick = () => {
        const val = btn.getAttribute("data-val");
        if (val === "(-)") {
          this.sciExpression += "-";
        } else if (val === "Ans") {
          this.sciExpression += this.lastAnswer;
        } else {
          this.sciExpression += val;
        }
        updateDisplay();
      };
    });

    if (eqBtn) {
      eqBtn.onclick = () => {
        if (!this.sciExpression.trim()) return;
        try {
          const evaluated = this.evaluateMath(this.sciExpression);
          this.lastAnswer = evaluated;
          if (resDisplay) {
            // Format cleanly
            const rounded = Number.isInteger(evaluated) ? evaluated : Number(evaluated.toFixed(6));
            resDisplay.textContent = isNaN(rounded) ? "Error" : String(rounded);
          }
        } catch (e) {
          if (resDisplay) resDisplay.textContent = "Error";
        }
      };
    }
  },

  evaluateMath(expr) {
    let clean = expr
      .replace(/\bpi\b/g, String(Math.PI))
      .replace(/\be\b/g, String(Math.E))
      .replace(/\^/g, "**")
      .replace(/\bsqrt\(/g, "Math.sqrt(")
      .replace(/\babs\(/g, "Math.abs(")
      .replace(/\blog10\(/g, "Math.log10(")
      .replace(/\blog\(/g, "Math.log10(")
      .replace(/\bln\(/g, "Math.log(");

    // Trig replacements with deg/rad support (asin/acos/atan MUST precede sin/cos/tan)
    if (this.angleMode === "deg") {
      clean = clean
        .replace(/\basin\(([^)]+)\)/g, "(Math.asin($1) * 180 / Math.PI)")
        .replace(/\bacos\(([^)]+)\)/g, "(Math.acos($1) * 180 / Math.PI)")
        .replace(/\batan\(([^)]+)\)/g, "(Math.atan($1) * 180 / Math.PI)")
        .replace(/\bsin\(([^)]+)\)/g, "Math.sin(($1) * Math.PI / 180)")
        .replace(/\bcos\(([^)]+)\)/g, "Math.cos(($1) * Math.PI / 180)")
        .replace(/\btan\(([^)]+)\)/g, "Math.tan(($1) * Math.PI / 180)");
    } else {
      clean = clean
        .replace(/\basin\(/g, "Math.asin(")
        .replace(/\bacos\(/g, "Math.acos(")
        .replace(/\batan\(/g, "Math.atan(")
        .replace(/\bsin\(/g, "Math.sin(")
        .replace(/\bcos\(/g, "Math.cos(")
        .replace(/\btan\(/g, "Math.tan(");
    }

    // Safe mathematical evaluation: disallow harmful tokens
    if (/(window|document|fetch|eval|Function|localStorage|sessionStorage|alert|console|process|import|require)/i.test(clean)) {
      throw new Error("Invalid formula expression");
    }

    if (/[^a-zA-Z0-9\+\-\*\/\(\)\.\,\s]/.test(clean)) {
      throw new Error("Invalid characters in expression");
    }

    return Function(`"use strict"; return (${clean});`)();
  },

  drawGraph() {
    const canvas = document.getElementById("calc-graph-canvas");
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const w = canvas.width;
    const h = canvas.height;

    ctx.clearRect(0, 0, w, h);

    // Draw background
    ctx.fillStyle = "#ffffff";
    ctx.fillRect(0, 0, w, h);

    // Draw Grid Lines
    ctx.strokeStyle = "#e2e8f0";
    ctx.lineWidth = 1;

    const startX = this.originX % this.graphScale;
    for (let x = startX; x < w; x += this.graphScale) {
      ctx.beginPath();
      ctx.moveTo(x, 0);
      ctx.lineTo(x, h);
      ctx.stroke();
    }

    const startY = this.originY % this.graphScale;
    for (let y = startY; y < h; y += this.graphScale) {
      ctx.beginPath();
      ctx.moveTo(0, y);
      ctx.lineTo(w, y);
      ctx.stroke();
    }

    // Axes
    ctx.strokeStyle = "#64748b";
    ctx.lineWidth = 1.8;

    // X Axis
    ctx.beginPath();
    ctx.moveTo(0, this.originY);
    ctx.lineTo(w, this.originY);
    ctx.stroke();

    // Y Axis
    ctx.beginPath();
    ctx.moveTo(this.originX, 0);
    ctx.lineTo(this.originX, h);
    ctx.stroke();

    // Axis Labels
    ctx.fillStyle = "#64748b";
    ctx.font = "11px Inter, sans-serif";
    ctx.textAlign = "center";

    // Numbers on X
    for (let x = startX; x < w; x += this.graphScale * 2) {
      const val = Math.round((x - this.originX) / this.graphScale);
      if (val !== 0) {
        ctx.fillText(val, x, Math.min(h - 5, Math.max(15, this.originY + 14)));
      }
    }

    // Numbers on Y
    ctx.textAlign = "right";
    for (let y = startY; y < h; y += this.graphScale * 2) {
      const val = Math.round(-(y - this.originY) / this.graphScale);
      if (val !== 0) {
        ctx.fillText(val, Math.min(w - 5, Math.max(20, this.originX - 6)), y + 4);
      }
    }

    // Plot functions
    this.functions.forEach((fnStr, index) => {
      if (!fnStr) return;
      const color = this.activeColor[index % this.activeColor.length];
      this.plotSingleFunction(ctx, fnStr, color, w, h);
    });
  },

  plotSingleFunction(ctx, fnStr, color, w, h) {
    let jsExpr = fnStr
      .replace(/\^/g, "**")
      .replace(/\basin\(/g, "Math.asin(")
      .replace(/\bacos\(/g, "Math.acos(")
      .replace(/\batan\(/g, "Math.atan(")
      .replace(/\bsin\(/g, "Math.sin(")
      .replace(/\bcos\(/g, "Math.cos(")
      .replace(/\btan\(/g, "Math.tan(")
      .replace(/\bsqrt\(/g, "Math.sqrt(")
      .replace(/\babs\(/g, "Math.abs(")
      .replace(/\blog10\(/g, "Math.log10(")
      .replace(/\blog\(/g, "Math.log10(")
      .replace(/\bln\(/g, "Math.log(")
      .replace(/\bpi\b/g, "Math.PI")
      .replace(/\be\b/g, "Math.E");

    // Support implicit multiplication like 2x, 3(x), (x)(x), etc.
    jsExpr = jsExpr
      .replace(/(\d)x/gi, "$1*x")
      .replace(/(\d)\(/g, "$1*(")
      .replace(/\)\(/g, ")*(")
      .replace(/x\(/gi, "x*(")
      .replace(/\)x/gi, ")*x");

    ctx.strokeStyle = color;
    ctx.lineWidth = 2.2;
    ctx.beginPath();

    let started = false;
    for (let px = 0; px <= w; px += 2) {
      const x = (px - this.originX) / this.graphScale;
      try {
        const y = Function("x", `"use strict"; return (${jsExpr});`)(x);
        if (isNaN(y) || !isFinite(y)) {
          started = false;
          continue;
        }

        const py = this.originY - y * this.graphScale;
        if (!started) {
          ctx.moveTo(px, py);
          started = true;
        } else {
          ctx.lineTo(px, py);
        }
      } catch (e) {
        started = false;
      }
    }
    ctx.stroke();
  },

  open() {
    const modal = document.getElementById("calc-modal");
    if (modal) {
      modal.classList.remove("hidden");
      setTimeout(() => this.drawGraph(), 50);
    }
  }
};
