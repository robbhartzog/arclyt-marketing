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
      </nav>
    </div>
  </header>
</template>

<script setup>
// Logo is served from public folder
const logoUrl = '/assets/arclyt_logo.png'

const scrollToSection = (event) => {
	event.preventDefault()
	const href = event.currentTarget.getAttribute('href')
	if (href && href.startsWith('#')) {
		const targetId = href.substring(1)
		if (targetId === 'top') {
			window.scrollTo({
				top: 0,
				behavior: 'smooth'
			})
		} else {
			const targetElement = document.getElementById(targetId)
			if (targetElement) {
				const headerOffset = 80
				const elementPosition = targetElement.getBoundingClientRect().top
				const offsetPosition = elementPosition + window.pageYOffset - headerOffset
				
				window.scrollTo({
					top: offsetPosition,
					behavior: 'smooth'
				})
			}
		}
	}
}

const scrollToTop = (event) => {
	event.preventDefault()
	window.scrollTo({
		top: 0,
		behavior: 'smooth'
	})
}
</script>
