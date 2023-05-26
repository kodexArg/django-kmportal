/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../../portal/**/*.{html,js}"],
  theme: {
    extend: {
      fontFamily: {
        'quicksand': ['Quicksand', 'Rubik', 'sans-serif'],
        'rubik': ['Rubik', 'Quicksand', 'sans-serif'],
        'Roboto': ['Roboto', 'Quicksand', 'sans-serif'],
      },
    },
    plugins: [],
  },
}