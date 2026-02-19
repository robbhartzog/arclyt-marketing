<template>
  <section id="process">
    <div class="section-head">
      <div>
        <h2>How we work</h2>
      </div>
      <p class="section-microline">Simple process. Tight feedback loops. Clear ownership.</p>
    </div>

    <div class="grid">
      <div class="card">
        <div class="process-icon">
          <svg viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <title>Align</title>
            <desc>Converging lines representing alignment and focus</desc>
            <!-- Converging lines -->
            <line x1="10" y1="20" x2="30" y2="30" stroke="#7aa7ff" stroke-width="2" opacity="0.6" stroke-linecap="round" />
            <line x1="50" y1="20" x2="30" y2="30" stroke="#ff9000" stroke-width="2" opacity="0.7" stroke-linecap="round" />
            <line x1="10" y1="40" x2="30" y2="30" stroke="#7ef0c1" stroke-width="2" opacity="0.6" stroke-linecap="round" />
            <line x1="50" y1="40" x2="30" y2="30" stroke="#ff9000" stroke-width="2" opacity="0.7" stroke-linecap="round" />
            <!-- Center focus point -->
            <circle cx="30" cy="30" r="5" fill="#7aa7ff" />
            <circle cx="30" cy="30" r="3" fill="#ff9000" />
            <!-- Alignment arc -->
            <path d="M 20 30 Q 30 20 40 30" stroke="#ff9000" stroke-width="2.5" fill="none" stroke-linecap="round" opacity="1" />
          </svg>
        </div>
        <h3>Align</h3>
        <p>We define outcomes, constraints, and success metrics.<br/>Then we shape a deliverable you can validate early.</p>
        <div class="card-meta">Discovery · Scope definition</div>
      </div>
      <div class="card">
        <div class="process-icon">
          <svg viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <title>Build</title>
            <desc>Stacked layers representing incremental building</desc>
            <!-- Base layer -->
            <rect x="10" y="40" width="40" height="8" fill="#7aa7ff" opacity="0.4" stroke="#7aa7ff" stroke-width="1.5" />
            <!-- Middle layer -->
            <rect x="15" y="28" width="30" height="8" fill="#ff9000" opacity="0.6" stroke="#ff9000" stroke-width="1.5" />
            <!-- Top layer - highlighted -->
            <rect x="20" y="16" width="20" height="8" fill="#7aa7ff" stroke="#7aa7ff" stroke-width="2" />
            <!-- Connection lines -->
            <line x1="30" y1="24" x2="30" y2="40" stroke="#ff9000" stroke-width="2" opacity="0.8" stroke-linecap="round" />
            <line x1="30" y1="12" x2="30" y2="28" stroke="#7aa7ff" stroke-width="2" opacity="0.8" stroke-linecap="round" />
            <!-- Architectural arc -->
            <path d="M 10 44 Q 30 30 50 44" stroke="#ff9000" stroke-width="2.5" fill="none" stroke-linecap="round" opacity="1" />
          </svg>
        </div>
        <h3>Build</h3>
        <p>Incremental delivery with working software.<br/>Architecture stays clear. Changes stay reversible.</p>
        <div class="card-meta">Iterations · Continuous validation</div>
      </div>
      <div class="card">
        <div class="process-icon">
          <svg viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <title>Operate</title>
            <desc>Flow and operational nodes representing continuous operation</desc>
            <!-- Operational nodes -->
            <circle cx="15" cy="20" r="4" fill="#7ef0c1" opacity="0.7" />
            <circle cx="30" cy="15" r="6" fill="#ff9000" />
            <circle cx="45" cy="20" r="4" fill="#7ef0c1" opacity="0.7" />
            <circle cx="20" cy="40" r="4" fill="#7aa7ff" opacity="0.6" />
            <circle cx="40" cy="40" r="4" fill="#ff9000" opacity="0.7" />
            <!-- Flow lines -->
            <line x1="15" y1="20" x2="30" y2="15" stroke="#ff9000" stroke-width="2" opacity="0.7" stroke-linecap="round" />
            <line x1="30" y1="15" x2="45" y2="20" stroke="#ff9000" stroke-width="2" opacity="0.7" stroke-linecap="round" />
            <line x1="30" y1="20" x2="20" y2="40" stroke="#7aa7ff" stroke-width="2" opacity="0.5" stroke-linecap="round" />
            <line x1="30" y1="20" x2="40" y2="40" stroke="#ff9000" stroke-width="2" opacity="0.6" stroke-linecap="round" />
            <!-- Operational arc -->
            <path d="M 15 20 Q 30 10 45 20" stroke="#ff9000" stroke-width="2.5" fill="none" stroke-linecap="round" opacity="1" />
          </svg>
        </div>
        <h3>Operate</h3>
        <p>We ship with monitoring, documentation, and structured handoff.<br/>When appropriate, we stay to harden and extend.</p>
        <div class="card-meta">Handoff · Operational readiness</div>
      </div>
    </div>
  </section>
</template>

<script setup>
</script>
