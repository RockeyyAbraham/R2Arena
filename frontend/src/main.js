import "./styles/global.css";
import { renderApp } from "./App.js";

const appRoot = document.querySelector("#app");

if (appRoot) {
  renderApp(appRoot);
}
