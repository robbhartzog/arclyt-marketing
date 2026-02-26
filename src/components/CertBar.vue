<template>
  <div class="certbar">
    <p class="certbar-eyebrow">Certified Expertise</p>
    <p class="certbar-caption">Architected by AWS Certified Cloud Engineers</p>

    <div class="certbar-badges">

      <div class="certbar-badge" data-tooltip="AWS Certified Cloud Practitioner">
        <svg viewBox="0 0 72 72" xmlns="http://www.w3.org/2000/svg" aria-label="AWS Certified Cloud Practitioner">
          <circle cx="36" cy="36" r="34" fill="none" stroke="#4A90D9" stroke-width="1.5" opacity="0.9" />
          <circle cx="36" cy="36" r="28" fill="#0e1826" />
          <path d="M 24 42 Q 20 42 20 38 Q 20 34 24 33 Q 23 28 28 27 Q 31 23 36 24 Q 41 24 43 28 Q 47 28 48 32 Q 51 33 51 37 Q 51 42 47 42 Z"
                fill="none" stroke="#4A90D9" stroke-width="1.5" stroke-linejoin="round" />
          <text x="36" y="55" text-anchor="middle" font-size="7" font-weight="700"
                font-family="ui-monospace, monospace" fill="#4A90D9" letter-spacing="1">CCP</text>
        </svg>
        <span class="certbar-name">Cloud Practitioner</span>
      </div>

      <div class="certbar-badge" data-tooltip="AWS Certified Solutions Architect – Associate">
        <svg viewBox="0 0 72 72" xmlns="http://www.w3.org/2000/svg" aria-label="AWS Certified Solutions Architect Associate">
          <circle cx="36" cy="36" r="34" fill="none" stroke="#FF9900" stroke-width="1.5" opacity="0.9" />
          <circle cx="36" cy="36" r="28" fill="#0e1826" />
          <rect x="28" y="24" width="10" height="8" fill="none" stroke="#FF9900" stroke-width="1.5" rx="1" />
          <rect x="20" y="38" width="10" height="8" fill="none" stroke="#FF9900" stroke-width="1.5" rx="1" />
          <rect x="38" y="38" width="10" height="8" fill="none" stroke="#FF9900" stroke-width="1.5" rx="1" />
          <line x1="33" y1="32" x2="25" y2="38" stroke="#FF9900" stroke-width="1.2" opacity="0.7" />
          <line x1="33" y1="32" x2="43" y2="38" stroke="#FF9900" stroke-width="1.2" opacity="0.7" />
          <text x="36" y="57" text-anchor="middle" font-size="7" font-weight="700"
                font-family="ui-monospace, monospace" fill="#FF9900" letter-spacing="1">SAA</text>
        </svg>
        <span class="certbar-name">Solutions Architect</span>
      </div>

      <div class="certbar-badge" data-tooltip="AWS Certified Developer – Associate">
        <svg viewBox="0 0 72 72" xmlns="http://www.w3.org/2000/svg" aria-label="AWS Certified Developer Associate">
          <circle cx="36" cy="36" r="34" fill="none" stroke="#FF9900" stroke-width="1.5" opacity="0.9" />
          <circle cx="36" cy="36" r="28" fill="#0e1826" />
          <polyline points="28,28 22,36 28,44" fill="none" stroke="#FF9900" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" />
          <polyline points="44,28 50,36 44,44" fill="none" stroke="#FF9900" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" />
          <line x1="38" y1="26" x2="34" y2="46" stroke="#FF9900" stroke-width="1.4" stroke-linecap="round" opacity="0.6" />
          <text x="36" y="57" text-anchor="middle" font-size="7" font-weight="700"
                font-family="ui-monospace, monospace" fill="#FF9900" letter-spacing="1">DVA</text>
        </svg>
        <span class="certbar-name">Developer Associate</span>
      </div>

      <div class="certbar-badge" data-tooltip="AWS Certified SysOps Administrator – Associate">
        <svg viewBox="0 0 72 72" xmlns="http://www.w3.org/2000/svg" aria-label="AWS Certified SysOps Administrator Associate">
          <circle cx="36" cy="36" r="34" fill="none" stroke="#FF9900" stroke-width="1.5" opacity="0.9" />
          <circle cx="36" cy="36" r="28" fill="#0e1826" />
          <circle cx="36" cy="36" r="6" fill="none" stroke="#FF9900" stroke-width="1.5" />
          <circle cx="36" cy="36" r="2.5" fill="#FF9900" opacity="0.6" />
          <line x1="36" y1="24" x2="36" y2="27" stroke="#FF9900" stroke-width="2" stroke-linecap="round" />
          <line x1="36" y1="45" x2="36" y2="48" stroke="#FF9900" stroke-width="2" stroke-linecap="round" />
          <line x1="24" y1="36" x2="27" y2="36" stroke="#FF9900" stroke-width="2" stroke-linecap="round" />
          <line x1="45" y1="36" x2="48" y2="36" stroke="#FF9900" stroke-width="2" stroke-linecap="round" />
          <line x1="27.5" y1="27.5" x2="29.6" y2="29.6" stroke="#FF9900" stroke-width="2" stroke-linecap="round" />
          <line x1="42.4" y1="42.4" x2="44.5" y2="44.5" stroke="#FF9900" stroke-width="2" stroke-linecap="round" />
          <line x1="44.5" y1="27.5" x2="42.4" y2="29.6" stroke="#FF9900" stroke-width="2" stroke-linecap="round" />
          <line x1="29.6" y1="42.4" x2="27.5" y2="44.5" stroke="#FF9900" stroke-width="2" stroke-linecap="round" />
          <text x="36" y="57" text-anchor="middle" font-size="7" font-weight="700"
                font-family="ui-monospace, monospace" fill="#FF9900" letter-spacing="1">SOA</text>
        </svg>
        <span class="certbar-name">SysOps Administrator</span>
      </div>

    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>
.certbar {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  padding: 32px 24px;
  border-radius: var(--radius);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-top: 1px solid rgba(47, 129, 247, 0.28);
  background: linear-gradient(180deg, rgba(19, 27, 46, 0.70), rgba(19, 27, 46, 0.35));
  margin-bottom: 4px;
}

.certbar-eyebrow {
  margin: 0;
  font-size: 0.72rem;
  font-weight: 600;
  letter-spacing: 0.13em;
  text-transform: uppercase;
  color: rgba(47, 129, 247, 0.80);
}

.certbar-caption {
  margin: 0;
  font-size: 0.9rem;
  font-weight: 500;
  color: rgba(240, 244, 255, 0.75);
  letter-spacing: 0.02em;
  text-align: center;
}

/* ── Badges ──────────────────────────────────────────────── */

.certbar-badges {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 32px;
  flex-wrap: wrap;
}

.certbar-badge {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 9px;
  cursor: default;
  position: relative;
}

/* CSS tooltip */
.certbar-badge::after {
  content: attr(data-tooltip);
  position: absolute;
  bottom: calc(100% + 10px);
  left: 50%;
  transform: translateX(-50%) translateY(4px);
  background: rgba(15, 22, 36, 0.96);
  border: 1px solid rgba(255, 255, 255, 0.12);
  color: #f0f4ff;
  font-size: 0.7rem;
  letter-spacing: 0.03em;
  padding: 5px 10px;
  border-radius: 6px;
  white-space: nowrap;
  pointer-events: none;
  opacity: 0;
  transition: opacity 0.2s ease, transform 0.2s ease;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.4);
  z-index: 10;
}

.certbar-badge:hover::after {
  opacity: 1;
  transform: translateX(-50%) translateY(0);
}

/* Badge SVG — grayscale at rest, color + cobalt glow on hover */
.certbar-badge svg {
  width: 76px;
  height: 76px;
  filter: grayscale(100%) opacity(0.55);
  transform-origin: center bottom;
  transition: all 0.3s ease;
}

.certbar-badge:hover svg {
  filter: grayscale(0%) opacity(1)
          drop-shadow(0 0 10px rgba(47, 129, 247, 0.40))
          drop-shadow(0 0 24px rgba(47, 129, 247, 0.16));
  transform: translateY(-3px) scale(1.08);
}

.certbar-name {
  font-size: 0.7rem;
  color: rgba(255, 255, 255, 0.35);
  letter-spacing: 0.04em;
  text-align: center;
  transition: color 0.25s ease;
  white-space: nowrap;
}

.certbar-badge:hover .certbar-name {
  color: rgba(255, 255, 255, 0.7);
}

@media (max-width: 600px) {
  .certbar-badges {
    gap: 20px;
  }

  .certbar-badge svg {
    width: 60px;
    height: 60px;
  }
}
</style>
