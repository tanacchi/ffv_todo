<template>
  <label class="item-row">
    <input type="checkbox"
           :checked="item.done"
           @change="switch_item_progress">
    <span :class="{ done: item.done }">
      {{ item.title }}
    </span>
  </label>
</template>
<script>
  import axios from 'axios'

  const api_baseurl = process.env.VUE_APP_API_BASEURL ? process.env.VUE_APP_API_BASEURL : 'http://localhost:5000/';

  export default {
    props: ['item_id', 'item', 'list_id'],
    data: function() {
      return {
      };
    },
    methods: {
      switch_item_progress: function() {
        const update_progress_url = api_baseurl + 'api/items';
        this.item.done = !this.item.done;
        axios.post(update_progress_url, {
                list_id: this.list_id,
                item_id: this.item_id,
                done: this.item.done.toString(),
              })
             .then(response => {
               console.log(`progress updated. ${response}`);
             });
      }
    }
  };
</script>
<style>
.done {
  text-decoration: line-through;
}
.item-row {
  display: flex;
  width: 80%;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 10px;
}
</style>
