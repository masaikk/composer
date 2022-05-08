<template>
  <div>
    <div>获取歌词的组件</div>
    <div>
      <el-button @click="sendAjax">合成旋律！</el-button>
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
    const developmentURL = "http://127.0.0.1:8000/lyrics/getAudioPath/";

    const sendAjax = () => {
      ElMessage({ showClose: true, message: "合成请求已经发送！" });
      axios
        .get(developmentURL, {
          params: {
            lyrics: lyrics.value,
          },
        })
        .then((response) => {
          console.log(response.data);
          store.commit("setAudioURLAndFlag", {
            audioURL: response.data.music_url,
          });
          store.commit("setLyrics", lyrics);

          ElMessage({
            showClose: true,
            message: "旋律已经生成！\n 请点击下方按钮播放！",
            type: "success",
          });
        })
        .catch((err) => {
          alert(err);
          ElMessage({
            showClose: true,
            message: "抱歉，旋律生成错误！\n请稍后重试！",
            type: "error",
          });
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
