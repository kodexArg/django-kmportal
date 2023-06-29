/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        '../../**/*.py',
	
	/**
	 * Flowbite
	*/
	'./node_modules/flowbite/**/*.js'
	
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
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/line-clamp'),
        require('@tailwindcss/aspect-ratio'),
	require('flowbite/plugin')
    ],
}
