<template>
  <v-card
    class="mx-auto my-4 card-glass"
    color="purple-darken-4"
    theme="light"
    max-width="540"
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
          <p style="font-size: 14px;" class="text-h7">Average number of vehichles on Location </p>
        </div>
      </v-card-text>
    </div>
  </v-card>
</template>

<script setup>

const props = defineProps({
    pred:{
        type:Number,
        required:true
    }
})

// let content = (props.post.content).slice(0,80);
// const readMore = ref(false);
// function alterContentLen(){
//   if (readMore) {
//     content = content.slice(0,40);
//     readMore.value = false;
//   }
//   else{
//     content = props.post.content;
//     readMore.value = true;
//   }
// }

// killer date conversion function
function formatDate(raw) {
  const rawDate = new Date(raw);
  const date = rawDate.getDate();
  const month = new Intl.DateTimeFormat("en-US", {
    month: "short",
  }).format(rawDate);
  const formattedDate = new Intl.DateTimeFormat("en-US", {
    month: "short",
    weekday: "short",
    day: "numeric",
  }).format(rawDate);

  return { date, month, formattedDate };
}

</script>

<style scoped>
.card-glass {
    background-color: rgba(81, 4, 120, 0.55) !important;
    backdrop-filter: blur(8px) saturate(160%) !important;
    -webkit-backdrop-filter: blur(8px) saturate(160%) !important;
}
.cursor-pointer:hover{
  cursor: pointer;
}
</style>