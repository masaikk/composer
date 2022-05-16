<template>
  <div class="home">
    <img alt="Composer logo" src="../assets/logo.png" />
    <h2>欢迎来到composer！</h2>
    <div id="toMain" @click="click2MainPage">
      <h5>点击此处跳转首页</h5>
    </div>
  </div>
</template>

<script>
import { useRouter } from "vue-router";
export default {
  name: "HomeView",
  setup() {
    const router = useRouter();
    const click2MainPage = () => {
      router.push("/compose/main");
    };
    return {
      click2MainPage,
    };
  },
};
</script>
