<template>
  <div class="list">
    <new-item-form @item-added="push_item" />
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
  import NewItemForm from "@/components/items/NewItemForm.vue"

  const api_baseurl = process.env.VUE_APP_API_BASEURL ? process.env.VUE_APP_API_BASEURL : 'http://localhost:5000/';

  export default {
    components: {
      NewItemForm,
    },
    data: function() {
      return {
        newitem_id: 1,
        list_name: '',
        items: {}
      }
    },
    mounted: function() {
      const get_items_url = api_baseurl + 'api/lists/' + this.$route.params.id;
      axios.get(get_items_url)
           .then(response => {
             this.list_name = response.data.name;
             this.items = response.data.items;
             this.newitem_id = Object.keys(this.items).length + 1;
           });
    },
    methods: {
      push_item: function(title) {
        this.$set(
          this.items,
          this.newitem_id.toString(),
          {
            title: title,
            done: false
          }
        );
      },
      toggle_item_progress(id, item) {
        item.done = !item.done;
        this.$set(this.items, id, item);
        const update_progress_url = api_baseurl + 'api/items';
        axios.post(update_progress_url, {
                list_id: this.$route.params.id,
                item_id: id,
                done: item.done.toString(),
              })
             .then(response => {
               console.log(`progress updated. ${response}`)
             });
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
