import { Card } from "../components/Card.js";

export function Tournaments() {
  return Card({
    className: "glass-panel page-placeholder",
    content: `
      <p class="eyebrow">Tournaments</p>
      <h2>Upcoming tournaments page</h2>
      <p class="placeholder-text">This page is ready for tournament listings, filters, and match details.</p>
    `
  });
}
