// referenceSheet.js - Official Digital SAT Math Reference Sheet Modal

export const ReferenceSheet = {
  renderModal() {
    return `
    <div id="reference-modal" class="sat-modal-overlay hidden" role="dialog" aria-modal="true" aria-labelledby="ref-sheet-title">
      <div class="sat-modal-content ref-sheet-modal">
        <div class="sat-modal-header">
          <div class="modal-title-wrap">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/>
              <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>
            </svg>
            <h2 id="ref-sheet-title">Reference Sheet</h2>
          </div>
          <button id="close-ref-modal" class="sat-modal-close" aria-label="Close Reference Sheet">&times;</button>
        </div>

        <div class="sat-modal-body ref-sheet-body">
          <div class="ref-intro">
            <strong>Reference Information:</strong> Use this official College Board reference sheet as needed during the Math section.
          </div>

          <div class="ref-grid">
            <!-- Circle Area & Circumference -->
            <div class="ref-card">
              <svg width="120" height="85" viewBox="0 0 120 85">
                <circle cx="60" cy="45" r="32" fill="#f8fafc" stroke="#1e293b" stroke-width="2"/>
                <line x1="60" y1="45" x2="92" y2="45" stroke="#2563eb" stroke-width="2"/>
                <circle cx="60" cy="45" r="2.5" fill="#1e293b"/>
                <text x="73" y="40" font-size="12" fill="#2563eb" font-weight="600">r</text>
              </svg>
              <div class="ref-formula">\\(A = \\pi r^2\\)</div>
              <div class="ref-formula">\\(C = 2\\pi r\\)</div>
            </div>

            <!-- Rectangle Area -->
            <div class="ref-card">
              <svg width="120" height="85" viewBox="0 0 120 85">
                <rect x="25" y="20" width="70" height="45" fill="#f8fafc" stroke="#1e293b" stroke-width="2"/>
                <text x="56" y="15" font-size="12" fill="#334155" font-weight="600">\\(l\\)</text>
                <text x="100" y="47" font-size="12" fill="#334155" font-weight="600">\\(w\\)</text>
              </svg>
              <div class="ref-formula">\\(A = lw\\)</div>
            </div>

            <!-- Triangle Area -->
            <div class="ref-card">
              <svg width="120" height="85" viewBox="0 0 120 85">
                <polygon points="20,68 100,68 60,18" fill="#f8fafc" stroke="#1e293b" stroke-width="2"/>
                <line x1="60" y1="18" x2="60" y2="68" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="3,2"/>
                <text x="64" y="46" font-size="11" fill="#dc2626">\\(h\\)</text>
                <text x="58" y="80" font-size="12" fill="#334155">\\(b\\)</text>
              </svg>
              <div class="ref-formula">\\(A = \\frac{1}{2}bh\\)</div>
            </div>

            <!-- Pythagorean Theorem -->
            <div class="ref-card">
              <svg width="120" height="85" viewBox="0 0 120 85">
                <polygon points="25,70 95,70 95,20" fill="#f8fafc" stroke="#1e293b" stroke-width="2"/>
                <rect x="85" y="60" width="10" height="10" fill="none" stroke="#1e293b" stroke-width="1"/>
                <text x="55" y="82" font-size="12" fill="#334155">\\(a\\)</text>
                <text x="102" y="48" font-size="12" fill="#334155">\\(b\\)</text>
                <text x="50" y="40" font-size="12" fill="#2563eb" font-weight="600">\\(c\\)</text>
              </svg>
              <div class="ref-formula">\\(c^2 = a^2 + b^2\\)</div>
            </div>

            <!-- Special Right Triangle 1 (30-60-90) -->
            <div class="ref-card">
              <svg width="130" height="85" viewBox="0 0 130 85">
                <polygon points="20,70 100,70 100,15" fill="#f8fafc" stroke="#1e293b" stroke-width="2"/>
                <rect x="90" y="60" width="10" height="10" fill="none" stroke="#1e293b" stroke-width="1"/>
                <text x="35" y="66" font-size="10" fill="#475569">\\(30^\\circ\\)</text>
                <text x="82" y="32" font-size="10" fill="#475569">\\(60^\\circ\\)</text>
                <text x="55" y="82" font-size="11" fill="#334155">\\(x\\sqrt{3}\\)</text>
                <text x="105" y="46" font-size="11" fill="#334155">\\(x\\)</text>
                <text x="50" y="38" font-size="11" fill="#2563eb" font-weight="600">\\(2x\\)</text>
              </svg>
              <div class="ref-formula">Special Right \\(30^\\circ-60^\\circ-90^\\circ\\)</div>
            </div>

            <!-- Special Right Triangle 2 (45-45-90) -->
            <div class="ref-card">
              <svg width="130" height="85" viewBox="0 0 130 85">
                <polygon points="30,70 95,70 95,15" fill="#f8fafc" stroke="#1e293b" stroke-width="2"/>
                <rect x="85" y="60" width="10" height="10" fill="none" stroke="#1e293b" stroke-width="1"/>
                <text x="42" y="66" font-size="10" fill="#475569">\\(45^\\circ\\)</text>
                <text x="77" y="30" font-size="10" fill="#475569">\\(45^\\circ\\)</text>
                <text x="60" y="82" font-size="11" fill="#334155">\\(s\\)</text>
                <text x="102" y="45" font-size="11" fill="#334155">\\(s\\)</text>
                <text x="48" y="38" font-size="11" fill="#2563eb" font-weight="600">\\(s\\sqrt{2}\\)</text>
              </svg>
              <div class="ref-formula">Special Right \\(45^\\circ-45^\\circ-90^\\circ\\)</div>
            </div>

            <!-- Rectangular Prism Volume -->
            <div class="ref-card">
              <svg width="120" height="85" viewBox="0 0 120 85">
                <rect x="25" y="35" width="55" height="35" fill="#f8fafc" stroke="#1e293b" stroke-width="1.5"/>
                <polygon points="25,35 45,18 100,18 80,35" fill="#f1f5f9" stroke="#1e293b" stroke-width="1.5"/>
                <polygon points="80,35 100,18 100,53 80,70" fill="#e2e8f0" stroke="#1e293b" stroke-width="1.5"/>
                <text x="50" y="80" font-size="11" fill="#334155">\\(l\\)</text>
                <text x="92" y="65" font-size="11" fill="#334155">\\(w\\)</text>
                <text x="15" y="55" font-size="11" fill="#334155">\\(h\\)</text>
              </svg>
              <div class="ref-formula">\\(V = lwh\\)</div>
            </div>

            <!-- Cylinder Volume -->
            <div class="ref-card">
              <svg width="120" height="85" viewBox="0 0 120 85">
                <ellipse cx="60" cy="22" rx="30" ry="10" fill="#f8fafc" stroke="#1e293b" stroke-width="1.5"/>
                <path d="M 30,22 L 30,62 A 30,10 0 0,0 90,62 L 90,22" fill="#f8fafc" stroke="#1e293b" stroke-width="1.5"/>
                <line x1="60" y1="22" x2="90" y2="22" stroke="#2563eb" stroke-width="1.5"/>
                <text x="73" y="19" font-size="10" fill="#2563eb">\\(r\\)</text>
                <text x="96" y="46" font-size="11" fill="#334155">\\(h\\)</text>
              </svg>
              <div class="ref-formula">\\(V = \\pi r^2 h\\)</div>
            </div>

            <!-- Sphere Volume -->
            <div class="ref-card">
              <svg width="120" height="85" viewBox="0 0 120 85">
                <circle cx="60" cy="42" r="28" fill="#f8fafc" stroke="#1e293b" stroke-width="1.5"/>
                <ellipse cx="60" cy="42" rx="28" ry="8" fill="none" stroke="#94a3b8" stroke-dasharray="3,2" stroke-width="1"/>
                <line x1="60" y1="42" x2="88" y2="42" stroke="#2563eb" stroke-width="1.5"/>
                <circle cx="60" cy="42" r="2" fill="#1e293b"/>
                <text x="72" y="38" font-size="10" fill="#2563eb">\\(r\\)</text>
              </svg>
              <div class="ref-formula">\\(V = \\frac{4}{3}\\pi r^3\\)</div>
            </div>

            <!-- Cone Volume -->
            <div class="ref-card">
              <svg width="120" height="85" viewBox="0 0 120 85">
                <ellipse cx="60" cy="65" rx="30" ry="9" fill="#f8fafc" stroke="#1e293b" stroke-width="1.5"/>
                <line x1="30" y1="65" x2="60" y2="15" stroke="#1e293b" stroke-width="1.5"/>
                <line x1="90" y1="65" x2="60" y2="15" stroke="#1e293b" stroke-width="1.5"/>
                <line x1="60" y1="15" x2="60" y2="65" stroke="#dc2626" stroke-width="1" stroke-dasharray="3,2"/>
                <line x1="60" y1="65" x2="90" y2="65" stroke="#2563eb" stroke-width="1.5"/>
                <text x="73" y="62" font-size="10" fill="#2563eb">\\(r\\)</text>
                <text x="52" y="40" font-size="10" fill="#dc2626">\\(h\\)</text>
              </svg>
              <div class="ref-formula">\\(V = \\frac{1}{3}\\pi r^2 h\\)</div>
            </div>

            <!-- Pyramid Volume -->
            <div class="ref-card">
              <svg width="120" height="85" viewBox="0 0 120 85">
                <polygon points="25,65 75,65 95,50 45,50" fill="#f8fafc" stroke="#1e293b" stroke-width="1.5"/>
                <line x1="25" y1="65" x2="60" y2="15" stroke="#1e293b" stroke-width="1.5"/>
                <line x1="75" y1="65" x2="60" y2="15" stroke="#1e293b" stroke-width="1.5"/>
                <line x1="95" y1="50" x2="60" y2="15" stroke="#1e293b" stroke-width="1.5"/>
                <line x1="60" y1="15" x2="60" y2="57" stroke="#dc2626" stroke-width="1" stroke-dasharray="3,2"/>
                <text x="50" y="78" font-size="11" fill="#334155">\\(l\\)</text>
                <text x="88" y="62" font-size="11" fill="#334155">\\(w\\)</text>
                <text x="52" y="38" font-size="10" fill="#dc2626">\\(h\\)</text>
              </svg>
              <div class="ref-formula">\\(V = \\frac{1}{3}lwh\\)</div>
            </div>
          </div>

          <!-- Crucial Geometry Notes -->
          <div class="ref-notes">
            <ul>
              <li>The number of degrees of arc in a circle is <strong>360</strong>.</li>
              <li>The number of radians of arc in a circle is <strong>\\(2\\pi\\)</strong>.</li>
              <li>The sum of the measures in degrees of the angles of a triangle is <strong>180</strong>.</li>
            </ul>
          </div>
        </div>

        <div class="sat-modal-footer">
          <button id="btn-ref-close-footer" class="sat-btn sat-btn-primary">Close Reference</button>
        </div>
      </div>
    </div>
    `;
  },

  initEvents() {
    const modal = document.getElementById("reference-modal");
    const closeBtn = document.getElementById("close-ref-modal");
    const closeFooter = document.getElementById("btn-ref-close-footer");

    if (!modal) return;

    const hide = () => modal.classList.add("hidden");
    if (closeBtn) closeBtn.onclick = hide;
    if (closeFooter) closeFooter.onclick = hide;

    // Close on overlay click
    modal.onclick = (e) => {
      if (e.target === modal) hide();
    };

    // Close on Escape key
    window.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && !modal.classList.contains("hidden")) {
        hide();
      }
    });
  },

  open() {
    const modal = document.getElementById("reference-modal");
    if (modal) {
      modal.classList.remove("hidden");
      if (window.renderMathInElement) {
        window.renderMathInElement(modal, {
          delimiters: [
            { left: "$$", right: "$$", display: true },
            { left: "\\(", right: "\\)", display: false }
          ]
        });
      }
    }
  }
};
