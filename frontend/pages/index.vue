<template>
    <v-container class="text-center">
      <section v-if="pending">
        <loading message="Loadng Posts..." />
      </section>
      <section v-else>
        <div class="displaySection">
          <div class="rightSection d-none d-sm-flex">
            okok
          </div>
          <div class="postsSection">
            <post-card v-for="(post, i) in posts" :key="i" :post="post"/>
          </div>
          <div class="leftSection d-none d-sm-flex">
            <v-btn @click="drawer=true" class="mx-auto" size="large" variant="tonal" color="primary" prepend-icon="$filter">Filters</v-btn>
              <v-navigation-drawer
                v-model="drawer"
                location="right"
                temporary
              >
                <v-divider></v-divider>
                <v-list density="compact" nav>
                    <div v-for="(item, i) in filters" :key="i">
                        <v-list-item style="text-align: start;" :prepend-icon="item.icon" :title="item.name" :value="item.name"></v-list-item>
                    </div>
                </v-list>
              </v-navigation-drawer>
          </div>
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

const filters = [
  {
    'name':'Latest',
    'icon':'$flash',
    'slug':'posts/latest'
  },
    {
    'name':'Popular',
    'icon':'$flash',
    'slug':'posts/popular'
  },
]

const posts = ref(null);
const {pending, data, error, refresh } = await useFetchApi("posts/popular", {
  lazy:true,
  query:{page: 1}
})

// onMounted(() => { 
//   console.log(defaultCity);
//   if (defaultCity.value) {
//     navigateTo(`/${defaultCity.value}/city`);
//   }
// });

watch(data,()=>{
  posts.value = data.value.data.data
  console.log(posts.value);
})

watch( reactiveQuery ,()=>{
  refresh();
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