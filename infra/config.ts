/**
 * Configuration for Arclyt infrastructure
 */
export const config = {
  // Domain configuration
  domainName: 'arclyt.io',
  enableWww: true, // Set to false to disable www subdomain
  
  // AWS regions
  mainRegion: 'us-east-1', // S3 and CloudFront stack (must be us-east-1 for CloudFront)
  certRegion: 'us-east-1', // ACM certificate must be in us-east-1 for CloudFront
  
  // Site source folder (relative to infra directory)
  siteSourceFolder: '../dist', // Vite builds to dist/ (relative to infra/)
  
  // Contact form configuration
  contactEmail: process.env.CONTACT_EMAIL || 'connect@arclyt.io', // Email to receive contact form submissions
};
