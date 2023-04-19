<template>
  <v-container fluid class="text-center">
    <v-progress-circular indeterminate size="64" color="purple-accent-4"></v-progress-circular
    ><br /><br />
    {{ message || "Loading data..." }}
  </v-container>
</template>
<script setup>

const props = defineProps({
    message:{
        type:String,
        required: true
    }
})

</script>
