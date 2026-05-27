<template>
  <section id="engagements">
    <div class="section-head">
      <div>
        <h2>Featured Engagements</h2>
      </div>
      <p class="section-microline">Real problems. Measured outcomes.</p>
    </div>

    <p class="section-intro">A sample of engagements Arclyt has delivered—from stabilizing legacy systems to building high-throughput data infrastructure.</p>

    <div class="grid">

      <!-- ── LifeHaus ── -->
      <div class="card eng-card">
        <div class="card-visual">
          <svg viewBox="0 0 120 80" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <title>Household Operating System</title>
            <desc>House silhouette with sync nodes representing a multi-tenant family coordination platform</desc>
            <!-- House body -->
            <rect x="32" y="37" width="56" height="33" fill="currentColor" opacity="0.09"
                  stroke="currentColor" stroke-width="1.5" stroke-opacity="0.22" />
            <!-- Roof -->
            <path d="M 26 37 L 60 10 L 94 37"
                  stroke="currentColor" stroke-width="1.5" fill="none"
                  stroke-linecap="round" stroke-linejoin="round" opacity="0.28" />
            <!-- Door -->
            <rect x="52" y="54" width="16" height="16"
                  fill="currentColor" opacity="0.10"
                  stroke="currentColor" stroke-width="1" stroke-opacity="0.18" />
            <!-- Hub node at roof peak (Cognito / API Gateway) -->
            <circle cx="60" cy="10" r="4.5" fill="#7aa7ff" />
            <circle cx="60" cy="10" r="9"   fill="none" stroke="#7aa7ff" stroke-width="1" opacity="0.22" />
            <!-- Family member nodes inside house -->
            <circle cx="44" cy="49" r="3.5" fill="#7aa7ff"    opacity="0.72" />
            <circle cx="76" cy="49" r="3.5" fill="#ff9000"    opacity="0.75" />
            <circle cx="60" cy="49" r="3"   fill="currentColor" opacity="0.30"
                    stroke="currentColor" stroke-width="1.5" />
            <!-- Spokes from members to hub -->
            <line x1="44" y1="46" x2="57" y2="14"
                  stroke="#7aa7ff" stroke-width="1.5" opacity="0.28" stroke-linecap="round" />
            <line x1="76" y1="46" x2="63" y2="14"
                  stroke="#ff9000" stroke-width="1.5" opacity="0.28" stroke-linecap="round" />
            <!-- Real-time sync arc across members -->
            <path d="M 44 49 Q 60 32 76 49"
                  stroke="#7aa7ff" stroke-width="2" fill="none"
                  stroke-linecap="round" opacity="0.80" />
          </svg>
        </div>
        <h3>Family SaaS Ecosystem <span class="eng-client">LifeHaus</span></h3>
        <div class="eng-rows">
          <div class="eng-row">
            <span class="eng-label">Challenge</span>
            <p>Creating a multi-user family coordination platform that maintains enterprise-grade security and strict data isolation for thousands of households.</p>
          </div>
          <div class="eng-row">
            <span class="eng-label">Solution</span>
            <p>Engineered a serverless architecture using AWS Cognito for secure identity management and API Gateway / Lambda for high-performance, stateless processing. Built a multi-tenant data model to ensure privacy while maintaining sub-100ms response times for the Vue 3 frontend.</p>
          </div>
          <div class="eng-row eng-row--result">
            <span class="eng-label eng-label--result">Result</span>
            <p>Launched a scalable production SaaS with sub-100ms response times — a core IP asset for Arclyt that bridges complex enterprise patterns with consumer-facing simplicity.</p>
          </div>
        </div>
        <div class="tags eng-stack">
          <span class="tag">AWS</span>
          <span class="tag">Node.js</span>
          <span class="tag">Vue 3</span>
          <span class="tag">Cognito</span>
          <span class="tag">Lambda</span>
          <span class="tag">DynamoDB</span>
        </div>
        <div class="card-meta">product engineering · saas · serverless architecture · ip portfolio</div>
      </div>

      <!-- ── Real-Time Analytics ── -->
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
            <p>An enterprise event management platform—serving Fortune 500 clients including AWS—relied on batch pipelines that couldn't sustain real-time reporting latency across millions of daily attendance and engagement records.</p>
          </div>
          <div class="eng-row">
            <span class="eng-label">Solution</span>
            <p>Architected an asynchronous reporting pipeline using Kinesis, Lambda, and Redshift—with CloudFront-accelerated delivery and automated usage notifications replacing manual batch exports.</p>
          </div>
          <div class="eng-row eng-row--result">
            <span class="eng-label eng-label--result">Result</span>
            <p>Enabled scalable, real-time usage reporting across high-volume event data with consistent latency improvements and fully automated notification delivery.</p>
          </div>
        </div>
        <div class="tags eng-stack">
          <span class="tag">Kinesis</span>
          <span class="tag">Redshift</span>
          <span class="tag">Lambda</span>
          <span class="tag">CloudFront</span>
        </div>
        <div class="card-meta">streaming · kinesis · redshift · cloudfront</div>
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
            <p>A large-scale commercial real estate SaaS platform—serving over half a billion square feet of managed property—required stabilized deployment pipelines, hardened credential security, and a large-scale DNS infrastructure overhaul.</p>
          </div>
          <div class="eng-row">
            <span class="eng-label">Solution</span>
            <p>Automated the migration of 2,500+ DNS records to Cloudflare via API scripting, implemented CircleCI pipelines across multiple codebases, and replaced all hardcoded credentials with AWS Secrets Manager.</p>
          </div>
          <div class="eng-row eng-row--result">
            <span class="eng-label eng-label--result">Result</span>
            <p>Deployment frequency increased by +50% and post-release issues reduced by 25%. DNS migration eliminated manual record management across the full portfolio.</p>
          </div>
        </div>
        <div class="tags eng-stack">
          <span class="tag">ColdFusion</span>
          <span class="tag">Cloudflare</span>
          <span class="tag">CircleCI</span>
          <span class="tag">Secrets Manager</span>
        </div>
        <div class="card-meta">ci/cd · cloudflare api · secrets management · coldfusion</div>
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
            <p>An enterprise event management platform required a secure, reliable Amazon Pay integration with idempotency guarantees for high-value booking transactions across a distributed serverless environment.</p>
          </div>
          <div class="eng-row">
            <span class="eng-label">Solution</span>
            <p>Implemented Node.js Lambda functions integrated with Amazon Pay for idempotent payment workflows—covering transaction validation, error recovery, and dead-letter queue processing.</p>
          </div>
          <div class="eng-row eng-row--result">
            <span class="eng-label eng-label--result">Result</span>
            <p>Delivered a production-grade serverless payment system processing hundreds of thousands of dollars in event bookings with zero manual scaling and full transaction auditability.</p>
          </div>
        </div>
        <div class="tags eng-stack">
          <span class="tag">Node.js</span>
          <span class="tag">Amazon Pay</span>
          <span class="tag">Lambda</span>
          <span class="tag">Event-Driven</span>
        </div>
        <div class="card-meta">amazon pay · lambda · idempotency · serverless</div>
      </div>

    </div>
  </section>
</template>

<script setup>
</script>

<style scoped>
/* 2×2 grid for 4 cards — overrides the global 3-col .grid */
.grid {
  grid-template-columns: repeat(2, 1fr);
}

@media (max-width: 720px) {
  .grid {
    grid-template-columns: 1fr;
  }
}

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

/* Client name sub-label in card title */
.eng-client {
  display: inline-block;
  margin-left: 6px;
  font-size: 0.72rem;
  font-weight: 500;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: rgba(47, 129, 247, 0.75);
  vertical-align: middle;
  position: relative;
  top: -1px;
  padding: 2px 7px;
  border: 1px solid rgba(47, 129, 247, 0.28);
  border-radius: 99px;
  background: rgba(47, 129, 247, 0.06);
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
