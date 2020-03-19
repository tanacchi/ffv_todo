<template>
  <div class="list">
    <div class="new-item-form">
      <input v-model="newitem_title"
             @keypress.enter="add_item">
    </div>
    <ul>
      <li v-for="item in items"
          :key="item.id"
          class="item-row">
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
  justify-content: center;
  align-items: center;
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
