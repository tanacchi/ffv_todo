<template>
  <input class="new-list"
         type="text"
         v-model="newListName">
</template>
<script>
  export default {
    data: function() {
      return {
        newListName: '',
      };
    },
    methods: {
    },
  };
</script>
<style scoped>
</style>
