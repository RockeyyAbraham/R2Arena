export function select(selector, parent = document) {
  return parent.querySelector(selector);
}

export function selectAll(selector, parent = document) {
  return Array.from(parent.querySelectorAll(selector));
}

export function setActiveItem(items, activeItem, className = "active") {
  items.forEach((item) => item.classList.remove(className));
  activeItem.classList.add(className);
}
