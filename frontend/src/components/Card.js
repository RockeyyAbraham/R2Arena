export function Card({ className = "", content = "" } = {}) {
  return `<section class="${className}">${content}</section>`;
}
