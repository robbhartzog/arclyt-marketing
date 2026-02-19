<template>
  <section class="hero" :style="{ backgroundImage: `url(${backgroundUrl})` }">
    <div class="hero-overlay"></div>
    <div class="hero-content">
      <div class="hero-card hero-card-left">
        <h1>We build modern cloud systems designed to scale.</h1>
      </div>

      <div class="hero-card hero-card-right">
        <p class="lead">
          Arclyt designs and builds modern cloud systems—custom applications and platforms grounded in strong architecture, delivered with clarity.
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

const backgroundUrl = '/assets/backsplash2.jpg'
const isModalOpen = ref(false)

const openModal = () => {
  isModalOpen.value = true
}

const closeModal = () => {
  isModalOpen.value = false
}
</script>
