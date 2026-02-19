<template>
  <section class="hero" :style="{ backgroundImage: `url(${backgroundUrl})` }">
    <div class="hero-overlay"></div>
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
          <button class="btn primary" @click="openModal">Start a project</button>
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
const isModalOpen = ref(false)

const openModal = () => {
  isModalOpen.value = true
}

const closeModal = () => {
  isModalOpen.value = false
}
</script>
