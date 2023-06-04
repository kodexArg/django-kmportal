/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "../../portal/**/*.{html,js}",
    "../../portal/app/templatetags/*.py",
  ],
  theme: {
    fontSize: {
      'tiny': '.5rem',
      'xs': '.75rem',
      'sm': '.875rem',
      'base': '1rem',
      'lg': '1.125rem',
      'xl': '1.25rem',
      '2xl': '1.5rem',
      '3xl': '1.875rem',
      '4xl': '2.25rem',
      '5xl': '3rem',
      '6xl': '4rem',
    },
    extend: {
      fontFamily: {
        'quicksand': ['Quicksand', 'Rubik', 'sans-serif'],
        'rubik': ['Rubik', 'Quicksand', 'sans-serif'],
        'Roboto': ['Roboto', 'Quicksand', 'sans-serif'],
      },
    },
    plugins: [
      require('@tailwindcss/typography'),
      require('@tailwindcss/forms'),
      require('@tailwindcss/aspect-ratio'),
      require('@tailwindcss/container-queries'),
    ],
  },
}