<template>
  <div class="common-layout">
    <el-container>
      <el-header>
        <div id="header-root">
          <el-container>
            <h3>Composer</h3>
            <div style="margin: auto 1vw">
              <svg class="icon" aria-hidden="true">
                <use xlink:href="#icon-c"></use>
              </svg>
            </div>
          </el-container>
        </div>
      </el-header>
      <el-container>
        <el-aside width="200px">
          <!--          <nav>
            <router-link to="/">
              <el-button>home</el-button>
            </router-link>
            |
            <router-link to="/about">About</router-link>
            |
            <router-link to="/main">Main</router-link>
            |
            <router-link to="/history">history</router-link>
          </nav>-->

          <el-row class="tac">
            <el-col :span="24">
              <el-menu
                default-active="2"
                class="el-menu-vertical-demo"
                @open="handleOpen"
                @close="handleClose"
              >
                <el-sub-menu index="1">
                  <template #title>
                    <el-icon>
                      <location />
                    </el-icon>
                    <span>Navigator One</span>
                  </template>
                  <el-menu-item-group title="Group One">
                    <el-menu-item index="1-1">item one</el-menu-item>
                    <el-menu-item index="1-2">item one</el-menu-item>
                  </el-menu-item-group>
                  <el-menu-item-group title="Group Two">
                    <el-menu-item index="1-3">item three</el-menu-item>
                  </el-menu-item-group>
                  <el-sub-menu index="1-4">
                    <template #title>item four</template>
                    <el-menu-item index="1-4-1">item one</el-menu-item>
                  </el-sub-menu>
                </el-sub-menu>
                <el-menu-item index="2">
                  <el-icon>
                    <icon-menu />
                  </el-icon>
                  <span>Navigator Two</span>
                </el-menu-item>
                <el-menu-item index="3" disabled>
                  <el-icon>
                    <document />
                  </el-icon>
                  <span>Navigator Three</span>
                </el-menu-item>
                <el-menu-item index="4">
                  <el-icon>
                    <setting />
                  </el-icon>
                  <span>Navigator Four</span>
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
import { Menu as IconMenu, Setting } from "@element-plus/icons-vue";
import { onMounted, nextTick, ref } from "vue";

const handleOpen = (key, keyPath) => {
  console.log(key, keyPath);
};
const handleClose = (key, keyPath) => {
  console.log(key, keyPath);
};
let height = ref("600px");

onMounted(() => {
  nextTick(() => {
    height.value =
      (window.innerHeight - 200 < 600 ? 600 : window.innerHeight - 200) + "px";

    console.log(height.value);
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
</style>
