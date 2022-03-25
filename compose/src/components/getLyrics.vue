<template>
  <div>
    <div>占位</div>
    <div>
      <el-button @click="sendAjax">sendTO</el-button>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import axios from "axios";
import { useStore } from "vuex";
import { ElMessage } from "element-plus";

export default {
  name: "getLyrics",
  setup() {
    const store = useStore();
    let lyrics = ref("this is a sentence");
    let developFlag = ref(true);
    const developmentURL = "http://127.0.0.1:8000/form/getAudioPath/";

    const sendAjax = () => {
      axios
        .get(developmentURL)
        .then((response) => {
          /*        alert(
          "".concat(
            response.data,
            "\r\n",
            response.status,
            "\r\n",
            response.statusText,
            "\r\n",
            response.headers,
            "\r\n",
            response.config
          )*/
          console.log("Got audio url : " + response.data);
          store.commit("setAudioURLAndFlag", {
            audioURL: response.data,
          });
          ElMessage({
            message: "旋律已经生成！",
            type: "success",
          });
        })
        .catch((err) => {
          alert(err);
        });
    };
    const showInfoFromStore = () => {
      let info = store.getters.audioInfo;
      console.log(info);
    };

    return {
      lyrics,
      developFlag,
      sendAjax,
      showInfoFromStore,
    };
  },
};
</script>

<style scoped></style>
