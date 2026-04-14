export function Button({ id = "", label = "Button", variant = "primary", type = "button" } = {}) {
  const buttonId = id ? `id="${id}"` : "";

  if (variant === "secondary") {
    return `
      <button class="action-button" ${buttonId} type="${type}">
        ${label}
      </button>
    `;
  }

  return `
    <button class="group relative" ${buttonId} type="${type}">
      <div class="absolute -inset-1 bg-primary blur opacity-25 transition duration-500 group-hover:opacity-60"></div>
      <div class="clipped-corner relative bg-primary px-12 py-5 font-headline text-xl font-black italic tracking-tighter text-on-primary uppercase transition-transform duration-200 hover:scale-105 active:scale-95">
        ${label}
      </div>
    </button>
  `;
}
