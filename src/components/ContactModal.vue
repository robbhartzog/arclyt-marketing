<template>
  <Teleport to="body">
    <Transition name="modal">
      <div
        v-if="isOpen"
        class="modal-overlay"
        role="dialog"
        aria-modal="true"
        :aria-labelledby="step === 'success' ? 'modal-title-success' : 'modal-title'"
        @click.self="close"
      >
        <div class="modal-container" :class="`modal--${step}`">

          <!-- ── Header ───────────────────────────────────────────── -->
          <div class="modal-header">
            <div class="modal-header-text">
              <p class="modal-eyebrow">Architecture Consultation</p>
              <h2 id="modal-title">Schedule a Strategy Call</h2>
              <p class="modal-subline">30 minutes &nbsp;·&nbsp; AWS Certified Engineer &nbsp;·&nbsp; No obligation</p>
            </div>

            <!-- Step indicator (hidden on success) -->
            <div v-if="step !== 'success'" class="modal-steps" aria-hidden="true">
              <button
                v-if="step === 'form'"
                :class="['modal-step', 'modal-step--back']"
                @click="step = 'calendar'"
                type="button"
                aria-label="Back to date and time"
              >
                <span class="step-dot"></span>Date &amp; Time
              </button>
              <span
                v-else
                :class="['modal-step', { active: step === 'calendar' }]"
              >
                <span class="step-dot"></span>Date &amp; Time
              </span>
              <span class="step-sep">›</span>
              <span :class="['modal-step', { active: step === 'form' }]">
                <span class="step-dot"></span>Details
              </span>
            </div>

            <button class="modal-close" @click="close" aria-label="Close">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none">
                <path d="M18 6L6 18M6 6L18 18" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
              </svg>
            </button>
          </div>

          <!-- ── Step: Calendar + Time Slots ─────────────────────── -->
          <div v-if="step === 'calendar'" class="modal-body modal-body--sched">

            <!-- Left: Calendar -->
            <div class="sched-panel sched-cal-panel">
              <div class="cal-nav">
                <button class="cal-nav-btn" @click="prevMonth" :disabled="isAtMinMonth" aria-label="Previous month">
                  <svg width="14" height="14" viewBox="0 0 16 16" fill="none">
                    <path d="M10 12L6 8L10 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
                  </svg>
                </button>
                <span class="cal-month-label">{{ monthLabel }}</span>
                <button class="cal-nav-btn" @click="nextMonth" :disabled="isAtMaxMonth" aria-label="Next month">
                  <svg width="14" height="14" viewBox="0 0 16 16" fill="none">
                    <path d="M6 4L10 8L6 12" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
                  </svg>
                </button>
              </div>

              <div class="cal-body">
                <div class="cal-grid">
                  <div class="cal-dow" v-for="d in DAYS_OF_WEEK" :key="d">{{ d }}</div>
                  <div v-for="n in firstDayOffset" :key="`blank-${n}`" class="cal-blank"></div>
                  <button
                    v-for="day in daysInMonth"
                    :key="day"
                    class="cal-day"
                    :class="{
                      'is-today':    isTodayFn(day),
                      'is-selected': isSelectedFn(day),
                    }"
                    :disabled="isPastFn(day) || isUnavailableFn(day)"
                    :aria-label="`${day} ${monthLabel}`"
                    :aria-pressed="isSelectedFn(day)"
                    @click="selectDate(day)"
                  >{{ day }}</button>
                </div>

                <div v-if="availabilityLoading" class="cal-loading-overlay" aria-label="Loading available dates">
                  <span class="cal-spinner"></span>
                </div>
              </div>

              <p class="cal-legend" :class="{ 'cal-legend--error': availabilityError }">
                <template v-if="availabilityError">Could not load live availability &nbsp;·&nbsp; Showing weekdays</template>
                <template v-else-if="availabilityLoading">Loading availability…</template>
                <template v-else>Select an available date &nbsp;·&nbsp; {{ userTzAbbr }}</template>
              </p>
            </div>

            <!-- Right: Time Slots -->
            <div class="sched-panel sched-slots-panel">
              <!-- No date selected -->
              <div v-if="!selectedDate" class="slots-empty-state">
                <svg width="36" height="36" viewBox="0 0 48 48" fill="none" class="slots-empty-icon">
                  <rect x="8" y="12" width="32" height="28" rx="3" stroke="currentColor" stroke-width="1.5"/>
                  <path d="M8 20H40" stroke="currentColor" stroke-width="1.5"/>
                  <path d="M16 8V14M32 8V14" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
                  <circle cx="17" cy="30" r="1.5" fill="currentColor"/>
                  <circle cx="24" cy="30" r="1.5" fill="currentColor"/>
                  <circle cx="31" cy="30" r="1.5" fill="currentColor"/>
                </svg>
                <p>Choose a date to see available times.</p>
              </div>

              <template v-else>
                <div class="slots-header">
                  <span class="slots-date">{{ selectedDateLabel }}</span>
                  <span class="slots-tz">{{ userTzAbbr }}</span>
                </div>

                <div v-if="slotsLoading" class="slots-loading">
                  <span class="cal-spinner"></span>
                  <span class="slots-loading-label">Loading times…</span>
                </div>

                <div v-else-if="availableSlots.length === 0" class="slots-empty-state">
                  <p>No times available on this date.<br>Please pick another day.</p>
                </div>

                <div v-else class="slots-grid">
                  <button
                    v-for="slot in availableSlots"
                    :key="slot"
                    class="slot-pill"
                    :class="{ 'is-selected': selectedTime === slot }"
                    @click="selectTime(slot)"
                  >{{ displaySlot(slot) }}</button>
                </div>

                <p v-if="slotsError" class="slots-error-note">Could not load live times — showing default slots</p>
              </template>
            </div>
          </div>

          <!-- ── Step: Contact Details Form ──────────────────────── -->
          <div v-else-if="step === 'form'" class="modal-body modal-body--form">

            <!-- Booking summary bar -->
            <div class="booking-bar">
              <div class="booking-bar-info">
                <svg width="13" height="13" viewBox="0 0 16 16" fill="none">
                  <rect x="2" y="3" width="12" height="11" rx="2" stroke="currentColor" stroke-width="1.5"/>
                  <path d="M2 7H14" stroke="currentColor" stroke-width="1.5"/>
                  <path d="M5 1V4M11 1V4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
                </svg>
                <span>{{ selectedDateLabel }} &nbsp;·&nbsp; {{ displaySlot(selectedTime) }} {{ userTzAbbr }}</span>
              </div>
              <button class="change-btn" @click="backToCalendar">Change</button>
            </div>

            <!-- Form -->
            <form @submit.prevent="handleSubmit" class="booking-form">
              <div class="form-row">
                <div class="form-group">
                  <label>Name <span class="required">*</span></label>
                  <input type="text" v-model="form.name" :class="{ error: formErrors.name }" autocomplete="name" />
                  <span v-if="formErrors.name" class="error-message">{{ formErrors.name }}</span>
                </div>
                <div class="form-group">
                  <label>Email <span class="required">*</span></label>
                  <input type="email" v-model="form.email" :class="{ error: formErrors.email }" autocomplete="email" />
                  <span v-if="formErrors.email" class="error-message">{{ formErrors.email }}</span>
                </div>
              </div>

              <div class="form-row">
                <div class="form-group">
                  <label>Company</label>
                  <input type="text" v-model="form.company" autocomplete="organization" />
                </div>
                <div class="form-group">
                  <label>Current Tech Stack</label>
                  <input
                    type="text"
                    v-model="form.techStack"
                    placeholder="e.g., ColdFusion 2018, on-prem Oracle DB"
                    autocomplete="off"
                  />
                </div>
              </div>

              <div class="form-group">
                <label>Additional Comments</label>
                <textarea
                  v-model="form.comments"
                  rows="3"
                  placeholder="Anything else you'd like us to know before the call"
                  autocomplete="off"
                  class="form-textarea"
                ></textarea>
              </div>

              <div v-if="submitStatus === 'error'" class="form-status-error">
                Something went wrong. Email us at <a href="mailto:connect@arclyt.io">connect@arclyt.io</a>
              </div>

              <button type="submit" class="confirm-btn" :disabled="isSubmitting">
                <svg v-if="isSubmitting" class="spinner-icon" width="14" height="14" viewBox="0 0 24 24" fill="none">
                  <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2.5" stroke-dasharray="31.4" stroke-dashoffset="10" stroke-linecap="round"/>
                </svg>
                {{ isSubmitting ? 'Confirming…' : 'Confirm Strategy Call' }}
              </button>
            </form>

            <p class="form-footer-note">
              30 minutes &nbsp;·&nbsp; AWS Certified Engineer &nbsp;·&nbsp; No obligation<br>
              <a href="mailto:connect@arclyt.io">connect@arclyt.io</a> &nbsp;·&nbsp; NDA available on request
            </p>
          </div>

          <!-- ── Step: Success ────────────────────────────────────── -->
          <div v-else-if="step === 'success'" class="modal-body modal-body--success">
            <div class="success-check">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none">
                <path d="M5 13l4 4L19 7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </div>
            <h3 id="modal-title-success">You're confirmed.</h3>
            <p class="success-slot">{{ selectedDateLabel }} &nbsp;·&nbsp; {{ displaySlot(selectedTime) }} {{ userTzAbbr }}</p>
            <p class="success-sub">
              A confirmation will be sent to <strong>{{ form.email }}</strong>.<br>
              We look forward to speaking with you.
            </p>
            <button class="ghost-btn" @click="close">Done</button>
          </div>

        </div>
      </div>
    </Transition>
  </Teleport>
</template>

<script setup>
import { ref, reactive, computed, watch, onMounted, onUnmounted } from 'vue'
import { event } from 'vue-gtag'

// ── Props / emits ──────────────────────────────────────────────────
const props = defineProps({ isOpen: { type: Boolean, default: false } })
const emit  = defineEmits(['close'])

// ── API config ─────────────────────────────────────────────────────
const SCHEDULE_BASE = import.meta.env.VITE_SCHEDULE_BASE_URL
const TENANT_ID     = import.meta.env.VITE_SCHEDULE_TENANT_ID

// ── Calendar constants ──────────────────────────────────────────────
const DAYS_OF_WEEK = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']
const MONTHS = [
  'January','February','March','April','May','June',
  'July','August','September','October','November','December',
]
const FALLBACK_SLOTS = [
  '9:00 AM','10:00 AM','11:00 AM','12:00 PM',
  '1:00 PM','2:00 PM','3:00 PM','4:00 PM',
]

// ── Step state ─────────────────────────────────────────────────────
const step = ref('calendar') // 'calendar' | 'form' | 'success'

// ── Availability state ──────────────────────────────────────────────
const availableDates      = ref(new Set())
const availabilityLoading = ref(false)
const availabilityError   = ref(false)

// ── Slots state ─────────────────────────────────────────────────────
const availableSlots = ref([])
const slotsLoading   = ref(false)
const slotsError     = ref(false)

// ── Calendar state ──────────────────────────────────────────────────
const today        = new Date()
const currentMonth = ref(today.getMonth())
const currentYear  = ref(today.getFullYear())
const selectedDate = ref(null)
const selectedTime = ref('')

// ── Form state ──────────────────────────────────────────────────────
const form = reactive({ name: '', email: '', company: '', techStack: '', comments: '' })
const formErrors  = reactive({ name: '', email: '' })
const isSubmitting = ref(false)
const submitStatus  = ref('')

// ── Calendar computed ───────────────────────────────────────────────
const monthLabel = computed(() => `${MONTHS[currentMonth.value]} ${currentYear.value}`)

const firstDayOffset = computed(() =>
  new Date(currentYear.value, currentMonth.value, 1).getDay()
)
const daysInMonth = computed(() =>
  new Date(currentYear.value, currentMonth.value + 1, 0).getDate()
)
const isAtMinMonth = computed(() =>
  currentYear.value === today.getFullYear() && currentMonth.value === today.getMonth()
)
const maxDate = new Date(today.getFullYear(), today.getMonth() + 3, 1)
const isAtMaxMonth = computed(() =>
  currentYear.value > maxDate.getFullYear() ||
  (currentYear.value === maxDate.getFullYear() && currentMonth.value >= maxDate.getMonth())
)
const selectedDateLabel = computed(() => {
  if (!selectedDate.value) return ''
  return selectedDate.value.toLocaleDateString('en-US', {
    weekday: 'long', month: 'long', day: 'numeric',
  })
})
const selectedISODate = computed(() => {
  if (!selectedDate.value) return ''
  const d = selectedDate.value
  return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`
})

// ── Day helpers ─────────────────────────────────────────────────────
const dateFor = (day) => new Date(currentYear.value, currentMonth.value, day)

const isTodayFn = (day) => {
  const d = dateFor(day)
  return d.getDate() === today.getDate() &&
         d.getMonth() === today.getMonth() &&
         d.getFullYear() === today.getFullYear()
}
const isSelectedFn = (day) =>
  !!selectedDate.value && dateFor(day).getTime() === selectedDate.value.getTime()

const isPastFn = (day) => {
  const d = dateFor(day)
  const cutoff = new Date(today)
  cutoff.setHours(0, 0, 0, 0)
  return d <= cutoff
}
const isWeekendFn = (day) => { const dow = dateFor(day).getDay(); return dow === 0 || dow === 6 }

const toISODate = (day) => {
  const d = dateFor(day)
  const y = d.getFullYear()
  const m = String(d.getMonth() + 1).padStart(2, '0')
  const dd = String(d.getDate()).padStart(2, '0')
  return `${y}-${m}-${dd}`
}

const isUnavailableFn = (day) => {
  if (availabilityLoading.value || availabilityError.value) return isWeekendFn(day)
  return !availableDates.value.has(toISODate(day))
}

const to12h = (t) => {
  if (!t || /AM|PM/i.test(t)) return t
  const [h, m] = t.split(':').map(Number)
  const period = h >= 12 ? 'PM' : 'AM'
  return `${h % 12 || 12}:${String(m).padStart(2, '0')} ${period}`
}

// ── Timezone helpers ─────────────────────────────────────────────────

/** User's local timezone abbreviation, e.g. "CST", "PST", "GMT+1" */
const userTzAbbr = new Intl.DateTimeFormat('en-US', { timeZoneName: 'short' })
  .formatToParts(new Date())
  .find(p => p.type === 'timeZoneName')?.value ?? 'Local'

/**
 * Converts an EST slot string ("10:00 AM") on a given ISO date to the
 * user's local time string ("11:00 AM" for CT, "8:00 AM" for PT, etc.).
 * Slots are always in America/New_York (handles EST/EDT automatically).
 */
const estToLocal = (isoDate, estSlot) => {
  if (!isoDate || !estSlot) return estSlot
  // Parse EST time to 24h
  const match = estSlot.match(/(\d+):(\d+)\s*(AM|PM)?/i)
  if (!match) return estSlot
  let h = Number(match[1])
  const m = Number(match[2])
  const period = match[3]?.toUpperCase()
  if (period === 'PM' && h !== 12) h += 12
  if (period === 'AM' && h === 12) h = 0

  // Find New York UTC offset for this date (handles DST automatically)
  const [yr, mo, dy] = isoDate.split('-').map(Number)
  const probe = new Date(Date.UTC(yr, (mo ?? 1) - 1, dy ?? 1, 12)) // noon UTC
  const nyOffset = new Intl.DateTimeFormat('en-US', {
    timeZone: 'America/New_York', timeZoneName: 'longOffset',
  }).formatToParts(probe).find(p => p.type === 'timeZoneName')?.value ?? 'GMT-05:00'
  const offsetMatch = nyOffset.match(/GMT([+-])(\d+):(\d+)/)
  const sign = offsetMatch?.[1] === '+' ? 1 : -1
  const offsetMin = sign * ((Number(offsetMatch?.[2] ?? 5)) * 60 + Number(offsetMatch?.[3] ?? 0))

  // Convert NY local → UTC → user local
  const utcMin = h * 60 + m - offsetMin
  const utcDate = new Date(Date.UTC(yr, (mo ?? 1) - 1, dy ?? 1, 0, utcMin))
  return utcDate.toLocaleTimeString('en-US', { hour: 'numeric', minute: '2-digit', hour12: true })
}

/** Display label for a stored EST slot in the user's local time */
const displaySlot = (estSlot) => estToLocal(selectedISODate.value, estSlot)

// ── Data fetchers ────────────────────────────────────────────────────

/** Selects the earliest available date strictly after today if none is selected yet. */
const autoSelectFirstDate = () => {
  if (selectedDate.value || availableDates.value.size === 0) return

  // Compute today's midnight fresh on every call to avoid stale closures
  const now = new Date()
  now.setHours(0, 0, 0, 0)

  // Sort the available date strings and find the first one whose Date is > today
  const sorted = [...availableDates.value].sort()
  const first = sorted.find(iso => {
    const [y, m, d] = iso.split('-').map(Number)
    const candidate = new Date(y, (m ?? 1) - 1, d ?? 1)
    return candidate > now          // strictly after today's midnight
  })
  if (!first) return

  const [y, m, d] = first.split('-').map(Number)
  selectedDate.value = new Date(y, (m ?? 1) - 1, d ?? 1)
  currentMonth.value = (m ?? 1) - 1
  currentYear.value  = y ?? today.getFullYear()
  fetchSlots(first)
}

const fetchAvailability = async () => {
  if (!SCHEDULE_BASE || !TENANT_ID) { availabilityLoading.value = false; return }
  availabilityLoading.value = true
  availabilityError.value   = false
  try {
    const res = await fetch(
      `${SCHEDULE_BASE}/public/scheduling/dates?tenantId=${TENANT_ID}&days=90`
    )
    if (!res.ok) throw new Error()
    const data = await res.json()
    availableDates.value = new Set(data.availableDates ?? [])
    autoSelectFirstDate()
  } catch {
    availabilityError.value = true
  } finally {
    availabilityLoading.value = false
  }
}

const fetchSlots = async (isoDate) => {
  if (!SCHEDULE_BASE || !TENANT_ID) return
  slotsLoading.value = true
  slotsError.value   = false
  availableSlots.value = []
  try {
    const res = await fetch(
      `${SCHEDULE_BASE}/public/scheduling/availability?tenantId=${TENANT_ID}&date=${isoDate}`
    )
    if (!res.ok) throw new Error()
    const data = await res.json()
    const raw = data.slots ?? data.availableSlots ?? []
    availableSlots.value = raw.map(s => typeof s === 'string' ? to12h(s) : to12h(s.startTime))
  } catch {
    slotsError.value = true
    availableSlots.value = FALLBACK_SLOTS
  } finally {
    slotsLoading.value = false
  }
}

// ── Navigation ───────────────────────────────────────────────────────
const prevMonth = () => {
  if (isAtMinMonth.value) return
  if (currentMonth.value === 0) { currentMonth.value = 11; currentYear.value-- }
  else { currentMonth.value-- }
}
const nextMonth = () => {
  if (isAtMaxMonth.value) return
  if (currentMonth.value === 11) { currentMonth.value = 0; currentYear.value++ }
  else { currentMonth.value++ }
}

// ── Selection ────────────────────────────────────────────────────────
const selectDate = (day) => {
  selectedDate.value = dateFor(day)
  selectedTime.value = ''
  fetchSlots(toISODate(day))
}
const selectTime = (slot) => {
  selectedTime.value = slot
  step.value = 'form'
}
const backToCalendar = () => {
  selectedTime.value = ''
  step.value = 'calendar'
}

// ── Form validation & submit ─────────────────────────────────────────
const validate = () => {
  formErrors.name  = form.name.trim()  ? '' : 'Name is required'
  formErrors.email = !form.email.trim() ? 'Email is required'
    : !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.email) ? 'Enter a valid email'
    : ''
  return !formErrors.name && !formErrors.email
}

const handleSubmit = async () => {
  if (!validate()) return
  isSubmitting.value = true
  submitStatus.value = ''
  try {
    if (!SCHEDULE_BASE || !TENANT_ID) throw new Error('API not configured')
    const res = await fetch(
      `${SCHEDULE_BASE}/public/scheduling/bookings?tenantId=${TENANT_ID}`,
      {
        method:  'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          name:          form.name,
          email:         form.email,
          company:       form.company   || undefined,
          techStack:     form.techStack || undefined,
          comments:      form.comments  || undefined,
          scheduledDate: selectedISODate.value,
          scheduledTime: selectedTime.value,
        }),
      }
    )
    if (!res.ok) throw new Error()
    event('form_submission', { form_name: 'strategy_call_booking' })
    step.value = 'success'
  } catch {
    submitStatus.value = 'error'
  } finally {
    isSubmitting.value = false
  }
}

// ── Reset ─────────────────────────────────────────────────────────────
const reset = () => {
  step.value         = 'calendar'
  selectedDate.value = null
  selectedTime.value = ''
  availableSlots.value = []
  submitStatus.value   = ''
  Object.keys(form).forEach(k => { form[k] = '' })
  Object.keys(formErrors).forEach(k => { formErrors[k] = '' })
  // Reset to current month
  currentMonth.value = today.getMonth()
  currentYear.value  = today.getFullYear()
}

// ── Open / close ─────────────────────────────────────────────────────
const close = () => emit('close')

const handleEscape = (e) => { if (e.key === 'Escape' && props.isOpen) close() }

watch(() => props.isOpen, (open) => {
  if (open) {
    event('modal_open', { modal_name: 'strategy_call' })
    document.addEventListener('keydown', handleEscape)
    document.body.style.overflow = 'hidden'
    // Fetch availability when modal first opens (if not yet loaded)
    if (availableDates.value.size === 0 && !availabilityLoading.value) {
      fetchAvailability()
    } else {
      // Availability already cached — auto-select first date on re-open
      autoSelectFirstDate()
    }
  } else {
    document.removeEventListener('keydown', handleEscape)
    document.body.style.overflow = ''
    // Wait for close animation then reset
    setTimeout(reset, 220)
  }
})

onMounted(() => {
  if (props.isOpen) {
    document.addEventListener('keydown', handleEscape)
    document.body.style.overflow = 'hidden'
  }
})
onUnmounted(() => {
  document.removeEventListener('keydown', handleEscape)
  document.body.style.overflow = ''
})
</script>

<style scoped>
/* ── Overlay ───────────────────────────────────────────────────────── */
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.80);
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
  z-index: 1000;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  padding: 32px 16px;
  overflow-y: auto;
}

/* ── Container ─────────────────────────────────────────────────────── */
.modal-container {
  background: #0d1117;
  border: 1px solid rgba(255, 255, 255, 0.10);
  border-radius: 14px;
  box-shadow: 0 32px 80px rgba(0, 0, 0, 0.70), 0 0 0 1px rgba(255, 255, 255, 0.04) inset;
  width: 100%;
  max-width: 860px;
  /* Reset the global main.css min-height: calc(100vh - 48px) rule,
     then pin height to content only. */
  min-height: 0;
  height: fit-content;
  max-height: calc(100vh - 64px);
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  align-self: flex-start;
}

/* ── Header ────────────────────────────────────────────────────────── */
.modal-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  padding: 22px 28px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.07);
}

.modal-header-text {
  flex: 1;
  min-width: 0;
}

.modal-eyebrow {
  margin: 0 0 4px;
  font-size: 0.70rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: rgba(255, 255, 255, 0.35);
  font-weight: 500;
}

.modal-header h2 {
  margin: 0;
  font-size: 1.05rem;
  font-weight: 600;
  color: var(--text);
  letter-spacing: 0.01em;
}

.modal-subline {
  margin: 4px 0 0;
  font-size: 0.72rem;
  color: rgba(255, 255, 255, 0.28);
  letter-spacing: 0.03em;
}

/* Step indicator */
.modal-steps {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-shrink: 0;
}

.modal-step {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 0.72rem;
  color: rgba(255, 255, 255, 0.22);
  transition: color 0.2s ease;
  white-space: nowrap;
}
.modal-step.active { color: rgba(255, 255, 255, 0.75); }
.modal-step.done   { color: rgba(255, 255, 255, 0.40); }

.modal-step--back {
  background: none;
  border: none;
  padding: 0;
  cursor: pointer;
  color: rgba(255, 255, 255, 0.40);
}
.modal-step--back:hover {
  color: rgba(255, 255, 255, 0.75);
}
.modal-step--back:hover .step-dot {
  background: rgba(255, 255, 255, 0.75);
}

.step-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: currentColor;
  flex-shrink: 0;
}
.modal-step.active .step-dot { background: rgba(255, 255, 255, 0.80); }
.modal-step.done   .step-dot { background: rgba(255, 255, 255, 0.40); }

.step-sep {
  color: rgba(255, 255, 255, 0.14);
  font-size: 0.68rem;
}

.modal-close {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 30px;
  height: 30px;
  border-radius: 6px;
  border: 1px solid rgba(255, 255, 255, 0.08);
  background: transparent;
  color: rgba(255, 255, 255, 0.35);
  cursor: pointer;
  transition: color 0.15s ease, background 0.15s ease, border-color 0.15s ease;
  flex-shrink: 0;
}
.modal-close:hover {
  color: rgba(255, 255, 255, 0.80);
  background: rgba(255, 255, 255, 0.05);
  border-color: rgba(255, 255, 255, 0.16);
}

/* ── Body layouts ──────────────────────────────────────────────────── */
.modal-body { padding: 0; }

/* Calendar step: 2-column */
.modal-body--sched {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 0;
}
@media (max-width: 680px) {
  .modal-body--sched { grid-template-columns: 1fr; }
}

/* Form step: single column */
.modal-body--form {
  padding: 24px 28px 28px;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

/* Success step */
.modal-body--success {
  padding: 56px 28px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: 14px;
}

/* ── Scheduler panels ──────────────────────────────────────────────── */
.sched-panel {
  padding: 24px;
}

.sched-cal-panel {
  min-width: 272px;
  border-right: 1px solid rgba(255, 255, 255, 0.07);
}

@media (max-width: 680px) {
  .sched-cal-panel {
    border-right: none;
    border-bottom: 1px solid rgba(255, 255, 255, 0.07);
  }
}

.sched-slots-panel {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

/* ── Calendar ──────────────────────────────────────────────────────── */
.cal-nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
}

.cal-month-label {
  font-size: 0.82rem;
  font-weight: 600;
  color: var(--text);
  letter-spacing: 0.02em;
}

.cal-nav-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 26px;
  height: 26px;
  border-radius: 5px;
  border: 1px solid rgba(255, 255, 255, 0.08);
  background: transparent;
  color: rgba(255, 255, 255, 0.35);
  cursor: pointer;
  transition: background 0.15s, border-color 0.15s, color 0.15s;
}
.cal-nav-btn:hover:not(:disabled) {
  background: rgba(255, 255, 255, 0.06);
  border-color: rgba(255, 255, 255, 0.20);
  color: var(--text);
}
.cal-nav-btn:disabled {
  opacity: 0.25;
  cursor: not-allowed;
}

.cal-body { position: relative; }

.cal-grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 2px;
}

.cal-dow {
  text-align: center;
  font-size: 0.62rem;
  font-weight: 500;
  letter-spacing: 0.06em;
  color: rgba(255, 255, 255, 0.22);
  text-transform: uppercase;
  padding-bottom: 8px;
}

.cal-day {
  aspect-ratio: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 6px;
  border: 1px solid transparent;
  background: transparent;
  color: rgba(255, 255, 255, 0.70);
  font-size: 0.78rem;
  cursor: pointer;
  transition: background 0.12s, border-color 0.12s, color 0.12s;
}
.cal-day:hover:not(:disabled) {
  background: rgba(255, 255, 255, 0.06);
  border-color: rgba(255, 255, 255, 0.18);
  color: var(--text);
}
.cal-day.is-today {
  border-color: rgba(255, 255, 255, 0.22);
  color: var(--text);
}
.cal-day.is-selected {
  background: rgba(255, 255, 255, 0.92);
  border-color: rgba(255, 255, 255, 0.92);
  color: #0d1117;
  font-weight: 600;
}
.cal-day:disabled {
  color: rgba(255, 255, 255, 0.14);
  cursor: not-allowed;
  background: transparent;
  border-color: transparent;
}

.cal-loading-overlay {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(13, 17, 23, 0.65);
  border-radius: 6px;
}

.cal-spinner {
  width: 18px;
  height: 18px;
  border: 1.5px solid rgba(255, 255, 255, 0.10);
  border-top-color: rgba(255, 255, 255, 0.55);
  border-radius: 50%;
  animation: spin 0.7s linear infinite;
}

@keyframes spin { to { transform: rotate(360deg); } }

.cal-legend {
  margin: 12px 0 0;
  font-size: 0.68rem;
  color: rgba(255, 255, 255, 0.22);
  letter-spacing: 0.04em;
  text-align: center;
}
.cal-legend--error { color: rgba(255, 120, 120, 0.50); }

/* ── Slots panel ───────────────────────────────────────────────────── */
.slots-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
}

.slots-date {
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--text);
}

.slots-tz {
  font-size: 0.68rem;
  font-family: var(--mono);
  color: rgba(255, 255, 255, 0.28);
  letter-spacing: 0.06em;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.07);
  border-radius: 4px;
  padding: 2px 6px;
}

.slots-loading {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  padding: 48px 0;
}
.slots-loading-label {
  font-size: 0.78rem;
  color: rgba(255, 255, 255, 0.32);
}

.slots-empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 40px 16px;
  text-align: center;
  gap: 12px;
}
.slots-empty-icon { color: rgba(255, 255, 255, 0.12); }
.slots-empty-state p {
  margin: 0;
  font-size: 0.82rem;
  color: rgba(255, 255, 255, 0.28);
  line-height: 1.65;
}

.slots-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 7px;
}

.slot-pill {
  padding: 9px 10px;
  border-radius: 7px;
  border: 1px solid rgba(255, 255, 255, 0.12);
  background: transparent;
  color: rgba(255, 255, 255, 0.55);
  font-family: var(--mono);
  font-size: 0.78rem;
  cursor: pointer;
  transition: background 0.12s, border-color 0.12s, color 0.12s;
  text-align: center;
  letter-spacing: 0.02em;
}
.slot-pill:hover {
  background: rgba(255, 255, 255, 0.05);
  border-color: rgba(255, 255, 255, 0.30);
  color: var(--text);
}
.slot-pill.is-selected {
  background: rgba(255, 255, 255, 0.10);
  border-color: rgba(255, 255, 255, 0.55);
  color: var(--text);
  font-weight: 500;
}

.slots-error-note {
  margin: 8px 0 0;
  font-size: 0.68rem;
  color: rgba(255, 120, 120, 0.45);
  text-align: center;
}

/* ── Form step ─────────────────────────────────────────────────────── */
.booking-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding: 10px 14px;
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.10);
  background: rgba(255, 255, 255, 0.03);
}
.booking-bar-info {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.82rem;
  color: rgba(255, 255, 255, 0.60);
}
.booking-bar-info svg { color: rgba(255, 255, 255, 0.28); flex-shrink: 0; }
.change-btn {
  background: transparent;
  border: none;
  color: rgba(255, 255, 255, 0.40);
  font-size: 0.75rem;
  cursor: pointer;
  padding: 3px 8px;
  border-radius: 4px;
  transition: color 0.15s, background 0.15s;
  white-space: nowrap;
}
.change-btn:hover { color: var(--text); background: rgba(255, 255, 255, 0.05); }

.booking-form {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}
@media (max-width: 560px) {
  .form-row { grid-template-columns: 1fr; }
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 5px;
}
.form-group label {
  font-size: 0.80rem;
  font-weight: 500;
  color: rgba(255, 255, 255, 0.55);
  letter-spacing: 0.03em;
}
.required { color: rgba(255, 255, 255, 0.25); }

.form-group input {
  padding: 9px 11px;
  border: 1px solid rgba(255, 255, 255, 0.10);
  border-radius: 7px;
  background: rgba(255, 255, 255, 0.03);
  color: var(--text);
  font-family: var(--sans);
  font-size: 0.875rem;
  transition: border-color 0.15s, background 0.15s;
}
.form-group input:focus {
  outline: none;
  border-color: rgba(255, 255, 255, 0.30);
  background: rgba(255, 255, 255, 0.05);
}
.form-group input.error { border-color: rgba(255, 100, 100, 0.50); }

.form-textarea {
  padding: 9px 11px;
  border: 1px solid rgba(255, 255, 255, 0.10);
  border-radius: 7px;
  background: rgba(255, 255, 255, 0.03);
  color: var(--text);
  font-family: var(--sans);
  font-size: 0.875rem;
  line-height: 1.55;
  resize: vertical;
  transition: border-color 0.15s, background 0.15s;
}
.form-textarea:focus {
  outline: none;
  border-color: rgba(255, 255, 255, 0.30);
  background: rgba(255, 255, 255, 0.05);
}
.form-textarea::placeholder { color: rgba(255, 255, 255, 0.20); }

.error-message {
  font-size: 0.75rem;
  color: rgba(255, 110, 110, 0.75);
}

.form-status-error {
  font-size: 0.82rem;
  color: rgba(255, 130, 130, 0.75);
  padding: 10px 14px;
  border-radius: 7px;
  border: 1px solid rgba(255, 100, 100, 0.20);
  background: rgba(255, 100, 100, 0.05);
  line-height: 1.5;
}
.form-status-error a { color: rgba(255, 160, 160, 0.85); }

/* Ghost confirm button */
.confirm-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  width: 100%;
  padding: 13px 20px;
  margin-top: 4px;
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.22);
  background: rgba(255, 255, 255, 0.03);
  color: rgba(255, 255, 255, 0.80);
  font-size: 0.92rem;
  font-weight: 500;
  letter-spacing: 0.02em;
  cursor: pointer;
  transition: border-color 0.2s, background 0.2s, color 0.2s;
}
.confirm-btn:hover:not(:disabled) {
  border-color: rgba(255, 255, 255, 0.55);
  background: rgba(255, 255, 255, 0.07);
  color: var(--text);
}
.confirm-btn:disabled {
  opacity: 0.40;
  cursor: not-allowed;
}

.spinner-icon { animation: spin 0.8s linear infinite; flex-shrink: 0; }

.form-footer-note {
  margin: 0;
  font-size: 0.72rem;
  color: rgba(255, 255, 255, 0.22);
  text-align: center;
  line-height: 1.7;
  letter-spacing: 0.02em;
}
.form-footer-note a { color: rgba(255, 255, 255, 0.32); text-decoration: none; }
.form-footer-note a:hover { color: rgba(255, 255, 255, 0.55); }

/* ── Success step ──────────────────────────────────────────────────── */
.success-check {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  border: 1px solid rgba(255, 255, 255, 0.18);
  background: rgba(255, 255, 255, 0.05);
  display: flex;
  align-items: center;
  justify-content: center;
  color: rgba(255, 255, 255, 0.75);
  margin-bottom: 6px;
}
.modal-body--success h3 {
  margin: 0;
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--text);
}
.success-slot {
  margin: 0;
  display: inline-block;
  padding: 5px 14px;
  border-radius: 99px;
  border: 1px solid rgba(255, 255, 255, 0.14);
  background: rgba(255, 255, 255, 0.04);
  font-size: 0.82rem;
  font-family: var(--mono);
  color: rgba(255, 255, 255, 0.55);
}
.success-sub {
  margin: 0;
  font-size: 0.875rem;
  color: rgba(255, 255, 255, 0.38);
  max-width: 36ch;
  line-height: 1.65;
}
.success-sub strong { color: rgba(255, 255, 255, 0.65); }

/* Ghost done button */
.ghost-btn {
  margin-top: 10px;
  background: transparent;
  border: 1px solid rgba(255, 255, 255, 0.16);
  color: rgba(255, 255, 255, 0.45);
  padding: 8px 24px;
  border-radius: 7px;
  font-size: 0.85rem;
  cursor: pointer;
  transition: border-color 0.2s, color 0.2s, background 0.2s;
}
.ghost-btn:hover {
  border-color: rgba(255, 255, 255, 0.35);
  color: rgba(255, 255, 255, 0.75);
  background: rgba(255, 255, 255, 0.04);
}

/* ── Modal transitions ─────────────────────────────────────────────── */
.modal-enter-active, .modal-leave-active {
  transition: opacity 0.2s ease;
}
.modal-enter-active .modal-container,
.modal-leave-active .modal-container {
  transition: transform 0.2s ease, opacity 0.2s ease;
}
.modal-enter-from, .modal-leave-to { opacity: 0; }
.modal-enter-from .modal-container,
.modal-leave-to .modal-container { transform: translateY(12px) scale(0.97); opacity: 0; }
</style>
