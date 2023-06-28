/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "../../portal/**/*.{html,js}",
    "../../portal/app/templatetags/*.py",
    "./node_modules/flowbite/**/*.js"
  ],
  theme: {
    fontSize: {
      'tiny': '.3rem',
      'xxxs': '.45rem',
      'xxs': '.65rem',
      'xs': '.75rem',
      'sm': '.875rem',
      'base': '1rem',
      'lg': '1.125rem',
      'xl': '1.25rem',
      '2xl': '1.70rem',
      '3xl': '1.875rem',
      '4xl': '2.25rem',
    },
    extend: {
      aspectRatio: {
        'fibbo-up': '1.618', //golden ratio'
        'fibbo-down': '0.618',
        'fibbo-ret': '0.382',
        'fibbo-fwd': '1.382',
        'fibbo-half': '0.5', // wheres the fibbo?
      },
      fontFamily: {
        'quicksand': ['Quicksand', 'Rubik', 'sans-serif'],
        'rubik': ['Rubik', 'Quicksand', 'sans-serif'],
        'Roboto': ['Roboto', 'Quicksand', 'sans-serif'],
        'Monserrat': ['Monserrat', 'Quicksand', 'sans-serif'],
      },
      colors: {
        'pantone307c': 'rgb(0, 105, 166)',
        'pantone7689c': 'rgb(43, 142, 193)',
        'pantone7472c': 'rgb(90, 183, 178)',
      },
    },
    corePlugins: {
      aspectRatio: false,
    },
    plugins: [
      require('@tailwindcss/forms'),
      require('@tailwindcss/aspect-ratio'),
      require('@tailwindcss/container-queries'), // how to use: https://github.com/tailwindlabs/tailwindcss-container-queries
      require('flowbite/plugin')
    ],
  },
}