/* app.js — GRC Grader frontend */

const editor      = document.getElementById("editor");
const saveBtn     = document.getElementById("saveBtn");
const gradeBtn    = document.getElementById("gradeBtn");
const gradeBtnTxt = document.getElementById("gradeBtnText");
const gradeBtnSpn = document.getElementById("gradeBtnSpinner");
const saveStatus  = document.getElementById("saveStatus");
const resultsPanel= document.getElementById("resultsPanel");
const errorPanel  = document.getElementById("errorPanel");
const scoreBadge  = document.getElementById("scoreBadge");
const checklist   = document.getElementById("checklist");
const feedbackText= document.getElementById("feedbackText");

// ─── Helpers ──────────────────────────────────────────────────────────────────

function post(url, body) {
  return fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRF-Token": CSRF_TOKEN,
    },
    body: JSON.stringify(body),
  });
}

function showError(msg) {
  errorPanel.textContent = msg;
  errorPanel.classList.remove("hidden");
  resultsPanel.classList.add("hidden");
}

function clearError() {
  errorPanel.classList.add("hidden");
  errorPanel.textContent = "";
}

function setGrading(loading) {
  gradeBtn.disabled       = loading;
  saveBtn.disabled        = loading;
  gradeBtnTxt.textContent = loading ? "Grading…" : "Grade";
  gradeBtnSpn.classList.toggle("hidden", !loading);
}

// ─── Save ─────────────────────────────────────────────────────────────────────

let saveTimer = null;

async function doSave() {
  clearError();
  saveStatus.textContent = "Saving…";

  try {
    const res = await post("/save", {
      artifact_id: ARTIFACT_ID,
      content: editor.value,
    });

    if (!res.ok) {
      const data = await res.json().catch(() => ({}));
      saveStatus.textContent = "Save failed";
      showError(data.error || "Save failed. Please try again.");
      return;
    }

    saveStatus.textContent = "Saved ✓";
    setTimeout(() => { saveStatus.textContent = ""; }, 2500);
  } catch (e) {
    saveStatus.textContent = "Save failed";
    showError("Network error — could not save.");
  }
}

// Auto-save 1.5s after the user stops typing
editor.addEventListener("input", () => {
  saveStatus.textContent = "Unsaved changes";
  clearTimeout(saveTimer);
  saveTimer = setTimeout(doSave, 1500);
});

saveBtn.addEventListener("click", doSave);

// ─── Grade ────────────────────────────────────────────────────────────────────

gradeBtn.addEventListener("click", async () => {
  clearError();
  resultsPanel.classList.add("hidden");
  setGrading(true);

  try {
    const res = await post("/grade", {
      artifact_id: ARTIFACT_ID,
      content: editor.value,
    });

    const data = await res.json().catch(() => ({}));

    if (res.status === 429) {
      const secs = data.retry_after || 60;
      showError(`Grading limit reached — try again in ${secs} seconds.`);
      startRetryCountdown(secs);
      return;
    }

    if (!res.ok) {
      showError(data.error || "Grading failed. Please try again.");
      return;
    }

    renderResults(data);

  } catch (e) {
    showError("Network error — could not reach the grader.");
  } finally {
    setGrading(false);
  }
});

// ─── Render Results ───────────────────────────────────────────────────────────

function makeCheckItem(item) {
  const icon = item.status === "pass"    ? "✓"
             : item.status === "partial" ? "◑"
             :                             "✗";

  const wrapper = document.createElement("div");
  wrapper.className = `check-item status-${item.status}`;

  const iconEl = document.createElement("span");
  iconEl.className = "check-icon";
  iconEl.textContent = icon;

  const body = document.createElement("div");

  const label = document.createElement("div");
  label.className = "check-label";
  label.textContent = item.item;
  body.appendChild(label);

  if (item.note) {
    const note = document.createElement("div");
    note.className = "check-note";
    note.textContent = item.note;
    body.appendChild(note);
  }

  wrapper.appendChild(iconEl);
  wrapper.appendChild(body);
  return wrapper;
}

function renderResults(data) {
  // Score badge
  scoreBadge.textContent = `${data.score} / ${data.max_score}`;

  // Checklist — built with DOM methods, no innerHTML
  checklist.textContent = "";
  for (const item of data.checklist) {
    checklist.appendChild(makeCheckItem(item));
  }

  // Feedback (plain text)
  feedbackText.textContent = data.feedback;

  resultsPanel.classList.remove("hidden");
  resultsPanel.scrollIntoView({ behavior: "smooth", block: "start" });
}

// ─── Rate limit countdown ─────────────────────────────────────────────────────

function startRetryCountdown(seconds) {
  gradeBtn.disabled = true;
  let remaining = seconds;

  const interval = setInterval(() => {
    remaining--;
    gradeBtnTxt.textContent = `Wait ${remaining}s`;
    if (remaining <= 0) {
      clearInterval(interval);
      gradeBtn.disabled = false;
      gradeBtnTxt.textContent = "Grade";
    }
  }, 1000);
}
