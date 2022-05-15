<template>
  <div>
    <div class="newfinno-con"></div>

    <div class="tips">
      <h2 class="b-text">矮油~~您访问的页面不在地球上...</h2>
      <p class="m-box">
        <span class="m-text">休息一下,去首页逛逛看吧。</span>
        <a class="back-index" @click="return2MainPage">返回首页</a>
      </p>
    </div>
  </div>
</template>

<script>
import { useRouter } from "vue-router";
export default {
  name: "my404Page",
  setup() {
    const router = useRouter();
    const return2MainPage = () => {
      router.push("/");

      return false;
    };
    return {
      return2MainPage,
    };
  },
};
</script>

<style scoped>
a {
  transition-property: background, color;
  transition-duration: 0.2s;
  transition-timing-function: ease-out;
  -moz-transition-timing-function: ease-out;
  -webkit-transition-timing-function: ease-out;
  -o-transition-timing-function: ease-out;
  text-decoration: none;
}
.newfinno-con {
  background: url(../assets/404.png) no-repeat;
  width: 768px;
  height: 424px;
  margin: 20px auto 0;
}
.tips {
  text-align: center;
}
.tips h2 {
  font-size: 20px;
  margin-bottom: 20px;
}
.tips .m-box {
  width: 295px;
  margin: auto;
}
.tips .m-text {
  font-size: 12px;
  line-height: 32px;
}
.tips .back-index {
  display: block;
  width: 110px;
  height: 30px;
  background-color: #e3453d;
  border-radius: 10px;
  float: right;
  color: #fff;
  line-height: 30px;
}
</style>
