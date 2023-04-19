<template>
    <div>
        <section class="analysis mt-14 mx-10 text-h6">
            <v-col class="mx-8">
                <v-autocomplete v-model="formData.junction" :items="cities" item-title="name" item-value="url" label="Select Junction City*" color="primary"
                class="mx-2"  outlined prepend-inner-icon="$location"></v-autocomplete>
                <v-text-field
                v-model="formData.date"
                label="Founded at*"
                placeholder="Founded at"
                type="date"
                name="founded"
                class="mx-2"
                variant="outlined"
                color="primary"
                min="1900-01-01"
                max="2023-12-31"
                id="foundedDatePicker"
                ></v-text-field>
            </v-col>
        </section>
        <section >
            <v-row class="flex justify-center m-4">
                <v-btn variant="tonal" color="primary" class="card-glass" @click="predict">
                    Predict Cars per minute
                </v-btn>
            </v-row>
            <v-row v-if="fetching" class="flex justify-center">
                <Loading message="Processing..." />
            </v-row>
            <v-row class="flex justify-center m-8 p-8" v-else >
                <v-card rounded="4" class="card-glass pa-4 mt-8 text-center" v-if="submitted">
                    <p class="text-h5 pa-12">Number of vehicles per minute at junction are  {{~~(predictions * 100)}} </p>
                    <p class="text-h6" >Hence traffic at selected location is {{ chechVolume(~~(predictions * 100)) }}</p>
                </v-card>

            </v-row>
        </section>
    </div>
</template>
<script setup>

const { $useFetchApi: useFetchApi } = useNuxtApp();
const route = useRoute();
const reactiveQuery = computed(() => route.query);
const predictions = ref([]);
const formData = reactive({
    date:null,
    junction: null
})
const fetching = ref(false);
const submitted = ref(false);
const volume = ref(null);

// const cities = ref([
//     {1:'Panvel'},
//     {2:'Pune'},
//     {3:'Nashik'},
//     {4:'Thane'}
// ])
const cities = ref([
    'Panvel', 'Pune', 'Nashik', 'Thane'
]);

async function predict()
{
    switch (formData.junction) {
        case 'Panvel':
            formData.junction = 1;
            break;
        case 'Pune':
            formData.junction = 2;
            break;
        case 'Nashik':
            formData.junction = 3;
            break;
        case 'Thane':
            formData.junction = 4;
            break;
    
        default:
            break;
    }

    fetching.value = true;
    
    const { data, pending, error, refresh } = await useFetch('http://localhost:5000/predict_by_date', {
        method: "POST",
        body: {
            date: formData.date,
            junction:formData.junction
        },
        query: reactiveQuery
    })
    watch(data, () => {
        predictions.value = data.value.predictions[0][0];
        fetching.value = false;
    })
    predictions.value = data.value.predictions[0][0];
    submitted.value = true;
    fetching.value = false;
}

function chechVolume(inp) {
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


watch(reactiveQuery, () => {
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
    title: "Home"
})



</script>

<style >

</style>