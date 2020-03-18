<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <h1>Welcome to Your Vue.js App</h1>
    <input v-model="newitem_title"
           @keypress.enter="add_item">
    <p>{{ newitem_title }}</p>
    <ul>
      <li v-for="item in items"
          :key="item.id">
        <button @click="toggle_item_progress(item)">
          done
        </button>
        <div :class="{ done: item.done }">
          {{ item.title }}
        </div>
      </li>
    </ul>
  </div>
</template>
<script>
  module.exports = {
    data: function() {
      return {
        newitem_title: '',
        newitem_id: 3,
        items: [
          {
            id: 1,
            title: "Todo 1",
            done: false
          },
          {
            id: 2,
            title: "Todo 2",
            done: true
          }
        ]
      }
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
.done {
  text-decoration: line-through;
}
</style>
