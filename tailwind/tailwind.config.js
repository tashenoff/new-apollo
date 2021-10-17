module.exports = {
  future: {
      removeDeprecatedGapUtilities: true,
      purgeLayersByDefault: true,
  },
  purge: {
      enabled: true, //true for production build
      content: [
          '../**/templates/*.html',
          '../**/templates/**/*.html'
      ]
  },
  darkMode: 'class',
  theme: {

    borderRadius: {
      'none': '0',
     'sm': '0.125rem',
     DEFAULT: '0.25rem',
     DEFAULT: '4px',
     'md': '0.375rem',
     'lg': '0.3rem',
     'full': '9999px',
     'large': '12px',
    },
      
    container: {
        screens: {
          sm: "100%",
          md: "100%",
          lg: "1140px",
          xl: "1140px"
        }
      },
  
      extend: {
        zIndex: {
          '60': '60',
        }
      },
      colors: {
        primary: '#010101',
        darkLight: '#0c162d',
        primarylight: '#9361e2',
        secondary: '#e045e6',
        secondaryLight: '#dc31e3',
        green: '#47E189',
        greenDark: '#42cf7e',
        black: '#333',
        white: '#fff',
        red: '#e045e6',
        gray: '#F4F4F4',
        blueLight: '#c3d9f6'
      }
  },
  variants: {},
  plugins: [],
}