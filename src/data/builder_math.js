// Math Question Builder with rich, authentic SAT question structures
import { DOMAINS } from './scoring.js';

export function makeMathMCQ(id, domain, subdomain, stimulus, prompt, choices, correctLetter, explanation, difficulty = "Medium", visual = null) {
  return {
    id,
    type: "mcq",
    domain,
    subdomain,
    difficulty,
    stimulus: visual ? `${visual}<br>${stimulus || ''}` : stimulus,
    prompt,
    choices: choices.map((c, i) => ({
      letter: String.fromCharCode(65 + i),
      text: c
    })),
    correctAnswer: correctLetter,
    explanation
  };
}

export function makeMathSPR(id, domain, subdomain, stimulus, prompt, correctAnswers, explanation, difficulty = "Medium", visual = null) {
  return {
    id,
    type: "spr", // Student-Produced Response
    domain,
    subdomain,
    difficulty,
    stimulus: visual ? `${visual}<br>${stimulus || ''}` : stimulus,
    prompt,
    correctAnswer: Array.isArray(correctAnswers) ? correctAnswers : [correctAnswers],
    explanation
  };
}

// Helper SVG diagram generators for realistic SAT geometry problems
export function svgRightTriangle(a, b, c, angleA = "A", angleB = "B", angleC = "C") {
  return `
  <div style="text-align: center; margin: 12px 0;">
    <svg width="220" height="150" viewBox="0 0 220 150" style="max-width: 100%; height: auto;">
      <polygon points="30,120 190,120 190,30" fill="#f8fafc" stroke="#1e293b" stroke-width="2.5" />
      <rect x="175" y="105" width="15" height="15" fill="none" stroke="#1e293b" stroke-width="1.5" />
      <text x="18" y="130" font-size="14" font-weight="600" fill="#0f172a">${angleA}</text>
      <text x="195" y="130" font-size="14" font-weight="600" fill="#0f172a">${angleC}</text>
      <text x="195" y="25" font-size="14" font-weight="600" fill="#0f172a">${angleB}</text>
      <text x="110" y="138" font-size="13" font-weight="500" fill="#334155">${a}</text>
      <text x="202" y="80" font-size="13" font-weight="500" fill="#334155">${b}</text>
      <text x="100" y="65" font-size="13" font-weight="500" fill="#334155">${c}</text>
    </svg>
    <div style="font-size: 12px; color: #64748b; margin-top: 4px;">Note: Figure not drawn to scale.</div>
  </div>`;
}

export function svgCircleWithAngle(centerLabel = "O", radiusVal = "r", angleVal = "60°", arcLabel = "AB") {
  return `
  <div style="text-align: center; margin: 12px 0;">
    <svg width="180" height="180" viewBox="0 0 180 180" style="max-width: 100%; height: auto;">
      <circle cx="90" cy="90" r="70" fill="#f8fafc" stroke="#1e293b" stroke-width="2" />
      <line x1="90" y1="90" x2="160" y2="90" stroke="#1e293b" stroke-width="2" />
      <line x1="90" y1="90" x2="125" y2="29" stroke="#1e293b" stroke-width="2" />
      <circle cx="90" cy="90" r="3" fill="#0f172a" />
      <text x="80" y="105" font-size="13" font-weight="600" fill="#0f172a">${centerLabel}</text>
      <text x="165" y="95" font-size="13" font-weight="600" fill="#0f172a">A</text>
      <text x="125" y="22" font-size="13" font-weight="600" fill="#0f172a">B</text>
      <text x="112" y="80" font-size="12" font-weight="500" fill="#2563eb">${angleVal}</text>
      <text x="120" y="105" font-size="12" font-weight="500" fill="#475569">${radiusVal}</text>
    </svg>
    <div style="font-size: 12px; color: #64748b; margin-top: 4px;">Note: Figure not drawn to scale.</div>
  </div>`;
}

export function svgCoordinateParabola(h = 2, k = -3) {
  return `
  <div style="text-align: center; margin: 12px 0;">
    <svg width="240" height="180" viewBox="0 0 240 180" style="max-width: 100%; height: auto;">
      <!-- Grid lines -->
      <line x1="20" y1="90" x2="220" y2="90" stroke="#94a3b8" stroke-width="1.5" />
      <line x1="120" y1="10" x2="120" y2="170" stroke="#94a3b8" stroke-width="1.5" />
      <!-- Arrows -->
      <polygon points="220,90 214,86 214,94" fill="#64748b" />
      <polygon points="120,10 116,16 124,16" fill="#64748b" />
      <text x="224" y="94" font-size="12" fill="#475569">x</text>
      <text x="122" y="12" font-size="12" fill="#475569">y</text>
      <!-- Parabola curve vertex at (140, 120) opening upward -->
      <path d="M 80,40 Q 140,150 200,40" fill="none" stroke="#2563eb" stroke-width="2.5" />
      <circle cx="140" cy="120" r="3.5" fill="#dc2626" />
      <text x="145" y="132" font-size="11" font-weight="600" fill="#dc2626">Vertex (${h}, ${k})</text>
    </svg>
  </div>`;
}
