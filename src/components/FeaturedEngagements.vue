<template>
  <section id="engagements">
    <div class="section-head">
      <div>
        <h2>Featured Engagements</h2>
      </div>
      <p class="section-microline">Real problems. Measured outcomes.</p>
    </div>

    <p class="section-intro">A sample of the work we've done—from modernizing brittle systems to building high-throughput data infrastructure.</p>

    <div class="grid">

      <div class="card eng-card">
        <div class="card-visual">
          <svg viewBox="0 0 120 80" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <title>Real-Time Data Stream</title>
            <desc>Streaming data pipeline with flowing signal and metric points</desc>
            <!-- Base timeline -->
            <line x1="10" y1="55" x2="110" y2="55" stroke="currentColor" stroke-width="1.5" opacity="0.15" stroke-linecap="round" />
            <!-- Signal path -->
            <path d="M 10 55 L 25 40 L 40 55 L 55 28 L 70 50 L 85 38 L 100 55"
                  stroke="currentColor" stroke-width="1.5" opacity="0.35" fill="none" stroke-linecap="round" stroke-linejoin="round" />
            <!-- Highlighted data points -->
            <circle cx="25" cy="40" r="3" fill="currentColor" opacity="0.4" />
            <circle cx="55" cy="28" r="4" fill="#7aa7ff" />
            <circle cx="85" cy="38" r="3" fill="#ff9000" opacity="0.8" />
            <!-- Velocity tick lines -->
            <line x1="55" y1="14" x2="55" y2="28" stroke="#7aa7ff" stroke-width="1.5" opacity="0.5" stroke-linecap="round" />
            <line x1="85" y1="24" x2="85" y2="38" stroke="#ff9000" stroke-width="1.5" opacity="0.5" stroke-linecap="round" />
            <!-- Architectural arc spanning the stream -->
            <path d="M 10 55 Q 60 30 110 55" stroke="#7aa7ff" stroke-width="2" fill="none" stroke-linecap="round" opacity="0.8" />
          </svg>
        </div>
        <h3>Real-Time Analytics Platform</h3>
        <div class="eng-rows">
          <div class="eng-row">
            <span class="eng-label">Challenge</span>
            <p>A fintech client's batch pipeline couldn't sustain sub-second dashboard latency across millions of daily transaction events.</p>
          </div>
          <div class="eng-row">
            <span class="eng-label">Solution</span>
            <p>Rebuilt ingestion with Kinesis and Lambda, backed by a read-optimized DynamoDB serving tier for the frontend.</p>
          </div>
          <div class="eng-row eng-row--result">
            <span class="eng-label eng-label--result">Result</span>
            <p>Dashboard latency fell from 4 minutes to under 800ms. System now processes 12M+ events per day with zero data loss.</p>
          </div>
        </div>
        <div class="tags eng-stack">
          <span class="tag">Kinesis</span>
          <span class="tag">Redshift</span>
          <span class="tag">Lambda</span>
          <span class="tag">API Gateway</span>
        </div>
        <div class="card-meta">streaming · kinesis · lambda · dynamodb</div>
      </div>

      <div class="card eng-card">
        <div class="card-visual">
          <svg viewBox="0 0 120 80" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <title>Monolith to Services Transformation</title>
            <desc>Dense legacy block breaking apart into distributed service modules</desc>
            <!-- Legacy monolith (left) -->
            <rect x="5" y="18" width="28" height="44" fill="currentColor" opacity="0.2" stroke="currentColor" stroke-width="1.5" />
            <!-- Fracture lines through monolith -->
            <path d="M 18 18 L 12 32 L 22 38 L 14 62" stroke="#ff9000" stroke-width="1.5" fill="none" opacity="0.6" stroke-linecap="round" />
            <!-- Extracted service modules (right) -->
            <rect x="68" y="10" width="16" height="12" fill="#7aa7ff" opacity="0.5" stroke="#7aa7ff" stroke-width="1.5" />
            <rect x="90" y="10" width="16" height="12" fill="currentColor" opacity="0.25" stroke="currentColor" stroke-width="1.5" />
            <rect x="68" y="30" width="16" height="12" fill="#7ef0c1" opacity="0.5" stroke="#7ef0c1" stroke-width="1.5" />
            <rect x="90" y="30" width="16" height="12" fill="currentColor" opacity="0.25" stroke="currentColor" stroke-width="1.5" />
            <rect x="79" y="52" width="16" height="12" fill="#ff9000" opacity="0.5" stroke="#ff9000" stroke-width="1.5" />
            <!-- Transform arc -->
            <path d="M 33 40 Q 50 28 68 20" stroke="#ff9000" stroke-width="2" fill="none" stroke-linecap="round" opacity="0.9" />
          </svg>
        </div>
        <h3>Enterprise Modernization</h3>
        <div class="eng-rows">
          <div class="eng-row">
            <span class="eng-label">Challenge</span>
            <p>Legacy SaaS platform requiring stabilized deployment pipelines and hardened credential security across a multi-stack environment.</p>
          </div>
          <div class="eng-row">
            <span class="eng-label">Solution</span>
            <p>Implemented CircleCI pipelines and AWS Secrets Manager, eliminating manual deployments and replacing hardcoded credentials site-wide.</p>
          </div>
          <div class="eng-row eng-row--result">
            <span class="eng-label eng-label--result">Result</span>
            <p>Deployment frequency increased by <span class="eng-metric">+50%</span> and post-release issues reduced by <span class="eng-metric">25%</span>.</p>
          </div>
        </div>
        <div class="tags eng-stack">
          <span class="tag">ColdFusion</span>
          <span class="tag">AWS</span>
          <span class="tag">CircleCI</span>
          <span class="tag">Secrets Manager</span>
        </div>
        <div class="card-meta">ci/cd · secrets management · coldfusion · aws</div>
      </div>

      <div class="card eng-card">
        <div class="card-visual">
          <svg viewBox="0 0 120 80" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <title>Serverless Payment State Machine</title>
            <desc>Payment flow nodes connected through a serverless state machine</desc>
            <!-- Flow nodes -->
            <circle cx="15" cy="50" r="5" fill="currentColor" opacity="0.3" stroke="currentColor" stroke-width="1.5" />
            <circle cx="38" cy="28" r="5" fill="#7aa7ff" opacity="0.7" />
            <circle cx="62" cy="44" r="5" fill="currentColor" opacity="0.3" stroke="currentColor" stroke-width="1.5" />
            <circle cx="84" cy="24" r="5" fill="#7ef0c1" opacity="0.7" />
            <circle cx="106" cy="44" r="5" fill="#ff9000" opacity="0.8" />
            <!-- Connection lines -->
            <line x1="20" y1="46" x2="33" y2="32" stroke="currentColor" stroke-width="1.5" opacity="0.35" stroke-linecap="round" />
            <line x1="43" y1="32" x2="57" y2="40" stroke="#7aa7ff" stroke-width="1.5" opacity="0.5" stroke-linecap="round" />
            <line x1="67" y1="40" x2="79" y2="28" stroke="currentColor" stroke-width="1.5" opacity="0.35" stroke-linecap="round" />
            <line x1="89" y1="28" x2="101" y2="40" stroke="#ff9000" stroke-width="1.5" opacity="0.6" stroke-linecap="round" />
            <!-- Idempotency loop arc on validate step -->
            <path d="M 33 24 Q 38 12 43 24" stroke="#7aa7ff" stroke-width="1.5" fill="none" stroke-linecap="round" opacity="0.7" />
            <!-- Spanning arc -->
            <path d="M 15 50 Q 60 15 106 44" stroke="#ff9000" stroke-width="2" fill="none" stroke-linecap="round" opacity="0.85" />
          </svg>
        </div>
        <h3>Serverless Payments Migration</h3>
        <div class="eng-rows">
          <div class="eng-row">
            <span class="eng-label">Challenge</span>
            <p>Unpredictable traffic spikes pushed over-provisioned payment infrastructure to $40k/month at idle, with no path to cost-effective scale.</p>
          </div>
          <div class="eng-row">
            <span class="eng-label">Solution</span>
            <p>Migrated to API Gateway, Lambda, and Step Functions with idempotent payment state machines and dead-letter queue handling.</p>
          </div>
          <div class="eng-row eng-row--result">
            <span class="eng-label eng-label--result">Result</span>
            <p>Infrastructure costs fell 78%. The system now handles 0 to 50k concurrent transactions with zero manual scaling intervention.</p>
          </div>
        </div>
        <div class="tags eng-stack">
          <span class="tag">Node.js 20</span>
          <span class="tag">Amazon Pay</span>
          <span class="tag">CloudFormation</span>
          <span class="tag">Event-Driven</span>
        </div>
        <div class="card-meta">api gateway · lambda · step functions · serverless</div>
      </div>

    </div>
  </section>
</template>

<script setup>
</script>

<style scoped>
.eng-card {
  display: flex;
  flex-direction: column;
  background: #0d1117;
  border: 1px solid #30363d;
  border-top: 1px solid rgba(47, 129, 247, 0.30);
  transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
}

.eng-card:hover {
  transform: translateY(-8px);
  border-color: rgba(47, 129, 247, 0.42);
  box-shadow:
    0 24px 60px rgba(0, 0, 0, 0.55),
    0 0 0 1px rgba(47, 129, 247, 0.10),
    0 0 28px rgba(47, 129, 247, 0.08);
}

.eng-rows {
  display: flex;
  flex-direction: column;
  gap: 12px;
  flex: 1;
  margin-top: 14px;
}

.eng-row {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.eng-label {
  font-size: 0.72rem;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: rgba(255, 255, 255, 0.38);
  line-height: 1;
}

.eng-label--result {
  color: rgba(240, 244, 255, 0.55);
}

.eng-row p {
  margin: 0;
  color: var(--muted);
  font-size: 0.875rem;
  line-height: 1.55;
}

.eng-row--result p {
  color: rgba(240, 244, 255, 0.82);
  transition: color 0.3s ease;
  line-height: 1.7;
}

.eng-metric {
  display: inline-block;
  font-size: 1.25rem;
  font-weight: 700;
  line-height: 1;
  letter-spacing: -0.01em;
  color: #ffffff;
  vertical-align: baseline;
  position: relative;
  top: 0.05em;
}

.eng-card:hover .eng-row--result p {
  color: rgba(240, 244, 255, 1);
}

.eng-card:hover .eng-label--result {
  color: rgba(240, 244, 255, 0.75);
}

.eng-stack {
  margin-top: 16px;
  padding-top: 14px;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
  transition: border-color 0.25s ease;
}

.eng-card:hover .eng-stack {
  border-top-color: rgba(47, 129, 247, 0.18);
}

/* Cobalt-bordered transparent tags */
.eng-stack .tag {
  background: transparent;
  border: 1px solid rgba(47, 129, 247, 0.32);
  color: rgba(47, 129, 247, 0.80);
  transition: color 0.25s ease, border-color 0.25s ease;
}

.eng-card:hover .eng-stack .tag {
  color: rgba(168, 200, 255, 0.95);
  border-color: rgba(47, 129, 247, 0.58);
}
</style>
