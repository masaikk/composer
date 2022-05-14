<template>
  <div>
    <router-view />
  </div>
</template>

<!--<script setup>
import {
  Menu as IconMenu,
  QuestionFilled,
  Reading,
} from "@element-plus/icons-vue";
import { onMounted, nextTick, ref, reactive } from "vue";
import { useStore } from "vuex";

// 获取VueX
const store = useStore();

const handleOpen = (key, keyPath) => {
  console.log(key, keyPath);
};
const handleClose = (key, keyPath) => {
  console.log(key, keyPath);
};
let height = ref("600px");
let userInfo = reactive({
  uid: 0,
  name: "",
});

onMounted(() => {
  nextTick(() => {
    height.value =
      (window.innerHeight - 200 < 600 ? 600 : window.innerHeight - 200) + "px";

    console.log(height.value);
    userInfo.uid = store.getters.getUid();
    userInfo.name = store.getters.getName();
    console.log(userInfo.uid);
    console.log(userInfo.name);
  });
});
</script>-->

<style lang="less">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}

#main-root {
  //height: v-bind("height.value");
}

#header-root {
  border-bottom: 2px blue solid;
  background-color: #fffebe;
}

#foot-root {
  margin: 0 auto;
  justify-content: center;
  border-top: black 2px solid;
}
</style>
