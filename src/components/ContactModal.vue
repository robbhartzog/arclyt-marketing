<template>
  <Teleport to="body">
    <Transition name="modal">
      <div v-if="isOpen" class="modal-overlay" @click.self="close" role="dialog" aria-modal="true" aria-labelledby="modal-title">
        <div class="modal-container">
          <div class="modal-header">
            <div>
              <div class="section-eyebrow">Contact</div>
              <h2 id="modal-title">Let's build something clear.</h2>
              <p class="section-subtitle">Tell us what you're trying to ship or modernize. We'll respond with next steps, not a sales script.</p>
            </div>
            <button class="modal-close" @click="close" aria-label="Close modal">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M18 6L6 18M6 6L18 18" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </button>
          </div>
          <div class="modal-body">
            <ContactForm form-id="modal" @success="handleSuccess" />
            <p class="contact-microcopy">
              Or email: <a href="mailto:connect@arclyt.io">connect@arclyt.io</a><br/>
              Typical response time: 1–2 business days.
            </p>
            <p class="contact-trust">
              We can sign an NDA if needed.
            </p>
          </div>
        </div>
      </div>
    </Transition>
  </Teleport>
</template>

<script setup>
import { defineProps, defineEmits, onMounted, onUnmounted, watch } from 'vue'
import ContactForm from './ContactForm.vue'

const props = defineProps({
  isOpen: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['close'])

const close = () => {
  emit('close')
}

const handleSuccess = () => {
  // Close modal after a short delay to show success message
  setTimeout(() => {
    close()
  }, 2000)
}

// Handle ESC key to close modal
const handleEscape = (event) => {
  if (event.key === 'Escape' && props.isOpen) {
    close()
  }
}

watch(() => props.isOpen, (isOpen) => {
  if (isOpen) {
    document.addEventListener('keydown', handleEscape)
  } else {
    document.removeEventListener('keydown', handleEscape)
  }
})

onMounted(() => {
  if (props.isOpen) {
    document.addEventListener('keydown', handleEscape)
  }
})

onUnmounted(() => {
  document.removeEventListener('keydown', handleEscape)
})
</script>
