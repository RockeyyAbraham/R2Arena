import { Home, initHomePage } from "./pages/Home.js";

export function renderApp(rootElement) {
  rootElement.innerHTML = Home();

  if (window.tailwind?.refresh) {
    window.tailwind.refresh();
  }

  initHomePage();
}
