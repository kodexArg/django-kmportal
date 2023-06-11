/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "../../portal/**/*.{html,js}",
    "../../portal/app/templatetags/*.py",
  ],
  theme: {
    fontSize: {
      'tiny': '.25rem',
      'xs': '.5rem',
      'sm': '.75rem',
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
      colors: {
        'pantone307c': 'rgb(0, 105, 166)',
        'pantone7689c': 'rgb(43, 142, 193)',
        'pantone7472c': 'rgb(90, 183, 178)',
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