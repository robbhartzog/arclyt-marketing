<template>
  <section id="capabilities">
    <div class="section-head">
      <div>
        <h2>Engineering</h2>
      </div>
      <p class="section-microline">Built for teams that ship.</p>
    </div>

    <p class="section-intro">We embed with teams to improve reliability and delivery speed—without sacrificing long-term maintainability.</p>

    <div class="bento-grid">

      <!-- WIDE: Cloud Infrastructure & Modernization (spans 2 cols) -->
      <div class="bento-block bento-block--wide bento-block--dark">
        <span class="bento-eyebrow">Featured Capability</span>
        <div class="bento-wide-inner">
          <div class="bento-wide-left">
            <div class="capability-icon">
              <svg viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                <title>Cloud Infrastructure & Modernization</title>
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
            <h3>Cloud Infrastructure &amp; Modernization</h3>
            <p class="bento-desc">We bridge the gap between legacy systems and modern cloud-native environments—migrating on-prem, ColdFusion, and monolith architectures to resilient, serverless AWS infrastructure without disrupting live operations.</p>
          </div>
          <div class="bento-wide-right">
            <ul class="capability-list">
              <li>Legacy-to-cloud migration patterns (strangler fig, lift &amp; shift)</li>
              <li>Multi-environment setup (dev / stage / prod)</li>
              <li>Infrastructure as code and automated pipelines</li>
              <li>Incremental modernization without freezing delivery</li>
              <li>Resilient deployment topology and failover design</li>
              <li>Network and access boundary design</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- System Architecture -->
      <div class="bento-block">
        <div class="capability-icon">
          <svg viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <title>System Architecture</title>
            <desc>Modular system components with architectural connections</desc>
            <rect x="10" y="15" width="16" height="16" fill="#7aa7ff" opacity="0.4" stroke="#7aa7ff" stroke-width="1.5" />
            <rect x="34" y="15" width="16" height="16" fill="#7ef0c1" opacity="0.4" stroke="#7ef0c1" stroke-width="1.5" />
            <rect x="10" y="35" width="16" height="16" fill="currentColor" opacity="0.3" stroke="currentColor" stroke-width="1.5" />
            <rect x="34" y="35" width="16" height="16" fill="#ff9000" opacity="0.5" stroke="#ff9000" stroke-width="1.5" />
            <line x1="26" y1="23" x2="34" y2="23" stroke="#7aa7ff" stroke-width="2" opacity="0.6" stroke-linecap="round" />
            <line x1="18" y1="35" x2="18" y2="31" stroke="currentColor" stroke-width="2" opacity="0.4" stroke-linecap="round" />
            <line x1="42" y1="31" x2="42" y2="35" stroke="#ff9000" stroke-width="2" opacity="0.6" stroke-linecap="round" />
            <path d="M 18 23 Q 30 10 42 23" stroke="#7aa7ff" stroke-width="2.5" fill="none" stroke-linecap="round" opacity="0.8" />
          </svg>
        </div>
        <h3>System Architecture</h3>
        <ul class="capability-list">
          <li>Clear domain model and ownership boundaries</li>
          <li>Modular services that stay maintainable</li>
          <li>APIs and integrations that don't break easily</li>
          <li>Event-driven patterns when they simplify scale</li>
          <li>Data strategies that support growth</li>
        </ul>
      </div>

      <!-- Reliability & Operations -->
      <div class="bento-block">
        <div class="capability-icon">
          <svg viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <title>Reliability & Operations</title>
            <desc>Monitoring and operational flow with reliability metrics</desc>
            <path d="M 10 30 C 20 20 40 40 50 30" stroke="currentColor" stroke-width="1.5" fill="none" opacity="0.4" stroke-linecap="round" />
            <circle cx="20" cy="25" r="4" fill="#7aa7ff" />
            <circle cx="30" cy="30" r="4" fill="#7ef0c1" opacity="0.7" />
            <circle cx="40" cy="25" r="4" fill="#ff9000" opacity="0.7" />
            <line x1="20" y1="25" x2="20" y2="45" stroke="#7aa7ff" stroke-width="1.5" opacity="0.3" stroke-linecap="round" />
            <line x1="30" y1="30" x2="30" y2="50" stroke="#7ef0c1" stroke-width="1.5" opacity="0.3" stroke-linecap="round" />
            <line x1="40" y1="25" x2="40" y2="45" stroke="#ff9000" stroke-width="1.5" opacity="0.3" stroke-linecap="round" />
            <path d="M 20 45 Q 30 50 40 45" stroke="#7aa7ff" stroke-width="2.5" fill="none" stroke-linecap="round" opacity="0.8" />
          </svg>
        </div>
        <h3>Reliability &amp; Operations</h3>
        <ul class="capability-list">
          <li>Monitoring and tracing (logs, metrics, traces)</li>
          <li>Reliability targets and alerting (SLOs)</li>
          <li>Incident response and runbooks</li>
          <li>Capacity planning and performance tuning</li>
          <li>Operational risk reduction</li>
        </ul>
      </div>

      <!-- Secure-by-Design -->
      <div class="bento-block bento-block--dark">
        <div class="capability-icon">
          <svg viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <title>Secure-by-Design Systems</title>
            <desc>Security layers protecting core system</desc>
            <circle cx="30" cy="30" r="22" fill="none" stroke="currentColor" stroke-width="1.5" opacity="0.2" />
            <circle cx="30" cy="30" r="16" fill="none" stroke="#7aa7ff" stroke-width="1.5" opacity="0.4" />
            <circle cx="30" cy="30" r="10" fill="#7aa7ff" opacity="0.6" />
            <circle cx="30" cy="30" r="6" fill="#ff9000" />
            <rect x="12" y="28" width="6" height="6" fill="#7ef0c1" opacity="0.6" />
            <rect x="42" y="28" width="6" height="6" fill="#7ef0c1" opacity="0.6" />
            <line x1="18" y1="31" x2="20" y2="30" stroke="#7ef0c1" stroke-width="1.5" opacity="0.4" stroke-linecap="round" />
            <line x1="42" y1="31" x2="40" y2="30" stroke="#7ef0c1" stroke-width="1.5" opacity="0.4" stroke-linecap="round" />
            <path d="M 12 28 Q 30 15 48 28" stroke="#ff9000" stroke-width="2.5" fill="none" stroke-linecap="round" opacity="0.9" />
          </svg>
        </div>
        <h3>Secure-by-Design Systems</h3>
        <ul class="capability-list">
          <li>Identity and access modeling</li>
          <li>Secrets and configuration strategy</li>
          <li>Reduce attack surface by design</li>
          <li>Secure implementation review</li>
        </ul>
      </div>

      <!-- Specialty callout block (completes the 3×2 bento grid) -->
      <div class="bento-block bento-block--callout">
        <span class="bento-eyebrow">Specialty</span>
        <h3>ColdFusion &amp; Legacy Migrations</h3>
        <p class="bento-desc">Purpose-built patterns for teams moving off aging stacks—without disrupting live systems or halting feature delivery.</p>
        <div class="bento-tags">
          <span class="tag">ColdFusion</span>
          <span class="tag">Strangler Fig</span>
          <span class="tag">Serverless</span>
          <span class="tag">CircleCI</span>
        </div>
      </div>

    </div>
  </section>
</template>

<script setup>
</script>

<style scoped>

.bento-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 14px;
  align-items: start;
}

.bento-block {
  padding: 24px;
  border-radius: var(--radius);
  border: 1px solid #30363d;
  border-top: 1px solid rgba(47, 129, 247, 0.22);
  background: #0d1117;
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
}

/* Secure-by-Design — same background, slightly dimmer cobalt top accent */
.bento-block--dark {
  border-top-color: rgba(47, 129, 247, 0.12);
}

/* Featured Modernization block — deep navy inner shadow for depth */
.bento-block--wide {
  grid-column: span 2;
  background: #0d1117;
  box-shadow: inset 0 0 40px rgba(0, 8, 20, 0.65);
  border-top: 1px solid rgba(47, 129, 247, 0.40);
}

.bento-block:hover {
  transform: translateY(-2px);
  box-shadow: 0 16px 45px rgba(0, 0, 0, 0.5);
  border-color: #444c56;
}

.bento-block--wide:hover {
  box-shadow:
    inset 0 0 40px rgba(0, 8, 20, 0.65),
    0 16px 45px rgba(0, 0, 0, 0.5);
}

.bento-block h3 {
  margin: 0 0 16px;
  font-size: 1.05rem;
  font-weight: 500;
  letter-spacing: 0.2px;
  color: #f0f4ff;
}

.bento-eyebrow {
  display: block;
  font-size: 0.72rem;
  font-weight: 600;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: rgba(47, 129, 247, 0.80);
  margin-bottom: 14px;
}

.bento-wide-inner {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 32px;
  align-items: start;
}

.bento-desc {
  margin: 0;
  font-size: 0.875rem;
  color: rgba(255, 255, 255, 0.48);
  line-height: 1.6;
}

.bento-block--wide .bento-desc {
  margin-top: 10px;
}

.bento-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-top: 16px;
}

@media (max-width: 920px) {
  .bento-grid {
    grid-template-columns: 1fr;
  }

  .bento-block--wide {
    grid-column: span 1;
  }

  .bento-wide-inner {
    grid-template-columns: 1fr;
    gap: 20px;
  }
}
</style>
