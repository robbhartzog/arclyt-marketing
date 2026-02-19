<template>
  <footer>
    <div class="footer-grid">
      <div>
        <div style="display:flex; align-items:center; gap:10px; margin-bottom:8px">
          <img :src="logoUrl" alt="Arclyt" class="logo-small" />
        </div>
        <div class="small muted">
          Architecture-led cloud engineering.<br/>
          <span class="mono">© {{ currentYear }} Arclyt</span>
        </div>
      </div>

      <div class="right">
        <button class="btn primary" @click="openModal">Get in touch</button>
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
