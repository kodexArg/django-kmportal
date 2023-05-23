/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../../portal/**/*.{html,js}", "../../portal/**/*.{py}"],
  theme: {
    extend: {
      fontFamily: {
        'quicksand': ['Quicksand', 'Rubik', 'sans-serif'],
        'rubik': ['Rubik', 'Quicksand', 'sans-serif'],
      },
    },
    plugins: [],
  },
}