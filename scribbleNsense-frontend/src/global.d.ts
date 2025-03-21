export {}; // ✅ prevents "Cannot redeclare block-scoped variable" errors

declare global {
  interface Window {
    MathJax: unknown;
  }
}
