const defaultTheme = require('tailwindcss/defaultTheme');

module.exports = {
  theme: {
    extend: {
      fontFamily: {
        sans: ['Barlow', ...defaultTheme.fontFamily.sans]
      },
      container: {
        center: true,
        padding: '1.25rem'
      },
      screens: {
        xl: '1120px'
      },
      spacing: {
        18: '4.5rem'
      }
    }
  },
  variants: {
      borderWidth: ['responsive', 'hover']
  },
  plugins: []
};
