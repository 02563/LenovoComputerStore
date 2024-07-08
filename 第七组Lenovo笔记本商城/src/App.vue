<!-- app.vue -->
<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png" />
    <HelloWorld msg="Hello Vue!" />
    <ol>
      <todo-item
        v-for="item in list"
        v-bind:todo="item"
        v-bind:key="item.id"
      ></todo-item>
    </ol>
  </div>
</template>

<script>
import HelloWorld from "./components/HelloWorld.vue";
import TodoItem from "./components/TodoItem.vue";

export default {
  name: "App",
  data() {
    return {
      list: [
        {
          id: 0,
          text: "读书",
        },
        {
          id: 1,
          text: "写字",
        },
        {
          id: 2,
          text: "看电视",
        },
      ],
    };
  },
  components: {
    HelloWorld,
    TodoItem,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

