<template>
  <section id="stack">
    <div class="section-head">
      <div>
        <h2>Adaptable by design</h2>
      </div>
      <p class="section-microline">We meet you where you are — and make the next step clear.</p>
    </div>

    <div class="capabilities-grid">
      <div class="capability-block">
        <h3>Cloud &amp; Platforms</h3>
        <p>AWS-first cloud engineering with the flexibility to support Azure when needed.
        Serverless, containers, and infrastructure as code—designed for security, cost control, and reliability.</p>
      </div>

      <div class="capability-block">
        <h3>App Engineering</h3>
        <p>Modern TypeScript/JavaScript systems with clean APIs and maintainable frontends—built so teams can move fast without accumulating debt.</p>
      </div>
    </div>

    <p class="section-closing">Tooling follows architecture — not the other way around.</p>
  </section>
</template>

<script setup>
</script>

<style scoped>
section {
  border-top: 1px solid rgba(47, 129, 247, 0.30);
}

.card {
  transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
}

.card:hover {
  transform: translateY(-8px);
  border-color: rgba(47, 129, 247, 0.42);
  box-shadow:
    0 24px 60px rgba(0, 0, 0, 0.55),
    0 0 0 1px rgba(47, 129, 247, 0.10),
    0 0 28px rgba(47, 129, 247, 0.08);
}
</style>
