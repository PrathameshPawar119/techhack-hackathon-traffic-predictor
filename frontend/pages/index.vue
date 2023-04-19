<template>
    <v-container class="text-center">
      <section v-if="pending">
        <loading message="Loading Todays traffic..." />
      </section>
      <section v-else>
        <div class="displaySection">
          <h2 class="text-h3">Today's traffic at All Places</h2>
        </div>
        <div>
        </div>
        <div class="grid mt-6">
            <v-card
              class="mx-2 my-4 card-glass"
              color="purple-darken-4"
              theme="light"
              max-width="540"
              v-for="(item, i) in predictions" :key="i"
            >
              <v-img
                cover
                height="250"
                style="margin-top: 0px; cursor: pointer;"
                v-html="maps[i]"
              ></v-img>
              <div class="content" style="text-align: start;">
                <v-card-text class="text-h6 mt-2">
                  <div class="chips mt-0 px-1" style="display: flex; flex-direction: row; flex-wrap: wrap; justify-content: space-between;">
                    <p style="font-size: 14px;" class="text-h7">Average number of vehichles on Location {{ i+1 }} is  {{ ~~(item * 100) }}</p>
                    
                  </div>
                  <v-chip variant="tonal">{{ chechVolume(~~(item * 100)) }}</v-chip>
                </v-card-text>
              </div>
            </v-card>
        </div>
      </section>
    </v-container>
</template>

<script setup>
import Chart from 'chart.js/auto'

const {$useFetchApi:useFetchApi} = useNuxtApp();
const route = useRoute();
const reactiveQuery = computed(() => route.query);
const predictions = ref([]);
const volume = ref(null);

const maps = ref([
 '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d120726.33744703334!2d73.03195514573571!3d18.988938318645776!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3be7e83e1f23f23d%3A0xe3a106c431e3fd0a!2sPanvel%2C%20Navi%20Mumbai%2C%20Maharashtra!5e0!3m2!1sen!2sin!4v1681883790367!5m2!1sen!2sin" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>',
 '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d119981.39107468927!2d73.72107902366564!3d19.990944013144848!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bddd290b09914b3%3A0xcb07845d9d28215c!2sNashik%2C%20Maharashtra!5e0!3m2!1sen!2sin!4v1681883735597!5m2!1sen!2sin" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>',
 '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d121059.0471115297!2d73.78056553325965!3d18.524598599546472!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bc2bf2e67461101%3A0x828d43bf9d9ee343!2sPune%2C%20Maharashtra!5e0!3m2!1sen!2sin!4v1681883691436!5m2!1sen!2sin" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>',
 '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3766.1338735575246!2d72.95571837508153!3d19.276543581969747!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3be7ba4e77ee6873%3A0x78a2fd935af0acb8!2sGhodbunder%20Rd%2C%20Gowniwada%2C%20Owale%2C%20Thane%20West%2C%20Thane%2C%20Maharashtra!5e0!3m2!1sen!2sin!4v1681883495501!5m2!1sen!2sin" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'

]);



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


function chechVolume(inp)
{
  if (inp < 10 && inp > 0) {
    volume.value = 'Not conjusted';
  }
  if (inp < 20 && inp > 10) {
    volume.value = 'Less conjusted';
  }
  if (inp < 30 && inp > 20) {
    volume.value = 'Medium conjusted';
  }
  if (inp < 40 && inp > 30) {
    volume.value = 'Highly conjusted';
  }

  return volume.value;
}

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

@media (max-width: 660px){
  .grid{
    display: grid;
    grid-template-columns: 1fr;
    grid-template-rows: 1fr;
  }

  .rightSection, .leftSection{
    display: none;
  }
}

</style>