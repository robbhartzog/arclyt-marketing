<template>
  <section id="capabilities">
    <div class="section-head">
      <div>
        <h2>Engineering</h2>
      </div>
      <p class="section-microline">Architecture-first. Operational by design.</p>
    </div>

    <div class="capabilities-grid">
      <div class="capability-block">
        <div class="capability-icon">
          <svg viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <title>System Architecture</title>
            <desc>Modular system components with architectural connections</desc>
            <!-- Modular components -->
            <rect x="10" y="15" width="16" height="16" fill="#7aa7ff" opacity="0.4" stroke="#7aa7ff" stroke-width="1.5" />
            <rect x="34" y="15" width="16" height="16" fill="#7ef0c1" opacity="0.4" stroke="#7ef0c1" stroke-width="1.5" />
            <rect x="10" y="35" width="16" height="16" fill="currentColor" opacity="0.3" stroke="currentColor" stroke-width="1.5" />
            <rect x="34" y="35" width="16" height="16" fill="#ff9000" opacity="0.5" stroke="#ff9000" stroke-width="1.5" />
            <!-- Connection lines -->
            <line x1="26" y1="23" x2="34" y2="23" stroke="#7aa7ff" stroke-width="2" opacity="0.6" stroke-linecap="round" />
            <line x1="18" y1="35" x2="18" y2="31" stroke="currentColor" stroke-width="2" opacity="0.4" stroke-linecap="round" />
            <line x1="42" y1="31" x2="42" y2="35" stroke="#ff9000" stroke-width="2" opacity="0.6" stroke-linecap="round" />
            <!-- Architectural arc -->
            <path d="M 18 23 Q 30 10 42 23" stroke="#7aa7ff" stroke-width="2.5" fill="none" stroke-linecap="round" opacity="0.8" />
          </svg>
        </div>
        <h3>System Architecture</h3>
        <ul class="capability-list">
          <li>Domain modeling and boundary definition</li>
          <li>Service decomposition and modular design</li>
          <li>API and integration architecture</li>
          <li>Event-driven and asynchronous systems</li>
          <li>Scalable data strategies</li>
        </ul>
      </div>

      <div class="capability-block">
        <div class="capability-icon">
          <svg viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <title>Reliability & Operations</title>
            <desc>Monitoring and operational flow with reliability metrics</desc>
            <!-- Signal line -->
            <path d="M 10 30 C 20 20 40 40 50 30" stroke="currentColor" stroke-width="1.5" fill="none" opacity="0.4" stroke-linecap="round" />
            <!-- Monitoring points -->
            <circle cx="20" cy="25" r="4" fill="#7aa7ff" />
            <circle cx="30" cy="30" r="4" fill="#7ef0c1" opacity="0.7" />
            <circle cx="40" cy="25" r="4" fill="#ff9000" opacity="0.7" />
            <!-- Vertical metric indicators -->
            <line x1="20" y1="25" x2="20" y2="45" stroke="#7aa7ff" stroke-width="1.5" opacity="0.3" stroke-linecap="round" />
            <line x1="30" y1="30" x2="30" y2="50" stroke="#7ef0c1" stroke-width="1.5" opacity="0.3" stroke-linecap="round" />
            <line x1="40" y1="25" x2="40" y2="45" stroke="#ff9000" stroke-width="1.5" opacity="0.3" stroke-linecap="round" />
            <!-- Operational arc -->
            <path d="M 20 45 Q 30 50 40 45" stroke="#7aa7ff" stroke-width="2.5" fill="none" stroke-linecap="round" opacity="0.8" />
          </svg>
        </div>
        <h3>Reliability &amp; Operations</h3>
        <ul class="capability-list">
          <li>Observability architecture</li>
          <li>SLO-driven reliability design</li>
          <li>Incident response structuring</li>
          <li>Capacity and performance planning</li>
          <li>Operational risk reduction</li>
        </ul>
      </div>

      <div class="capability-block">
        <div class="capability-icon">
          <svg viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <title>Cloud & Infrastructure Architecture</title>
            <desc>Cloud infrastructure nodes with deployment layers</desc>
            <!-- Infrastructure layers -->
            <rect x="8" y="40" width="44" height="8" fill="currentColor" opacity="0.3" stroke="currentColor" stroke-width="1.5" />
            <rect x="12" y="28" width="36" height="8" fill="#7aa7ff" opacity="0.4" stroke="#7aa7ff" stroke-width="1.5" />
            <!-- Cloud nodes -->
            <circle cx="20" cy="18" r="5" fill="#7aa7ff" />
            <circle cx="40" cy="18" r="5" fill="#ff9000" opacity="0.8" />
            <circle cx="30" cy="10" r="4" fill="#7ef0c1" />
            <!-- Connection lines -->
            <line x1="20" y1="23" x2="20" y2="28" stroke="#7aa7ff" stroke-width="2" opacity="0.5" stroke-linecap="round" />
            <line x1="40" y1="23" x2="40" y2="28" stroke="#ff9000" stroke-width="2" opacity="0.6" stroke-linecap="round" />
            <line x1="30" y1="14" x2="30" y2="28" stroke="#7ef0c1" stroke-width="2" opacity="0.5" stroke-linecap="round" />
            <!-- Architectural arc -->
            <path d="M 8 44 Q 30 25 52 44" stroke="#ff9000" stroke-width="2.5" fill="none" stroke-linecap="round" opacity="0.9" />
          </svg>
        </div>
        <h3>Cloud &amp; Infrastructure Architecture</h3>
        <ul class="capability-list">
          <li>Multi-environment system design</li>
          <li>Network and access boundary modeling</li>
          <li>Resilient deployment topology</li>
          <li>Infrastructure as code</li>
          <li>Deployment pipeline design</li>
          <li>Infrastructure modernization</li>
        </ul>
      </div>

      <div class="capability-block">
        <div class="capability-icon">
          <svg viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <title>Secure-by-Design Systems</title>
            <desc>Security layers protecting core system</desc>
            <!-- Outer security layer -->
            <circle cx="30" cy="30" r="22" fill="none" stroke="currentColor" stroke-width="1.5" opacity="0.2" />
            <!-- Middle security layer -->
            <circle cx="30" cy="30" r="16" fill="none" stroke="#7aa7ff" stroke-width="1.5" opacity="0.4" />
            <!-- Inner protected core -->
            <circle cx="30" cy="30" r="10" fill="#7aa7ff" opacity="0.6" />
            <circle cx="30" cy="30" r="6" fill="#ff9000" />
            <!-- Security nodes -->
            <rect x="12" y="28" width="6" height="6" fill="#7ef0c1" opacity="0.6" />
            <rect x="42" y="28" width="6" height="6" fill="#7ef0c1" opacity="0.6" />
            <!-- Connection lines -->
            <line x1="18" y1="31" x2="20" y2="30" stroke="#7ef0c1" stroke-width="1.5" opacity="0.4" stroke-linecap="round" />
            <line x1="42" y1="31" x2="40" y2="30" stroke="#7ef0c1" stroke-width="1.5" opacity="0.4" stroke-linecap="round" />
            <!-- Security arc -->
            <path d="M 12 28 Q 30 15 48 28" stroke="#ff9000" stroke-width="2.5" fill="none" stroke-linecap="round" opacity="0.9" />
          </svg>
        </div>
        <h3>Secure-by-Design Systems</h3>
        <ul class="capability-list">
          <li>Identity and access modeling</li>
          <li>Secrets and configuration strategy</li>
          <li>Architectural threat surface reduction</li>
          <li>Secure implementation review</li>
        </ul>
      </div>
    </div>
  </section>
</template>

<script setup>
</script>
