<template>
  <div class="lists">
    <new-list-form v-on:list-created="fetchList" />
    <list-row
      v-for="(list, id) in lists"
      :key="id"
      :list_id="id"
      :list_name="list.name">
    </list-row>
  </div>
</template>
<script>
  import axios from 'axios'
  import NewListForm from "@/components/lists/NewListForm.vue"
  import ListRow from "@/components/lists/ListRow.vue"

  const apiBaseURL = process.env.VUE_APP_API_BASEURL ? process.env.VUE_APP_API_BASEURL : 'http://localhost:5000';

  export default {
    components: {
      NewListForm,
      ListRow,
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
