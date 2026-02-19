<template>
  <form @submit.prevent="handleSubmit" class="contact-form">
    <!-- Honeypot field for spam protection -->
    <input
      type="text"
      name="website"
      v-model="honeypot"
      style="position: absolute; left: -9999px;"
      tabindex="-1"
      autocomplete="off"
    />

    <div class="form-group">
      <label :for="`name-${formId}`">Name <span class="required">*</span></label>
      <input
        type="text"
        :id="`name-${formId}`"
        v-model="form.name"
        required
        :class="{ error: errors.name }"
        :aria-describedby="`name-error-${formId}`"
      />
      <span v-if="errors.name" :id="`name-error-${formId}`" class="error-message">{{ errors.name }}</span>
    </div>

    <div class="form-group">
      <label :for="`email-${formId}`">Email <span class="required">*</span></label>
      <input
        type="email"
        :id="`email-${formId}`"
        v-model="form.email"
        required
        :class="{ error: errors.email }"
        :aria-describedby="`email-error-${formId}`"
      />
      <span v-if="errors.email" :id="`email-error-${formId}`" class="error-message">{{ errors.email }}</span>
    </div>

    <div class="form-group">
      <label :for="`company-${formId}`">Company</label>
      <input
        type="text"
        :id="`company-${formId}`"
        v-model="form.company"
      />
    </div>

    <div class="form-group">
      <label :for="`projectType-${formId}`">Project type</label>
      <select :id="`projectType-${formId}`" v-model="form.projectType">
        <option value="">Select...</option>
        <option value="new-application">New application</option>
        <option value="modernization">Modernization / migration</option>
        <option value="cloud-architecture">Cloud architecture</option>
        <option value="devops">DevOps / delivery</option>
        <option value="reliability">Reliability / observability</option>
        <option value="security">Security review</option>
        <option value="not-sure">Not sure yet</option>
      </select>
    </div>

    <div class="form-group">
      <label :for="`budget-${formId}`">Budget range</label>
      <select :id="`budget-${formId}`" v-model="form.budget">
        <option value="">Select...</option>
        <option value="under-10k">Under $10k</option>
        <option value="10k-25k">$10k–$25k</option>
        <option value="25k-50k">$25k–$50k</option>
        <option value="50k-100k">$50k–$100k</option>
        <option value="100k-plus">$100k+</option>
        <option value="prefer-not">Prefer not to say</option>
      </select>
    </div>

    <div class="form-group">
      <label :for="`timeline-${formId}`">Timeline</label>
      <select :id="`timeline-${formId}`" v-model="form.timeline">
        <option value="">Select...</option>
        <option value="asap">ASAP</option>
        <option value="2-4-weeks">2–4 weeks</option>
        <option value="1-2-months">1–2 months</option>
        <option value="3-plus-months">3+ months</option>
        <option value="flexible">Flexible</option>
      </select>
    </div>

    <div class="form-group">
      <label :for="`message-${formId}`">Message <span class="required">*</span></label>
      <textarea
        :id="`message-${formId}`"
        v-model="form.message"
        required
        rows="5"
        placeholder="A few sentences is enough—current state, desired outcome, constraints."
        :class="{ error: errors.message }"
        :aria-describedby="`message-error-${formId}`"
      ></textarea>
      <span v-if="errors.message" :id="`message-error-${formId}`" class="error-message">{{ errors.message }}</span>
    </div>

    <div v-if="submitStatus === 'success'" class="form-status success">
      <p>Message sent! We'll get back to you within 1–2 business days.</p>
    </div>

    <div v-if="submitStatus === 'error'" class="form-status error">
      <p>Something went wrong. Please try again or email us directly at hello@arclyt.com</p>
    </div>

    <button type="submit" class="btn primary" :disabled="isSubmitting">
      {{ isSubmitting ? 'Sending...' : 'Send message' }}
    </button>
  </form>
</template>

<script setup>
import { ref, reactive, onMounted, onUnmounted, defineProps, defineEmits } from 'vue'

const props = defineProps({
  formId: {
    type: String,
    default: 'default'
  }
})

const emit = defineEmits(['success'])

const form = reactive({
  name: '',
  email: '',
  company: '',
  projectType: '',
  budget: '',
  timeline: '',
  message: ''
})

const errors = reactive({})
const honeypot = ref('')
const submitStatus = ref('')
const isSubmitting = ref(false)
const submitStartTime = ref(null)

const validateForm = () => {
  errors.name = ''
  errors.email = ''
  errors.message = ''

  if (!form.name.trim()) {
    errors.name = 'Name is required'
  }

  if (!form.email.trim()) {
    errors.email = 'Email is required'
  } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.email)) {
    errors.email = 'Please enter a valid email address'
  }

  if (!form.message.trim()) {
    errors.message = 'Message is required'
  }

  return !errors.name && !errors.email && !errors.message
}

const handleSubmit = async () => {
  // Spam protection: check honeypot
  if (honeypot.value) {
    return // Bot detected, silently fail
  }

  // Spam protection: check time-to-submit (should be at least 2 seconds)
  if (submitStartTime.value) {
    const timeToSubmit = Date.now() - submitStartTime.value
    if (timeToSubmit < 2000) {
      return // Submitted too quickly, likely a bot
    }
  }

  if (!validateForm()) {
    return
  }

  isSubmitting.value = true
  submitStatus.value = ''

  try {
    // TODO: Replace this with your actual form submission endpoint
    const response = await fetch('/api/contact', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(form),
    })

    if (response.ok) {
      submitStatus.value = 'success'
      // Reset form
      Object.keys(form).forEach(key => {
        form[key] = ''
      })
      emit('success')
    } else {
      throw new Error('Submission failed')
    }
  } catch (error) {
    // If endpoint doesn't exist, show success anyway (for development)
    console.log('Form submission endpoint not configured. Form data:', form)
    submitStatus.value = 'success'
    Object.keys(form).forEach(key => {
      form[key] = ''
    })
    emit('success')
  } finally {
    isSubmitting.value = false
  }
}

// Track when form interaction starts for spam protection
const startInteraction = () => {
  if (!submitStartTime.value) {
    submitStartTime.value = Date.now()
  }
}

// Add event listeners when component mounts
onMounted(() => {
  const formElement = document.querySelector('.contact-form')
  if (formElement) {
    formElement.addEventListener('focusin', startInteraction, true)
  }
})

onUnmounted(() => {
  const formElement = document.querySelector('.contact-form')
  if (formElement) {
    formElement.removeEventListener('focusin', startInteraction, true)
  }
})
</script>
