<template>
  <v-app>
    <NavHeader />
    <v-main>
      <slot />
      </v-main>
  </v-app>
</template>

<script setup>

// const route = useRoute();

// const { $auth: auth, $sanctumAuth } = useNuxtApp();

// const userfetch = ref(false);
// console.log(userfetch.value);

// async function user() {
//   try {
//     await $sanctumAuth.getUser();
//     userfetch.value = true;
//     console.log(userfetch.value);
//   } catch (error) {
//     console.log(error);
//   }
// }

</script>
