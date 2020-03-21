<template>
  <div class="list">
    <div class="new-item-form">
      <input v-model="newitem_title"
             @keypress.enter="add_item">
    </div>
    <label v-for="(item, id) in items"
           :key="id"
           class="item-row">
      <input type="checkbox" :checked="item.done" @change="toggle_item_progress(id, item)">
      <span :class="{ done: item.done }">
        {{ item.title }}
      </span>
    </label>
  </div>
</template>
<script>
  import axios from 'axios'

  export default {
    data: function() {
      return {
        newitem_title: '',
        newitem_id: 1,
        items: {}
      }
    },
    mounted: function() {
      const api_baseurl = process.env.VUE_APP_API_BASEURL ? process.env.VUE_APP_API_BASEURL : 'http://localhost:5000/';
      const get_items_url = api_baseurl + 'api/items';
      axios.get(get_items_url)
           .then(response => {
             this.items = response.data;
             this.newitem_id = Object.keys(this.items).length + 1;
           });
    },
    methods: {
      add_item: function() {
        this.$set(
          this.items,
          this.newitem_id.toString(),
          {
            title: this.newitem_title,
            done: false
          }
        );
        this.newitem_title = '';
        this.newitem_id++;
      },
      toggle_item_progress(id, item) {
        item.done = !item.done;
        this.$set(this.items, id, item);
      }
    }
  }
</script>
<style scoped>
.list {
  width: 80%;
  margin-left: auto;
  margin-right: auto;
}
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
.new-item-form {
  width: 80%;
  margin-top: 20px;
  margin-left: auto;
  margin-right: auto;
  align-items: center;
}
input.new-item-form {
  width: 100%;
  padding: 6px;
  border: solid 1px grey;
  border-radius: 3px;
}
input.new-item-form:hover {
  border-color: orange;
}
</style>
