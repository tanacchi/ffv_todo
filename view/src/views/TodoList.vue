<template>
  <div class="list">
    <div class="new-item-form">
      <input v-model="newitem_title"
             @keypress.enter="add_item">
    </div>
    <label v-for="item in items"
           :key="item.id"
           class="item-row">
      <input type="checkbox" :checked="item.done" @change="toggle_item_progress(item)">
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
        newitem_id: 3,
        items: []
      }
    },
    mounted: function() {
      const get_items_url = 'http://localhost:5000' + '/api/items';
      axios.get(get_items_url)
           .then(response => {
             console.log(response);
           });
    },
    methods: {
      add_item: function() {
        this.items.push({
          id: this.newitem_id++,
          title: this.newitem_title
        });
        this.newitem_title = '';
      },
      toggle_item_progress(item) {
        item.done = !item.done;
        let target_idx = this.items.findIndex(i => i.id === item.id);
        this.items.splice(target_idx, 1, item);
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
