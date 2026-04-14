import { Button } from "../components/Button.js";
import { Navbar } from "../components/Navbar.js";
import { select, selectAll, setActiveItem } from "../utils/helpers.js";

export function Home() {
  return `
    <div class="app-shell">
      <div class="arena-splash" id="arena-splash">
        ${Navbar()}
        <main class="relative flex h-screen w-full items-center justify-center overflow-hidden bg-surface text-on-surface font-body selection:bg-primary selection:text-on-primary">
          <div class="absolute inset-0 z-0">
            <img alt="Cinematic Background" class="h-full w-full object-cover opacity-30 mix-blend-screen" src="https://lh3.googleusercontent.com/aida-public/AB6AXuAhjUoKDO7WC1rAWYXFeSUvyYvAyezi88X-4YnUi4CYC7FKadIx7ntwRYPLIijIo8tRcGQ-9ZjsrktZnC03a4ZRQxcAfd-U3uvAWZPPnQT1p9SY3FnM5_5ljp8aOIw9dTNxWtcr6jVykWOZQJD9T-7qWGLSbbDrl-kpKuDKTSfLD0G2OEKplX98ie7A4ysAV0ex9_jRGI0ctzeEf6GqNSOIGl7NlgeKQSjkfaryNIIbFp1L7FsozXZlZDguub4cwn5NED-2MYGvbLyk">
            <div class="absolute inset-0 bg-gradient-to-t from-surface via-transparent to-surface/40"></div>
            <div class="scanline absolute inset-0 pointer-events-none"></div>
          </div>

          <div class="relative z-10 flex flex-col items-center px-4 text-center">
            <div class="mb-2 flex items-center gap-4">
              <div class="h-[2px] w-24 bg-gradient-to-r from-transparent to-primary"></div>
              <span class="font-label text-xs uppercase tracking-[0.5em] text-primary/80">ESTABLISHED 2026</span>
              <div class="h-[2px] w-24 bg-gradient-to-l from-transparent to-primary"></div>
            </div>
            <h1 class="glitch-gradient mb-4 bg-clip-text font-headline text-7xl font-black italic tracking-tighter text-transparent drop-shadow-[0_0_35px_rgba(57,255,20,0.3)] md:text-9xl">
              R2 GAMING
            </h1>
            <p class="mb-12 font-headline text-xl font-bold italic uppercase tracking-[0.3em] text-on-surface/90 md:text-2xl">
              ADDICTION TO ACCOMPLISHMENT
            </p>
            <div class="flex flex-col items-center gap-6 md:flex-row">
              ${Button({ id: "enter-arena-button", label: "ENTER THE ARENA" })}
            </div>
          </div>

          <div class="pointer-events-none absolute inset-0 opacity-20">
            <div class="absolute left-1/4 top-0 h-full w-[1px] bg-primary/30"></div>
            <div class="absolute right-1/4 top-0 h-full w-[1px] bg-primary/30"></div>
            <div class="absolute left-0 top-1/3 h-[1px] w-full bg-primary/30"></div>
            <div class="absolute bottom-1/3 left-0 h-[1px] w-full bg-primary/30"></div>
          </div>
        </main>
      </div>

      <div class="dashboard-shell">
        <aside class="sidebar glass-panel">
          <div class="brand">
            <div class="brand-mark logo-mark" aria-hidden="true">
              <span>R2</span>
            </div>
            <div>
              <h1>R2Gaming</h1>
              <p>Esports Command Center</p>
            </div>
          </div>

          <nav class="sidebar-nav">
            <button class="nav-item active" data-section="dashboard">Dashboard</button>
            <button class="nav-item" data-section="tournaments">Tournaments</button>
            <button class="nav-item" data-section="players">Players</button>
            <button class="nav-item" data-section="analytics">Analytics</button>
          </nav>

          <div class="sidebar-card glass-inner">
            <p class="sidebar-label">Live Pulse</p>
            <h2>24 Matches Running</h2>
            <p class="sidebar-text">Real-time activity is up 18% compared to yesterday.</p>
          </div>
        </aside>

        <main class="main-content">
          <header class="topbar glass-panel">
            <div>
              <p class="eyebrow">Welcome Back</p>
              <h2>R2Gaming Dashboard</h2>
            </div>
            <div class="status-pill">Neon Arena Online</div>
          </header>

          <section class="stats-grid" id="dashboard">
            <article class="stat-card glass-panel">
              <p class="stat-label">Active Players</p>
              <h3>18,420</h3>
              <span class="stat-trend positive">+12.4%</span>
            </article>
            <article class="stat-card glass-panel">
              <p class="stat-label">Live Matches</p>
              <h3>248</h3>
              <span class="stat-trend positive">+8.1%</span>
            </article>
            <article class="stat-card glass-panel">
              <p class="stat-label">Revenue</p>
              <h3>$92.4K</h3>
              <span class="stat-trend warning">+5.7%</span>
            </article>
          </section>

          <section class="content-grid">
            <section class="table-panel glass-panel" id="tournaments">
              <div class="panel-heading">
                <div>
                  <p class="eyebrow">Tournaments</p>
                  <h3>Upcoming Events</h3>
                </div>
                ${Button({ label: "View All", variant: "secondary" })}
              </div>

              <div class="table-wrap">
                <table>
                  <thead>
                    <tr>
                      <th>Tournament</th>
                      <th>Game</th>
                      <th>Prize Pool</th>
                      <th>Status</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>R2 Masters Cup</td>
                      <td>Valorant</td>
                      <td>$18,000</td>
                      <td><span class="badge live">Live</span></td>
                    </tr>
                    <tr>
                      <td>Neon Clash Series</td>
                      <td>BGMI</td>
                      <td>$11,500</td>
                      <td><span class="badge soon">Starts Soon</span></td>
                    </tr>
                    <tr>
                      <td>Elite Arena Finals</td>
                      <td>CS2</td>
                      <td>$25,000</td>
                      <td><span class="badge closed">Closed</span></td>
                    </tr>
                    <tr>
                      <td>Legends Grid Open</td>
                      <td>FIFA</td>
                      <td>$7,800</td>
                      <td><span class="badge soon">Starts Soon</span></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </section>

            <section class="chart-panel glass-panel" id="analytics">
              <div class="panel-heading">
                <div>
                  <p class="eyebrow">Analytics</p>
                  <h3>Weekly Engagement</h3>
                </div>
              </div>

              <div class="chart-placeholder">
                <div class="chart-bars">
                  <div class="bar" style="--height: 52%"></div>
                  <div class="bar" style="--height: 68%"></div>
                  <div class="bar" style="--height: 60%"></div>
                  <div class="bar" style="--height: 82%"></div>
                  <div class="bar" style="--height: 74%"></div>
                  <div class="bar" style="--height: 92%"></div>
                  <div class="bar" style="--height: 79%"></div>
                </div>
                <div class="chart-labels">
                  <span>Mon</span>
                  <span>Tue</span>
                  <span>Wed</span>
                  <span>Thu</span>
                  <span>Fri</span>
                  <span>Sat</span>
                  <span>Sun</span>
                </div>
              </div>
            </section>
          </section>

          <section class="bottom-grid">
            <section class="players-panel glass-panel" id="players">
              <div class="panel-heading">
                <div>
                  <p class="eyebrow">Players</p>
                  <h3>Top Ranked Squad</h3>
                </div>
              </div>

              <div class="player-list">
                <div class="player-row glass-inner">
                  <span class="avatar">A</span>
                  <div>
                    <h4>Astra</h4>
                    <p>Rank #1 Captain</p>
                  </div>
                </div>
                <div class="player-row glass-inner">
                  <span class="avatar">V</span>
                  <div>
                    <h4>Volt</h4>
                    <p>Rank #2 Strategist</p>
                  </div>
                </div>
                <div class="player-row glass-inner">
                  <span class="avatar">N</span>
                  <div>
                    <h4>Nova</h4>
                    <p>Rank #3 Entry Fragger</p>
                  </div>
                </div>
              </div>
            </section>

            <section class="revenue-panel glass-panel">
              <p class="eyebrow">Snapshot</p>
              <h3>Season Revenue Goal</h3>
              <div class="progress-track">
                <div class="progress-fill"></div>
              </div>
              <p class="progress-text">$92.4K of $120K reached</p>
            </section>
          </section>
        </main>
      </div>
    </div>
  `;
}

function setupArenaSplash() {
  const arenaSplash = select("#arena-splash");
  const enterArenaButton = select("#enter-arena-button");

  if (!arenaSplash) {
    return;
  }

  let splashDismissed = false;

  const hideSplash = () => {
    if (splashDismissed) {
      return;
    }

    splashDismissed = true;
    arenaSplash.classList.add("hidden");
    document.body.classList.remove("splash-active");
  };

  document.body.classList.add("splash-active");

  if (enterArenaButton) {
    enterArenaButton.addEventListener("click", hideSplash);
  }
}

function setupSidebarNavigation() {
  const navItems = selectAll(".nav-item");

  navItems.forEach((item) => {
    item.addEventListener("click", () => {
      setActiveItem(navItems, item, "active");
    });
  });
}

function animateChartBars() {
  const chartBars = selectAll(".bar");

  chartBars.forEach((bar, index) => {
    const finalHeight = bar.style.getPropertyValue("--height");
    bar.style.setProperty("--height", "0%");

    window.setTimeout(() => {
      bar.style.setProperty("--height", finalHeight);
    }, 150 + index * 120);
  });
}

function setupPanelHoverGlow() {
  const panels = selectAll(".glass-panel");

  panels.forEach((panel) => {
    panel.addEventListener("mousemove", (event) => {
      const bounds = panel.getBoundingClientRect();
      const x = event.clientX - bounds.left;
      const y = event.clientY - bounds.top;

      panel.style.background = `
        radial-gradient(circle at ${x}px ${y}px, rgba(255, 179, 71, 0.08), transparent 34%),
        rgba(18, 18, 18, 0.68)
      `;
    });

    panel.addEventListener("mouseleave", () => {
      panel.style.background = "";
    });
  });
}

export function initHomePage() {
  setupArenaSplash();
  setupSidebarNavigation();
  animateChartBars();
  setupPanelHoverGlow();
}
