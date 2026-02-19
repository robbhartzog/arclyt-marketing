<template>
  <section id="services">
    <div class="section-head">
      <div>
        <h2>Services</h2>
      </div>
      <p class="section-microline">From roadmap to reliability. Built to ship and keep systems running.</p>
    </div>

    <div class="grid">
      <div class="card">
        <div class="card-visual">
          <svg viewBox="0 0 120 80" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <title>Application Structure</title>
            <desc>Layered application modules with clean architecture</desc>
            <!-- Base layer modules -->
            <rect x="15" y="50" width="20" height="12" fill="currentColor" opacity="0.3" stroke="currentColor" stroke-width="1.5" />
            <rect x="45" y="50" width="20" height="12" fill="currentColor" opacity="0.3" stroke="currentColor" stroke-width="1.5" />
            <rect x="75" y="50" width="20" height="12" fill="currentColor" opacity="0.3" stroke="currentColor" stroke-width="1.5" />
            <!-- Middle layer -->
            <rect x="25" y="30" width="25" height="12" fill="currentColor" opacity="0.3" stroke="currentColor" stroke-width="1.5" />
            <rect x="60" y="30" width="25" height="12" fill="currentColor" opacity="0.3" stroke="currentColor" stroke-width="1.5" />
            <!-- Top layer - highlighted -->
            <rect x="35" y="10" width="30" height="12" fill="#7aa7ff" stroke="#7aa7ff" stroke-width="1.5" />
            <!-- Connection lines -->
            <line x1="50" y1="22" x2="37" y2="50" stroke="#ff9000" stroke-width="1.5" opacity="0.5" stroke-linecap="round" />
            <line x1="50" y1="22" x2="55" y2="50" stroke="currentColor" stroke-width="1.5" opacity="0.3" stroke-linecap="round" />
            <line x1="50" y1="22" x2="85" y2="50" stroke="#ff9000" stroke-width="1.5" opacity="0.5" stroke-linecap="round" />
            <!-- Architectural arc -->
            <path d="M 15 56 Q 60 40 105 56" stroke="#ff9000" stroke-width="2" fill="none" stroke-linecap="round" opacity="0.8" />
          </svg>
        </div>
        <h3>Custom Application Development</h3>
        <p>Customer-facing apps and internal tools teams can iterate on quickly—without creating long-term maintenance drag.</p>
        <div class="card-meta">product engineering · web apps · apis</div>
      </div>

      <div class="card">
        <div class="card-visual">
          <svg viewBox="0 0 120 80" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <title>Cloud Architecture Network</title>
            <desc>Minimal node network with architectural arc connecting services</desc>
            <!-- Nodes -->
            <circle cx="20" cy="20" r="4" fill="currentColor" opacity="0.4" />
            <circle cx="50" cy="15" r="4" fill="currentColor" opacity="0.4" />
            <circle cx="80" cy="25" r="4" fill="currentColor" opacity="0.4" />
            <circle cx="30" cy="50" r="4" fill="currentColor" opacity="0.4" />
            <circle cx="70" cy="55" r="4" fill="currentColor" opacity="0.4" />
            <circle cx="100" cy="45" r="4" fill="currentColor" opacity="0.4" />
            <!-- Highlighted nodes -->
            <circle cx="50" cy="15" r="5" fill="#7aa7ff" />
            <circle cx="70" cy="55" r="5" fill="#ff9000" />
            <!-- Connection lines -->
            <line x1="20" y1="20" x2="50" y2="15" stroke="#ff9000" stroke-width="1.5" opacity="0.5" stroke-linecap="round" />
            <line x1="50" y1="15" x2="80" y2="25" stroke="currentColor" stroke-width="1.5" opacity="0.3" stroke-linecap="round" />
            <line x1="20" y1="20" x2="30" y2="50" stroke="currentColor" stroke-width="1.5" opacity="0.3" stroke-linecap="round" />
            <line x1="80" y1="25" x2="70" y2="55" stroke="#ff9000" stroke-width="1.5" opacity="0.6" stroke-linecap="round" />
            <line x1="70" y1="55" x2="100" y2="45" stroke="currentColor" stroke-width="1.5" opacity="0.3" stroke-linecap="round" />
            <!-- Architectural arc -->
            <path d="M 20 20 Q 60 5 100 45" stroke="#ff9000" stroke-width="2" fill="none" stroke-linecap="round" opacity="0.9" />
          </svg>
        </div>
        <h3>System &amp; Cloud Architecture</h3>
        <p>Clear system design that prevents complexity from creeping in—so teams can move faster with fewer surprises.</p>
        <div class="card-meta">cloud-native · serverless · microservices</div>
      </div>

      <div class="card">
        <div class="card-visual">
          <svg viewBox="0 0 120 80" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <title>Legacy to Modern Transformation</title>
            <desc>Rigid legacy structure transitioning to modern architecture via arc bridge</desc>
            <!-- Legacy side (left) - rigid grid -->
            <rect x="5" y="15" width="8" height="8" fill="currentColor" opacity="0.3" />
            <rect x="15" y="15" width="8" height="8" fill="currentColor" opacity="0.3" />
            <rect x="25" y="15" width="8" height="8" fill="currentColor" opacity="0.3" />
            <rect x="5" y="25" width="8" height="8" fill="currentColor" opacity="0.3" />
            <rect x="15" y="25" width="8" height="8" fill="currentColor" opacity="0.3" />
            <rect x="25" y="25" width="8" height="8" fill="currentColor" opacity="0.3" />
            <rect x="5" y="35" width="8" height="8" fill="currentColor" opacity="0.3" />
            <rect x="15" y="35" width="8" height="8" fill="currentColor" opacity="0.3" />
            <rect x="25" y="35" width="8" height="8" fill="currentColor" opacity="0.3" />
            <!-- Modern side (right) - cleaner geometry -->
            <circle cx="85" cy="20" r="5" fill="currentColor" opacity="0.4" />
            <circle cx="105" cy="25" r="5" fill="currentColor" opacity="0.4" />
            <circle cx="90" cy="40" r="5" fill="currentColor" opacity="0.4" />
            <circle cx="110" cy="45" r="5" fill="currentColor" opacity="0.4" />
            <!-- Highlighted modern node -->
            <circle cx="90" cy="40" r="6" fill="#ff9000" />
            <!-- Arc bridge -->
            <path d="M 33 30 Q 60 20 85 40" stroke="#ff9000" stroke-width="2" fill="none" stroke-linecap="round" opacity="0.9" />
          </svg>
        </div>
        <h3>Modernization &amp; Migration</h3>
        <p>Modernize legacy systems without freezing delivery—reduce risk, improve stability, and keep shipping.</p>
        <div class="card-meta">refactoring · migration · stability</div>
      </div>

      <div class="card">
        <div class="card-visual">
          <svg viewBox="0 0 120 80" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <title>DevOps Pipeline with Checkpoints</title>
            <desc>Horizontal pipeline of modules connected with lines and arc segment</desc>
            <!-- Pipeline modules -->
            <rect x="10" y="35" width="12" height="12" fill="currentColor" opacity="0.3" stroke="currentColor" stroke-width="1.5" />
            <rect x="30" y="35" width="12" height="12" fill="currentColor" opacity="0.3" stroke="currentColor" stroke-width="1.5" />
            <rect x="50" y="35" width="12" height="12" fill="currentColor" opacity="0.3" stroke="currentColor" stroke-width="1.5" />
            <rect x="70" y="35" width="12" height="12" fill="currentColor" opacity="0.3" stroke="currentColor" stroke-width="1.5" />
            <rect x="90" y="35" width="12" height="12" fill="currentColor" opacity="0.3" stroke="currentColor" stroke-width="1.5" />
            <!-- Highlighted checkpoint -->
            <rect x="50" y="35" width="12" height="12" fill="#ff9000" stroke="#ff9000" stroke-width="1.5" />
            <!-- Connection lines -->
            <line x1="22" y1="41" x2="30" y2="41" stroke="currentColor" stroke-width="1.5" opacity="0.4" stroke-linecap="round" />
            <line x1="42" y1="41" x2="50" y2="41" stroke="#ff9000" stroke-width="1.5" opacity="0.6" stroke-linecap="round" />
            <line x1="62" y1="41" x2="70" y2="41" stroke="#ff9000" stroke-width="1.5" opacity="0.6" stroke-linecap="round" />
            <line x1="82" y1="41" x2="90" y2="41" stroke="currentColor" stroke-width="1.5" opacity="0.4" stroke-linecap="round" />
            <!-- Arc segment -->
            <path d="M 42 41 Q 46 25 62 41" stroke="#ff9000" stroke-width="2" fill="none" stroke-linecap="round" opacity="0.9" />
          </svg>
        </div>
        <h3>DevOps &amp; Infrastructure</h3>
        <p>Release automation and cloud infrastructure that make deployments routine, predictable, and safer.</p>
        <div class="card-meta">iac · ci/cd · release hygiene</div>
      </div>

      <div class="card">
        <div class="card-visual">
          <svg viewBox="0 0 120 80" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <title>Observability Metrics</title>
            <desc>Signal lines and metrics visualization with monitoring points</desc>
            <!-- Base line -->
            <line x1="15" y1="60" x2="105" y2="60" stroke="currentColor" stroke-width="1.5" opacity="0.2" stroke-linecap="round" />
            <!-- Signal lines -->
            <path d="M 15 50 L 25 45 L 35 55 L 45 40 L 55 50 L 65 35 L 75 45 L 85 50 L 95 40 L 105 45" 
                  stroke="currentColor" stroke-width="1.5" opacity="0.4" fill="none" stroke-linecap="round" />
            <!-- Monitoring points -->
            <circle cx="25" cy="45" r="3" fill="currentColor" opacity="0.4" />
            <circle cx="45" cy="40" r="3" fill="#ff9000" opacity="0.7" />
            <circle cx="65" cy="35" r="4" fill="#7aa7ff" />
            <circle cx="85" cy="50" r="3" fill="currentColor" opacity="0.4" />
            <circle cx="105" cy="45" r="3" fill="#ff9000" opacity="0.7" />
            <!-- Vertical metric lines -->
            <line x1="25" y1="20" x2="25" y2="45" stroke="currentColor" stroke-width="1.5" opacity="0.2" stroke-linecap="round" />
            <line x1="45" y1="15" x2="45" y2="40" stroke="#ff9000" stroke-width="1.5" opacity="0.5" stroke-linecap="round" />
            <line x1="65" y1="10" x2="65" y2="35" stroke="#7aa7ff" stroke-width="1.5" opacity="0.5" stroke-linecap="round" />
            <!-- Arc connecting metrics -->
            <path d="M 25 45 Q 45 30 65 35" stroke="#ff9000" stroke-width="2" fill="none" stroke-linecap="round" opacity="0.9" />
          </svg>
        </div>
        <h3>Observability &amp; Reliability</h3>
        <p>Make systems measurable and calm—so issues are caught early and incidents are easier to resolve.</p>
        <div class="card-meta">monitoring · sre · alerting</div>
      </div>

      <div class="card">
        <div class="card-visual">
          <svg viewBox="0 0 120 80" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <title>Security Layers</title>
            <desc>Concentric security layers with protected core</desc>
            <!-- Outer security layer -->
            <circle cx="60" cy="40" r="28" fill="none" stroke="currentColor" stroke-width="1.5" opacity="0.2" />
            <!-- Middle security layer -->
            <circle cx="60" cy="40" r="20" fill="none" stroke="currentColor" stroke-width="1.5" opacity="0.3" />
            <!-- Inner security layer -->
            <circle cx="60" cy="40" r="12" fill="none" stroke="#ff9000" stroke-width="2" opacity="0.7" />
            <!-- Protected core -->
            <circle cx="60" cy="40" r="6" fill="#7aa7ff" />
            <!-- Security nodes -->
            <circle cx="35" cy="25" r="3" fill="#ff9000" opacity="0.7" />
            <circle cx="85" cy="25" r="3" fill="currentColor" opacity="0.4" />
            <circle cx="35" cy="55" r="3" fill="currentColor" opacity="0.4" />
            <circle cx="85" cy="55" r="3" fill="#ff9000" opacity="0.7" />
            <!-- Connection lines to core -->
            <line x1="35" y1="25" x2="54" y2="34" stroke="#ff9000" stroke-width="1.5" opacity="0.4" stroke-linecap="round" />
            <line x1="85" y1="25" x2="66" y2="34" stroke="currentColor" stroke-width="1.5" opacity="0.2" stroke-linecap="round" />
            <line x1="35" y1="55" x2="54" y2="46" stroke="currentColor" stroke-width="1.5" opacity="0.2" stroke-linecap="round" />
            <line x1="85" y1="55" x2="66" y2="46" stroke="#ff9000" stroke-width="1.5" opacity="0.4" stroke-linecap="round" />
            <!-- Architectural arc -->
            <path d="M 35 25 Q 60 15 85 25" stroke="#ff9000" stroke-width="2" fill="none" stroke-linecap="round" opacity="0.9" />
          </svg>
        </div>
        <h3>Security-Minded Delivery</h3>
        <p>Security built in from the start—identity, credentials, and access controls handled correctly.</p>
        <div class="card-meta">iam · secrets · secure by design</div>
      </div>
    </div>
  </section>
</template>

<script setup>
</script>
