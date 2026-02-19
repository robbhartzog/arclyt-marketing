<template>
  <footer>
    <div class="footer-grid">
      <div class="footer-left">
        <img :src="logoUrl" alt="Arclyt" class="logo-small" />
      </div>

      <div class="footer-center">
        <div class="small muted">
          Cloud systems built to scale—with clarity. |  © {{ currentYear }} Arclyt
        </div>
      </div>

      <div class="footer-icons">
        <a href="#" @click.prevent="openModal" class="footer-icon-link" aria-label="Contact us">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            <polyline points="22,6 12,13 2,6" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </a>
        <a href="https://www.linkedin.com/company/arclyt/" target="_blank" rel="noopener noreferrer" class="footer-icon-link" aria-label="LinkedIn">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            <rect x="2" y="9" width="4" height="12" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            <circle cx="4" cy="4" r="2" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </a>
      </div>
    </div>

    <ContactModal :is-open="isModalOpen" @close="closeModal" />
  </footer>
</template>

<script setup>
import { ref } from 'vue'
import ContactModal from './ContactModal.vue'

// Logo is served from public folder
const logoUrl = '/assets/arclyt_logo.png'
const currentYear = ref(new Date().getFullYear())
const isModalOpen = ref(false)

const openModal = () => {
  isModalOpen.value = true
}

const closeModal = () => {
  isModalOpen.value = false
}
</script>
