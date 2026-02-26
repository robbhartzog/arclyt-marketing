<template>
  <div class="ticker-section">
    <p class="ticker-eyebrow">Technologies We Master</p>

    <div class="ticker-wrap">
      <div class="ticker-track">
        <div
          v-for="tech in ticker"
          :key="tech.key"
          class="ticker-item"
        >
          <svg
            :viewBox="tech.vb"
            class="ticker-svg"
            :aria-label="tech.name"
            v-html="tech.svg"
          ></svg>
          <span class="ticker-name">{{ tech.name }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const baseTechs = [
  {
    name: 'AWS',
    vb: '0 0 44 38',
    svg: `
      <path d="M 8 17 Q 10 7 18 9 Q 20 3 27 5 Q 34 3 37 11 Q 43 13 41 19 L 7 19 Q 4 19 5 16 Z"
            fill="#FF9900" opacity="0.13" stroke="#FF9900" stroke-width="1.4" stroke-linejoin="round"/>
      <path d="M 8 28 Q 22 37 36 28" fill="none" stroke="#FF9900" stroke-width="2.5" stroke-linecap="round"/>
      <path d="M 32 24 L 36 28 L 32 32" fill="none" stroke="#FF9900" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
    `,
  },
  {
    name: 'Node.js',
    vb: '0 0 44 40',
    svg: `
      <polygon points="22,3 39,13 39,27 22,37 5,27 5,13"
               fill="#539E43" opacity="0.10" stroke="#539E43" stroke-width="1.8" stroke-linejoin="round"/>
      <polygon points="22,10 33,17 33,23 22,30 11,23 11,17"
               fill="#539E43" opacity="0.15" stroke="#539E43" stroke-width="1.2" stroke-linejoin="round"/>
      <circle cx="22" cy="20" r="4" fill="#539E43" opacity="0.55"/>
    `,
  },
  {
    name: 'Vue.js',
    vb: '0 0 44 36',
    svg: `
      <path d="M 2 2 L 22 34 L 42 2 L 34 2 L 22 20 L 10 2 Z" fill="#41B883" opacity="0.14"/>
      <path d="M 2 2 L 22 34 L 42 2" fill="none" stroke="#41B883" stroke-width="2.5"
            stroke-linejoin="round" stroke-linecap="round"/>
      <path d="M 12 2 L 22 18 L 32 2" fill="none" stroke="#41B883" stroke-width="2"
            stroke-linejoin="round" stroke-linecap="round" opacity="0.6"/>
    `,
  },
  {
    name: 'ColdFusion',
    vb: '0 0 44 36',
    svg: `
      <rect x="4" y="2" width="36" height="32" rx="5"
            fill="#CC0000" opacity="0.10" stroke="#CC0000" stroke-width="1.5"/>
      <text x="22" y="25" text-anchor="middle" font-size="14" font-weight="700"
            font-style="italic" font-family="Georgia,'Times New Roman',serif" fill="#CC0000">CF</text>
    `,
  },
  {
    name: 'DynamoDB',
    vb: '0 0 44 38',
    svg: `
      <ellipse cx="22" cy="10" rx="13" ry="4.5"
               fill="#4053D6" opacity="0.18" stroke="#4053D6" stroke-width="1.5"/>
      <line x1="9"  y1="10" x2="9"  y2="28" stroke="#4053D6" stroke-width="1.5" opacity="0.55"/>
      <line x1="35" y1="10" x2="35" y2="28" stroke="#4053D6" stroke-width="1.5" opacity="0.55"/>
      <path d="M 9 28 Q 22 34 35 28" fill="none" stroke="#4053D6" stroke-width="1.5" stroke-linecap="round"/>
      <line x1="9" y1="17" x2="35" y2="17" stroke="#4053D6" stroke-width="1" opacity="0.38"/>
      <line x1="9" y1="23" x2="35" y2="23" stroke="#4053D6" stroke-width="1" opacity="0.38"/>
    `,
  },
  {
    name: 'Redshift',
    vb: '0 0 44 38',
    svg: `
      <polygon points="22,3 38,13 38,25 22,35 6,25 6,13"
               fill="#8C4FFF" opacity="0.10" stroke="#8C4FFF" stroke-width="1.5" stroke-linejoin="round"/>
      <circle cx="22" cy="19" r="5" fill="#8C4FFF" opacity="0.40" stroke="#8C4FFF" stroke-width="1.2"/>
      <circle cx="13" cy="24" r="3" fill="#8C4FFF" opacity="0.28"/>
      <circle cx="31" cy="24" r="3" fill="#8C4FFF" opacity="0.28"/>
      <line x1="17" y1="20" x2="13" y2="24" stroke="#8C4FFF" stroke-width="1.3" opacity="0.5" stroke-linecap="round"/>
      <line x1="27" y1="20" x2="31" y2="24" stroke="#8C4FFF" stroke-width="1.3" opacity="0.5" stroke-linecap="round"/>
    `,
  },
  {
    name: 'Cloudflare',
    vb: '0 0 44 36',
    svg: `
      <path d="M 34 23 Q 41 23 41 16 Q 41 9 34 9 Q 33 3 26 2 Q 18 0 13 7 Q 7 7 5 13 Q 1 13 1 18 Q 1 24 8 24 Z"
            fill="#F38020" opacity="0.12" stroke="#F38020" stroke-width="1.5" stroke-linejoin="round"/>
      <path d="M 37 28 Q 37 31 34 31 L 10 31 Q 7 31 7 28 Q 11 24 22 24 Q 33 24 37 28 Z"
            fill="#F38020" opacity="0.22" stroke="#F38020" stroke-width="1"/>
    `,
  },
]

// Duplicate the set for a seamless CSS loop
const ticker = computed(() => [
  ...baseTechs.map((t, i) => ({ ...t, key: `a${i}` })),
  ...baseTechs.map((t, i) => ({ ...t, key: `b${i}` })),
])
</script>

<style scoped>
.ticker-section {
  padding: 36px 0 32px;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
  overflow: hidden;
}

.ticker-eyebrow {
  margin: 0 0 22px;
  text-align: center;
  font-size: 0.72rem;
  font-weight: 600;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: rgba(255, 255, 255, 0.28);
}

/* ── Ticker belt ─────────────────────────────────────────── */

.ticker-wrap {
  position: relative;
  /* Fade masks on left + right */
  -webkit-mask-image: linear-gradient(
    to right,
    transparent 0%,
    black 8%,
    black 92%,
    transparent 100%
  );
  mask-image: linear-gradient(
    to right,
    transparent 0%,
    black 8%,
    black 92%,
    transparent 100%
  );
}

.ticker-wrap:hover .ticker-track {
  animation-play-state: paused;
}

.ticker-track {
  display: flex;
  align-items: center;
  width: max-content;
  animation: ticker-scroll 38s linear infinite;
}

@keyframes ticker-scroll {
  from { transform: translateX(0); }
  to   { transform: translateX(-50%); }
}

/* ── Individual items ────────────────────────────────────── */

.ticker-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  padding: 0 36px;
  cursor: default;
  filter: grayscale(1) opacity(0.45);
  transition: filter 0.28s ease, transform 0.28s ease;
}

.ticker-item:hover {
  filter: grayscale(0) opacity(1);
  transform: translateY(-2px);
}

.ticker-svg {
  width: auto;
  height: 36px;
  display: block;
}

.ticker-name {
  font-family: var(--mono);
  font-size: 0.68rem;
  letter-spacing: 0.06em;
  color: rgba(176, 189, 216, 0.6);
  white-space: nowrap;
  transition: color 0.28s ease;
}

.ticker-item:hover .ticker-name {
  color: rgba(240, 244, 255, 0.9);
}
</style>
