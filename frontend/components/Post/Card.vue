<template>
  <v-card
    class="mx-auto my-4 card-glass"
    color="purple-darken-4"
    theme="light"
    max-width="540"
  >
    <!-- <template v-slot:prepend>
      <v-icon size="x-large"></v-icon>
    </template> -->
    <v-img
      cover
      height="250"
      style="margin-top: 0px; cursor: pointer;"
      @click="navigateTo(`/${post.id}/post`)"
      :src="post.image ? post.image : 'https://images.pexels.com/photos/1457842/pexels-photo-1457842.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'"
    ></v-img>
    <div class="content" style="text-align: start;">
      <v-card-text class="text-h6 mt-2">
        <div class="chips mt-0 px-1" style="display: flex; flex-direction: row; flex-wrap: wrap; justify-content: space-between;">
          <div>
            <v-chip>Project Completed</v-chip>
            <v-chip>Painting</v-chip>
          </div>
          <p style="font-size: 14px;" class="text-h7">{{ formatDate(post.created_at).formattedDate}}</p>
        </div>
      </v-card-text>
      <v-card-text class="py-1" style="font-size: 18px; cursor: pointer;"   @click="navigateTo(`/${post.id}/post`)">
          {{ post.content }} 
        <div @click="alterContentLen" style="display: inline;">...{{readMore ? 'less' : 'more'}}</div>
      </v-card-text>
    </div>

    <v-card-actions>
      <v-list-item class="w-100">
        <template v-slot:prepend>
            <v-avatar
            @click="navigateTo(`/${post.creator}/social`)"
            class="cursor-pointer"
            color="grey-darken-3"
            image="https://avataaars.io/?avatarStyle=Transparent&topType=ShortHairShortCurly&accessoriesType=Prescription02&hairColor=Black&facialHairType=Blank&clotheType=Hoodie&clotheColor=White&eyeType=Default&eyebrowType=DefaultNatural&mouthType=Default&skinColor=Light"
            ></v-avatar>
        </template>
        
          <v-list-item-title style="text-align: start; cursor: pointer;" @click="navigateTo(`/${post.creator}/social`)">
            {{post.name}}
          </v-list-item-title>
          <v-list-item-subtitle style="text-align: start;">{{ post.title }}</v-list-item-subtitle>

        <template v-slot:append>
          <div class="justify-self-end">
            <v-icon class="me-1" icon="$heart2"></v-icon>
            <span class="subheading me-2">{{post.likes}}</span>
            <span class="me-1">·</span>
            <v-icon class="me-1" icon="$share"></v-icon>
            <span class="subheading">45</span>
          </div>
        </template>
      </v-list-item>
    </v-card-actions>
  </v-card>
</template>

<script setup>

const props = defineProps({
    post:{
        type:Object,
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