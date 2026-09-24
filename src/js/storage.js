// storage.js - LocalStorage manager for Digital SAT tests, progress, and history

const STORAGE_KEYS = {
  CURRENT_SESSION: "sat2026_current_session",
  TEST_HISTORY: "sat2026_test_history",
  SETTINGS: "sat2026_settings"
};

export const Storage = {
  saveSession(sessionData) {
    try {
      localStorage.setItem(STORAGE_KEYS.CURRENT_SESSION, JSON.stringify(sessionData));
    } catch (e) {
      console.error("Failed to save session to localStorage", e);
    }
  },

  getSession() {
    try {
      const data = localStorage.getItem(STORAGE_KEYS.CURRENT_SESSION);
      return data ? JSON.parse(data) : null;
    } catch (e) {
      console.error("Failed to read session", e);
      return null;
    }
  },

  clearSession() {
    try {
      localStorage.removeItem(STORAGE_KEYS.CURRENT_SESSION);
    } catch (e) {
      console.error("Failed to clear session", e);
    }
  },

  saveCompletedTest(report) {
    try {
      const history = this.getHistory();
      // Remove previous entry for same test if any, then prepend
      const filtered = history.filter(h => h.testId !== report.testId);
      filtered.unshift({
        id: "att_" + Date.now(),
        testId: report.testId,
        testTitle: report.testTitle,
        date: new Date().toISOString(),
        totalScore: report.totalScore,
        rwScore: report.rw.score,
        mathScore: report.math.score,
        percentile: report.percentile,
        rwCorrect: report.rw.correct,
        mathCorrect: report.math.correct,
        reportData: report
      });
      localStorage.setItem(STORAGE_KEYS.TEST_HISTORY, JSON.stringify(filtered));
    } catch (e) {
      console.error("Failed to save test history", e);
    }
  },

  getHistory() {
    try {
      const data = localStorage.getItem(STORAGE_KEYS.TEST_HISTORY);
      return data ? JSON.parse(data) : [];
    } catch (e) {
      console.error("Failed to read history", e);
      return [];
    }
  },

  getTestRecord(testId) {
    const history = this.getHistory();
    return history.find(h => h.testId === testId) || null;
  },

  clearAllData() {
    try {
      localStorage.removeItem(STORAGE_KEYS.CURRENT_SESSION);
      localStorage.removeItem(STORAGE_KEYS.TEST_HISTORY);
    } catch (e) {
      console.error("Failed to clear data", e);
    }
  }
};
