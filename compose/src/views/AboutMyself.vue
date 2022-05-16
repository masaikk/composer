<template>
  <div id="myself-root">
    <div id="myself-head">
      <h3>个人信息</h3>
    </div>
    <div id="myself-main">{{ userData }}</div>
    <div id="myself-foot">
      <el-button @click="flushUserInfo">刷新个人信息</el-button>
    </div>
  </div>
</template>

<script>
import { useStore } from "vuex";
import { reactive, onBeforeMount } from "vue";
import { ElMessage } from "element-plus";
import { getMyInfoByUid as getMyInfoByUidAxios } from "@/apis";

export default {
  name: "AboutMyself",
  setup() {
    const store = useStore();
    let userData = reactive({
      uid: 0,
      name: "",
      phone: "",
      accountTime: "",
    });
    const getUserInfoByUid = () => {
      getMyInfoByUidAxios({
        uid: store.getters.getUid(),
      }).then((res) => {
        console.log(res.data);
        userData.uid = res.data.uid;
        userData.name = res.data.username;
        userData.phone = res.data.phone_number;
        userData.accountTime = res.data.user_time;
      });
    };
    onBeforeMount(() => {
      getUserInfoByUid();
    });

    const flushUserInfo = () => {
      getUserInfoByUid();
      ElMessage({
        showClose: true,
        message: "信息刷新成功！",
        type: "success",
      });
    };

    return {
      userData,
      getUserInfoByUid,
      flushUserInfo,
    };
  },
};
</script>

<style scoped>
#myself-root {
  align-content: center;
  margin: 0 auto;
}
</style>
