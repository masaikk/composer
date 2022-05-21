<template>
  <div>
    <top-bar>
      <template v-slot:top-bar-header>
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
                  {{ t("message.topBar.welcome") }}用户ID为
                  {{ userInfo.uid }} 的用户 {{ userInfo.name }} !
                </p>
              </div>
            </el-container>
            <div id="logout-button-holder">
              <el-select v-model="langeValue" class="m-2" placeholder="Select">
                <el-option
                  v-for="item in options"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
                />
              </el-select>
              <el-button id="logout-button" @click="logOut"
                >{{ t("message.logout") }}
              </el-button>
            </div>
          </el-container>
        </div>
      </template>
      <template v-slot:top-bar-aside>
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
                  <headset />
                </el-icon>
                <router-link to="/compose/main"
                  >{{ t("message.asideBar.generate") }}
                </router-link>
              </el-menu-item>
              <el-menu-item index="2">
                <el-icon>
                  <user-filled />
                </el-icon>
                <router-link to="/compose/myself"
                  >{{ t("message.asideBar.myInfo") }}
                </router-link>
              </el-menu-item>
              <el-menu-item index="3">
                <el-icon>
                  <reading />
                </el-icon>
                <router-link to="/compose/history"
                  >{{ t("message.asideBar.myHistory") }}
                </router-link>
              </el-menu-item>
              <el-menu-item index="4">
                <el-icon>
                  <comment />
                </el-icon>
                <router-link to="/compose/comment"
                  >{{ t("message.asideBar.comment") }}
                </router-link>
              </el-menu-item>
              <el-menu-item index="5">
                <el-icon>
                  <question-filled />
                </el-icon>
                <router-link to="/compose/about"
                  >{{ t("message.asideBar.system") }}
                </router-link>
              </el-menu-item>
            </el-menu>
          </el-col>
        </el-row>
      </template>
      <template v-slot:top-bar-main>
        <router-view />
      </template>
      <template v-slot:top-bar-footer>
        <el-container id="foot-root">
          <h3>{{ t("message.footBar.school") }} 201830660420</h3>
        </el-container>
      </template>
    </top-bar>
  </div>
</template>

<script setup>
import {
  UserFilled,
  QuestionFilled,
  Reading,
  Headset,
  Comment,
} from "@element-plus/icons-vue";
import { onMounted, nextTick, ref, reactive, watch, computed } from "vue";
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import { useI18n } from "vue-i18n";
import TopBar from "@/components/topBar";

// 获取VueX
const store = useStore();

//获取router
const router = useRouter();

const { t, locale } = useI18n();
const langeValue = ref(store.getters.getCurrentLocale());

const changeLang = (newLang) => {
  console.log(`设置了新语言${newLang}`);
  store.commit("setCurrentLocale", JSON.stringify(newLang));
  //设置vuex中的语言内容
  locale.value = newLang;
};
watch(
  () => langeValue.value,
  (newLang) => {
    changeLang(newLang);
    //监听是否有变化
  }
);
const options = [
  {
    value: "en",
    label: "English",
  },
  {
    value: "zh",
    label: "简体中文",
  },
  {
    value: "ja",
    label: "日本語",
  },
];

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

const currentId = computed(() => {
  return store.getters.getUid();
});

watch(currentId, (newValue) => {
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
