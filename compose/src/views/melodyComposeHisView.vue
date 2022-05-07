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

    <div id="history-main">
      <el-table :data="logData.data" stripe style="width: 100%">
        <el-table-column prop="mid" label="Date" />
        <el-table-column prop="uid" label="Name" />
        <el-table-column prop="instru_id" label="Address" />
        <el-table-column prop="create_time" label="Address" />
        <el-table-column prop="duration_time" label="Address" />
        <el-table-column prop="file_path" label="Address" />
      </el-table>
    </div>
    <div id="history-foot">
      <el-button @click="getHistoryByUid">刷新</el-button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { List } from "@element-plus/icons";
import { ElMessage } from "element-plus";
// eslint-disable-next-line
import { reactive, ref, onMounted } from "vue";

export default {
  name: "melodyComposeHisView",
  components: {
    List,
  },

  setup() {
    let logData = reactive({
      data: [],
    });
    const getHistoryByUid = () => {
      axios
        .get("http://127.0.0.1:8000/api/get_log", {
          params: {
            uid: 1,
          },
        })
        .then((res) => {
          ElMessage({
            showClose: true,
            message: "您有" + res.data.logs.length + "条历史记录！",
            type: "success",
          });
          logData.data = res.data.logs;
          console.log(logData.data[0]);
        });
    };
    onMounted(() => {
      getHistoryByUid;
    });

    return {
      logData,
      getHistoryByUid,
    };
  },
};
</script>

<style scoped>
.no-inherit {
  margin: auto 0;
}
</style>
