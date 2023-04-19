<template>
    <v-container class="text-center">
      <section v-if="pending">
        <loading message="Loadng Todays traffic..." />
      </section>
      <section v-else>
        <div class="displaySection">
          <h2 class="text-h3">Today's traffic at All Places</h2>
        </div>
        <div>
        </div>
        <div class="grid mt-6">
            <v-card
              class="mx-4 my-4 card-glass"
              color="purple-darken-4"
              theme="light"
              max-width="540"
              v-for="(item, i) in predictions" :key="i"
            >
              <v-img
                cover
                height="250"
                style="margin-top: 0px; cursor: pointer;"
                :src="'https://images.pexels.com/photos/1457842/pexels-photo-1457842.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'"
              ></v-img>
              <div class="content" style="text-align: start;">
                <v-card-text class="text-h6 mt-2">
                  <div class="chips mt-0 px-1" style="display: flex; flex-direction: row; flex-wrap: wrap; justify-content: space-between;">
                    <p style="font-size: 14px;" class="text-h7">Average number of vehichles on Location 1 is  {{ ~~(item * 100) }}</p>
                    <h2 class="text-h4"></h2>
                  </div>
                </v-card-text>
              </div>
            </v-card>
        </div>
      </section>
    </v-container>
</template>

<script setup>
// import { useCitiesStore } from "@/stores/cities";
// import { storeToRefs } from "pinia";
import Chart from 'chart.js/auto'

const {$useFetchApi:useFetchApi} = useNuxtApp();
// const cities = useCitiesStore();
// const { defaultCity, cookieCity } = storeToRefs(cities);
const route = useRoute();
const reactiveQuery = computed(() => route.query);
const predictions = ref([]);



// async function fetchPreds() {
//   try {
//     const response = await $axios.post('http://localhost:5000/predict_all_junction', {
//       date: "2015-01-11",
//     })
//     predictions.value = response.data.predictions
//   } catch (error) {
//     console.log(error)
//   }
// }

const { data, pending, error, refresh } = await useFetch('http://localhost:5000/predict_all_junction', {
  method: "POST",
  body:{
    date:"2015-01-11"
  },
  query:reactiveQuery
})
watch(data, ()=>{
  predictions.value = data.value.predictions;
})
predictions.value[0] = data.value.predictions[0][0][0];
predictions.value[1] = data.value.predictions[1][0][0];
predictions.value[2] = data.value.predictions[2][0][0];
predictions.value[3] = data.value.predictions[3][0][0];

console.log("predications -----", predictions.value);
watch(reactiveQuery, ()=>{
  refresh();
})



// (async function () {
//   const data =  [
//     {'location 1':predictions.value[0]},
//      { 'location 2': predictions.value[1] },
//       { 'location 3': predictions.value[2] },
//       { 'location 4': predictions.value[3] },

//   ];

//   new Chart(
//     document.getElementById('acquisitions'),
//     {
//       type: 'bar',
//       data: {
//         labels: data.map(row => row.year),
//         datasets: [
//           {
//             label: 'Acquisitions by year',
//             data: data.map(row => row.count)
//           }
//         ]
//       }
//     }
//   );
// })();



useHead({
  title:"Home"
})




</script>

<style scoped>
.grid{
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-template-rows: 1fr;
}
  .rightSection, .leftSection{
    display: block;
    /* position: fixed; */
  }

@media screen and (max-width: 660px){
  .displaySection{
    /* display: grid;
    grid-template-columns: 1fr;
    grid-template-rows: 1fr; */
  }

  .rightSection, .leftSection{
    display: none;
  }
}

</style>