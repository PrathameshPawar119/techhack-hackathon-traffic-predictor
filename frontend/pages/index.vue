<template>
    <v-container class="text-center">
      <section v-if="pending">
        <loading message="Loadng Posts..." />
      </section>
      <section v-else>
        <div class="displaySection">
          <h1 class="text-h2 font-weight-bold">Today's traffic at All Places</h1>
        </div>
      </section>
    </v-container>
</template>

<script setup>
import { useCitiesStore } from "@/stores/cities";
import { storeToRefs } from "pinia";

const {$useFetchApi:useFetchApi} = useNuxtApp();
const cities = useCitiesStore();
const { defaultCity, cookieCity } = storeToRefs(cities);
const route = useRoute();
const reactiveQuery = computed(() => route.query);
const drawer = ref(false);


useHead({
  title:"Home"
})




</script>

<style scoped>
.displaySection{
  display: grid;
  grid-template-columns: 1fr 4fr 2fr;
  grid-template-rows: 1fr;
}
  .rightSection, .leftSection{
    display: block;
    /* position: fixed; */
  }

@media screen and (max-width: 660px){
  .displaySection{
    display: grid;
    grid-template-columns: 1fr;
    grid-template-rows: 1fr;
  }

  .rightSection, .leftSection{
    display: none;
  }
}

</style>