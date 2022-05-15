<template>
  <div class="common-layout">
    <el-container>
      <el-header>
        <div id="header-root">
          <el-container>
            <el-container style="width: 80%">
              <h3>Composer</h3>
              <div style="margin: auto 1vw">
                <svg class="icon" aria-hidden="true">
                  <use xlink:href="#icon-c"></use>
                </svg>
              </div>
              <div>
                <p>
                  欢迎您！ 用户ID为 {{ userInfo.uid }} 的用户
                  {{ userInfo.name }} !
                </p>
              </div>
            </el-container>
            <div id="logout-button-holder">
              <el-button id="logout-button" @click="logOut">注销</el-button>
            </div>
          </el-container>
        </div>
      </el-header>
      <el-container>
        <el-aside width="200px">
          <el-row class="tac">
            <el-col :span="24">
              <el-menu
                default-active="2"
                class="el-menu-vertical-demo"
                @open="handleOpen"
                @close="handleClose"
              >
                <el-menu-item index="1">
                  <el-icon>
                    <icon-menu />
                  </el-icon>
                  <router-link to="/compose/myself"> 我的信息 </router-link>
                </el-menu-item>
                <el-menu-item index="2">
                  <el-icon>
                    <icon-menu />
                  </el-icon>
                  <router-link to="/compose/myself"> 我的信息 </router-link>
                </el-menu-item>
                <el-menu-item index="3">
                  <el-icon><reading /></el-icon>
                  <router-link to="/compose/history">我的历史</router-link>
                </el-menu-item>
                <el-menu-item index="4">
                  <el-icon><reading /></el-icon>
                  <router-link to="/compose/main">合成音乐</router-link>
                </el-menu-item>
                <el-menu-item index="5">
                  <el-icon><question-filled /></el-icon>
                  <router-link to="/compose/comment">评价</router-link>
                </el-menu-item>
                <el-menu-item index="6">
                  <el-icon><question-filled /></el-icon>
                  <router-link to="/compose/about">关于</router-link>
                </el-menu-item>
              </el-menu>
            </el-col>
          </el-row>
        </el-aside>
        <el-container>
          <el-main id="main-root">
            <router-view />
          </el-main>
          <el-footer>
            <el-container id="foot-root">
              <h3>华南理工大学 软件学院 201830660420</h3>
            </el-container>
          </el-footer>
        </el-container>
      </el-container>
    </el-container>
  </div>
</template>

<script setup>
import {
  Menu as IconMenu,
  QuestionFilled,
  Reading,
} from "@element-plus/icons-vue";
import { onMounted, nextTick, ref, reactive, watch } from "vue";
import { useStore } from "vuex";
import { useRouter } from "vue-router";

// 获取VueX
const store = useStore();

//获取router
const router = useRouter();

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

const logOut = () => {
  store.commit("setUid", 1);
};
const toMainPage = () => {
  router.push("/");
};

watch(store.getters.getUid(), (newValue) => {
  if (parseInt(newValue) === 0) {
    toMainPage();
  }
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
</script>

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

#logout-button-holder {
  margin: auto 0;
}
</style>
