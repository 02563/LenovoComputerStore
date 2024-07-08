<!-- TodoItem.vue -->
<template>
    <li class="text">{{ todo.text }}</li>
  </template>
  <script>
  export default {
    props: ["todo"],
  };
  </script>
  
  <style scoped>
  .text {
    color: #2c3e50;
  }
  </style>
  