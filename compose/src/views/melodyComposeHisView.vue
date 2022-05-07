<template>
  <div id="history-root">
    <div id="top-bar">
      <el-container>
        <h3>您的音乐合成历史</h3>
        <el-icon color="#409EFC" class="no-inherit">
          <list />
        </el-icon>
      </el-container>
    </div>

    <div id="history-main"></div>
  </div>
</template>

<script>
import axios from "axios";
import { List } from "@element-plus/icons";
import { reactive } from "vue";
export default {
  name: "melodyComposeHisView",
  components: {
    List,
  },
  setup() {
    axios.get("http://127.0.0.1:8000/api/get_log", {
      uid: 1,
    });
    let logData = reactive({});

    return {
      logData,
    };
  },
};
</script>

<style scoped>
.no-inherit {
  margin: auto 0;
}
</style>
