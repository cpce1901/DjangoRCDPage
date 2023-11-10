/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    '../templates/**/*.html',
    '../static/**/*.js'
],
  theme: {
    extend: {},
    fontFamily: {
      "exo": ['"exo 2"'],
      "rale": ['"Raleway"'],
    },
  },
  plugins: [],
}

