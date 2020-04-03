<template>
  <div class="list">
    <new-item-form @item-added="push_item" />
    <item-row v-for="(item, id) in items"
              :key="id"
              :item="item"
              :item_id="id"
              :list_id="$route.params.id"
              class="item-row" />
  </div>
</template>
<script>
  import axios from 'axios'
  import NewItemForm from "@/components/items/NewItemForm.vue"
  import ItemRow from "@/components/items/ItemRow.vue"

  const api_baseurl = process.env.VUE_APP_API_BASEURL ? process.env.VUE_APP_API_BASEURL : 'http://localhost:5000/';

  export default {
    components: {
      NewItemForm,
      ItemRow,
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
</style>
