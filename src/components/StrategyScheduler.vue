<template>
  <section>
    <div class="wrap">

      <div class="section-head">
        <div>
          <p class="sched-eyebrow">Architecture Consultation</p>
          <h2>Schedule a Strategy Call</h2>
        </div>
        <p class="section-microline">30 minutes &middot; AWS Certified Engineer &middot; No obligation</p>
      </div>

      <!-- ── Success screen ── -->
      <div v-if="step === 'success'" class="sched-success">
        <div class="success-check">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
            <path d="M5 13l4 4L19 7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </div>
        <h3>You're confirmed</h3>
        <p class="success-slot-label">{{ selectedDateLabel }} &nbsp;&middot;&nbsp; {{ selectedTime }} EST</p>
        <p class="success-sub">
          A confirmation will be sent to <strong>{{ form.email }}</strong>.<br>
          We look forward to speaking with you.
        </p>
        <button class="sched-ghost-btn" @click="reset">Book another time</button>
      </div>

      <!-- ── Main scheduler layout ── -->
      <div v-else class="sched-layout">

        <!-- Left: Calendar -->
        <div class="sched-panel sched-cal-panel">
          <div class="cal-nav">
            <button class="cal-nav-btn" @click="prevMonth" :disabled="isAtMinMonth" aria-label="Previous month">
              <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
                <path d="M10 12L6 8L10 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </button>
            <span class="cal-month-label">{{ monthLabel }}</span>
            <button class="cal-nav-btn" @click="nextMonth" :disabled="isAtMaxMonth" aria-label="Next month">
              <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
                <path d="M6 4L10 8L6 12" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </button>
          </div>

          <div class="cal-body">
            <div class="cal-grid">
              <div class="cal-dow" v-for="d in DAYS_OF_WEEK" :key="d">{{ d }}</div>
              <div v-for="n in firstDayOffset" :key="`blank-${n}`" class="cal-blank" aria-hidden="true"></div>
              <button
                v-for="day in daysInMonth"
                :key="day"
                class="cal-day"
                :class="{
                  'is-today': isTodayFn(day),
                  'is-selected': isSelectedFn(day),
                }"
                :disabled="isPastFn(day) || isUnavailableFn(day)"
                :aria-label="`${day} ${monthLabel}`"
                :aria-pressed="isSelectedFn(day)"
                @click="selectDate(day)"
              >{{ day }}</button>
            </div>

            <!-- Loading overlay -->
            <div v-if="availabilityLoading" class="cal-loading-overlay" aria-label="Loading available dates">
              <span class="cal-spinner"></span>
            </div>
          </div>

          <p v-if="availabilityError" class="cal-legend cal-legend--error">
            Could not load availability &nbsp;&middot;&nbsp; Showing weekdays
          </p>
          <p v-else class="cal-legend">
            {{ availabilityLoading ? 'Loading availability…' : 'Select an available date' }}
            &nbsp;&middot;&nbsp; EST
          </p>
        </div>

        <!-- Right: Time slots or Form -->
        <div class="sched-panel sched-right-panel">

          <!-- Step indicator -->
          <div class="sched-steps" aria-hidden="true">
            <span :class="['sched-step', { active: !selectedDate, done: !!selectedDate }]">
              <span class="step-num">1</span>Date
            </span>
            <span class="step-sep">›</span>
            <span :class="['sched-step', { active: !!selectedDate && step === 'calendar', done: !!selectedTime }]">
              <span class="step-num">2</span>Time
            </span>
            <span class="step-sep">›</span>
            <span :class="['sched-step', { active: step === 'form' }]">
              <span class="step-num">3</span>Details
            </span>
          </div>

          <!-- No date selected -->
          <div v-if="!selectedDate" class="sched-empty">
            <svg width="44" height="44" viewBox="0 0 48 48" fill="none" class="empty-icon">
              <rect x="8" y="12" width="32" height="28" rx="3" stroke="currentColor" stroke-width="1.5"/>
              <path d="M8 20H40" stroke="currentColor" stroke-width="1.5"/>
              <path d="M16 8V14M32 8V14" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
              <circle cx="17" cy="30" r="1.5" fill="currentColor"/>
              <circle cx="24" cy="30" r="1.5" fill="currentColor"/>
              <circle cx="31" cy="30" r="1.5" fill="currentColor"/>
            </svg>
            <p>Select an available date on the calendar<br>to see open time slots.</p>
          </div>

          <!-- Time slot picker -->
          <div v-else-if="step === 'calendar'" class="sched-slots">
            <div class="slots-header">
              <span class="slots-date">{{ selectedDateLabel }}</span>
              <span class="slots-tz">EST</span>
            </div>

            <!-- Loading slots -->
            <div v-if="slotsLoading" class="slots-loading">
              <span class="cal-spinner"></span>
              <span class="slots-loading-label">Loading times…</span>
            </div>

            <!-- No slots returned -->
            <div v-else-if="!slotsLoading && availableSlots.length === 0 && !slotsError"
                 class="slots-empty">
              <p>No available times on this date.<br>Please select another day.</p>
            </div>

            <!-- Slot grid (live or fallback) -->
            <div v-else class="slots-grid">
              <button
                v-for="slot in availableSlots"
                :key="slot"
                class="slot-pill"
                :class="{ 'is-selected': selectedTime === slot }"
                @click="selectTime(slot)"
              >{{ slot }}</button>
            </div>

            <p v-if="slotsError" class="slots-error-note">
              Could not load live times — showing all slots
            </p>
          </div>

          <!-- Meeting details form -->
          <div v-else-if="step === 'form'" class="sched-form-wrap">
            <div class="booking-summary">
              <div class="booking-summary-info">
                <svg width="13" height="13" viewBox="0 0 16 16" fill="none" class="summary-icon">
                  <rect x="2" y="3" width="12" height="11" rx="2" stroke="currentColor" stroke-width="1.5"/>
                  <path d="M2 7H14" stroke="currentColor" stroke-width="1.5"/>
                  <path d="M5 1V4M11 1V4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
                </svg>
                <span>{{ selectedDateLabel }} &nbsp;&middot;&nbsp; {{ selectedTime }} EST</span>
              </div>
              <button class="change-btn" @click="backToSlots">Change</button>
            </div>

            <form @submit.prevent="handleSubmit" class="booking-form">

              <div class="form-group">
                <label>Name <span class="required">*</span></label>
                <input type="text" v-model="form.name" :class="{ error: errors.name }" autocomplete="name" />
                <span v-if="errors.name" class="error-message">{{ errors.name }}</span>
              </div>

              <div class="form-group">
                <label>Email <span class="required">*</span></label>
                <input type="email" v-model="form.email" :class="{ error: errors.email }" autocomplete="email" />
                <span v-if="errors.email" class="error-message">{{ errors.email }}</span>
              </div>

              <div class="form-group">
                <label>Company</label>
                <input type="text" v-model="form.company" autocomplete="organization" />
              </div>

              <div class="form-group">
                <label>Current Tech Stack</label>
                <textarea
                  v-model="form.techStack"
                  rows="3"
                  placeholder="e.g., ColdFusion 2018, on-prem Oracle DB, legacy Node.js monolith"
                ></textarea>
              </div>

              <div v-if="submitStatus === 'error'" class="form-status error">
                <p>Something went wrong. Please try again or email us at connect@arclyt.io</p>
              </div>

              <button type="submit" class="confirm-btn" :disabled="isSubmitting">
                <svg v-if="isSubmitting" class="spinner-icon" width="15" height="15" viewBox="0 0 24 24" fill="none">
                  <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2.5" stroke-dasharray="31.4" stroke-dashoffset="10" stroke-linecap="round"/>
                </svg>
                {{ isSubmitting ? 'Confirming...' : 'Confirm Booking' }}
              </button>

            </form>
          </div>

        </div>
      </div>

    </div>
  </section>
</template>

<script setup>
import { ref, reactive, computed, onMounted } from 'vue'

const DAYS_OF_WEEK = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
const MONTHS = [
  'January', 'February', 'March', 'April', 'May', 'June',
  'July', 'August', 'September', 'October', 'November', 'December'
]
const TIME_SLOTS = [
  '9:00 AM',  '9:30 AM',
  '10:00 AM', '10:30 AM',
  '11:00 AM', '11:30 AM',
  '12:00 PM', '12:30 PM',
  '1:00 PM',  '1:30 PM',
  '2:00 PM',  '2:30 PM',
  '3:00 PM',  '3:30 PM',
  '4:00 PM',  '4:30 PM',
]

// ── Shared API config ───────────────────────────────────────
const SCHEDULE_BASE   = import.meta.env.VITE_SCHEDULE_BASE_URL
const TENANT_ID       = import.meta.env.VITE_SCHEDULE_TENANT_ID

// ── Available dates state (calendar) ──────────────────────
const availableDates      = ref(new Set())
const availabilityLoading = ref(true)
const availabilityError   = ref(false)

// ── Available slots state (time picker) ───────────────────
const availableSlots  = ref([])
const slotsLoading    = ref(false)
const slotsError      = ref(false)

// ── Calendar state ──────────────────────────────────────────
const today = new Date()
const currentMonth = ref(today.getMonth())
const currentYear  = ref(today.getFullYear())
const selectedDate = ref(null)
const selectedTime = ref('')

// ── UI step: 'calendar' | 'form' | 'success' ───────────────
const step = ref('calendar')

// ── Form state ─────────────────────────────────────────────
const form = reactive({ name: '', email: '', company: '', techStack: '' })
const errors = reactive({ name: '', email: '' })
const isSubmitting = ref(false)
const submitStatus  = ref('')

// ── Calendar computed ──────────────────────────────────────
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

// Allow up to 3 months forward (matches the 90-day fetch window)
const maxDate = new Date(today.getFullYear(), today.getMonth() + 3, 1)
const isAtMaxMonth = computed(() =>
  currentYear.value > maxDate.getFullYear() ||
  (currentYear.value === maxDate.getFullYear() && currentMonth.value >= maxDate.getMonth())
)
const selectedDateLabel = computed(() => {
  if (!selectedDate.value) return ''
  return selectedDate.value.toLocaleDateString('en-US', {
    weekday: 'long', month: 'long', day: 'numeric'
  })
})

// ── Day helpers ────────────────────────────────────────────
const dateFor = (day) => new Date(currentYear.value, currentMonth.value, day)

const isTodayFn = (day) => {
  const d = dateFor(day)
  return (
    d.getDate()     === today.getDate()     &&
    d.getMonth()    === today.getMonth()    &&
    d.getFullYear() === today.getFullYear()
  )
}
const isSelectedFn = (day) => {
  if (!selectedDate.value) return false
  return dateFor(day).getTime() === selectedDate.value.getTime()
}
const isPastFn = (day) => {
  const d = dateFor(day)
  const cutoff = new Date(today)
  cutoff.setHours(0, 0, 0, 0)
  return d <= cutoff
}
const isWeekendFn = (day) => {
  const dow = dateFor(day).getDay()
  return dow === 0 || dow === 6
}

// Build a local ISO string (YYYY-MM-DD) without UTC conversion
const toISODate = (day) => {
  const d = dateFor(day)
  const y  = d.getFullYear()
  const m  = String(d.getMonth() + 1).padStart(2, '0')
  const dd = String(d.getDate()).padStart(2, '0')
  return `${y}-${m}-${dd}`
}

// Disable a day if it's not in the API availability set.
// Falls back to weekday-only logic while loading or if the fetch failed.
const isUnavailableFn = (day) => {
  if (availabilityLoading.value || availabilityError.value) return isWeekendFn(day)
  return !availableDates.value.has(toISODate(day))
}

// Normalise "HH:MM" / "HH:MM:SS" → "H:MM AM/PM" (passthrough if already 12h)
const to12h = (t) => {
  if (!t || /AM|PM/i.test(t)) return t
  const [h, m] = t.split(':').map(Number)
  const period = h >= 12 ? 'PM' : 'AM'
  return `${h % 12 || 12}:${String(m).padStart(2, '0')} ${period}`
}

// ── Available dates fetch (on mount) ──────────────────────
const fetchAvailability = async () => {
  if (!SCHEDULE_BASE || !TENANT_ID) { availabilityLoading.value = false; return }
  try {
    const res = await fetch(
      // 90 days covers the 3-month window the calendar allows navigating into
      `${SCHEDULE_BASE}/public/scheduling/dates?tenantId=${TENANT_ID}&days=90`
    )
    if (!res.ok) throw new Error()
    const data = await res.json()
    availableDates.value = new Set(data.availableDates ?? [])
  } catch {
    availabilityError.value = true
  } finally {
    availabilityLoading.value = false
  }
}

// ── Available slots fetch (on date select) ─────────────────
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
    // Backend returns [{ startTime: "09:00", endTime: "10:00" }, ...].
    // Accept plain strings too for forward-compatibility.
    const raw = data.slots ?? data.availableSlots ?? []
    availableSlots.value = raw.map(s =>
      typeof s === 'string' ? to12h(s) : to12h(s.startTime)
    )
  } catch {
    slotsError.value = true
    availableSlots.value = TIME_SLOTS // fall back to full hardcoded list
  } finally {
    slotsLoading.value = false
  }
}

onMounted(fetchAvailability)

// ── Navigation ─────────────────────────────────────────────
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

// ── Selection ──────────────────────────────────────────────
const selectDate = (day) => {
  selectedDate.value = dateFor(day)
  selectedTime.value = ''
  step.value = 'calendar'
  fetchSlots(toISODate(day))
}
const selectTime = (slot) => {
  selectedTime.value = slot
  step.value = 'form'
}
const backToSlots = () => {
  selectedTime.value = ''
  step.value = 'calendar'
}

// ── Form validation ────────────────────────────────────────
const validateForm = () => {
  errors.name  = ''
  errors.email = ''
  if (!form.name.trim())  errors.name  = 'Name is required'
  if (!form.email.trim()) errors.email = 'Email is required'
  else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.email))
    errors.email = 'Enter a valid email address'
  return !errors.name && !errors.email
}

// ── Submit ─────────────────────────────────────────────────
const handleSubmit = async () => {
  if (!validateForm()) return

  isSubmitting.value = true
  submitStatus.value = ''

  try {
    if (!SCHEDULE_BASE || !TENANT_ID) throw new Error('Scheduling API not configured')
    const apiUrl = `${SCHEDULE_BASE}/public/scheduling/bookings?tenantId=${TENANT_ID}`

    const payload = {
      name:          form.name,
      email:         form.email,
      company:       form.company   || undefined,
      techStack:     form.techStack || undefined,
      scheduledDate: selectedDateLabel.value,
      scheduledTime: selectedTime.value,
    }

    const res = await fetch(apiUrl, {
      method:  'POST',
      headers: { 'Content-Type': 'application/json' },
      body:    JSON.stringify(payload),
    })

    if (!res.ok) throw new Error('Request failed')
    step.value = 'success'

  } catch {
    submitStatus.value = 'error'
  } finally {
    isSubmitting.value = false
  }
}

// ── Reset ──────────────────────────────────────────────────
const reset = () => {
  selectedDate.value = null
  selectedTime.value = ''
  step.value = 'calendar'
  Object.keys(form).forEach(k => { form[k] = '' })
  submitStatus.value = ''
}
</script>

<style scoped>
section {
  border-top: 1px solid rgba(47, 129, 247, 0.30);
}

.sched-eyebrow {
  font-size: 0.75rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: rgba(47, 129, 247, 0.80);
  margin: 0 0 8px;
  font-weight: 500;
}

/* ── Layout ─────────────────────────────────────────────── */
.sched-layout {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 20px;
  align-items: start;
}

@media (max-width: 780px) {
  .sched-layout {
    grid-template-columns: 1fr;
  }
}

.sched-panel {
  background: #0d1117;
  border: 1px solid #30363d;
  border-top: 1px solid rgba(47, 129, 247, 0.30);
  border-radius: 12px;
  padding: 24px;
}

/* ── Calendar ───────────────────────────────────────────── */
.sched-cal-panel {
  min-width: 296px;
}

.cal-nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
}

.cal-month-label {
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--text);
  letter-spacing: 0.02em;
}

.cal-nav-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 28px;
  border-radius: 6px;
  border: 1px solid rgba(255, 255, 255, 0.10);
  background: transparent;
  color: var(--muted);
  cursor: pointer;
  transition: background 0.15s ease, border-color 0.15s ease, color 0.15s ease;
}
.cal-nav-btn:hover:not(:disabled) {
  background: rgba(47, 129, 247, 0.10);
  border-color: rgba(47, 129, 247, 0.35);
  color: var(--text);
}
.cal-nav-btn:disabled {
  opacity: 0.28;
  cursor: not-allowed;
}

.cal-grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 3px;
}

.cal-dow {
  text-align: center;
  font-size: 0.68rem;
  font-weight: 500;
  letter-spacing: 0.05em;
  color: rgba(240, 244, 255, 0.32);
  text-transform: uppercase;
  padding-bottom: 8px;
}

.cal-day {
  aspect-ratio: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 7px;
  border: 1px solid transparent;
  background: transparent;
  color: var(--text);
  font-size: 0.80rem;
  cursor: pointer;
  transition: background 0.15s ease, border-color 0.15s ease, color 0.15s ease;
}
.cal-day:hover:not(:disabled) {
  background: rgba(47, 129, 247, 0.12);
  border-color: rgba(47, 129, 247, 0.30);
}
.cal-day.is-today {
  border-color: rgba(47, 129, 247, 0.48);
  color: rgba(47, 129, 247, 0.92);
}
.cal-day.is-selected {
  background: #2f81f7;
  border-color: #2f81f7;
  color: #ffffff;
  font-weight: 600;
}
.cal-day.is-selected.is-today {
  background: #2f81f7;
  border-color: #2f81f7;
  color: #ffffff;
}
.cal-day:disabled {
  color: rgba(240, 244, 255, 0.18);
  cursor: not-allowed;
  background: transparent;
  border-color: transparent;
}

.cal-body {
  position: relative;
}

.cal-loading-overlay {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(13, 17, 23, 0.60);
  border-radius: 8px;
  backdrop-filter: blur(2px);
}

.cal-spinner {
  width: 20px;
  height: 20px;
  border: 2px solid rgba(47, 129, 247, 0.18);
  border-top-color: rgba(47, 129, 247, 0.80);
  border-radius: 50%;
  animation: spin 0.7s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.cal-legend {
  margin: 14px 0 0;
  font-size: 0.70rem;
  color: rgba(240, 244, 255, 0.28);
  letter-spacing: 0.04em;
  text-align: center;
}

.cal-legend--error {
  color: rgba(255, 100, 100, 0.55);
}

/* ── Right panel ────────────────────────────────────────── */
.sched-right-panel {
  min-height: 340px;
  display: flex;
  flex-direction: column;
  gap: 18px;
}

/* Step indicator */
.sched-steps {
  display: flex;
  align-items: center;
  gap: 8px;
  padding-bottom: 2px;
}
.sched-step {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 0.76rem;
  color: rgba(240, 244, 255, 0.28);
  transition: color 0.2s ease;
  white-space: nowrap;
}
.sched-step.active { color: rgba(47, 129, 247, 0.90); }
.sched-step.done   { color: rgba(240, 244, 255, 0.52); }

.step-num {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 17px;
  height: 17px;
  border-radius: 50%;
  border: 1px solid currentColor;
  font-size: 0.65rem;
  font-weight: 600;
  flex-shrink: 0;
}
.step-sep {
  color: rgba(255, 255, 255, 0.14);
  font-size: 0.72rem;
}

/* ── Empty state ────────────────────────────────────────── */
.sched-empty {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 14px;
  padding: 32px 16px;
  text-align: center;
}
.empty-icon {
  color: rgba(47, 129, 247, 0.25);
}
.sched-empty p {
  margin: 0;
  font-size: 0.875rem;
  color: rgba(240, 244, 255, 0.36);
  line-height: 1.65;
}

/* ── Time slots ─────────────────────────────────────────── */
.sched-slots {
  display: flex;
  flex-direction: column;
  gap: 14px;
}
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
  font-size: 0.72rem;
  font-family: var(--mono);
  color: rgba(240, 244, 255, 0.35);
  letter-spacing: 0.05em;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 4px;
  padding: 2px 6px;
}

.slots-loading {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  padding: 32px 0;
}

.slots-loading-label {
  font-size: 0.80rem;
  color: rgba(240, 244, 255, 0.38);
  letter-spacing: 0.03em;
}

.slots-empty {
  padding: 32px 0;
  text-align: center;
}

.slots-empty p {
  margin: 0;
  font-size: 0.875rem;
  color: rgba(240, 244, 255, 0.38);
  line-height: 1.65;
}

.slots-error-note {
  margin: 10px 0 0;
  font-size: 0.70rem;
  color: rgba(255, 100, 100, 0.50);
  letter-spacing: 0.03em;
  text-align: center;
}

.slots-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
}
.slot-pill {
  padding: 9px 12px;
  border-radius: 8px;
  border: 1px solid rgba(47, 129, 247, 0.28);
  background: transparent;
  color: rgba(47, 129, 247, 0.78);
  font-family: var(--mono);
  font-size: 0.80rem;
  cursor: pointer;
  transition: background 0.15s ease, border-color 0.15s ease, color 0.15s ease, transform 0.15s ease;
  text-align: center;
}
.slot-pill:hover {
  background: rgba(47, 129, 247, 0.09);
  border-color: rgba(47, 129, 247, 0.52);
  color: #f0f4ff;
  transform: translateY(-1px);
}
.slot-pill.is-selected {
  background: rgba(47, 129, 247, 0.16);
  border-color: #2f81f7;
  color: #f0f4ff;
  font-weight: 500;
}

/* ── Meeting details form ───────────────────────────────── */
.sched-form-wrap {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.booking-summary {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 14px;
  border-radius: 8px;
  border: 1px solid rgba(47, 129, 247, 0.28);
  background: rgba(47, 129, 247, 0.06);
  gap: 12px;
}
.booking-summary-info {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.82rem;
  color: rgba(240, 244, 255, 0.72);
}
.summary-icon {
  color: rgba(47, 129, 247, 0.65);
  flex-shrink: 0;
}
.change-btn {
  background: transparent;
  border: none;
  color: rgba(47, 129, 247, 0.80);
  font-size: 0.76rem;
  cursor: pointer;
  padding: 3px 8px;
  border-radius: 4px;
  transition: color 0.15s ease, background 0.15s ease;
  white-space: nowrap;
}
.change-btn:hover {
  color: #f0f4ff;
  background: rgba(47, 129, 247, 0.10);
}

/* Form fields reuse global .form-group styles */
.booking-form {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.confirm-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  width: 100%;
  padding: 12px 20px;
  margin-top: 4px;
  border-radius: 8px;
  border: 1px solid #2f81f7;
  background: #2f81f7;
  color: #ffffff;
  font-size: 0.95rem;
  font-weight: 500;
  cursor: pointer;
  transition: background 0.2s ease, border-color 0.2s ease, transform 0.2s ease;
}
.confirm-btn:hover:not(:disabled) {
  background: #1a6de8;
  border-color: #1a6de8;
  transform: translateY(-1px);
}
.confirm-btn:active:not(:disabled) {
  transform: translateY(0);
}
.confirm-btn:disabled {
  opacity: 0.58;
  cursor: not-allowed;
}

.spinner-icon {
  animation: spin 0.8s linear infinite;
  flex-shrink: 0;
}
@keyframes spin {
  to { transform: rotate(360deg); }
}

/* ── Success screen ─────────────────────────────────────── */
.sched-success {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 16px;
  padding: 72px 24px;
  text-align: center;
  background: #0d1117;
  border: 1px solid #30363d;
  border-top: 1px solid rgba(47, 129, 247, 0.30);
  border-radius: 12px;
}
.success-check {
  width: 54px;
  height: 54px;
  border-radius: 50%;
  background: rgba(47, 129, 247, 0.10);
  border: 1px solid rgba(47, 129, 247, 0.38);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #2f81f7;
}
.sched-success h3 {
  margin: 0;
  font-size: 1.35rem;
  font-weight: 600;
  color: var(--text);
}
.success-slot-label {
  margin: 0;
  display: inline-block;
  padding: 6px 16px;
  border-radius: 99px;
  border: 1px solid rgba(47, 129, 247, 0.35);
  background: rgba(47, 129, 247, 0.07);
  font-size: 0.875rem;
  color: rgba(47, 129, 247, 0.88);
  font-family: var(--mono);
}
.success-sub {
  margin: 0;
  font-size: 0.875rem;
  color: rgba(240, 244, 255, 0.48);
  max-width: 38ch;
  line-height: 1.65;
}
.sched-ghost-btn {
  margin-top: 8px;
  background: transparent;
  border: 1px solid rgba(240, 244, 255, 0.20);
  color: rgba(240, 244, 255, 0.60);
  padding: 8px 20px;
  border-radius: 8px;
  font-size: 0.85rem;
  cursor: pointer;
  transition: border-color 0.2s ease, color 0.2s ease, background 0.2s ease;
}
.sched-ghost-btn:hover {
  border-color: rgba(240, 244, 255, 0.40);
  color: rgba(240, 244, 255, 0.90);
  background: rgba(255, 255, 255, 0.04);
}
</style>
