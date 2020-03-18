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
        {{ item.title }}
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
            title: "Todo 1"
          },
          {
            id: 2,
            title: "Todo 2"
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
      }
    }
  }
</script>
