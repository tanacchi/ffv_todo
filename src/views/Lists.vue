<template>
  <div class="lists">
    <p v-for="(list, id) in lists"
           :key="id"
           class="">
      <span>{{ list.name }}</span>
    </p>
  </div>
</template>
<script>
  import axios from 'axios'

  const apiBaseURL = process.env.VUE_APP_API_BASEURL ? process.env.VUE_APP_API_BASEURL : 'http://localhost:5000';

  export default {
    data: function() {
      return {
        lists: {}
      }
    },
    mounted: function() {
      const lists_uri = apiBaseURL + 'api/lists';
      axios.get(lists_uri)
           .then(response => {
             this.lists = response.data;
           });
      console.log("lists: " + this.lists);
    }
  }
</script>
