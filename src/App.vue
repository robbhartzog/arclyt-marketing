<template>
  <Header />
  <main id="top" class="wrap">
    <Hero />
    <Services />
    <Capabilities />
    <CertBar />
    <FeaturedEngagements />
    <Process />
    <Stack />
    <TechTicker />
    <Footer />
  </main>

  <!-- Auto-opened when visiting /schedule directly -->
  <ContactModal :is-open="scheduleModalOpen" @close="scheduleModalOpen = false" />
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { event } from 'vue-gtag'
import Header from './components/Header.vue'
import Hero from './components/Hero.vue'
import Services from './components/Services.vue'
import Capabilities from './components/Capabilities.vue'
import CertBar from './components/CertBar.vue'
import FeaturedEngagements from './components/FeaturedEngagements.vue'
import Process from './components/Process.vue'
import Stack from './components/Stack.vue'
import TechTicker from './components/TechTicker.vue'
import Footer from './components/Footer.vue'
import ContactModal from './components/ContactModal.vue'

const scheduleModalOpen = ref(false)

onMounted(() => {
  if (window.location.pathname === '/schedule') {
    event('cta_click', { cta_location: 'direct_link' })
    scheduleModalOpen.value = true
  }
})
</script>
