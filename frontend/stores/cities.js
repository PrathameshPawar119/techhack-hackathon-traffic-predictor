import { defineStore } from 'pinia'

export const useCitiesStore = defineStore('cities', ()=>{
    const cities = ref([])
    const defaultCity = ref(null)
    const cookieCity = useCookie('city')

    const getCities = computed(()=>{
        return cities.value.data || []
    })
    
    async function setCities(){
        const config = useRuntimeConfig();
        const {data, error} = await useFetch('all-cities', {
            baseURL: config.public.apiVersion
        })
        this.cities = data.value;
        syncCityFromCookie();
    }

    async function syncCityFromCookie(){
        let city = cities.value.data.find((element)=>{
            element.url = cookieCity.value
        })
        if(city == undefined){
            cookieCity.value = null
        } else {
            defaultCity.value = city.url
        }
    }


    return { cities, getCities, cookieCity, setCities, defaultCity };
})