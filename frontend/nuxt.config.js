// https://v3.nuxtjs.org/api/configuration/nuxt.config
import vuetify from 'vite-plugin-vuetify'
export default defineNuxtConfig({
  ssr: false,
  app: {
    head: {
      titleTemplate: '%s',
      title: 'Shramik',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        {
          hid: 'description',
          name: 'description',
        },
        { name: 'format-detection', content: 'telephone=no' },
      ],
      link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
    },
  },
  css: ['vuetify/styles', '~/assets/css/custom.css'],
  sourcemap: {
    server: false,
    client: false,
  },
  modules: [
    '@nuxtjs/google-fonts',
    '@pinia/nuxt',
    async (options, nuxt) => {
      nuxt.hooks.hook('vite:extendConfig', (config) =>
        config.plugins.push(
          vuetify({
            styles: {
              configFile: 'assets/css/settings.scss',
            },
          })
        )
      )
    },

  ],
  // hooks: {
  //   'vite:extendConfig': (config) => {
  //     config.plugins.push(
  //       vuetify({
  //         // autoImport: true,
  //         styles: { configFile: 'assets/css/settings.scss' },
  //       })
  //     )
  //   },
  // },

  runtimeConfig: {
    // The private keys which are only available server-side
    apiSecret: '123',
    // Keys within public are also exposed client-side
    public: {
      apiBase: 'http://localhost:8000/',
      apiVersion: 'http://localhost:8000/api/',
      sanctumAuth: {
        baseUrl: 'http://localhost:8000',
        endpoints: {
          csrf: '/sanctum/csrf-cookie',
          login: '/api/auth/login',
          logout: '/api/logout',
          user: '/api/details',
        },
        redirects: {
          home: '/',
          login: '/auth/sign-in',
          logout: '/',
        },
      },
    },
  },
  googleFonts: {
    download: false,
    families: {
      Hind: {
        wght: [400, 700],
      },
      Poppins: {
        wght: [600, 800],
      },
    },
  },
  build: {
    transpile: ['vuetify'],
  },
})
