<template>
  <div class="new-item-form">
    <input v-model="newitem_title"
           @keypress.enter="add_item">
  </div>
</template>
<script>
  import axios from 'axios'

  const api_baseurl = process.env.VUE_APP_API_BASEURL ? process.env.VUE_APP_API_BASEURL : 'http://localhost:5000/';

  export default {
    data: function() {
      return {
        newitem_title: '',
      };
    },
    methods: {
      add_item: function() {
        const create_item_url = api_baseurl + 'api/items/create';
        axios.post(create_item_url, {
                list_id: this.$route.params.id,
                title: this.newitem_title,
              })
             .then(response => {
               this.$emit('item-added', this.newitem_title);
               this.newitem_title = '';
               this.newitem_id++;
               console.log(`item created. ${response}`)
             });
      },
    }
  };
</script>
<style scoped>
</style>
