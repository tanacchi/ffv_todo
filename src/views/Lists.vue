<template>
  <div class="lists">
    <new-list-form v-on:list-created="fetchList" />
    <p v-for="(list, id) in lists"
           :key="id"
           class="">
    <router-link
      :to="{name: 'TodoList', params: {id: id}}">
      {{ list.name }}
    </router-link>
    </p>
  </div>
</template>
<script>
  import axios from 'axios'
  import NewListForm from "@/components/NewListForm.vue"

  const apiBaseURL = process.env.VUE_APP_API_BASEURL ? process.env.VUE_APP_API_BASEURL : 'http://localhost:5000';

  export default {
    components: {
      NewListForm,
    },
    data: function() {
      return {
        lists: {}
      }
    },
    methods: {
      fetchList: function() {
        const lists_uri = apiBaseURL + 'api/lists';
        axios.get(lists_uri)
             .then(response => {
               this.lists = response.data;
             });
        console.log("lists: " + this.lists);
      }
    },
    mounted: function() {
      this.fetchList();
    }
  }
</script>
