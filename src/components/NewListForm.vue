<template>
  <input class="new-list"
         type="text"
         v-model="newListName"
         @keypress.enter="createList">
</template>
<script>
  import axios from 'axios'

  const apiBaseURL = process.env.VUE_APP_API_BASE_URL ? process.env.VUE_APP_API_BASEURL : 'http://localhost:5000/';

  export default {
    data: function() {
      return {
        newListName: '',
      };
    },
    methods: {
      createList: function() {
        const createListURL = apiBaseURL + 'api/lists/create';
        axios.post(createListURL, {
                name: this.newListName,
              })
             .then(response => {
               console.log(response);
             });
      }
    },
  };
</script>
<style scoped>
</style>
