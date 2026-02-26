<template>
  <header class="topbar">
    <div class="nav">
      <a class="brand" href="#top" @click="scrollToTop" aria-label="Arclyt home">
        <img :src="logoUrl" alt="Arclyt" class="logo" />
      </a>

      <nav class="links" aria-label="primary">
        <a href="#services" @click="scrollToSection">Services</a>
        <a href="#capabilities" @click="scrollToSection">Capabilities</a>
        <a href="#process" @click="scrollToSection">Process</a>
        <a href="#stack" @click="scrollToSection">Stack</a>
        <a href="#" @click.prevent="openModal" class="nav-icon-link" aria-label="Contact us">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            <polyline points="22,6 12,13 2,6" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </a>
      </nav>

      <button class="mobile-menu-toggle" @click="toggleMobileMenu" :aria-expanded="isMobileMenuOpen" aria-label="Toggle navigation menu">
        <span class="hamburger-line" :class="{ 'active': isMobileMenuOpen }"></span>
        <span class="hamburger-line" :class="{ 'active': isMobileMenuOpen }"></span>
        <span class="hamburger-line" :class="{ 'active': isMobileMenuOpen }"></span>
      </button>
    </div>

    <nav class="mobile-menu" :class="{ 'open': isMobileMenuOpen }" aria-label="mobile navigation">
      <a href="#services" @click="scrollToSection">Services</a>
      <a href="#capabilities" @click="scrollToSection">Capabilities</a>
      <a href="#process" @click="scrollToSection">Process</a>
      <a href="#stack" @click="scrollToSection">Stack</a>
      <a href="#" @click.prevent="openModal" class="mobile-menu-icon" aria-label="Contact us">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          <polyline points="22,6 12,13 2,6" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        <span>Contact us</span>
      </a>
    </nav>

    <ContactModal :is-open="isModalOpen" @close="closeModal" />
  </header>
</template>

<style scoped>
header {
  backdrop-filter: blur(4px) saturate(160%);
  -webkit-backdrop-filter: blur(4px) saturate(160%);
  background: linear-gradient(
    to bottom,
    rgba(10, 15, 26, 0.72),
    rgba(10, 15, 26, 0.32)
  );
  border-bottom: 1px solid rgba(255, 255, 255, 0.07);
}
</style>

<script setup>
import { ref } from 'vue'
import ContactModal from './ContactModal.vue'

const logoUrl = '/assets/arclyt_logo.png'
const isMobileMenuOpen = ref(false)
const isModalOpen = ref(false)

const scrollToSection = (event) => {
  event.preventDefault()
  isMobileMenuOpen.value = false
  const href = event.currentTarget.getAttribute('href')
  if (href && href.startsWith('#')) {
    const targetId = href.substring(1)
    if (targetId === 'top') {
      window.scrollTo({ top: 0, behavior: 'smooth' })
    } else {
      const targetElement = document.getElementById(targetId)
      if (targetElement) {
        const headerOffset = 80
        const elementPosition = targetElement.getBoundingClientRect().top
        const offsetPosition = elementPosition + window.pageYOffset - headerOffset
        window.scrollTo({ top: offsetPosition, behavior: 'smooth' })
      }
    }
  }
}

const scrollToTop = (event) => {
  event.preventDefault()
  isMobileMenuOpen.value = false
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

const toggleMobileMenu = () => {
  isMobileMenuOpen.value = !isMobileMenuOpen.value
}

const openModal = () => {
  isMobileMenuOpen.value = false
  isModalOpen.value = true
}

const closeModal = () => {
  isModalOpen.value = false
}
</script>
