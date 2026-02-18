// Theme functions
const html = document.documentElement;

function getSystemTheme() {
  return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
}

function applyTheme(theme) {
  const themeToggle = document.getElementById("themeToggle");
  const moon = document.getElementById("moon");
  const sun = document.getElementById("sun");

  html.setAttribute("data-bs-theme", theme);

  if (theme === "dark") {
    sun.classList.remove("d-none");
    moon.classList.add("d-none");
    themeToggle.classList.replace("btn-outline-dark", "btn-outline-light");
  } else {
    moon.classList.remove("d-none");
    sun.classList.add("d-none");
    themeToggle.classList.replace("btn-outline-light", "btn-outline-dark");
  }
}

function initThemeToggle() {
  const themeToggle = document.getElementById("themeToggle");

  themeToggle.addEventListener("click", () => {
    const current = html.getAttribute("data-bs-theme");
    const next = current === "dark" ? "light" : "dark";
    applyTheme(next);
  });
}

// Copy button function
function initCopyButton(copyBtn, output) {
  const tooltip = new bootstrap.Tooltip(copyBtn, {trigger: "manual"});
  const originalHTML = copyBtn.innerHTML;

  copyBtn.addEventListener("click", () => {
    navigator.clipboard.writeText(output.value);

    // Show tooltip
    tooltip.show();

    // Visual feedback
    copyBtn.innerText = "Copied!";
    copyBtn.classList.replace("btn-success", "btn-secondary");
    copyBtn.disabled = true;

    // Restore after delay
    setTimeout(() => {
      tooltip.hide();
      copyBtn.innerHTML = originalHTML;
      copyBtn.classList.replace("btn-secondary", "btn-success");
      copyBtn.disabled = false;
    }, 700);
  });
}

// Password generator function
const lowercase = "abcdefghijklmnopqrstuvwxyz";
const uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const numbers = "0123456789";
const symbols = "?!@#$%^&*+";
const spec_symbols = "/()[],.:;=-_";

function getChar(str) {
  return str[Math.floor(Math.random() * str.length)];
}

function generatePassword() {
  let possibles = "";

  if (document.getElementById("Lowercase").checked) possibles += lowercase;
  if (document.getElementById("Uppercase").checked) possibles += uppercase;
  if (document.getElementById("Numbers").checked) possibles += numbers;
  if (document.getElementById("Symbols").checked) possibles += symbols;
  if (document.getElementById("spec_symbols").checked) possibles += spec_symbols;

  const length = Number(document.getElementById("length").value);
  let result = "";

  for (let i = 0; i < length; i++) {
    result += getChar(possibles);
  }

  return result;
}

// Length buttons function
function initLengthButtons() {
  const length = document.getElementById("length");

  document.getElementById("plus").addEventListener("click", () => {
    if (length.value < 64) length.value++;
  });

  document.getElementById("minus").addEventListener("click", () => {
    if (length.value > 1) length.value--;
  });
}

// Load SVG helper
async function loadSVG(id, file) {
  const container = document.getElementById(id);
  const svg = await fetch(file).then((res) => res.text());
  container.innerHTML = svg;
}

// Initialize app
async function initApp() {
  const output = document.getElementById("output");
  const copyBtn = document.getElementById("copy");
  const generateBtn = document.getElementById("generate");

  // Load icons
  await loadSVG("moon", "/assets/icons/moon.svg");
  await loadSVG("sun", "/assets/icons/sun.svg");
  await loadSVG("copyIcon", "/assets/icons/copy.svg");

  // Theme
  applyTheme(getSystemTheme());
  initThemeToggle();

  // Copy button
  initCopyButton(copyBtn, output);

  // Length buttons
  initLengthButtons();

  // Generator button
  generateBtn.addEventListener("click", () => {
    output.value = generatePassword();
  });

  // Generate once on load
  output.value = generatePassword();
}

// Start the app
initApp();
