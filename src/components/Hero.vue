<template>
  <section class="hero" :style="{ backgroundImage: `url(${backgroundUrl})` }">

    <!-- 1. Content -->
    <div class="hero-content">
      <div class="hero-card hero-card-left">
        <h1>Modern cloud systems built to scale with you.</h1>
      </div>

      <div class="hero-card hero-card-right">
        <p class="lead">
          We help product teams ship reliable cloud software that's easy to evolve.
          Strong foundations, clear ownership, and smooth handoffs—designed for delivery.
        </p>

        <div class="cta-row">
          <button class="btn primary" @click="openModal">Schedule a Strategy Call</button>
          <p class="cta-sub">Consult with an AWS Certified Engineer on your architecture or migration goals.</p>
        </div>
      </div>
    </div>

    <ContactModal :is-open="isModalOpen" @close="closeModal" />
  </section>
</template>

<script setup>
import { ref } from 'vue'
import ContactModal from './ContactModal.vue'

const backgroundUrl = '/assets/hero.jpg'
const isModalOpen   = ref(false)

const openModal  = () => { isModalOpen.value = true }
const closeModal = () => { isModalOpen.value = false }
</script>

<style scoped>
/* Content always on top of the photo overlay */
.hero-content {
  position: relative;
  z-index: 2;
}

/* Ghost button — hollow white, fills dark on hover */
.btn.primary {
  background: transparent;
  border: 1px solid rgba(240, 244, 255, 0.65);
  color: rgba(240, 244, 255, 0.90);
  font-weight: 500;
  box-shadow: none;
  transition: background 0.22s ease, border-color 0.22s ease,
              color 0.22s ease, transform 0.2s ease;
}

.btn.primary:hover {
  background: #1e2433;
  border-color: rgba(240, 244, 255, 0.85);
  color: #ffffff;
  box-shadow: none;
  transform: translateY(-1px);
}

.btn.primary:active {
  background: #2a3347;
  border-color: rgba(240, 244, 255, 0.7);
  color: #ffffff;
  transform: translateY(0);
}

.cta-sub {
  margin: 10px 0 0;
  font-size: 0.78rem;
  color: rgba(240, 244, 255, 0.45);
  line-height: 1.5;
  letter-spacing: 0.01em;
}

section {
  border: 1px solid #30363d;
  border-bottom-left-radius: 0;
  border-bottom-right-radius: 0;
}
</style>
