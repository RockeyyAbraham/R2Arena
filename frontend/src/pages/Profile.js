import { Card } from "../components/Card.js";

export function Profile() {
  return Card({
    className: "glass-panel page-placeholder",
    content: `
      <p class="eyebrow">Profile</p>
      <h2>Player profile page</h2>
      <p class="placeholder-text">This page is ready for player stats, achievements, and account settings.</p>
    `
  });
}
