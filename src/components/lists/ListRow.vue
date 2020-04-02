<template>
  <p>
    <router-link
      :to="linkPath">
      {{ list_name }}
    </router-link>
  </p>
</template>
<script>
  export default {
    props: ['list_id', 'list_name'],
    data: function() {
      return {
        linkPath: {
          name: 'TodoList',
          params: { id: this.list_id }
        }
      };
    }
  };
</script>
