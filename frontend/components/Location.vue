<template>
  <div>
    <v-btn @click.stop="citySelect = true">
      <v-icon start icon="$location" />
      <p class="h-6">
          {{ defaultCity ? defaultCity : "" }}
      </p>
    </v-btn>
    <v-dialog v-model="citySelect" :persistent="defaultCity === null ? true : false" max-width="400">
      <v-card class="card">
        <v-card-title>Select your Nearest Working city</v-card-title>
        <v-autocomplete v-model="defaultCity" :items="cities.getCities" item-title="name" item-value="url" label="Search"
          class="ma-4" outlined prepend-inner-icon="$location" @update:model-value="changeCity"></v-autocomplete>

            <button class="justify-end bg-gray hover:bg-slate-400 pa-3 " @click="citySelect = false"><v-icon icon="$close"></v-icon></button>
      </v-card>
    </v-dialog>
  </div>
</template>

<script setup>
import { useCitiesStore } from "@/stores/cities";
import { storeToRefs } from "pinia";

const citySelect = ref(false);
const cities = useCitiesStore();
const route = useRoute();

const {defaultCity, cookieCity} = storeToRefs(cities);

async function changeCity(){
    cookieCity.value= defaultCity.value
    citySelect.value = false

    await navigateTo(`/${defaultCity.value}`)
}


</script>