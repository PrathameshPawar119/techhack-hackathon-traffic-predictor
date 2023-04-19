import {
  defineNuxtPlugin,
  addRouteMiddleware,
  useState,
  useRuntimeConfig,
  navigateTo,
  useCookie,
} from '#app'
import { $fetch } from 'ohmyfetch'

export interface Endpoints {
  csrf: string
  login: string
  logout: string
  user: string
}

export interface Redirects {
  home: string
  login: string
  logout: string
}

export interface ModuleOptions {
  baseUrl: string
  endpoints: Endpoints
  redirects: Redirects
}

export default defineNuxtPlugin(async (nuxtApp) => {
  const auth = useState('auth', () => {
    return {
      user: null,
      loggedIn: false,
    }
  })
  const config: ModuleOptions = useRuntimeConfig().sanctumAuth
  // const router = useRouter()

  addRouteMiddleware('auth', async () => {
    await getUser()

    if (auth.value.loggedIn === false) {
      return navigateTo(config.redirects.login)
    }
  })
  addRouteMiddleware('guest', async () => {
    await getUser()

    if (auth.value.loggedIn) {
      return navigateTo(config.redirects.home)
    }
  })

  const apiFetch = $fetch.create({
    baseURL: config.baseUrl,
    credentials: 'include',
    headers: {
      Accept: 'application/json',
      'X-XSRF-TOKEN': useCookie('XSRF-TOKEN').value,
    },
  })

  const csrf = async () => {
    await $fetch(config.endpoints.csrf, {
      baseURL: config.baseUrl,
      credentials: 'include',
      method: 'GET',
      headers: {
        Accept: 'application/json',
      },
    })
  }

  const getUser = async () => {
    if (auth.value.loggedIn && auth.value.user) {
      return auth.value.user
    }

    try {
      const user = await apiFetch(config.endpoints.user)
      if (user) {
        auth.value.loggedIn = true
        auth.value.user = user
        return user
      }
    } catch (error) {
      // console.log(error)
    }
  }

  const login = async (data: any) => {
    await csrf()

    try {
      await apiFetch(config.endpoints.login, {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
          Accept: 'application/json',
          'X-XSRF-TOKEN': useCookie('XSRF-TOKEN').value,
        },
      })

      // await getUser()
      window.location.replace(config.redirects.home)
    } catch (error: any) {
      throw error.data
    }
  }

  const logout = async () => {
    try {
      await apiFetch(config.endpoints.logout, {
        method: 'GET',
      })
    } catch (error) {
      console.log(error)
    } finally {
      auth.value.loggedIn = false
      auth.value.user = null

      window.location.replace(config.redirects.logout)
    }
  }

  const useFetchApi = async (path: string, opts: any) => {
    const config = useRuntimeConfig()
    return await useFetch(path, {
      baseURL: config.public.apiVersion,
      credentials: 'include',
      headers: {
        Accept: 'application/json',
        'X-XSRF-TOKEN': useCookie('XSRF-TOKEN').value,
      },
      ...opts,
    })
  }

  return {
    provide: {
      apiFetch,
      csrf,
      useFetchApi,
      auth,
      sanctumAuth: {
        login,
        getUser,
        logout,
      },
    },
  }
})
